# AWS EFS TLS 1.3 Configuration with FIPS 140-2 Compliance

**Document Type:** Security Configuration Specification  
**Classification:** Infrastructure Security  
**Compliance:** FIPS 140-2, TLS 1.3  

---

## Overview

This document specifies the configuration requirements for enabling TLS 1.3 encryption on data transfers to AWS Elastic File System (EFS) storage, ensuring all cipher suites meet FIPS 140-2 standards.

---

## Prerequisites

### AWS Requirements
- AWS EFS file system with **encryption in transit** enabled
- IAM policies with `elasticfilesystem:ClientMount` permissions
- EC2 instances or compute resources with EFS mount targets in same VPC
- AWS Certificate Manager (ACM) for certificate management (if using custom certificates)

### Client Requirements
- Linux clients: `amazon-efs-utils` v1.34.0 or later
- TLS 1.3 support in OpenSSL (OpenSSL 1.1.1 or later)
- FIPS mode enabled on underlying cryptographic modules

---

## TLS 1.3 Configuration Specifications

### 1. EFS File System Configuration

Enable encryption in transit at the EFS level:

```bash
# Verify EFS encryption setting
aws efs describe-file-systems --file-system-id fs-xxxxxxxx \
  --query 'FileSystems[].Encrypted'
```

**Required Setting:** `Encrypted: true`

### 2. Mount Configuration with TLS 1.3

#### Using amazon-efs-utils (Recommended)

Create or update `/etc/amazon/efs/efs-utils.conf`:

```ini
[mount]
# Enforce TLS 1.3 only
tls_enabled = true
tls_minimum_version = 1.3

# FIPS 140-2 compliant settings
fips_mode_enabled = true

# Certificate verification
verify_cert = true
verify_hostname = true

# Certificate path (if using custom certs)
cert_bundle_path = /etc/pki/tls/certs/ca-bundle.crt
```

#### Mount Command with TLS 1.3

```bash
# Mount EFS with TLS 1.3 enforcement
sudo mount -t efs tls fs-xxxxxxxx.efs.us-east-1.amazonaws.com:/ /mnt/efs \
  -o tls,tls-min=1.3,fips
```

### 3. OpenSSL FIPS Configuration

Ensure OpenSSL is configured for FIPS 140-2 mode:

```ini
# /etc/crypto-policies/back-ends/opensslcnf.config
[system_default_sect]
MinProtocol = TLSv1.3
CipherString = TLS_AES_256_GCM_SHA384:TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256
Options = FIPS
```

Verify FIPS mode:
```bash
# Check FIPS status
fipsinstall -o /etc/ssl/fipsmodule.cnf -m /etc/ssl/fipsmodule.cnf
openssl version -a | grep -i fips
```

---

## FIPS 140-2 Compliant Cipher Suites

### TLS 1.3 Cipher Suites (FIPS Approved)

TLS 1.3 natively supports only FIPS 140-2 approved algorithms. The following cipher suites are permitted:

| Cipher Suite | RFC 8446 | FIPS Status | Key Size |
|--------------|----------|-------------|----------|
| `TLS_AES_256_GCM_SHA384` | RFC 8446 §9.1 | ✅ FIPS Approved | 256-bit |
| `TLS_AES_128_GCM_SHA256` | RFC 8446 §9.1 | ✅ FIPS Approved | 128-bit |
| `TLS_CHACHA20_POLY1305_SHA256` | RFC 8446 §9.1 | ⚠️ Non-FIPS (disable for strict compliance) | 256-bit |

### Recommended Cipher Suite Order

For **strict FIPS 140-2 compliance**, configure the following cipher suite preference:

```bash
# /etc/ssl/openssl.cnf or application-specific config
CipherString = TLS_AES_256_GCM_SHA384:TLS_AES_128_GCM_SHA256
```

**Note:** `TLS_CHACHA20_POLY1305_SHA256` is NOT FIPS 140-2 approved. Exclude this cipher suite for environments requiring strict FIPS compliance.

---

## Security Group Configuration

### Inbound Rules (EFS Mount Targets)

| Type | Protocol | Port Range | Source | Description |
|------|----------|------------|--------|-------------|
| NFS | TCP | 2049 | sg-xxxxxxxx (client security group) | EFS mount with TLS |

### Outbound Rules (Client Instances)

| Type | Protocol | Port Range | Destination | Description |
|------|----------|------------|-------------|-------------|
| NFS | TCP | 2049 | sg-yyyyyyyy (EFS security group) | EFS mount with TLS |

---

## IAM Policy Requirements

### Minimum IAM Permissions

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EFSTLSTransitAccess",
      "Effect": "Allow",
      "Action": [
        "elasticfilesystem:ClientMount",
        "elasticfilesystem:ClientWrite"
      ],
      "Resource": "arn:aws:elasticfilesystem:us-east-1:123456789012:file-system/fs-xxxxxxxx",
      "Condition": {
        "Bool": {
          "elasticfilesystem:AccessedViaMountTarget": "true"
        }
      }
    }
  ]
}
```

---

## Verification Procedures

### 1. Verify TLS Version

```bash
# Check negotiated TLS version during mount
sudo mount -t efs fs-xxxxxxxx.efs.us-east-1.amazonaws.com:/ /mnt/efs -o tls

# Inspect TLS connection
sudo openssl s_client -connect fs-xxxxxxxx.efs.us-east-1.amazonaws.com:2049 \
  -tls1_3 2>&1 | grep -E "Protocol|Cipher"
```

**Expected Output:**
```
Protocol  : TLSv1.3
Cipher    : TLS_AES_256_GCM_SHA384
```

### 2. Verify FIPS Mode

```bash
# Confirm FIPS mode is active
cat /proc/sys/crypto/fips_enabled
# Expected: 1
```

### 3. Verify Encryption in Transit

```bash
# Monitor EFS mount for TLS
sudo tcpdump -i any port 2049 -nn -v | grep -i tls
```

---

## Compliance Mapping

| Requirement | FIPS 140-2 Reference | Implementation |
|-------------|---------------------|----------------|
| Cryptographic Module | Section 4 | OpenSSL FIPS Object Module v2.0+ |
| Approved Algorithms | Appendix A | AES-GCM, SHA-256/384 |
| Key Establishment | Section 5 | TLS 1.3 handshake |
| Data Protection | Section 8 | AES-256-GCM encryption |

---

## Troubleshooting

### Common Issues

| Issue | Resolution |
|-------|------------|
| Mount fails with TLS error | Verify `amazon-efs-utils` version ≥ 1.34.0 |
| FIPS mode not enabled | Enable via `fips-mode-setup --enable` |
| Cipher suite mismatch | Update OpenSSL to 1.1.1+ and configure cipher string |
| Certificate verification failed | Ensure CA bundle is current: `update-ca-trust` |

---

## References

- [AWS EFS Encryption in Transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html)
- [RFC 8446 - TLS 1.3](https://tools.ietf.org/html/rfc8446)
- [FIPS 140-2 Standard](https://csrc.nist.gov/publications/detail/fips/140/2/final)
- [amazon-efs-utils Documentation](https://github.com/aws/efs-utils)

---

**Document Owner:** Security Engineering Team  
**Last Updated:** 2026-03-28  
**Review Cycle:** Quarterly or upon AWS/EFS service updates
