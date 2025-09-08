# Semantic Segmentation Template 2: Segmentation Verification

## Template Overview

**Template ID**: `domain-agnostic_segmentation_semantic_easy_2`  
**Task Type**: Semantic Segmentation  
**Difficulty**: Easy  
**Question Pattern**: Verification of segmentation accuracy for specific anatomical structures  

## Template Description

This template converts semantic segmentation datasets into MCVQA format by asking verification questions about whether a specific anatomical structure is correctly segmented in the image. It is designed for datasets where the goal is to evaluate the accuracy and completeness of pixel-level segmentation annotations.

## Question Generation Pattern

### Question Format
```
"Is the {structure} correctly segmented in this {modality} image?"
```

### Answer Format
- **Correctly segmented**: "Yes"
- **Incorrectly segmented or missing**: "No"

### Template Variables
- `{structure}`: The anatomical structure being evaluated (e.g., "liver", "heart", "optic disc")
- `{modality}`: The imaging modality (e.g., "CT", "MRI", "fundus", "X-ray", "ultrasound")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Segmentation",
  "question": "Is the {structure} correctly segmented in this {modality} image?",
  "answer": "Yes" | "No",
  "answer_type": "yes_no",
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Segmentation quality verification based on expert annotation validation",
  "provenance": {
    "original_label": "{segmentation_quality_label}",
    "rule_id": "domain-agnostic_segmentation_semantic_easy_2",
    "annotation_id": "{mask_validation_id}",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Semantic segmentation (Vision → Segmentation → Semantic segmentation)
- **Quality Labels**: Information about segmentation accuracy or validation status
- **Expert Validation**: Segmentations reviewed by medical professionals
- **Clear Structure Definition**: Well-defined target anatomical structures

## Template Usage Rules

1. **Structure Specificity**: Name the exact anatomical structure being verified
2. **Modality Context**: Include imaging modality for clinical relevance
3. **Quality Assessment**: Base answers on segmentation accuracy and completeness
4. **Consistent Evaluation**: Apply uniform criteria for "correct" segmentation
5. **Binary Decision**: Use clear Yes/No answers for segmentation quality

## Examples

### Example 1: Liver Segmentation Quality in CT
**Original Dataset**: Medical Segmentation Decathlon - Liver  
**Original Label**: Expert-validated liver segmentation  
**Generated Q&A**:
- **Question**: "Is the liver correctly segmented in this CT image?"
- **Answer**: "Yes"
- **Rationale**: "Liver boundaries accurately delineated with expert validation"

### Example 2: Left Ventricle Segmentation in Cardiac MRI
**Original Dataset**: ACDC Cardiac Segmentation Challenge  
**Original Label**: Quality-controlled LV segmentation  
**Generated Q&A**:
- **Question**: "Is the left ventricle correctly segmented in this MRI image?"
- **Answer**: "Yes"
- **Rationale**: "Left ventricle endocardial and epicardial borders precisely segmented"

### Example 3: Retinal Vessel Segmentation in Fundus
**Original Dataset**: DRIVE Retinal Vessel Database  
**Original Label**: Manual vessel segmentation by expert  
**Generated Q&A**:
- **Question**: "Are the retinal vessels correctly segmented in this fundus image?"
- **Answer**: "Yes"
- **Rationale**: "Retinal vessel network accurately traced by ophthalmology expert"

### Example 4: Skin Lesion Boundary in Dermoscopy
**Original Dataset**: ISIC Lesion Boundary Segmentation  
**Original Label**: Dermatologist-verified lesion boundary  
**Generated Q&A**:
- **Question**: "Is the skin lesion correctly segmented in this dermoscopy image?"
- **Answer**: "Yes"
- **Rationale**: "Lesion boundary accurately delineated for melanoma assessment"

### Example 5: Prostate Segmentation in MRI
**Original Dataset**: PROMISE12 Prostate Segmentation  
**Original Label**: Radiologist-approved prostate segmentation  
**Generated Q&A**:
- **Question**: "Is the prostate correctly segmented in this MRI image?"
- **Answer**: "Yes"
- **Rationale**: "Prostate gland boundaries accurately identified on T2-weighted MRI"

## Implementation Notes

### Advantages
- **Quality Assessment**: Tests understanding of segmentation accuracy
- **Expert Validation**: Leverages medical professional annotations
- **Binary Evaluation**: Simple yes/no format enables clear assessment
- **Clinical Relevance**: Mirrors real-world segmentation quality control

### Limitations
- **Requires Quality Labels**: Needs datasets with validation information
- **Subjective Assessment**: Segmentation quality can vary between experts
- **No Specificity**: Does not identify which parts are incorrectly segmented
- **Binary Only**: Cannot capture degrees of segmentation quality

### Quality Considerations
- Ensure access to expert-validated segmentation annotations
- Use consistent criteria for defining "correct" segmentation
- Verify that anatomical structure names match clinical terminology
- Confirm that imaging modality context is medically appropriate
- Validate that segmentation quality assessments are reliable
