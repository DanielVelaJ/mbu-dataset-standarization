#!/usr/bin/env python3
"""
Task 11: Analyze dataset descriptions for domain-specific template verification

This script examines the descriptions and task details of datasets in each domain
to verify that the proposed templates align with actual available data.
"""

import pandas as pd
import sys
from pathlib import Path

def analyze_domain_datasets(df: pd.DataFrame, domain: str, top_n: int = 10):
    """Analyze dataset descriptions for a specific domain."""
    
    print(f"\n" + "="*60)
    print(f"DOMAIN: {domain.upper()} - DATASET DESCRIPTIONS ANALYSIS")
    print("="*60)
    
    # Filter to domain
    domain_df = df[df['domain'] == domain]
    print(f"Total datasets: {len(domain_df)}")
    
    # Get task distribution with details
    print(f"\nDetailed Task Distribution:")
    task_distribution = domain_df.groupby(['primary_task.sub_modality', 'primary_task.sub_sub_modality']).size().reset_index(name='count')
    task_distribution = task_distribution.sort_values('count', ascending=False)
    
    for _, row in task_distribution.head(15).iterrows():
        if pd.notna(row['primary_task.sub_modality']) and pd.notna(row['primary_task.sub_sub_modality']):
            print(f"  {row['primary_task.sub_modality']} → {row['primary_task.sub_sub_modality']}: {row['count']} datasets")
    
    print(f"\nTop {top_n} Most Relevant Datasets:")
    print("-" * 40)
    
    # Select top datasets by various criteria
    relevant_datasets = domain_df[
        (domain_df['primary_task.modality'] == 'Vision') |
        (domain_df['primary_task.modality'] == 'Vision–Language')
    ].copy()
    
    # Sort by quality indicators and external validation
    relevant_datasets = relevant_datasets.sort_values([
        'flags.has_external_validation.value',
        'flags.annotated_by_medical_professionals.value',
        'quality_score'
    ], ascending=False, na_position='last')
    
    for i, (_, dataset) in enumerate(relevant_datasets.head(top_n).iterrows()):
        print(f"\n{i+1}. {dataset['dataset_name']}")
        print(f"   ID: {dataset['dataset_id']}")
        print(f"   Task: {dataset['primary_task.sub_modality']} → {dataset['primary_task.sub_sub_modality']}")
        
        # Show quality indicators
        quality_info = []
        if pd.notna(dataset.get('flags.annotated_by_medical_professionals.value')):
            quality_info.append(f"Medical annotation: {dataset['flags.annotated_by_medical_professionals.value']}")
        if pd.notna(dataset.get('flags.has_external_validation.value')):
            quality_info.append(f"External validation: {dataset['flags.has_external_validation.value']}")
        if pd.notna(dataset.get('quality_score')):
            quality_info.append(f"Quality score: {dataset['quality_score']}")
        
        if quality_info:
            print(f"   Quality: {', '.join(quality_info)}")
        
        # Show task reasoning (description)
        if pd.notna(dataset.get('task_reasoning')):
            reasoning = str(dataset['task_reasoning'])[:200] + "..." if len(str(dataset['task_reasoning'])) > 200 else str(dataset['task_reasoning'])
            print(f"   Description: {reasoning}")
    
    # Analyze common terms in dataset names and descriptions
    print(f"\nCommon Terms Analysis:")
    print("-" * 20)
    
    # Combine dataset names and task reasoning for term analysis
    text_data = []
    for _, row in relevant_datasets.head(20).iterrows():
        if pd.notna(row['dataset_name']):
            text_data.append(row['dataset_name'].lower())
        if pd.notna(row['task_reasoning']):
            text_data.append(str(row['task_reasoning']).lower())
    
    # Simple term frequency analysis
    from collections import Counter
    import re
    
    words = []
    for text in text_data:
        # Extract meaningful medical terms (3+ chars, alphabetic)
        words.extend([word for word in re.findall(r'\b[a-z]{3,}\b', text) 
                     if word not in ['the', 'and', 'with', 'for', 'this', 'that', 'from', 'dataset', 'data', 'image', 'images']])
    
    common_words = Counter(words).most_common(15)
    for word, count in common_words:
        if count > 1:  # Only show terms that appear multiple times
            print(f"   '{word}': {count} occurrences")

def main():
    """Analyze dataset descriptions for all domains."""
    
    # Read the dataset metadata
    metadata_path = Path("data/dataset_metadata/datasets_metadata.csv")
    if not metadata_path.exists():
        print(f"Error: Metadata file not found at {metadata_path}")
        return
    
    try:
        df = pd.read_csv(metadata_path)
        print(f"Loaded {len(df)} datasets from metadata")
        
        # Analyze each target domain
        domains = ['Dermatology', 'Radiology', 'Pathology', 'Surgery', 'Other-Medical']
        
        for domain in domains:
            domain_df = df[df['domain'] == domain]
            if len(domain_df) > 0:
                analyze_domain_datasets(df, domain)
        
        print(f"\n" + "="*60)
        print("ANALYSIS COMPLETE")
        print("="*60)
        
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return

if __name__ == "__main__":
    main()
