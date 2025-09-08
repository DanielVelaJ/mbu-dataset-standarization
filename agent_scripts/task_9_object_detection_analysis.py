#!/usr/bin/env python3
"""
Script to analyze object detection datasets from the MBU metadata.
This script identifies object detection subtypes and counts datasets.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Any


def load_dataset_metadata(csv_path: str) -> pd.DataFrame:
    """Load the dataset metadata from CSV file."""
    try:
        df = pd.read_csv(csv_path)
        print(f"Successfully loaded {len(df)} datasets from {csv_path}")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return pd.DataFrame()


def analyze_object_detection_datasets(df: pd.DataFrame) -> Dict[str, Any]:
    """Analyze object detection datasets and their subtypes."""
    # Filter for object detection datasets
    obj_detect_mask = df['primary_task.sub_modality'] == 'Object and Lesion Detection'
    obj_detect_df = df[obj_detect_mask].copy()
    
    print(f"\n🔍 Total Object Detection Datasets: {len(obj_detect_df)}")
    
    if len(obj_detect_df) == 0:
        print("No object detection datasets found!")
        return {}
    
    # Analyze subtypes
    subtypes = obj_detect_df['primary_task.sub_sub_modality'].value_counts()
    print(f"\n📊 Object Detection Subtypes:")
    for subtype, count in subtypes.items():
        if pd.notna(subtype):
            print(f"  - {subtype}: {count} datasets")
    
    # Analyze domains
    domains = obj_detect_df['domain'].value_counts()
    print(f"\n🏥 Domains Distribution:")
    for domain, count in domains.items():
        if pd.notna(domain):
            print(f"  - {domain}: {count} datasets")
    
    # Quality analysis
    quality_scores = obj_detect_df['quality_score'].dropna()
    if len(quality_scores) > 0:
        print(f"\n⭐ Quality Score Analysis:")
        print(f"  - Mean Quality Score: {quality_scores.mean():.1f}")
        print(f"  - Median Quality Score: {quality_scores.median():.1f}")
        print(f"  - High Quality (≥80): {len(quality_scores[quality_scores >= 80])} datasets")
        print(f"  - Medium Quality (60-79): {len(quality_scores[(quality_scores >= 60) & (quality_scores < 80)])} datasets")
        print(f"  - Lower Quality (<60): {len(quality_scores[quality_scores < 60])} datasets")
    
    # Top quality datasets by subtype
    print(f"\n🎯 Top Quality Datasets by Subtype:")
    for subtype in subtypes.index:
        if pd.notna(subtype):
            subtype_df = obj_detect_df[obj_detect_df['primary_task.sub_sub_modality'] == subtype]
            top_quality = subtype_df.nlargest(3, 'quality_score')
            print(f"\n  {subtype}:")
            for idx, row in top_quality.iterrows():
                name = row['dataset_name'] if pd.notna(row['dataset_name']) else 'N/A'
                domain = row['domain'] if pd.notna(row['domain']) else 'N/A'
                quality = row['quality_score'] if pd.notna(row['quality_score']) else 'N/A'
                print(f"    - {name} ({domain}) - Quality: {quality}")
    
    return {
        'total_count': len(obj_detect_df),
        'subtypes': dict(subtypes),
        'domains': dict(domains),
        'quality_stats': {
            'mean': quality_scores.mean() if len(quality_scores) > 0 else None,
            'median': quality_scores.median() if len(quality_scores) > 0 else None
        }
    }


def identify_missing_tasks(df: pd.DataFrame) -> List[str]:
    """Identify what other task types are missing from our templates."""
    print("\n🔄 Analyzing all task types in the dataset...")
    
    # Get all unique task combinations
    task_combinations = df.groupby([
        'primary_task.modality', 
        'primary_task.sub_modality', 
        'primary_task.sub_sub_modality'
    ]).size().reset_index(name='count')
    
    task_combinations = task_combinations[task_combinations['count'] > 0]
    task_combinations = task_combinations.sort_values('count', ascending=False)
    
    print(f"\n📋 All Task Types in Dataset (Top 20):")
    for idx, row in task_combinations.head(20).iterrows():
        modality = row['primary_task.modality'] if pd.notna(row['primary_task.modality']) else 'N/A'
        sub_modality = row['primary_task.sub_modality'] if pd.notna(row['primary_task.sub_modality']) else 'N/A'
        sub_sub_modality = row['primary_task.sub_sub_modality'] if pd.notna(row['primary_task.sub_sub_modality']) else 'N/A'
        count = row['count']
        
        print(f"  {modality} → {sub_modality} → {sub_sub_modality}: {count} datasets")
    
    # Compare with what we have templates for
    completed_tasks = [
        "Binary classification",
        "Multiclass classification", 
        "Multilabel classification",
        "Semantic segmentation",
        "Instance segmentation"
    ]
    
    print(f"\n✅ Template Status:")
    print(f"  Completed Templates:")
    for task in completed_tasks:
        task_count = len(df[df['primary_task.sub_sub_modality'] == task])
        print(f"    - {task}: {task_count} datasets")
    
    # Object detection (what we're working on now)
    obj_detect_count = len(df[df['primary_task.sub_modality'] == 'Object and Lesion Detection'])
    print(f"  🔧 In Progress:")
    print(f"    - Object Detection: {obj_detect_count} datasets")
    
    # Missing tasks
    print(f"\n❌ Still Missing Templates For:")
    missing_tasks = []
    
    for idx, row in task_combinations.iterrows():
        sub_sub_modality = row['primary_task.sub_sub_modality']
        sub_modality = row['primary_task.sub_modality']
        count = row['count']
        
        if pd.notna(sub_sub_modality) and sub_sub_modality not in completed_tasks:
            if sub_modality != 'Object and Lesion Detection':  # Exclude what we're working on
                if sub_sub_modality not in missing_tasks:
                    missing_tasks.append(sub_sub_modality)
                    print(f"    - {sub_sub_modality}: {count} datasets")
    
    return missing_tasks


def main():
    """Main analysis function."""
    print("🔍 MBU Object Detection Dataset Analysis")
    print("=" * 50)
    
    # Load metadata
    df = load_dataset_metadata('../data/dataset_metadata/datasets_metadata.csv')
    if df.empty:
        print("❌ Could not load dataset metadata!")
        return
    
    # Analyze object detection datasets
    obj_detect_analysis = analyze_object_detection_datasets(df)
    
    # Identify missing tasks
    missing_tasks = identify_missing_tasks(df)
    
    print(f"\n" + "=" * 50)
    print(f"📊 SUMMARY")
    print(f"=" * 50)
    print(f"Total Object Detection Datasets: {obj_detect_analysis.get('total_count', 0)}")
    print(f"Object Detection Subtypes: {len(obj_detect_analysis.get('subtypes', {}))}")
    print(f"Missing Task Types: {len(missing_tasks)}")


if __name__ == "__main__":
    main()
