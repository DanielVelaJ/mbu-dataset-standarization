# Pathology Domain-Specific Templates

This directory contains MCVQA templates specialized for pathological imaging tasks. These templates work with histopathological sections, whole slide imaging, and microscopic analysis for diagnostic and research applications.

## Template Organization

### Binary Classification (`classification/binary/`)
- **Malignant vs Benign Tissue Classification** - Core cancer diagnosis decisions
- **Tumor vs Normal Tissue Differentiation** - Surgical margin assessment
- **High-Grade vs Low-Grade Neoplasm Assessment** - Prognostic grading evaluation

### Multiclass Classification (`classification/multiclass/`)
- **Cancer Type Classification** - Specific oncological diagnosis
- **Tissue Type Identification** - Fundamental histological recognition
- **Inflammatory Pattern Classification** - Disease process characterization

### Segmentation (`segmentation/instance/`)
- **Nuclear Segmentation Quality Assessment** - Quantitative pathology evaluation (MCVQA format)

### Counting (`counting/direct/`)
- **Mitotic Figure Counting Assessment** - Proliferation index evaluation (MCVQA format)

## Example Question Generation

**Template**: `pathology_classification_binary_easy_1.md`  
**Question Formula**: "Based on the histopathological features, is this tissue malignant or benign?"  
**Answer Formula**: A. Malignant | B. Benign  
**Input**: H&E histopathological section showing malignant tissue  
**Generated Answer**: A. Malignant

## Clinical Context

These templates reflect pathological diagnostic workflows essential for cancer diagnosis, tissue classification, and quantitative analysis. They support AI development for digital pathology, automated diagnosis, and pathological education.
