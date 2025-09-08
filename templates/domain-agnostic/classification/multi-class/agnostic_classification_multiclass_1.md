# Multi-Class Classification Template 1: Basic Condition Identification

## Template Overview

- **Template ID**: agnostic_classification_multiclass_1
- **Task Type**: Multi-class classification
- **Difficulty**: Easy
- **Pattern**: Direct condition identification with multiple choice options
- **Domain**: Domain-agnostic (works across all medical specialties)

## Template Description

This template converts multi-class medical datasets into MCVQA format by asking direct questions about what medical condition is shown in an image. The template presents multiple specific medical conditions as answer options, where exactly one condition is correct. This approach mirrors clinical differential diagnosis scenarios where medical professionals must distinguish between several possible conditions.

The template is designed to work with datasets that have 3 or more mutually exclusive condition labels, making it suitable for a wide range of medical classification tasks across different specialties including radiology, pathology, dermatology, and ophthalmology.

## Question Generation Pattern

### Question Format
`"What medical condition is shown in this {modality} image?"`

### Answer Format
Multiple choice with options A, B, C, D, etc. (number of options matches dataset classes)

### Template Variables
- `{modality}`: Imaging modality (e.g., "chest X-ray", "fundus", "dermoscopy", "histopathology")
- `{condition_list}`: List of specific medical conditions from the dataset label set

### Example Pattern
```
Question: "What medical condition is shown in this chest X-ray image?"
A. Pneumonia
B. Pleural effusion  
C. Pneumothorax
D. Normal/No finding
```

## Mapping to Datum Schema

```json
{
  "questions-and-answers": [
    {
      "qa_id": "1",
      "task": "Classification",
      "question": "What medical condition is shown in this {modality} image?",
      "answer": "{correct_condition_label}",
      "answer_type": "single_label",
      "options": ["{condition_1}", "{condition_2}", "{condition_3}", "{condition_4}"],
      "difficulty": "easy",
      "uncertainty": "certain",
      "answer_confidence": 1.0,
      "rationale": "Multi-class condition identification using original dataset labels",
      "provenance": {
        "original_label": "{dataset_original_label}",
        "rule_id": "agnostic_classification_multiclass_1",
        "annotation_id": null,
        "created_by": "program"
      }
    }
  ]
}
```

## Dataset Requirements

### Essential Requirements
- **Multi-class labels**: Dataset must have 3+ mutually exclusive condition labels
- **Single ground truth**: Each image must have exactly one correct condition label
- **Medical conditions**: Labels must represent distinct medical conditions, findings, or diagnoses
- **Imaging data**: Dataset must contain medical images (any modality)

### Compatible Dataset Types
- Chest X-ray datasets with multiple pulmonary conditions
- Skin lesion datasets with multiple dermatological conditions  
- Fundus datasets with multiple ophthalmological conditions
- Histopathology datasets with multiple tissue/cancer types
- Brain imaging datasets with multiple neurological conditions

### Label Format Compatibility
- Categorical labels (string condition names)
- Numeric labels with condition mapping provided
- Multi-class datasets from medical vision taxonomy

## Template Usage Rules

### Implementation Guidelines
1. **Condition Ordering**: Randomize option order to prevent position bias
2. **Medical Terminology**: Use exact medical terminology from original dataset when clinically appropriate
3. **Option Count**: Include all dataset classes as options (3-8 options recommended for readability)
4. **Modality Specification**: Always specify the imaging modality in the question for context

### Quality Requirements
- All condition names must be medically accurate and specific
- Avoid ambiguous or overly general condition names
- Ensure mutual exclusivity between all options
- Verify clinical relevance of condition combinations

### Domain Adaptation
- **Radiology**: Use anatomically specific condition names (e.g., "pulmonary edema" vs "edema")
- **Pathology**: Include tissue type and grade when relevant (e.g., "adenocarcinoma grade 2")
- **Dermatology**: Use standard dermatological terminology (e.g., "seborrheic keratosis")
- **Ophthalmology**: Include anatomical specificity (e.g., "diabetic macular edema")

## Examples

### Example 1: Chest X-ray Multi-Class (4 conditions)
**Original Dataset**: Chest pathology classification
**Question**: "What medical condition is shown in this chest X-ray image?"
**Options**: 
- A. Pneumonia
- B. Pleural effusion
- C. Pneumothorax  
- D. Normal chest
**Answer**: "A" (if pneumonia is the ground truth label)

### Example 2: Skin Lesion Classification (5 conditions)
**Original Dataset**: Dermatology multi-class dataset
**Question**: "What medical condition is shown in this dermoscopy image?"
**Options**:
- A. Melanoma
- B. Basal cell carcinoma
- C. Seborrheic keratosis
- D. Actinic keratosis
- E. Nevus
**Answer**: "C" (if seborrheic keratosis is the ground truth label)

### Example 3: Fundus Multi-Class (4 conditions)
**Original Dataset**: Retinal disease classification
**Question**: "What medical condition is shown in this fundus image?"
**Options**:
- A. Diabetic retinopathy
- B. Glaucoma
- C. Age-related macular degeneration
- D. Normal retina
**Answer**: "B" (if glaucoma is the ground truth label)

### Example 4: Brain MRI Classification (3 conditions)
**Original Dataset**: Brain tumor classification
**Question**: "What medical condition is shown in this brain MRI image?"
**Options**:
- A. Glioma
- B. Meningioma
- C. Pituitary adenoma
**Answer**: "A" (if glioma is the ground truth label)

### Example 5: Histopathology Classification (6 conditions)
**Original Dataset**: Tissue type classification
**Question**: "What medical condition is shown in this histopathology image?"
**Options**:
- A. Adenocarcinoma
- B. Squamous cell carcinoma
- C. Small cell carcinoma
- D. Large cell carcinoma
- E. Normal tissue
- F. Benign lesion
**Answer**: "D" (if large cell carcinoma is the ground truth label)

## Implementation Notes

### Advantages
- **Clinical Relevance**: Directly maps to differential diagnosis scenarios
- **Scalability**: Works with any number of condition classes (3+)
- **Domain Flexibility**: Applicable across all medical imaging specialties
- **Evaluation Clarity**: Unambiguous success/failure assessment
- **Educational Value**: Teaches condition recognition and differentiation

### Limitations
- **No Severity Assessment**: Does not capture disease severity or staging
- **Single Condition Focus**: Cannot handle cases with multiple co-occurring conditions
- **No Spatial Information**: Does not assess localization or regional analysis
- **Label Dependency**: Quality depends on original dataset label accuracy and specificity

### Quality Considerations
- **Medical Accuracy**: All condition names must be clinically correct and current
- **Diagnostic Realism**: Option combinations should reflect realistic differential diagnoses
- **Terminology Consistency**: Use standardized medical terminology when available
- **Expert Validation**: Consider medical expert review for complex condition sets
- **Bias Prevention**: Randomize option ordering to prevent systematic bias

### Implementation Recommendations
- Use established medical ontologies (ICD-10, SNOMED CT) for condition naming when possible
- Include "Normal" or "No finding" as an option when appropriate to the dataset
- Limit options to 3-8 choices to maintain readability and prevent cognitive overload
- Ensure condition options are at similar levels of diagnostic specificity
- Consider domain-specific validation by medical professionals in relevant specialties
