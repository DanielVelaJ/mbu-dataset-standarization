# Binary Classification Template 9: Multi-Doctor Clinical Assessment

## Template Overview

**Template ID**: `domain-agnostic_classification_binary_hard_9`  
**Task Type**: Binary classification  
**Difficulty**: Hard  
**Question Pattern**: Multi-physician clinical reasoning with diagnostic disagreement scenarios  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires advanced clinical reasoning and ability to evaluate competing medical opinions. Knowledge of diagnostic accuracy, clinical differential diagnosis, and understanding of how different specialists might interpret the same imaging findings. Tests complex medical decision-making scenarios.  

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
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus photograph", "brain MRI"). Used to specify the type of clinical examination being evaluated by multiple physicians.
- `{target_condition}`: The medical condition that is actually present (positive cases). The correct diagnosis that some doctors identify and others miss.
- `{related_conditions}`: Medically plausible conditions from the same domain. Used to create realistic clinical differential diagnoses.
- `{unrelated_conditions}`: Conditions from different anatomical systems or domains. Used to represent misguided diagnostic reasoning.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, simulating real clinical consultation scenarios.

### Answer Construction
**For Positive Cases (original label = 1)**:
- Target condition is present and should be identified
- Doctor A and B include target condition in their assessments with related differentials
- Doctor C provides unrelated conditions, missing the target (incorrect)
- Answer: "Doctor C" (who missed the present finding)

**For Negative Cases (original label = 0)**:
- Currently requires implementation refinement
- Structure needs development for scenarios where no condition is present
- Future implementation will address negative case scenarios


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Clinical Context**: Well-defined medical conditions with established differential diagnoses and multiple plausible clinical interpretations
- **Domain Knowledge**: Conditions with known related and unrelated alternatives across different anatomical systems
- **Educational Value**: Cases where multiple clinical opinions are realistic and diagnostically challenging
- **Datasets from metadata file**: Compatible datasets include complex diagnostic imaging datasets with clear positive findings available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Create realistic clinical consultation scenarios with three physicians providing different assessments, focusing on positive cases where target condition is present
- **Label mapping rules**: Convert original dataset annotations to multi-physician assessment format:
  - Positive cases (1, "positive", "present") → Doctor A & B include target condition with related differentials, Doctor C misses target with unrelated conditions, Answer: "Doctor C"
  - Negative cases (0, "negative", "absent") → Currently requires implementation refinement (TODO)
- **Conversion Process**: Extract binary labels from original dataset, identify target condition and related/unrelated conditions from medical knowledge, construct three physician assessment scenarios with realistic differential diagnoses, present raw images without modifications, validate MCVQA compliance with single correct answer (currently positive cases only)
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "hard", options array with 4 physician choices, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_binary_hard_9"

## Examples

### Example 1: Chest X-ray Pneumonia Detection
**Original Dataset Context and Annotation Format**: ChestX-ray14 dataset with binary labels in CSV format (image_id, pneumonia_label) where 1 = pneumonia present, 0 = no pneumonia  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Three doctors examined this chest X-ray image: Doctor A suggests: Pneumonia, bronchitis, or respiratory infection; Doctor B suggests: Pneumonia, atelectasis, or consolidation; Doctor C suggests: Cardiomegaly, pleural thickening, or rib fracture. Which doctor missed a finding that is definitely present?"
- **Answer Choices**: ["Doctor A", "Doctor B", "Doctor C", "No doctor missed any findings"]
- **Correct Answer**: "Doctor C"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV indicating pneumonia presence
2. Identify "pneumonia" as target condition from dataset metadata and "chest X-ray" as modality
3. Construct three physician scenarios: Doctor A & B include pneumonia with related respiratory conditions, Doctor C suggests unrelated cardiac/thoracic conditions
4. Doctor C misses the target condition (pneumonia), making them the correct answer
5. Validate multi-physician assessment format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Pneumonia case testing ability to identify diagnostic errors in clinical consultation scenarios - Doctor A and B appropriately consider pneumonia alongside related respiratory conditions while Doctor C focuses on unrelated cardiac and structural abnormalities, demonstrating dangerous diagnostic miss requiring clinical reasoning evaluation

### Example 2: Fundus Diabetic Retinopathy Detection
**Original Dataset Context and Annotation Format**: Diabetic retinopathy screening dataset with binary labels where 0 = no diabetic retinopathy, 1 = diabetic retinopathy present  
**Image Presentation Method**: Raw fundus photograph displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Three doctors examined this fundus photograph: Doctor A suggests: Diabetic retinopathy, hypertensive retinopathy, or macular degeneration; Doctor B suggests: Diabetic retinopathy, glaucoma, or retinal vein occlusion; Doctor C suggests: Cataracts, refractive error, or normal aging changes. Which doctor missed a finding that is definitely present?"
- **Answer Choices**: ["Doctor A", "Doctor B", "Doctor C", "No doctor missed any findings"] 
- **Correct Answer**: "Doctor C"  
**Complete Conversion Process Explanation**:
1. Extract binary label "1" from dataset indicating diabetic retinopathy presence
2. Identify "diabetic retinopathy" as target condition and "fundus photograph" as modality from metadata
3. Construct three physician scenarios: Doctor A & B include diabetic retinopathy with related posterior segment conditions, Doctor C suggests anterior segment issues
4. Doctor C misses the retinal pathology by focusing on anterior segment, making them the incorrect physician
5. Verify multi-physician assessment format with single correct answer structure for MCVQA compliance  
**Clinical Rationale**: Diabetic retinopathy case requiring evaluation of competing clinical opinions - Doctor A and B appropriately consider posterior segment pathology including diabetic retinopathy while Doctor C incorrectly focuses on anterior segment issues (cataracts, refractive errors), missing the actual retinal vascular pathology present in the fundus examination
