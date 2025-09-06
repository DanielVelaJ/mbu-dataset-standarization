#!/usr/bin/env python3
"""
Script to analyze and select the best 3 binary classification datasets from the MBU metadata.
This script filters the datasets by task type and quality scores to recommend the most suitable datasets.
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


def filter_binary_classification_datasets(df: pd.DataFrame) -> pd.DataFrame:
    """Filter datasets that are binary classification tasks."""
    # Filter for binary classification datasets
    binary_mask = df['primary_task.sub_sub_modality'] == 'Binary classification'
    binary_datasets = df[binary_mask].copy()
    
    print(f"Found {len(binary_datasets)} binary classification datasets")
    return binary_datasets


def analyze_quality_factors(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze quality factors and create scores for ranking."""
    analysis_df = df.copy()
    
    # Convert quality_score to numeric, handling NaN values
    analysis_df['quality_score_numeric'] = pd.to_numeric(analysis_df['quality_score'], errors='coerce')
    
    # Create boolean flags for quality assessment
    quality_flags = [
        'flags.annotated_by_medical_professionals.value',
        'flags.has_external_validation.value',
        'flags.is_fine_grained_labels.value'
    ]
    
    # Convert string boolean values to actual booleans
    for flag in quality_flags:
        if flag in analysis_df.columns:
            analysis_df[f'{flag}_bool'] = analysis_df[flag].map({'TRUE': True, 'FALSE': False})
    
    # Create negative quality indicators
    negative_flags = [
        'flags.low_quality_flag.value',
        'flags.subset_or_split_of_another_dataset.value',
        'flags.synthetic_type.value'
    ]
    
    for flag in negative_flags:
        if flag in analysis_df.columns:
            analysis_df[f'{flag}_bool'] = analysis_df[flag].map({'TRUE': True, 'FALSE': False})
    
    return analysis_df


def rank_datasets(df: pd.DataFrame) -> pd.DataFrame:
    """Rank datasets based on quality scores and other factors."""
    ranked_df = df.copy()
    
    # Fill NaN quality scores with 0 for ranking purposes
    ranked_df['quality_score_for_ranking'] = ranked_df['quality_score_numeric'].fillna(0)
    
    # Create composite score based on multiple factors
    composite_score = ranked_df['quality_score_for_ranking'].copy()
    
    # Bonus points for positive quality indicators
    if 'flags.annotated_by_medical_professionals.value_bool' in ranked_df.columns:
        composite_score += ranked_df['flags.annotated_by_medical_professionals.value_bool'].fillna(False) * 10
    
    if 'flags.has_external_validation.value_bool' in ranked_df.columns:
        composite_score += ranked_df['flags.has_external_validation.value_bool'].fillna(False) * 10
    
    if 'flags.is_fine_grained_labels.value_bool' in ranked_df.columns:
        composite_score += ranked_df['flags.is_fine_grained_labels.value_bool'].fillna(False) * 5
    
    # Penalty points for negative quality indicators
    if 'flags.low_quality_flag.value_bool' in ranked_df.columns:
        composite_score -= ranked_df['flags.low_quality_flag.value_bool'].fillna(False) * 20
    
    if 'flags.subset_or_split_of_another_dataset.value_bool' in ranked_df.columns:
        composite_score -= ranked_df['flags.subset_or_split_of_another_dataset.value_bool'].fillna(False) * 15
    
    # Penalty for synthetic data
    if 'flags.synthetic_type.value_bool' in ranked_df.columns:
        synthetic_mask = ranked_df['flags.synthetic_type.value'] == 'synthetic'
        composite_score -= synthetic_mask * 10
    
    ranked_df['composite_score'] = composite_score
    
    # Sort by composite score in descending order
    ranked_df = ranked_df.sort_values('composite_score', ascending=False)
    
    return ranked_df


