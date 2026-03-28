# ONC-204 Phase II Study
## Interim Safety Review - Compliance Assessment Report

**Report Type:** Patient Enrollment Compliance Assessment  
**Study Protocol:** ONC-204 Phase II  
**Assessment Date:** 2026-03-29  
**Report Version:** 1.0  
**Classification:** CONFIDENTIAL - Clinical Trial Data  

---

## Executive Summary

This compliance assessment evaluates the ONC-204 Phase II study patient enrollment cohort against protocol-specified inclusion criteria. The assessment identified **critical compliance concerns** requiring immediate attention from the study steering committee and data safety monitoring board (DSMB).

### Key Findings

| Metric | Value |
|--------|-------|
| **Total Patients Assessed** | 5 |
| **Compliant Patients** | 2 |
| **Excluded Patients (Violations)** | 3 |
| **Overall Exclusion Rate** | **60.00%** |
| **Assessment Status** | ⚠️ **CRITICAL - IMMEDIATE ACTION REQUIRED** |

---

## 1. Inclusion Criteria

Per the ONC-204 Phase II protocol, all enrolled patients must meet the following inclusion criteria:

| Criterion | Requirement | Rationale |
|-----------|-------------|-----------|
| **Age** | ≥ 18 years | Adult population only; pediatric safety not established |
| **ECOG Performance Status** | ≤ 2 | Ensures patients have adequate functional status for treatment tolerance |

---

## 2. Compliance Analysis Results

### 2.1 Overall Compliance Statistics

```
┌─────────────────────────────────────────────────────────┐
│  COMPLIANCE ASSESSMENT SUMMARY                          │
├─────────────────────────────────────────────────────────┤
│  Total Patients in Cohort:             5                │
│  ✓ Compliant:                          2  (40.00%)      │
│  ✗ Non-Compliant:                      3  (60.00%)      │
└─────────────────────────────────────────────────────────┘
```

### 2.2 Violation Breakdown by Criterion

| Violation Type | Count | Percentage of Violations |
|----------------|-------|--------------------------|
| Age Violations (< 18 years) | 1 | 33.3% |
| ECOG Violations (> 2) | 2 | 66.7% |
| **Combined Violations** | **0** | **0.0%** |

### 2.3 Risk Stratification of Excluded Patients

| Risk Level | Count | Percentage | Definition |
|------------|-------|------------|------------|
| **CRITICAL** | 0 | 0.0% | Multiple violations (age + ECOG) |
| **HIGH** | 2 | 66.7% | ECOG ≥ 3 (poor performance status) |
| **MEDIUM** | 1 | 33.3% | Age < 18 only |
| **LOW** | 0 | 0.0% | Minor data quality issues |

---

## 3. Detailed Findings - Non-Compliant Patients

### 3.1 Patient-Level Compliance Results

| Patient ID | Age | ECOG | Status | Violations | Risk Level |
|------------|-----|------|--------|------------|------------|
| P-001 | 65 | 1 | ✓ COMPLIANT | None | N/A |
| P-002 | 16 | 0 | ✗ EXCLUDED | Age violation | MEDIUM |
| P-003 | 72 | 3 | ✗ EXCLUDED | ECOG violation | HIGH |
| P-004 | 55 | 2 | ✓ COMPLIANT | None | N/A |
| P-005 | 40 | 4 | ✗ EXCLUDED | ECOG violation | HIGH |

### 3.2 MEDIUM Risk Patients (n=1)

**Age violation only:**

| Patient ID | Age | ECOG | Violation |
|------------|-----|------|-----------|
| P-002 | 16 | 0 | Age below minimum (≥18) - **15 years under threshold** |

### 3.3 HIGH Risk Patients (n=2)

**ECOG performance status violations:**

| Patient ID | Age | ECOG | Violation | Clinical Concern |
|------------|-----|------|-----------|------------------|
| P-003 | 72 | 3 | ECOG exceeds maximum (≤2) | Limited self-care; bed/chair >50% waking hours |
| P-005 | 40 | 4 | ECOG exceeds maximum (≤2) | Completely disabled; totally bed/chair bound |

### 3.4 Compliant Patients (n=2)

| Patient ID | Age | ECOG | Status |
|------------|-----|------|--------|
| P-001 | 65 | 1 | Fully compliant |
| P-004 | 55 | 2 | Fully compliant |

---

## 4. Risk Factor Analysis

### 4.1 Patient P-002 - Age Violation (MEDIUM Risk)

**Violation:** Age 16 years (minimum required: 18 years)

**Risk Factors:**

1. **Regulatory Non-Compliance**
   - Protocol explicitly specifies adult population (≥18 years)
   - Pediatric enrollment requires separate protocol amendment and IRB approval
   - Represents a **major protocol deviation**

