# Dermatology Domain-Specific Templates

This directory contains MCVQA templates specialized for dermatological imaging tasks. These templates are designed to work with skin imaging datasets including clinical photography, dermoscopy, and dermatopathology images.

## Template Organization

### Binary Classification (`classification/binary/`)
- **Malignant vs Benign Assessment** - Core cancer screening decisions
- **Inflammatory vs Non-inflammatory** - Treatment pathway selection
- **Pigmented vs Non-pigmented** - Morphological categorization

### Multiclass Classification (`classification/multiclass/`)
- **Skin Cancer Type Classification** - Specific oncological diagnosis
- **Dermoscopic Pattern Recognition** - Pattern-based lesion analysis
- **Skin Condition Categories** - Morphological disease grouping
- **Anatomical Location-Specific Diagnosis** - Context-aware diagnosis

### Ordinal Classification (`classification/ordinal/`)
- **Fitzpatrick Skin Type Assessment** - Constitutional pigmentation grading

## Example Question Generation

**Template**: `dermatology_classification_binary_easy_1.md`
**Input**: Dermoscopic image of irregular, multicolored lesion
**Generated Question**: "Based on the dermatological features visible, is this lesion malignant or benign?"
**Options**: A. Malignant, B. Benign
**Answer**: A. Malignant

## Clinical Context

These templates reflect real dermatological diagnostic workflows, from basic malignancy screening to specialized dermoscopic analysis. They support AI development for skin cancer detection, inflammatory disease assessment, and dermatological education.