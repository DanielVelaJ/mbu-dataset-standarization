# Radiology Domain-Specific Templates

This directory contains MCVQA templates specialized for radiological imaging tasks. These templates work with various medical imaging modalities including chest X-rays, CT scans, MRI, and ultrasound images.

## Template Organization

### Binary Classification (`classification/binary/`)
- **Pneumonia Detection** - Emergency radiology screening
- **Fracture Detection** - Musculoskeletal trauma assessment
- **Normal vs Abnormal** - General screening applications

### Primary Finding Classification (`classification/multilabel/`)
- **Primary Finding Assessment** - Most prominent radiological finding identification (converted from multilabel to single-choice for MCVQA compatibility)

### Vision-Language Description (`vision-language/describe/short/`)
- **Radiological Finding Description Selection** - Medical communication assessment (converted from free text to multiple choice for MCVQA compatibility)

## Example Question Generation

**Template**: `radiology_classification_multilabel_easy_1.md`
**Input**: PA chest X-ray showing cardiomegaly and pulmonary edema
**Generated Question**: "What is the most prominent radiological finding in this chest X-ray?"
**Options**: A. Atelectasis, B. Cardiomegaly, C. Pleural effusion, D. Pneumonia, E. Pneumothorax, F. Pulmonary edema, G. Mass or nodule, H. Consolidation, I. No significant findings
**Answer**: B. Cardiomegaly

## Clinical Context

These templates reflect standard radiological workflows from emergency screening to comprehensive multi-finding assessment, supporting AI development for diagnostic imaging and radiological education.
