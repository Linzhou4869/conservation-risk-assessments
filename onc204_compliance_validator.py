#!/usr/bin/env python3
"""
ONC-204 Phase II Study - Patient Enrollment Compliance Validator
================================================================

This script performs automated compliance assessment for patient enrollment
against inclusion criteria for the ONC-204 Phase II interim safety review.

Inclusion Criteria:
- Age ≥ 18 years
- ECOG Performance Status ≤ 2

Author: Clinical Compliance Assessment System
Date: 2026-03-29
Version: 1.0
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import json
import sys


class ONC204ComplianceValidator:
    """
    Validates patient enrollment data against ONC-204 Phase II inclusion criteria.
    """
    
    # Inclusion criteria constants
    MIN_AGE = 18
    MAX_ECOG = 2
    
    def __init__(self, data_path: Optional[str] = None, data: Optional[pd.DataFrame] = None):
        """
        Initialize validator with data from file path or DataFrame.
        
        Args:
            data_path: Path to CSV/Excel file containing patient data
            data: Pre-loaded pandas DataFrame
        """
        self.data = None
        self.violations = []
        self.compliant_patients = []
        self.excluded_patients = []
        self.summary_stats = {}
        
        if data_path:
            self.load_data(data_path)
        elif data is not None:
            self.data = data.copy()
    
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load patient enrollment data from file.
        
        Args:
            file_path: Path to CSV, Excel, or JSON file
            
        Returns:
            Loaded DataFrame
        """
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith(('.xlsx', '.xls')):
                self.data = pd.read_excel(file_path)
            elif file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    data_list = json.load(f)
                self.data = pd.DataFrame(data_list)
            else:
                raise ValueError(f"Unsupported file format: {file_path}")
            
            print(f"✓ Successfully loaded {len(self.data)} patient records from {file_path}")
            return self.data
            
        except FileNotFoundError:
            print(f"✗ Error: File not found - {file_path}")
            raise
        except Exception as e:
            print(f"✗ Error loading data: {str(e)}")
            raise
    
    def validate_age(self, age: int) -> Tuple[bool, str]:
        """
        Validate patient age against inclusion criterion.
        
        Args:
            age: Patient age in years
            
        Returns:
            Tuple of (is_compliant, violation_message)
        """
        if pd.isna(age):
            return False, "Age data missing"
        
        try:
            age = int(age)
            if age < self.MIN_AGE:
                return False, f"Age {age} below minimum requirement (≥{self.MIN_AGE})"
            return True, ""
        except (ValueError, TypeError):
            return False, f"Invalid age value: {age}"
    
    def validate_ecog(self, ecog: int) -> Tuple[bool, str]:
        """
        Validate ECOG performance status against inclusion criterion.
        
        Args:
            ecog: ECOG performance status score
            
        Returns:
            Tuple of (is_compliant, violation_message)
        """
        if pd.isna(ecog):
            return False, "ECOG status data missing"
        
        try:
            ecog = int(ecog)
            if ecog < 0 or ecog > 5:
                return False, f"Invalid ECOG value: {ecog} (valid range: 0-5)"
            if ecog > self.MAX_ECOG:
                return False, f"ECOG {ecog} exceeds maximum allowed (≤{self.MAX_ECOG})"
            return True, ""
        except (ValueError, TypeError):
            return False, f"Invalid ECOG value: {ecog}"
    
    def assess_risk_level(self, violations: List[str]) -> str:
        """
        Assess risk level based on violation types.
        
        Args:
            violations: List of violation messages
            
        Returns:
            Risk level string (LOW, MEDIUM, HIGH, CRITICAL)
        """
        risk_score = 0
        
        for violation in violations:
            if "ECOG" in violation and "exceeds" in violation:
                risk_score += 3  # High risk - poor performance status
            elif "Age" in violation and "below" in violation:
                risk_score += 2  # Medium risk - age violation
            elif "missing" in violation.lower():
                risk_score += 2  # Medium risk - data quality issue
            elif "Invalid" in violation:
                risk_score += 1  # Lower risk - data entry error
        
        if risk_score >= 4:
            return "CRITICAL"
        elif risk_score >= 3:
            return "HIGH"
        elif risk_score >= 2:
            return "MEDIUM"
        else:
            return "LOW"
    
    def run_compliance_check(self) -> pd.DataFrame:
        """
        Execute full compliance assessment on all patients.
        
        Returns:
            DataFrame with compliance results
        """
        if self.data is None:
            raise ValueError("No data loaded. Call load_data() first.")
        
        required_columns = {'patient_id', 'age', 'ecog_status'}
        available_columns = set(self.data.columns.str.lower())
        
        # Handle column name variations
        column_mapping = {}
        for req_col in required_columns:
            for avail_col in available_columns:
                if req_col.replace('_', '') == avail_col.replace('_', ''):
                    column_mapping[avail_col] = req_col
                    break
        
        if column_mapping:
            self.data = self.data.rename(columns=column_mapping)
        
        # Validate required columns exist
        missing_cols = required_columns - set(self.data.columns.str.lower())
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        results = []
        
        for idx, row in self.data.iterrows():
            patient_id = row.get('patient_id', f'UNKNOWN_{idx}')
            age = row.get('age', row.get('Age', None))
            ecog = row.get('ecog_status', row.get('ECOG_status', row.get('ECOG', None)))
            
            age_compliant, age_violation = self.validate_age(age)
            ecog_compliant, ecog_violation = self.validate_ecog(ecog)
            
            is_compliant = age_compliant and ecog_compliant
            violations = []
            
            if not age_compliant:
                violations.append(age_violation)
            if not ecog_compliant:
                violations.append(ecog_violation)
            
            risk_level = self.assess_risk_level(violations) if violations else "N/A"
            
            result = {
                'patient_id': patient_id,
                'age': age,
                'ecog_status': ecog,
                'age_compliant': age_compliant,
                'ecog_compliant': ecog_compliant,
                'overall_compliant': is_compliant,
                'violations': '; '.join(violations) if violations else None,
                'risk_level': risk_level,
                'violation_count': len(violations)
            }
            
            results.append(result)
            
            if is_compliant:
                self.compliant_patients.append(patient_id)
            else:
                self.excluded_patients.append({
                    'patient_id': patient_id,
                    'violations': violations,
                    'risk_level': risk_level
                })
        
        self.results_df = pd.DataFrame(results)
        self.violations = self.excluded_patients
        self._calculate_summary_statistics()
        
        return self.results_df
    
    def _calculate_summary_statistics(self):
        """Calculate summary statistics for the compliance assessment."""
        if self.results_df is None:
            return
        
        total_patients = len(self.results_df)
        compliant_count = self.results_df['overall_compliant'].sum()
        excluded_count = total_patients - compliant_count
        exclusion_rate = (excluded_count / total_patients * 100) if total_patients > 0 else 0
        
        age_violations = (~self.results_df['age_compliant']).sum()
        ecog_violations = (~self.results_df['ecog_compliant']).sum()
        
        risk_distribution = self.results_df[self.results_df['risk_level'] != 'N/A']['risk_level'].value_counts().to_dict()
        
        self.summary_stats = {
            'total_patients': total_patients,
            'compliant_patients': int(compliant_count),
            'excluded_patients': int(excluded_count),
            'exclusion_rate_percent': round(exclusion_rate, 2),
            'age_violations': int(age_violations),
            'ecog_violations': int(ecog_violations),
            'risk_distribution': risk_distribution,
            'assessment_date': datetime.now().isoformat()
        }
    
    def get_summary_report(self) -> Dict:
        """
        Generate summary statistics dictionary.
        
        Returns:
            Dictionary containing summary statistics
        """
        if not self.summary_stats:
            self.run_compliance_check()
        return self.summary_stats
    
    def export_results(self, output_path: str, format: str = 'csv') -> str:
        """
        Export compliance results to file.
        
        Args:
            output_path: Output file path
            format: Output format ('csv', 'excel', 'json')
            
        Returns:
            Path to exported file
        """
        if self.results_df is None:
            raise ValueError("No results to export. Run compliance check first.")
        
        try:
            if format == 'csv':
                self.results_df.to_csv(output_path, index=False)
            elif format == 'excel':
                self.results_df.to_excel(output_path, index=False)
            elif format == 'json':
                self.results_df.to_json(output_path, orient='records', indent=2)
            else:
                raise ValueError(f"Unsupported export format: {format}")
            
            print(f"✓ Results exported to {output_path}")
            return output_path
            
        except Exception as e:
            print(f"✗ Error exporting results: {str(e)}")
            raise
    
    def generate_flagged_entries(self) -> pd.DataFrame:
        """
        Get DataFrame of only non-compliant entries.
        
        Returns:
            DataFrame with flagged non-compliant patients
        """
        if self.results_df is None:
            raise ValueError("No results available. Run compliance check first.")
        
        return self.results_df[~self.results_df['overall_compliant']].copy()


