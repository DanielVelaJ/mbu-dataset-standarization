# Binary Classification Template 5: Exclusionary Assessment

## Template Overview

**Template ID**: `classification_binary_5`  
**Task Type**: Binary Classification  
**Difficulty**: Medium  
**Question Pattern**: Rule-out assessment to test negative predictive reasoning  

## Template Description

This template converts binary classification datasets into MCVQA format by asking whether a medical condition can be ruled out based on imaging findings. It specifically tests the model's ability to correctly identify when conditions cannot be excluded, which is critical for avoiding dangerous false negatives in clinical practice. This template is particularly valuable for testing model safety and negative predictive capabilities.

## Question Generation Pattern

### Question Format
```
"Can {condition} be ruled out based on this {modality} image?"
```

### Answer Format
- **Negative cases**: "Yes, can be ruled out"
- **Positive cases**: "No, cannot be ruled out"

### Template Variables
- `{condition}`: The medical condition or finding being assessed for exclusion
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus photograph", "brain MRI")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Can {condition} be ruled out based on this {modality} image?",
  "answer": "Yes, can be ruled out" | "No, cannot be ruled out",
  "answer_type": "single_label",
  "options": ["Yes, can be ruled out", "No, cannot be ruled out"],
  "difficulty": "medium",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Exclusionary assessment to test negative predictive reasoning",
  "provenance": {
    "original_label": "{original_label_value}",
    "rule_id": "classification_binary_5",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels where exclusionary reasoning is clinically appropriate
- **Clinical Context**: Scenarios where ruling out conditions is a critical clinical decision
- **Image Level**: Whole image classification

## Template Usage Rules

1. **Label Mapping (Inverted Logic)**:
   - **Negative Cases (Label = 0)**: "Yes, can be ruled out" 
   - **Positive Cases (Label = 1)**: "No, cannot be ruled out"
2. **Condition Selection**: Focus on conditions where exclusion has clinical significance
3. **Safety Emphasis**: This template tests critical safety scenarios where missing a condition could be harmful
4. **Clinical Appropriateness**: Ensure the imaging modality is actually capable of detecting or excluding the condition

## Examples

### Example 1: Chest X-ray Pneumothorax Exclusion
**Original Dataset**: Pneumothorax detection  
**Original Label**: 1 (pneumothorax present)  
**Generated Q&A**:
- **Question**: "Can pneumothorax be ruled out based on this chest X-ray image?"
- **Answer**: "No, cannot be ruled out"
- **Rationale**: "Pneumothorax is present and cannot be safely excluded"

### Example 2: Brain CT Stroke Exclusion
**Original Dataset**: Acute stroke detection  
**Original Label**: 0 (no stroke)  
**Generated Q&A**:
- **Question**: "Can acute stroke be ruled out based on this brain CT image?"
- **Answer**: "Yes, can be ruled out"
- **Rationale**: "CT findings allow exclusion of acute stroke"

### Example 3: Chest X-ray Pulmonary Embolism
**Original Dataset**: Pulmonary embolism screening  
**Original Label**: 1 (high probability PE)  
**Generated Q&A**:
- **Question**: "Can pulmonary embolism be ruled out based on this chest X-ray image?"
- **Answer**: "No, cannot be ruled out"
- **Rationale**: "Chest X-ray findings are suspicious and do not exclude pulmonary embolism"

### Example 4: Fundus Papilledema Exclusion
**Original Dataset**: Papilledema detection  
**Original Label**: 0 (no papilledema)  
**Generated Q&A**:
- **Question**: "Can papilledema be ruled out based on this fundus photograph?"
- **Answer**: "Yes, can be ruled out"
- **Rationale**: "Optic disc appearance is normal, excluding papilledema"

### Example 5: Abdominal CT Appendicitis Exclusion
**Original Dataset**: Appendicitis detection  
**Original Label**: 1 (appendicitis present)  
**Generated Q&A**:
- **Question**: "Can appendicitis be ruled out based on this abdominal CT image?"
- **Answer**: "No, cannot be ruled out"
- **Rationale**: "CT findings are consistent with appendicitis and condition cannot be excluded"

## Implementation Notes

### Advantages
- **Safety Testing**: Critical for identifying dangerous false negatives
- **Negative Predictive Focus**: Tests model's ability to correctly exclude conditions
- **Clinical Relevance**: Mirrors real clinical decision-making about ruling out conditions
- **Risk Assessment**: Helps evaluate model safety in high-stakes scenarios
- **Conservative Bias**: Encourages models to be appropriately conservative

### Limitations
- **Inverted Logic**: May be confusing since positive cases get "No" answers
- **Context Dependency**: Exclusion capability varies by imaging modality and clinical setting
- **Modality Limitations**: Some conditions cannot be definitively ruled out by certain imaging
- **Threshold Sensitivity**: Different clinical contexts may have different exclusion criteria

### Quality Considerations
- **Clinical Appropriateness**: Ensure the imaging modality can reasonably exclude the condition
- **Safety Focus**: Prioritize conditions where missing diagnosis has serious consequences
- **Threshold Validation**: Confirm exclusion criteria align with clinical practice standards
- **False Negative Impact**: Consider consequences of incorrectly ruling out present conditions

### Clinical Context Guidelines
- **High-stakes conditions**: Focus on conditions where exclusion has significant clinical implications
- **Emergency settings**: Particularly valuable for urgent conditions requiring immediate action
- **Screening contexts**: Useful for conditions where exclusion allows avoiding further testing
- **Modality-appropriate**: Ensure imaging method is actually capable of excluding the condition

### Safety Considerations
- **Conservative approach**: When in doubt, the model should choose "No, cannot be ruled out"
- **High sensitivity**: This template should favor high sensitivity over specificity
- **Error consequences**: Missing a present condition (false negative) is typically more dangerous than overcalling
- **Clinical follow-up**: "Cannot be ruled out" typically requires additional evaluation

### Implementation Strategy
- **Training emphasis**: Focus training on cases where conditions are present but might be missed
- **Validation priority**: Extensively validate on cases with confirmed positive findings
- **Threshold tuning**: Optimize for minimizing dangerous false negatives
- **Expert review**: Have clinical experts validate exclusion criteria and thresholds