def select_top_datasets(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Select top N datasets and ensure diversity across domains."""
    # First, get the highest scoring datasets
    top_candidates = df.head(n * 2)  # Get more candidates than needed for diversity selection
    
    selected_datasets = []
    used_domains = set()
    
    for idx, row in top_candidates.iterrows():
        domain = row.get('domain', 'Unknown')
        
        # Prioritize different domains for diversity, but allow same domain if quality is significantly higher
        if len(selected_datasets) < n:
            if domain not in used_domains or len(selected_datasets) == 0:
                selected_datasets.append(row)
                used_domains.add(domain)
            elif len(selected_datasets) < n:
                # If we need more datasets and have exhausted domain diversity, take highest quality
                selected_datasets.append(row)
    
    # Convert back to DataFrame
    return pd.DataFrame(selected_datasets)


def generate_dataset_summary(row: pd.Series) -> Dict[str, Any]:
    """Generate a summary for a selected dataset."""
    summary = {
        'dataset_id': row.get('dataset_id', 'Unknown'),
        'dataset_name': row.get('dataset_name', 'Unknown'),
        'domain': row.get('domain', 'Unknown'),
        'quality_score': row.get('quality_score_numeric', 'N/A'),
        'composite_score': row.get('composite_score', 'N/A'),
        'url': row.get('dataset_urls[0]', 'N/A'),
        'license': row.get('dataset_license', 'Unknown'),
        'annotated_by_professionals': row.get('flags.annotated_by_medical_professionals.value', 'Unknown'),
        'external_validation': row.get('flags.has_external_validation.value', 'Unknown'),
        'fine_grained_labels': row.get('flags.is_fine_grained_labels.value', 'Unknown'),
        'low_quality_flag': row.get('flags.low_quality_flag.value', 'Unknown'),
        'is_subset': row.get('flags.subset_or_split_of_another_dataset.value', 'Unknown'),
        'synthetic_type': row.get('flags.synthetic_type.value', 'Unknown'),
        'task_reasoning': row.get('task_reasoning', 'N/A')[:200] + '...' if pd.notna(row.get('task_reasoning')) and len(str(row.get('task_reasoning'))) > 200 else row.get('task_reasoning', 'N/A')
    }
    return summary


def main():
    """Main function to analyze and select binary classification datasets."""
    print("=== MBU Binary Classification Dataset Selection ===\n")
    
    # Load the dataset metadata
    csv_path = "data/dataset_metadata/datasets_metadata.csv"
    df = load_dataset_metadata(csv_path)
    
    if df.empty:
        print("Failed to load dataset. Exiting.")
        return
    
    # Filter for binary classification datasets
    binary_datasets = filter_binary_classification_datasets(df)
    
    if binary_datasets.empty:
        print("No binary classification datasets found. Exiting.")
        return
    
    # Analyze quality factors
    print("Analyzing quality factors...")
    analyzed_datasets = analyze_quality_factors(binary_datasets)
    
    # Rank datasets
    print("Ranking datasets by composite quality score...")
    ranked_datasets = rank_datasets(analyzed_datasets)
    
    # Select top 3 datasets
    print("Selecting top 3 datasets with domain diversity...")
    top_3_datasets = select_top_datasets(ranked_datasets, n=3)
    
    # Show more candidates for inspection
    print("\nTop 10 candidates for reference:")
    for i, (_, row) in enumerate(ranked_datasets.head(10).iterrows(), 1):
        print(f"{i:2d}. {row.get('dataset_name', 'Unknown')} ({row.get('domain', 'Unknown')}) - Score: {row.get('composite_score', 0):.1f}")
    
    # Generate summaries and recommendations
    print("\n" + "="*80)
    print("TOP 3 RECOMMENDED BINARY CLASSIFICATION DATASETS")
    print("="*80)
    
    for i, (_, row) in enumerate(top_3_datasets.iterrows(), 1):
        summary = generate_dataset_summary(row)
        
        print(f"\n{i}. {summary['dataset_name']}")
        print(f"   ID: {summary['dataset_id']}")
        print(f"   Domain: {summary['domain']}")
        print(f"   Quality Score: {summary['quality_score']}")
        print(f"   Composite Score: {summary['composite_score']:.1f}")
        print(f"   URL: {summary['url']}")
        print(f"   License: {summary['license']}")
        print(f"   Annotated by Professionals: {summary['annotated_by_professionals']}")
        print(f"   External Validation: {summary['external_validation']}")
        print(f"   Fine-grained Labels: {summary['fine_grained_labels']}")
        print(f"   Low Quality Flag: {summary['low_quality_flag']}")
        print(f"   Is Subset: {summary['is_subset']}")
        print(f"   Data Type: {summary['synthetic_type']}")
        print(f"   Task Reasoning: {summary['task_reasoning']}")
        print("-" * 80)
    
    # Generate additional statistics
    print(f"\nDATASET STATISTICS:")
    print(f"Total binary classification datasets found: {len(binary_datasets)}")
    print(f"Average quality score: {analyzed_datasets['quality_score_numeric'].mean():.1f}")
    print(f"Datasets with professional annotation: {(analyzed_datasets['flags.annotated_by_medical_professionals.value'] == 'TRUE').sum()}")
    print(f"Datasets with external validation: {(analyzed_datasets['flags.has_external_validation.value'] == 'TRUE').sum()}")
    print(f"Datasets with low quality flags: {(analyzed_datasets['flags.low_quality_flag.value'] == 'TRUE').sum()}")
    
    # Domain distribution
    print(f"\nDOMAIN DISTRIBUTION:")
    domain_counts = binary_datasets['domain'].value_counts()
    for domain, count in domain_counts.items():
        print(f"  {domain}: {count} datasets")
    
    print("\n" + "="*80)
    print("Analysis complete!")


if __name__ == "__main__":
    main()