def create_sample_data() -> pd.DataFrame:
    """
    Create sample patient enrollment data for demonstration.
    Replace this with actual ONC-204 data loading.
    """
    np.random.seed(42)
    
    sample_data = {
        'patient_id': [f'ONC204-{str(i).zfill(4)}' for i in range(1, 101)],
        'age': np.concatenate([
            np.random.randint(18, 75, 85),  # 85 compliant ages
            np.random.randint(16, 18, 10),  # 10 underage patients
            np.random.randint(18, 75, 5)    # 5 more compliant
        ]),
        'ecog_status': np.concatenate([
            np.random.randint(0, 3, 80),    # 80 compliant ECOG
            np.random.randint(3, 5, 15),    # 15 non-compliant ECOG
            np.random.randint(0, 3, 5)      # 5 more compliant
        ]),
        'enrollment_date': pd.date_range('2025-01-01', periods=100, freq='D'),
        'site_id': np.random.choice(['SITE-A', 'SITE-B', 'SITE-C', 'SITE-D'], 100)
    }
    
    # Introduce some specific violations for demonstration
    sample_data['age'][5] = 16  # Underage
    sample_data['age'][12] = 17  # Underage
    sample_data['age'][23] = 15  # Underage
    sample_data['ecog_status'][10] = 3  # ECOG violation
    sample_data['ecog_status'][15] = 4  # ECOG violation
    sample_data['ecog_status'][30] = 3  # ECOG violation
    
    return pd.DataFrame(sample_data)


