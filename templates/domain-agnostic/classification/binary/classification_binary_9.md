# Binary Classification Template 9: Multi-Doctor Clinical Assessment

## Template Overview

**Template ID**: `classification_binary_9`  
**Task Type**: Binary Classification  
**Difficulty**: Hard  
**Question Pattern**: Multi-physician clinical reasoning with diagnostic disagreement scenarios  

## Template Description

This template converts binary classification datasets into MCVQA format by presenting clinical scenarios where three doctors provide different assessments of the same image. It tests the model's ability to evaluate competing clinical opinions and identify diagnostic errors in complex scenarios. This approach mirrors real-world clinical consultations and second opinion scenarios, testing advanced clinical reasoning capabilities.

**⚠️ IMPLEMENTATION STATUS**: Currently implemented for positive cases only. Negative case structure requires further refinement and will be implemented in a future update.

## Question Generation Pattern

### Question Format (Positive Cases Only)
```
"Three doctors examined this {modality} image:
- Doctor A suggests: {target_condition, related_condition_1, related_condition_2}
- Doctor B suggests: {target_condition, different_related_1, different_related_2}  
- Doctor C suggests: {unrelated_condition_1, unrelated_condition_2, unrelated_condition_3}
Which doctor missed a finding that is definitely present?"
```

