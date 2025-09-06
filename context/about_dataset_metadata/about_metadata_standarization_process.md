# MBU Dataset Metadata Standardization & Filtering Report

## Overview

This document describes the comprehensive analysis and filtering of biomedical datasets from multiple sources (Hugging Face, Zenodo, Kaggle, Papers with Code) for the **MBU (Medical Benchmark Unified) project** \- a large-scale benchmark for medical/biomedical vision and vision-language models.

## What We Did

### 1\. Data Collection & Processing Pipeline

- **Sources**: Collected dataset metadata from 4 major platforms:  
  - **Hugging Face**: 2,088 datasets (from `.md` dataset cards)  
  - **Zenodo**: 674 datasets (from `.txt` reports)  
  - **Kaggle**: 375 datasets (from JSON reports)  
  - **Papers with Code**: 400 datasets (from Excel file)  
- **LLM Processing**: Each dataset report was processed using OpenAI GPT-4 with structured outputs  
- **Schema Validation**: All outputs validated against a unified JSON schema  
- **Total Raw Datasets**: 3,177 datasets across all sources

### 2\. Structured Metadata Extraction

Using platform-specific prompts, we extracted standardized metadata for each dataset:

- **Identification**: Platform-native IDs, human-readable names  
- **Domain Classification**: Medical specialties (Ophthalmology, Radiology, Dermatology, etc.)  
- **Task Taxonomy**: Detailed vision/vision-language task categorization  
- **Quality Flags**: 10+ boolean flags with evidence-based reasoning  
- **Lineage Tracking**: Parent-child dataset relationships  
- **Quality Scoring**: 0-100 quality assessment

### 3\. Filtering for High-Quality Biomedical Visual Datasets

Applied strict exclusion criteria to identify the most suitable datasets for medical AI benchmarking.

## Files Provided

### 1\. `merged_all_sources.csv` (Unfiltered)

- **3,177 total datasets** from all 4 sources  
- Complete metadata for every dataset found  
- Includes both suitable and unsuitable datasets  
- Size: \~25.7 MB

### 2\. `merged_all_sources_filtered.csv` (Filtered)

- **1,366 high-quality datasets** (43% of original)  
- Only datasets meeting strict quality criteria  
- Ready for biomedical AI research and benchmarking  
- Size: \~9.6 MB

### 3\. `merged_all_sources.jsonl` (Complete Structured Data)

- **3,177 total datasets** with full nested JSON structure  
- Contains complete metadata that gets flattened in CSV format  
- Includes all arrays, nested objects, and evidence details  
- Each record includes `source` field for traceability  
- Size: \~42.3 MB

## CSV vs JSONL: Which Format to Use?

### **CSV Format** (`merged_all_sources.csv`) \- Human-Friendly

**Best for**: Spreadsheet analysis, quick exploration, sharing with non-programmers

**What you get**:

- ✅ All key fields flattened into columns  
- ✅ Easy to open in Excel/Google Sheets  
- ✅ Flag reasoning text for each decision  
- ✅ Primary publication link and dataset URL  
- ✅ Complete original report text

**What's missing**:

- ❌ Detailed evidence with specific snippets  
- ❌ Multiple publication links (only first shown)  
- ❌ Platform metrics (downloads, likes, creation dates)  
- ❌ File analysis details (detected file types, visual modalities)  
- ❌ Author institutional affiliations  
- ❌ Secondary tasks beyond primary classification

### **JSONL Format** (`merged_all_sources.jsonl`) \- Research-Grade

**Best for**: Programmatic analysis, evidence validation, detailed research

**Everything from CSV, plus**:

- ✅ **Evidence objects**: Each decision backed by specific text snippets with URLs and line references  
- ✅ **Platform signals**: Complete download counts, likes, creation/update timestamps  
- ✅ **Publication arrays**: All associated papers, not just the first one  
- ✅ **File analysis**: Detected file types, visual modalities, example filenames  
- ✅ **Author affiliations**: Institutional context and research provenance  
- ✅ **Secondary tasks**: Additional tasks beyond primary classification  
- ✅ **Full provenance**: Complete chain from input report → evidence → reasoning → decision

