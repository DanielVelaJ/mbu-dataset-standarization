# Binary Classification Template 1: Presence Detection

## Template Overview

**Template ID**: `classification_binary_1`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Question Pattern**: Presence/absence detection for medical findings  

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct presence/absence questions about medical findings in images. It is designed for datasets where each image has a single binary label indicating whether a specific medical condition, finding, or pathology is present.

## Question Generation Pattern

### Question Format
```
"Is {finding} present in this {modality} image?"
```

### Answer Format
- **Positive cases**: "Yes"
- **Negative cases**: "No"

### Template Variables
- `{finding}`: The medical condition, pathology, or finding being detected
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus", "skin", "CT", "MRI")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Is {finding} present in this {modality} image?",
  "answer": "Yes" | "No",
  "answer_type": "yes_no",
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Direct binary classification question based on image-level label",
  "provenance": {
    "original_label": "{original_label_value}",
    "rule_id": "classification_binary_1",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Single binary label per image (0/1, positive/negative, yes/no)
- **Image Level**: Whole image classification (not region-specific)

## Template Usage Rules

1. **Finding Name**: Use the exact medical terminology from the dataset's label definitions
2. **Modality Specification**: Include the imaging modality to provide context
3. **Consistent Answers**: Always use "Yes" for positive cases and "No" for negative cases
4. **Label Mapping**:
   - Label "1", "positive", "present", "true" → "Yes"
   - Label "0", "negative", "absent", "false" → "No"

## Examples

### Example 1: Chest X-ray Pneumonia Detection
**Original Dataset**: ChestX-ray14 Pneumonia subset  
**Original Label**: 1 (positive for pneumonia)  
**Generated Q&A**:
- **Question**: "Is pneumonia present in this chest X-ray image?"
- **Answer**: "Yes"
- **Rationale**: "Patient diagnosed with pneumonia based on radiological findings"

### Example 2: Fundus Diabetic Retinopathy Screening
**Original Dataset**: Diabetic Retinopathy Detection  
**Original Label**: 0 (no diabetic retinopathy)  
**Generated Q&A**:
- **Question**: "Is diabetic retinopathy present in this fundus image?"
- **Answer**: "No"
- **Rationale**: "No signs of diabetic retinopathy detected in retinal examination"

### Example 3: Skin Lesion Melanoma Detection
**Original Dataset**: ISIC Melanoma Classification  
**Original Label**: 1 (malignant melanoma)  
**Generated Q&A**:
- **Question**: "Is melanoma present in this skin image?"
- **Answer**: "Yes"
- **Rationale**: "Lesion classified as malignant melanoma based on dermoscopic features"

### Example 4: Brain MRI Tumor Detection
**Original Dataset**: Brain Tumor Classification  
**Original Label**: 0 (no tumor)  
**Generated Q&A**:
- **Question**: "Is a brain tumor present in this MRI image?"
- **Answer**: "No"
- **Rationale**: "No abnormal masses or tumors detected in brain MRI scan"

### Example 5: Chest CT Pulmonary Nodule Detection
**Original Dataset**: LUNA16 Nodule Detection  
**Original Label**: 1 (nodule present)  
**Generated Q&A**:
- **Question**: "Is a pulmonary nodule present in this chest CT image?"
- **Answer**: "Yes"
- **Rationale**: "Pulmonary nodule identified and confirmed by radiological analysis"

## Implementation Notes

### Advantages
- **Simple and Direct**: Easy to understand and implement
- **Clinically Relevant**: Maps naturally to diagnostic decision-making
- **Low Ambiguity**: Clear yes/no questions reduce interpretation errors
- **Broad Applicability**: Works across different medical domains and modalities

### Limitations
- **Binary Only**: Cannot handle multi-class or multi-label scenarios
- **No Localization**: Does not ask about specific regions or provide spatial information
- **Basic Reasoning**: Does not test complex visual reasoning or multi-step logic

### Quality Considerations
- Ensure the finding name matches medical terminology used in the original dataset
- Verify that the modality description is accurate and informative
- Confirm that binary labels are correctly mapped to Yes/No answers
- Validate that the generated questions are clinically meaningful