2. **Safety Concerns**
   - Pharmacokinetics may differ significantly in pediatric patients
   - Dosing not established for patients < 18 years
   - Long-term developmental effects unknown
   - **Gap of 2 years below minimum age**

3. **Data Integrity Impact**
   - Cannot be included in primary efficacy analysis
   - Regulatory submission may be compromised
   - Potential for clinical hold from regulatory authorities

**Recommended Action:** Immediate discontinuation consideration; IRB notification required.

### 4.2 Patient P-003 - ECOG Violation (HIGH Risk)

**Violation:** ECOG 3 (maximum allowed: 2)

**Risk Factors:**

1. **Safety Concerns**
   - ECOG 3: Capable of only limited self-care; confined to bed/chair >50% of waking hours
   - Significantly increased risk of treatment-related adverse events
   - Reduced ability to tolerate protocol-specified treatment
   - **Age 72 with poor performance status compounds risk**

2. **Efficacy Impact**
   - Poor performance status confounds efficacy assessments
   - Higher likelihood of early discontinuation
   - May skew survival and progression-free survival endpoints

3. **Ethical Considerations**
   - Treatment may cause more harm than benefit in this population
   - Quality of life concerns for patients with poor performance status

**Recommended Action:** Safety review required; consider early discontinuation.

### 4.3 Patient P-005 - ECOG Violation (HIGH Risk)

**Violation:** ECOG 4 (maximum allowed: 2)

**Risk Factors:**

1. **Critical Safety Concerns**
   - ECOG 4: Completely disabled; cannot carry out any self-care; totally confined to bed/chair
   - **Highest risk category** for treatment-related complications
   - Extremely limited ability to tolerate any therapeutic intervention
   - May indicate advanced disease progression

2. **Efficacy Impact**
   - Patient unlikely to complete treatment protocol
   - Data will be non-evaluable for primary endpoints
   - High probability of treatment-related serious adverse events

3. **Ethical Considerations**
   - **Strong ethical concern** regarding enrollment of ECOG 4 patients
   - Treatment burden likely exceeds potential benefit
   - Informed consent capacity may be impaired

**Recommended Action:** **Urgent safety review**; strong consideration for immediate discontinuation; assess for reportable adverse event.

---

## 5. Recommendations

### 5.1 Immediate Actions (Within 24-48 Hours)

1. **Patient Safety Assessment - PRIORITY**
   - **P-005 (ECOG 4):** Urgent clinical review for immediate discontinuation
   - **P-003 (ECOG 3):** Safety assessment within 24 hours
   - **P-002 (Age 16):** Assess for adverse events; notify pediatric ethics consultant

2. **Protocol Deviation Documentation**
   - Document all three violations in protocol deviation log
   - Classify as major protocol deviations
   - Prepare for IRB reporting

3. **Site Notification**
   - Notify enrolling site principal investigator immediately
   - Request root cause analysis for each violation
   - Suspend further enrollment pending investigation

### 5.2 Short-Term Actions (Within 7 Days)

1. **Regulatory Notification**
   - **IRB Notification:** Submit protocol deviation report within 5 business days
   - **FDA Notification:** Assess if violations meet criteria for IND safety report
   - **Sponsor Notification:** Immediate notification to study sponsor

2. **Data Safety Monitoring Board (DSMB)**
   - Convene emergency DSMB review
   - Present all three excluded patients for safety assessment
   - Request DSMB recommendation on study continuation

3. **Site Investigation**
   - Root cause analysis: How did these patients pass screening?
   - Review site screening procedures and training records
   - Assess whether violations are isolated or systematic

### 5.3 Long-Term Actions (Within 30 Days)

1. **Process Improvements**
   - Implement automated eligibility screening in EDC system
   - Add real-time alerts for age <18 or ECOG >2
   - Enhance site training on inclusion/exclusion criteria

2. **Data Remediation**
   - Exclude P-002, P-003, P-005 from all efficacy analyses
   - Conduct sensitivity analyses with compliant patients only (n=2)
   - Document impact on study power (currently 40% of cohort excluded)

3. **Monitoring Enhancement**
   - Increase monitoring frequency at enrolling site
   - Implement 100% source document verification for eligibility criteria
   - Add eligibility criteria to risk-based monitoring plan

---

## 6. Validation Methodology

### 6.1 Automated Validation Script

A Python-based compliance validation script was developed and executed on this cohort:

**File:** `onc204_compliance_validator.py`

**Data Source:** `onc204_patient_cohort.json`

**Features:**
- Automated age and ECOG criterion validation
- Risk stratification (MEDIUM/HIGH/CRITICAL)
- JSON and CSV format support
- Export of flagged entries
- Summary statistics generation

**Usage:**
```bash
# Process JSON cohort data
python3 onc204_compliance_validator.py onc204_patient_cohort.json

# Process CSV cohort data
python3 onc204_compliance_validator.py patient_data.csv
```

