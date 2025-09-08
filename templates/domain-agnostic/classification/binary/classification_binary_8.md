# Binary Classification Template 8: Definition-Based Assessment

## Template Overview

**Template ID**: `classification_binary_8`  
**Task Type**: Binary Classification  
**Difficulty**: Hard  
**Question Pattern**: Medical definition matching to test knowledge beyond visual pattern recognition  

## Template Description

This template converts binary classification datasets into MCVQA format by asking which medical definition best describes what is shown in the image. It tests the model's understanding of medical terminology and pathophysiology, requiring both visual recognition and conceptual knowledge. This approach goes beyond simple pattern matching to ensure models truly understand what medical conditions represent.

## Question Generation Pattern

### Question Format
```
"Which definition best describes what is shown in this {modality} image?"
```

### Answer Format
- **Multiple Choice**: Four definition options (A, B, C, D)
- **Positive cases**: Correct definition of target condition + 3 related distractors
- **Negative cases**: 3 plausible but incorrect definitions + "None of the above definitions apply"

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus photograph", "skin lesion")
- `{target_definition}`: Accurate medical definition of the target condition
- `{distractor_definitions}`: Medically accurate definitions of related but different conditions

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Which definition best describes what is shown in this {modality} image?",
  "answer": "A" | "B" | "C" | "D",
  "answer_type": "single_label",
  "options": ["Definition A text", "Definition B text", "Definition C text", "Definition D text"],
  "difficulty": "hard",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Definition-based assessment testing medical knowledge beyond visual recognition",
  "provenance": {
    "original_label": "{original_label_value}",
    "rule_id": "classification_binary_8",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Medical Context**: Well-defined medical conditions with established definitions
- **Educational Value**: Conditions where understanding definitions is clinically important
- **Clear Pathophysiology**: Conditions with distinct pathophysiological mechanisms

## Template Usage Rules

1. **Definition Quality**: Use medically accurate, textbook-level definitions
2. **Appropriate Complexity**: Match definition complexity to clinical context
3. **Distractor Selection**: Choose definitions of conditions from the same medical domain
4. **Terminology Standards**: Use established medical terminology (avoid colloquialisms)
5. **Negative Case Structure**: Always include "None of the above definitions apply" for Label = 0

## Examples

### Example 1: Chest X-ray Pneumonia Detection
**Original Dataset**: ChestX-ray14 Pneumonia subset  
**Original Label**: 1 (pneumonia present)  
**Generated Q&A**:
- **Question**: "Which definition best describes what is shown in this chest X-ray image?"
- **Options**:
  - A: "Acute inflammation of lung parenchyma with consolidation and exudate formation"
  - B: "Collection of air in the pleural space causing lung collapse"
  - C: "Abnormal accumulation of fluid in the pleural cavity"
  - D: "Enlargement of the cardiac silhouette beyond normal limits"
- **Answer**: "A"
- **Rationale**: "Definition A accurately describes pneumonia pathophysiology"

### Example 2: Fundus Normal Case
**Original Dataset**: Diabetic Retinopathy Detection  
**Original Label**: 0 (no diabetic retinopathy)  
**Generated Q&A**:
- **Question**: "Which definition best describes what is shown in this fundus photograph?"
- **Options**:
  - A: "Progressive retinal vascular damage due to chronic hyperglycemia"
  - B: "Optic nerve damage characterized by increased intraocular pressure"
  - C: "Central retinal degeneration affecting photoreceptor cells"
  - D: "None of the above definitions apply"
- **Answer**: "D"
- **Rationale**: "Normal fundus does not match any pathological definition"

### Example 3: Skin Lesion Melanoma Detection
**Original Dataset**: ISIC Melanoma Classification  
**Original Label**: 1 (melanoma present)  
**Generated Q&A**:
- **Question**: "Which definition best describes what is shown in this skin lesion image?"
- **Options**:
  - A: "Malignant tumor arising from melanocytes with potential for metastasis"
  - B: "Slow-growing malignant tumor of basal keratinocytes"
  - C: "Benign proliferation of melanocytes in nests"
  - D: "Hyperkeratotic lesion due to chronic sun exposure"
- **Answer**: "A"
- **Rationale**: "Definition A correctly describes melanoma pathology"

### Example 4: Brain MRI Normal Case
**Original Dataset**: Brain Tumor Detection  
**Original Label**: 0 (no tumor)  
**Generated Q&A**:
- **Question**: "Which definition best describes what is shown in this brain MRI image?"
- **Options**:
  - A: "Abnormal proliferation of brain tissue with mass effect"
  - B: "Acute loss of brain function due to vascular occlusion"
  - C: "Inflammation of brain tissue due to infectious agents"
  - D: "None of the above definitions apply"
- **Answer**: "D"
- **Rationale**: "Normal brain anatomy does not match any pathological definition"

### Example 5: Chest CT Pulmonary Embolism Detection
**Original Dataset**: Pulmonary Embolism Detection  
**Original Label**: 1 (pulmonary embolism present)  
**Generated Q&A**:
- **Question**: "Which definition best describes what is shown in this chest CT image?"
- **Options**:
  - A: "Blockage of pulmonary arteries by embolic material"
  - B: "Acute inflammation of lung parenchyma with consolidation"
  - C: "Chronic scarring and thickening of lung tissue"
  - D: "Abnormal dilation of pulmonary arteries"
- **Answer**: "A"
- **Rationale**: "Definition A accurately describes pulmonary embolism pathophysiology"

## Implementation Notes

### Advantages
- **Knowledge Testing**: Tests medical understanding beyond visual pattern recognition
- **Educational Value**: Teaches precise medical terminology and pathophysiology
- **Prevents Memorization**: Cannot be solved through visual shortcuts alone
- **Clinical Relevance**: Understanding definitions is essential for medical practice
- **Comprehensive Assessment**: Tests both recognition and comprehension

### Limitations
- **High Complexity**: Requires extensive medical knowledge database
- **Definition Dependency**: Quality depends on accurate, well-written definitions
- **Context Sensitivity**: Some conditions may have multiple valid definitions
- **Implementation Difficulty**: Requires careful curation of definition pools

### Quality Considerations
- **Medical Accuracy**: All definitions must be medically correct and current
- **Clarity**: Definitions should be clear and unambiguous
- **Appropriate Level**: Match definition complexity to target audience
- **Consistency**: Maintain consistent definition style and depth
- **Expert Validation**: Have medical experts review all definitions

### Definition Sources
- **Medical Textbooks**: Standard reference textbooks for each specialty
- **Professional Guidelines**: Specialty society definitions and criteria
- **Medical Dictionaries**: Established medical terminology references
- **Peer-Reviewed Literature**: Current research-based definitions

### Implementation Strategy
- **Domain Expertise**: Collaborate with medical experts for each specialty
- **Definition Databases**: Build curated pools of high-quality definitions
- **Validation Process**: Multiple expert review of definition accuracy
- **Regular Updates**: Keep definitions current with medical knowledge
- **Quality Control**: Systematic review of definition appropriateness

### Clinical Educational Value
- **Terminology Mastery**: Reinforces proper medical vocabulary
- **Pathophysiology Understanding**: Tests mechanistic knowledge
- **Differential Diagnosis**: Helps distinguish between similar conditions
- **Clinical Communication**: Improves precision in medical communication
