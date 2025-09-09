#!/usr/bin/env python3
"""
Task 11: Analyze dataset metadata for domain-specific template creation

This script analyzes the dataset metadata CSV to understand the distribution
of datasets by domain and task types.
"""

import pandas as pd
import sys
from pathlib import Path

def analyze_datasets():
    """Analyze dataset metadata for each domain."""
    
    # Read the dataset metadata
    metadata_path = Path("data/dataset_metadata/datasets_metadata.csv")
    if not metadata_path.exists():
        print(f"Error: Metadata file not found at {metadata_path}")
        return
    
    try:
        df = pd.read_csv(metadata_path)
        print(f"Loaded {len(df)} datasets from metadata")
        
        # Get domain distribution
        print("\n" + "="*50)
        print("DOMAIN DISTRIBUTION")
        print("="*50)
        domain_counts = df['domain'].value_counts()
        for domain, count in domain_counts.items():
            print(f"{domain}: {count} datasets")
        
        # Analyze each target domain
        target_domains = ['Dermatology', 'Radiology', 'Pathology', 'Surgery', 'Other-Medical']
        
        for domain in target_domains:
            if domain in domain_counts.index:
                analyze_domain(df, domain)
        
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return

def analyze_domain(df: pd.DataFrame, domain: str):
    """Analyze a specific domain's datasets."""
    
    print(f"\n" + "="*50)
    print(f"DOMAIN: {domain.upper()}")
    print("="*50)
    
    # Filter to domain
    domain_df = df[df['domain'] == domain]
    print(f"Total datasets: {len(domain_df)}")
    
    # Task distribution
    print(f"\nTask Distribution:")
    task_cols = ['primary_task.modality', 'primary_task.sub_modality', 'primary_task.sub_sub_modality']
    
    for col in task_cols:
        if col in domain_df.columns:
            print(f"\n{col}:")
            counts = domain_df[col].value_counts()
            for task, count in counts.head(10).items():  # Top 10
                if pd.notna(task):
                    print(f"  {task}: {count}")
    
    # Sample dataset names for context
    print(f"\nSample dataset names:")
    sample_names = domain_df['dataset_name'].dropna().head(5)
    for name in sample_names:
        print(f"  - {name}")
    
    # Quality indicators
    print(f"\nQuality Indicators:")
    quality_cols = [
        'flags.annotated_by_medical_professionals.value',
        'flags.has_external_validation.value', 
        'flags.is_fine_grained_labels.value'
    ]
    
    for col in quality_cols:
        if col in domain_df.columns:
            true_count = domain_df[col].value_counts().get(True, 0)
            total_with_data = domain_df[col].notna().sum()
            if total_with_data > 0:
                print(f"  {col.replace('flags.', '').replace('.value', '')}: {true_count}/{total_with_data} ({true_count/total_with_data*100:.1f}%)")

if __name__ == "__main__":
    analyze_datasets()