### **Example: What You Miss in CSV**

For a chest X-ray dataset, the CSV shows:

flags.biomedical\_relevant.value: True

flags.biomedical\_relevant.reasoning: "Dataset contains chest X-ray images..."

The JSONL shows the same, PLUS:

"evidence": \[

  {

    "id": "ev3", 

    "snippet": "chest X rays.zip (2,463,365,435 bytes)",

    "file\_or\_field": "files list",

    "url": "https://huggingface.co/datasets/...",

    "line\_hint": "section: FILE STRUCTURE ANALYSIS"

  }

\]

This lets you verify exactly where each decision came from and how confident you should be in the classification.

### **Recommendation**

- **Start with CSV** for overview and quick analysis  
- **Use JSONL** when you need to validate decisions, build custom filters, or conduct rigorous research

## Filtering Logic & Results

### Exclusion Criteria (Dataset excluded if ANY criterion is met):

1. **Used to train LLM/VLM** → 20 datasets excluded  
   - Datasets explicitly used to train/finetune released models  
   - Avoids data contamination in benchmarks

2. **Is subset/split of another dataset** → 542 datasets excluded  
   - Derivative datasets that don't add unique content  
   - Prevents duplicate evaluation scenarios

3. **NOT biomedically relevant** → 468 datasets excluded  
   - Non-medical datasets found through broad searches  
   - Ensures medical domain focus

4. **Derived from PMCOA** → 13 datasets excluded  
   - PubMed Central Open Access derived datasets  
   - May have licensing/usage restrictions

5. **Is synthetic only** → 53 datasets excluded  
   - Purely machine-generated datasets  
   - Focus on real-world medical data

6. **Has no visual component** → 712 datasets excluded (largest exclusion)  
   - Text-only datasets without images/video  
   - Vision/vision-language benchmark requires visual data

7. **Domain is Non-medical** → 3 datasets excluded  
   - Final filter for non-medical content  
   - Ensures strict biomedical focus

### Filtering Results Summary:

Total datasets: 3,177

Excluded: 1,811 (57.0%)

Included: 1,366 (43.0%)

Exclusion breakdown by reason:

  Has no visual component: 712 (39.3% of exclusions)

  Is subset/split of another dataset: 542 (29.9% of exclusions)  

  NOT biomedically relevant: 468 (25.9% of exclusions)

  Is synthetic: 53 (2.9% of exclusions)

  Used to train LLM/VLM: 20 (1.1% of exclusions)

  Derived from PMCOA: 13 (0.7% of exclusions)

  Domain is Non-medical: 3 (0.2% of exclusions)

## Column Dictionary

### Core Identification

- **source**: Origin platform {huggingface, zenodo, kaggle, pwc}  
- **file\_id**: Internal tracking identifier (filename-based)  
- **dataset\_id**: Platform-native canonical ID (e.g., "owner/name" for HF)  
- **dataset\_name**: Human-readable dataset title  
- **domain**: Medical specialty classification

### Task Classification

- **primary\_task.modality**: {Vision, Vision–Language, "Not applicable \- no visual component"}  
- **primary\_task.sub\_modality**: Detailed task category (e.g., "Image-Level Classification")  
- **primary\_task.sub\_sub\_modality**: Specific task (e.g., "Binary classification")  
- **task\_reasoning**: Evidence-based explanation of task assignment

### Quality Flags (All include .value and .reasoning)

