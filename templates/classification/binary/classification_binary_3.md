# Binary Classification Template 3: Normal vs Abnormal Assessment

## Template Overview

**Template ID**: `classification_binary_3`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Question Pattern**: Normal vs abnormal classification for medical screening  

## Template Description

This template converts binary classification datasets into MCVQA format by asking whether an image shows normal or abnormal findings. It is designed for screening scenarios where the primary clinical question is distinguishing normal from any pathological condition, making it ideal for datasets where the positive label represents any abnormality.

## Question Generation Pattern

### Question Format
```
"Is this {modality} image normal or abnormal?"
```

### Answer Format
- **Normal cases**: "Normal"
- **Abnormal cases**: "Abnormal"

### Template Variables
- `{modality}`: The imaging modality with appropriate descriptors (e.g., "chest X-ray", "fundus photograph", "skin lesion", "brain MRI")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Is this {modality} image normal or abnormal?",
  "answer": "Normal" | "Abnormal",
  "answer_type": "single_label",
  "options": ["Normal", "Abnormal"],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Normal vs abnormal screening classification",
  "provenance": {
    "original_label": "{original_label_value}",
    "rule_id": "classification_binary_3",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels where 0 = normal/healthy and 1 = abnormal/pathological
- **Clinical Context**: Screening or general abnormality detection scenarios
- **Image Level**: Whole image classification

## Template Usage Rules

1. **Modality Description**: Use clinically appropriate modality descriptions
2. **Label Mapping**:
   - Label "0", "normal", "healthy", "negative" → "Normal"
   - Label "1", "abnormal", "pathological", "positive" → "Abnormal"
3. **Context Appropriateness**: Best suited for screening datasets rather than specific disease detection
4. **Consistent Terminology**: Always use "Normal" and "Abnormal" as answer options

## Examples

### Example 1: Chest X-ray Screening
**Original Dataset**: General chest X-ray screening dataset  
**Original Label**: 0 (normal chest)  
**Generated Q&A**:
- **Question**: "Is this chest X-ray image normal or abnormal?"
- **Answer**: "Normal"
- **Rationale**: "No pathological findings detected in chest radiograph"

### Example 2: Fundus Photography Screening
**Original Dataset**: Diabetic retinopathy screening  
**Original Label**: 1 (any retinopathy present)  
**Generated Q&A**:
- **Question**: "Is this fundus photograph normal or abnormal?"
- **Answer**: "Abnormal"
- **Rationale**: "Retinal abnormalities consistent with diabetic retinopathy detected"

### Example 3: Skin Lesion Screening
**Original Dataset**: Skin cancer screening  
**Original Label**: 1 (suspicious lesion)  
**Generated Q&A**:
- **Question**: "Is this skin lesion image normal or abnormal?"
- **Answer**: "Abnormal"
- **Rationale**: "Skin lesion shows features requiring further evaluation"

### Example 4: Brain MRI Screening
**Original Dataset**: Brain abnormality detection  
**Original Label**: 0 (normal brain)  
**Generated Q&A**:
- **Question**: "Is this brain MRI image normal or abnormal?"
- **Answer**: "Normal"
- **Rationale**: "No structural abnormalities detected in brain MRI"

### Example 5: Mammography Screening
**Original Dataset**: Breast cancer screening  
**Original Label**: 1 (abnormal findings)  
**Generated Q&A**:
- **Question**: "Is this mammography image normal or abnormal?"
- **Answer**: "Abnormal"
- **Rationale**: "Mammographic findings require additional evaluation"

## Implementation Notes

### Advantages
- **Screening Relevance**: Directly maps to clinical screening workflows
- **High Applicability**: Works with any binary abnormality detection dataset
- **Clear Decision Boundary**: Simple normal vs abnormal distinction
- **Patient Communication**: Matches how results are often communicated to patients
- **Triage Utility**: Useful for determining if further evaluation is needed

### Limitations
- **Low Specificity**: Does not identify what type of abnormality is present
- **Context Dependency**: May be too general for specialized diagnostic datasets
- **Threshold Sensitivity**: Different clinical contexts may have different normal/abnormal thresholds
- **Limited Educational Value**: Does not test knowledge of specific conditions

### Quality Considerations
- Ensure the dataset truly represents a normal vs abnormal classification paradigm
- Verify that "normal" cases are actually normal, not just negative for a specific condition
- Consider whether the clinical context supports general abnormality assessment
- Validate that abnormal cases represent clinically significant findings requiring attention

### Clinical Context Guidelines
- **Ideal for**: General screening datasets, population health studies, triage scenarios
- **Less suitable for**: Specific disease detection, research datasets focused on particular conditions
- **Threshold considerations**: Should align with clinical practice standards for what constitutes "abnormal"