def main():
    """Main execution function."""
    print("=" * 70)
    print("ONC-204 Phase II Study - Compliance Assessment")
    print("=" * 70)
    print()
    
    # Check for command line argument for data file
    if len(sys.argv) > 1:
        data_file = sys.argv[1]
        print(f"Loading data from: {data_file}")
        validator = ONC204ComplianceValidator(data_path=data_file)
    else:
        print("No data file provided. Using sample data for demonstration.")
        print("(Replace with actual ONC-204 patient enrollment data)")
        print()
        sample_data = create_sample_data()
        validator = ONC204ComplianceValidator(data=sample_data)
    
    print()
    print("-" * 70)
    print("Running Compliance Assessment...")
    print("-" * 70)
    
    # Run compliance check
    results = validator.run_compliance_check()
    
    # Get summary
    summary = validator.get_summary_report()
    
    print()
    print("=" * 70)
    print("COMPLIANCE ASSESSMENT SUMMARY")
    print("=" * 70)
    print(f"Total Patients Assessed:     {summary['total_patients']}")
    print(f"Compliant Patients:          {summary['compliant_patients']}")
    print(f"Excluded Patients:           {summary['excluded_patients']}")
    print(f"Overall Exclusion Rate:      {summary['exclusion_rate_percent']:.2f}%")
    print()
    print("Violation Breakdown:")
    print(f"  - Age Violations:          {summary['age_violations']}")
    print(f"  - ECOG Violations:         {summary['ecog_violations']}")
    print()
    
    if summary['risk_distribution']:
        print("Risk Level Distribution (Excluded Patients):")
        for risk, count in sorted(summary['risk_distribution'].items()):
            print(f"  - {risk}:                    {count}")
    print()
    
    # Show flagged entries
    flagged = validator.generate_flagged_entries()
    if len(flagged) > 0:
        print("-" * 70)
        print("FLAGGED NON-COMPLIANT PATIENTS")
        print("-" * 70)
        print(flagged[['patient_id', 'age', 'ecog_status', 'violations', 'risk_level']].to_string(index=False))
        print()
    
    # Export results
    validator.export_results('onc204_compliance_results.csv', format='csv')
    validator.export_results('onc204_compliance_results.json', format='json')
    
    print()
    print("=" * 70)
    print("Assessment Complete")
    print("=" * 70)
    
    return summary


if __name__ == "__main__":
    main()