- **flags.used\_to\_train\_llm\_or\_vlm**: Whether used to train released models  
- **flags.subset\_or\_split\_of\_another\_dataset**: Whether derivative of another dataset  
- **flags.biomedical\_relevant**: Whether biomedically/medically relevant  
- **flags.pmcoa\_derived**: Whether derived from PubMed Central Open Access  
- **flags.synthetic\_type**: Data type {real, synthetic, mixed}  
- **flags.no\_visual\_data**: Whether purely text/tabular (no images/video)  
- **flags.is\_fine\_grained\_labels**: Whether labels capture subtle medical distinctions  
- **flags.annotated\_by\_medical\_professionals**: Whether clinicians provided labels  
- **flags.has\_external\_validation**: Whether validated by papers/benchmarks  
- **flags.low\_quality\_flag**: Whether quality concerns identified

### Metadata & Provenance

- **quality\_score**: Overall quality (0-100 scale)  
- **dataset\_urls\[0\]**: Primary dataset page URL  
- **publication\_info\_first\_link**: Associated publication (DOI preferred)  
- **dataset\_license**: License information  
- **input\_report\_text**: Complete original source report (full traceability)

### Dataset Lineage

- **dataset\_lineage.is\_subset\_or\_split**: Parent-child relationship indicator  
- **dataset\_lineage.relationship\_type**: {subset, split, mirror, rehost, derived, unknown}  
- **dataset\_lineage.parent\_dataset\_id\_or\_url**: Parent dataset identifier  
- **dataset\_lineage.parent\_platform**: Platform hosting parent dataset

## Data Quality & Reliability

### Validation Process

- **Schema Compliance**: Every dataset record validated against unified JSON schema  
- **Evidence-Based Reasoning**: All flags include detailed justification with evidence IDs  
- **Platform-Specific Prompts**: Tailored extraction for each source's metadata format  
- **Retry Logic**: Failed extractions retried with clarifying instructions

### Quality Indicators in Filtered Dataset

- ✅ **Visual Data Present**: All datasets contain images/video/visual content  
- ✅ **Biomedically Relevant**: Confirmed medical/clinical focus  
- ✅ **Original Content**: Not subset/split of existing datasets  
- ✅ **Real Data**: Preference for authentic medical data over synthetic  
- ✅ **Benchmark Safe**: Excludes datasets used to train LLMs/VLMs

## Usage Recommendations

### For Benchmark Development

- Use **filtered dataset** (`merged_all_sources_filtered.csv`) for creating evaluation benchmarks  
- Prioritize datasets with:  
  - `flags.annotated_by_medical_professionals.value = True`  
  - `flags.has_external_validation.value = True`  
  - `quality_score >= 70`

### For Research Analysis

- Use **unfiltered dataset** (`merged_all_sources.csv`) for comprehensive landscape analysis  
- Filter by specific domains (e.g., `domain = "Ophthalmology"`) for specialty focus  
- Analyze `flags.*` columns to understand dataset characteristics

### For Programmatic Analysis

- Use **JSONL format** (`merged_all_sources.jsonl`) when you need:  
  - Complete nested data structures (arrays, objects)  
  - Evidence details with IDs and snippets  
  - Programmatic filtering without CSV parsing limitations  
  - Access to all metadata fields without flattening

### Data Interpretation Notes

- **Blank/Null Values**: Indicate insufficient evidence in source reports, not definitive "no"  
- **Reasoning Fields**: Provide evidence-based justification for all flag assignments  
- **Evidence IDs**: Reference detailed evidence in original JSONL files (if needed)  
- **Input Report Text**: Contains complete original metadata for re-analysis

## Technical Details

- **Processing Date**: August 24, 2025  
- **LLM Used**: OpenAI gpt-5-mini with Structured Outputs  
- **Schema**: Unified MBU schema (includes non-visual support)  
- **Processing Method**: Parallel processing with validation and retry logic  
- **Field Limit**: CSV optimized for large text fields (input reports)

## Contact & Questions

This analysis was conducted as part of the MBU (Medical Benchmark Unified) project for systematic evaluation of biomedical vision and vision-language models. For questions about methodology, additional filtering criteria, or access to raw JSONL data, please contact Daniel at daniel.vela.j.1997@gmail.com

---

*Generated as part of MBU Stage-3 metadata standardization pipeline*