### Answer Format
- **Positive cases (Label = 1)**: "Doctor C" (who missed the target condition)
- **Negative cases (Label = 0)**: **TODO - Structure needs refinement**

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus photograph", "brain MRI")
- `{target_condition}`: The medical condition that is actually present (positive cases)
- `{related_conditions}`: Medically plausible conditions from the same domain
- `{unrelated_conditions}`: Conditions from different anatomical systems or domains

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Three doctors examined this {modality} image: [doctor assessments]. Which doctor missed a finding that is definitely present?",
  "answer": "Doctor A" | "Doctor B" | "Doctor C",
  "answer_type": "single_label",
  "options": ["Doctor A", "Doctor B", "Doctor C", "No doctor missed any findings"],
  "difficulty": "hard",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Multi-doctor clinical assessment testing diagnostic reasoning",
  "provenance": {
    "original_label": "{original_label_value}",
    "rule_id": "classification_binary_9",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Clinical Context**: Well-defined medical conditions with established differential diagnoses
- **Domain Knowledge**: Conditions with known related and unrelated alternatives
- **Educational Value**: Cases where multiple clinical opinions are realistic

## Template Usage Rules

### For Positive Cases (Label = 1):
1. **Doctor A & B**: Both must include the target condition plus related plausible alternatives
2. **Doctor C**: Must include only unrelated conditions that miss the target entirely
3. **Answer**: Always "Doctor C" who missed the present finding
4. **Related Conditions**: Should be from the same anatomical domain or imaging modality
5. **Unrelated Conditions**: Should be from different systems to clearly distinguish the miss

### For Negative Cases (Label = 0):
**⚠️ TODO**: Negative case structure needs refinement before implementation
- Multiple approaches considered but require further evaluation
- Issues with ensuring single correct answer and clinical appropriateness
- Will be addressed in future template update

## Examples

### Example 1: Chest X-ray Pneumonia Detection
**Original Dataset**: ChestX-ray14 Pneumonia subset  
**Original Label**: 1 (pneumonia present)  
**Generated Q&A**:
- **Question**: "Three doctors examined this chest X-ray image:
  - Doctor A suggests: Pneumonia, bronchitis, or respiratory infection
  - Doctor B suggests: Pneumonia, atelectasis, or consolidation
  - Doctor C suggests: Cardiomegaly, pleural thickening, or rib fracture
  Which doctor missed a finding that is definitely present?"
- **Answer**: "Doctor C"
- **Rationale**: "Doctor C missed pneumonia, which is definitely present in the image"

### Example 2: Fundus Diabetic Retinopathy Detection
**Original Dataset**: Diabetic Retinopathy Detection  
**Original Label**: 1 (diabetic retinopathy present)  
**Generated Q&A**:
- **Question**: "Three doctors examined this fundus photograph:
  - Doctor A suggests: Diabetic retinopathy, hypertensive retinopathy, or macular degeneration
  - Doctor B suggests: Diabetic retinopathy, glaucoma, or retinal vein occlusion
  - Doctor C suggests: Cataracts, refractive error, or normal aging changes
  Which doctor missed a finding that is definitely present?"
- **Answer**: "Doctor C"
- **Rationale**: "Doctor C missed diabetic retinopathy, focusing on anterior segment issues"

### Example 3: Skin Lesion Melanoma Detection
**Original Dataset**: ISIC Melanoma Classification  
**Original Label**: 1 (melanoma present)  
**Generated Q&A**:
- **Question**: "Three doctors examined this skin lesion image:
  - Doctor A suggests: Melanoma, dysplastic nevus, or atypical mole
  - Doctor B suggests: Melanoma, basal cell carcinoma, or squamous cell carcinoma
  - Doctor C suggests: Eczema, psoriasis, or contact dermatitis
  Which doctor missed a finding that is definitely present?"
- **Answer**: "Doctor C"
- **Rationale**: "Doctor C focused on inflammatory conditions, missing the malignant lesion"

### Example 4: Brain MRI Tumor Detection
**Original Dataset**: Brain Tumor Detection  
**Original Label**: 1 (brain tumor present)  
**Generated Q&A**:
- **Question**: "Three doctors examined this brain MRI image:
  - Doctor A suggests: Brain tumor, metastasis, or glioma
  - Doctor B suggests: Brain tumor, stroke, or hemorrhage
  - Doctor C suggests: Motion artifact, poor image quality, or technical issues
  Which doctor missed a finding that is definitely present?"
- **Answer**: "Doctor C"
- **Rationale**: "Doctor C attributed findings to technical factors, missing the actual tumor"

### Example 5: Chest CT Pulmonary Embolism Detection
**Original Dataset**: Pulmonary Embolism Detection  
**Original Label**: 1 (pulmonary embolism present)  
**Generated Q&A**:
- **Question**: "Three doctors examined this chest CT image:
  - Doctor A suggests: Pulmonary embolism, deep vein thrombosis, or clot
  - Doctor B suggests: Pulmonary embolism, pneumonia, or infarction
  - Doctor C suggests: Emphysema, bronchiectasis, or chronic changes
  Which doctor missed a finding that is definitely present?"
- **Answer**: "Doctor C"
- **Rationale**: "Doctor C focused on chronic conditions, missing the acute embolism"

## Implementation Notes

### Advantages
- **Clinical Realism**: Mirrors real-world clinical disagreements and consultations
- **Complex Reasoning**: Tests ability to evaluate multiple clinical opinions
- **Educational Value**: Demonstrates importance of comprehensive differential diagnosis
- **Safety Testing**: Identifies dangerous diagnostic omissions
- **Meta-Cognitive**: Tests reasoning about clinical reasoning

### Limitations
- **High Complexity**: Requires extensive medical knowledge for realistic scenarios
- **Implementation Difficulty**: Complex to generate appropriate doctor opinions
- **Partial Implementation**: Negative cases not yet implemented
- **Domain Dependency**: Requires detailed knowledge of differential diagnoses
- **Quality Control**: Difficult to ensure all doctor opinions are clinically plausible

### Quality Considerations
- **Medical Accuracy**: All doctor suggestions must be clinically plausible
- **Appropriate Difficulty**: Unrelated conditions should be clearly different from target
- **Clinical Realism**: Doctor opinions should reflect realistic clinical reasoning
- **Consistency**: Maintain consistent quality across different medical domains
- **Expert Validation**: Requires review by medical experts for clinical appropriateness

### TODO: Negative Case Implementation
**Issue**: Need to develop structure for cases where target condition is absent

**Challenges**:
- Ensuring single correct answer when target condition is not present
- Avoiding ambiguity about what constitutes "appropriate" assessment
- Maintaining clinical realism while ensuring clear evaluation criteria

**Potential Approaches Under Consideration**:
1. Target condition avoidance: "Which doctor correctly avoided suggesting [condition]?"
2. Most appropriate assessment: "Which doctor provided the most clinically appropriate assessment?"
3. Conservative approach: "Which doctor avoided overdiagnosis?"

**Next Steps**: 
- Refine negative case question structure
- Validate approach with medical experts
- Implement and test negative case examples
- Update template with complete positive/negative case coverage

### Implementation Strategy
- **Domain Expertise**: Collaborate with specialists for each medical domain
- **Opinion Pools**: Develop realistic doctor opinion sets for different conditions
- **Validation Process**: Medical expert review of all doctor assessment combinations
- **Quality Control**: Systematic review of clinical appropriateness and realism
