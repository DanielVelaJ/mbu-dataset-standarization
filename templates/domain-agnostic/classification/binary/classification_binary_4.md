# Binary Classification Template 4: Likelihood Assessment

## Template Overview

**Template ID**: `classification_binary_4`  
**Task Type**: Binary Classification  
**Difficulty**: Medium  
**Question Pattern**: Probabilistic assessment with text-based likelihood categories  

## Template Description

This template converts binary classification datasets into MCVQA format by asking for likelihood assessment of medical conditions using descriptive probability categories. It tests the model's ability to express diagnostic confidence in clinically meaningful terms, moving beyond simple yes/no answers to probabilistic reasoning that better reflects medical decision-making.

## Question Generation Pattern

### Question Format
```
"What is the likelihood of {condition} in this {modality} image?"
```

### Answer Format
- **Four likelihood categories**: "Very unlikely", "Unlikely", "Likely", "Very likely"
- **Positive cases**: "Likely" or "Very likely"
- **Negative cases**: "Very unlikely" or "Unlikely"

### Template Variables
- `{condition}`: The medical condition or finding being assessed
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus photograph", "skin lesion")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What is the likelihood of {condition} in this {modality} image?",
  "answer": "Very unlikely" | "Unlikely" | "Likely" | "Very likely",
  "answer_type": "single_label",
  "options": ["Very unlikely", "Unlikely", "Likely", "Very likely"],
  "difficulty": "medium",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Probabilistic assessment of medical condition likelihood",
  "provenance": {
    "original_label": "{original_label_value}",
    "rule_id": "classification_binary_4",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels that can be mapped to likelihood categories
- **Clinical Context**: Scenarios where probabilistic assessment is clinically meaningful
- **Image Level**: Whole image classification

## Template Usage Rules

1. **Likelihood Mapping**:
   - **Positive Cases (Label = 1)**: Choose between "Likely" or "Very likely"
   - **Negative Cases (Label = 0)**: Choose between "Very unlikely" or "Unlikely"
2. **Condition Naming**: Use specific medical condition names rather than general terms
3. **Modality Specification**: Include appropriate imaging modality description
4. **Consistency**: Maintain consistent likelihood thresholds across similar datasets

### Likelihood Category Guidelines
- **Very unlikely** (0-25%): Strong evidence against the condition
- **Unlikely** (25-50%): Evidence suggests condition is not present
- **Likely** (50-75%): Evidence suggests condition is present
- **Very likely** (75-100%): Strong evidence supporting the condition

## Examples

### Example 1: Chest X-ray Pneumonia Assessment
**Original Dataset**: ChestX-ray14 Pneumonia subset  
**Original Label**: 1 (pneumonia present)  
**Generated Q&A**:
- **Question**: "What is the likelihood of pneumonia in this chest X-ray image?"
- **Answer**: "Very likely"
- **Rationale**: "Radiographic features strongly suggest pneumonia"

### Example 2: Fundus Diabetic Retinopathy Assessment
**Original Dataset**: Diabetic Retinopathy Detection  
**Original Label**: 0 (no diabetic retinopathy)  
**Generated Q&A**:
- **Question**: "What is the likelihood of diabetic retinopathy in this fundus photograph?"
- **Answer**: "Very unlikely"
- **Rationale**: "Retinal examination shows no signs of diabetic retinopathy"

### Example 3: Skin Lesion Melanoma Assessment
**Original Dataset**: ISIC Melanoma Classification  
**Original Label**: 1 (melanoma present)  
**Generated Q&A**:
- **Question**: "What is the likelihood of melanoma in this skin lesion image?"
- **Answer**: "Likely"
- **Rationale**: "Dermoscopic features suggest melanoma requiring histopathological confirmation"

### Example 4: Brain MRI Stroke Assessment
**Original Dataset**: Acute stroke detection  
**Original Label**: 0 (no acute stroke)  
**Generated Q&A**:
- **Question**: "What is the likelihood of acute stroke in this brain MRI image?"
- **Answer**: "Unlikely"
- **Rationale**: "MRI findings do not support acute stroke diagnosis"

### Example 5: Chest CT Pulmonary Embolism Assessment
**Original Dataset**: Pulmonary embolism detection  
**Original Label**: 1 (pulmonary embolism present)  
**Generated Q&A**:
- **Question**: "What is the likelihood of pulmonary embolism in this chest CT image?"
- **Answer**: "Very likely"
- **Rationale**: "CT findings strongly indicate pulmonary embolism"

## Implementation Notes

### Advantages
- **Clinical Realism**: Mirrors how clinicians think in probabilities rather than absolutes
- **Nuanced Assessment**: Allows expression of diagnostic confidence levels
- **Educational Value**: Teaches graduated assessment rather than binary thinking
- **Uncertainty Expression**: Captures the inherent uncertainty in medical diagnosis
- **Decision Support**: Provides more information for clinical decision-making

### Limitations
- **Subjective Thresholds**: Likelihood categories may be interpreted differently
- **Complexity**: More complex than simple yes/no questions
- **Context Dependency**: Likelihood may vary based on clinical setting and patient population
- **Calibration Challenges**: Models may not be well-calibrated for probability estimation

### Quality Considerations
- **Threshold Consistency**: Maintain consistent likelihood thresholds across similar cases
- **Clinical Validation**: Ensure likelihood categories align with expert clinical judgment
- **Context Appropriateness**: Consider whether probabilistic assessment fits the clinical scenario
- **Calibration**: Validate that model confidence aligns with actual diagnostic accuracy

### Clinical Context Guidelines
- **Ideal for**: Scenarios where diagnostic uncertainty is common and probabilistic reasoning is valued
- **Less suitable for**: Clear-cut cases where binary decisions are more appropriate
- **Training value**: Excellent for teaching models to express diagnostic confidence appropriately

### Implementation Strategies
- **Conservative mapping**: Use "Likely" for positive cases with some uncertainty, "Very likely" for clear cases
- **Liberal mapping**: Use "Very likely" for most positive cases, "Likely" for borderline cases
- **Balanced approach**: Distribute answers across all four categories based on case characteristics