### 6.2 Validation Logic Applied

```
┌─────────────────────────────────────────────────────────┐
│  COHORT: 5 Patients                                     │
├─────────────────────────────────────────────────────────┤
│  P-001: age=65 (≥18✓), ECOG=1 (≤2✓) → COMPLIANT        │
│  P-002: age=16 (≥18✗), ECOG=0 (≤2✓) → EXCLUDED         │
│  P-003: age=72 (≥18✓), ECOG=3 (≤2✗) → EXCLUDED         │
│  P-004: age=55 (≥18✓), ECOG=2 (≤2✓) → COMPLIANT        │
│  P-005: age=40 (≥18✓), ECOG=4 (≤2✗) → EXCLUDED         │
└─────────────────────────────────────────────────────────┘
```

### 6.3 Output Files Generated

| File | Format | Contents |
|------|--------|----------|
| `onc204_patient_cohort.json` | JSON | Input cohort data |
| `onc204_compliance_results.csv` | CSV | Patient-level results |
| `onc204_compliance_results.json` | JSON | Machine-readable results |
| `onc204_compliance_validator.py` | Python | Validation script |
| `ONC204_Compliance_Assessment_Report.md` | Markdown | This report |

---

## 7. Statistical Summary

### 7.1 Exclusion Rate Analysis

```
Exclusion Rate = (Excluded Patients / Total Patients) × 100
               = (3 / 5) × 100
               = 60.00%
```

**Interpretation:** A 60% exclusion rate is **critically high** and indicates:
- Systematic screening failures at enrolling site(s)
- Potential training deficiencies
- Possible coercion or inappropriate enrollment practices

### 7.2 Compliance by Criterion

| Criterion | Compliant | Non-Compliant | Compliance Rate |
|-----------|-----------|---------------|-----------------|
| Age (≥18) | 4 | 1 | 80.0% |
| ECOG (≤2) | 3 | 2 | 60.0% |
| **Both Criteria** | **2** | **3** | **40.0%** |

### 7.3 Impact on Study Power

With only 2 of 5 patients (40%) meeting inclusion criteria:
- **Effective enrollment rate:** 40%
- **Sample size impact:** Would require 2.5× more enrollments to achieve target
- **Timeline impact:** Significant delay expected if exclusion rate persists

---

## 8. Conclusion

The compliance assessment of the ONC-204 Phase II study patient cohort identified a **60.00% exclusion rate**, with 3 of 5 patients violating inclusion criteria.

### Critical Findings

| Patient | Violation | Risk Level | Action Required |
|---------|-----------|------------|-----------------|
| P-002 | Age 16 (< 18) | MEDIUM | IRB notification |
| P-003 | ECOG 3 (> 2) | HIGH | Safety review |
| P-005 | ECOG 4 (> 2) | HIGH | **Urgent discontinuation consideration** |

### Regulatory Impact

- **Three major protocol deviations** documented
- IRB reporting required within 5 business days
- FDA notification assessment required (if IND-held)
- DSMB emergency review recommended

### Study Continuation Considerations

The 60% exclusion rate raises serious concerns about:
1. Site screening procedures and training
2. Patient safety oversight
3. Data integrity for the enrolled cohort
4. Feasibility of achieving enrollment targets

**Recommendation:** **Immediate enrollment suspension** pending root cause analysis and corrective action plan implementation.

---

## Appendix A: ECOG Performance Status Scale

| Grade | Description |
|-------|-------------|
| 0 | Fully active; able to carry on all pre-disease activities without restriction |
| 1 | Restricted in physically strenuous activity but ambulatory; able to carry out light work |
| 2 | Ambulatory and capable of all self-care; unable to carry out work activities; up and about >50% of waking hours |
| 3 | Capable of only limited self-care; confined to bed or chair >50% of waking hours |
| 4 | Completely disabled; cannot carry out any self-care; totally confined to bed or chair |
| 5 | Dead |

---

## Appendix B: Data Files

All analysis files saved to workspace:
```
/mnt/afs_toolcall/zhoulin3/.openclaw/workspaces/gendata-worker-33/
├── onc204_patient_cohort.json      (Input data)
├── onc204_compliance_validator.py  (Validation script)
├── onc204_compliance_results.csv   (Results)
├── onc204_compliance_results.json  (Results)
└── ONC204_Compliance_Assessment_Report.md (This report)
```

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-29 | Clinical Compliance Assessment System | Initial report with actual cohort data |

---

**CONFIDENTIALITY NOTICE:** This document contains confidential clinical trial data. Distribution is restricted to authorized study personnel, regulatory authorities, and ethics committees with appropriate oversight responsibilities.

**Report Generated:** 2026-03-29 03:03 GMT+8  
**Assessment System:** ONC-204 Compliance Validator v1.0  
**Cohort Size:** 5 patients  
**Exclusion Rate:** 60.00%
