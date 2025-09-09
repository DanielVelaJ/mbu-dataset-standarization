# Binary Classification Template 5: Exclusionary Assessment

## Template Overview

**Template ID**: `domain-agnostic_classification_binary_medium_5`  
**Task Type**: Binary classification  
**Difficulty**: Medium  
**Question Pattern**: Rule-out assessment to test negative predictive reasoning  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires understanding of clinical exclusion criteria and negative predictive reasoning. Knowledge of when conditions can safely be ruled out versus when they cannot be excluded, which is critical for avoiding dangerous false negatives in clinical practice.  

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
- `{condition}`: The medical condition or finding being assessed for exclusion. Extracted from dataset metadata and used to specify what condition is being evaluated for rule-out.
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus photograph", "brain MRI"). Incorporated into question text to provide clinical context about the diagnostic imaging method.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, allowing for comprehensive clinical assessment of exclusion criteria.

### Answer Construction
**For Positive Cases (original label = 1)**:
- Condition is present, therefore cannot be ruled out
- Answer: "No, cannot be ruled out"
- Logic: Presence of condition means exclusion is impossible

**For Negative Cases (original label = 0)**:
- Condition is absent, therefore can be ruled out
- Answer: "Yes, can be ruled out"
- Logic: Absence of condition allows for safe exclusion


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels where exclusionary reasoning is clinically appropriate and diagnostically meaningful
- **Clinical Context**: Scenarios where ruling out conditions is a critical clinical decision with safety implications
- **Image Level**: Whole image classification
- **Datasets from metadata file**: Compatible datasets include emergency imaging datasets, screening datasets, and diagnostic datasets where condition exclusion has clinical significance, available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Focus on conditions where exclusion has clinical significance and ensure the imaging modality is capable of detecting or excluding the condition
- **Label mapping rules**: Convert original dataset annotations using inverted logic for exclusionary reasoning:
  - Negative cases (0, "negative", "absent") → "Yes, can be ruled out" (condition absent, safe to exclude)
  - Positive cases (1, "positive", "present") → "No, cannot be ruled out" (condition present, cannot exclude)
- **Conversion Process**: Extract binary labels from original dataset, identify condition and modality from metadata, apply inverted logic mapping for exclusionary framework, present raw images without modifications, validate MCVQA compliance with single correct answer, emphasize safety scenarios where missing a condition could be harmful
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "medium", options array with 2 exclusion choices, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_binary_medium_5"

## Examples

### Example 1: Chest X-ray Pneumothorax Exclusion
**Original Dataset Context and Annotation Format**: Pneumothorax detection dataset with binary labels in CSV format (image_id, pneumothorax_label) where 1 = pneumothorax present, 0 = no pneumothorax  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Can pneumothorax be ruled out based on this chest X-ray image?"
- **Answer Choices**: ["Yes, can be ruled out", "No, cannot be ruled out"]
- **Correct Answer**: "No, cannot be ruled out"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV indicating pneumothorax presence
2. Identify "pneumothorax" as condition and "chest X-ray" as modality from dataset metadata
3. Apply inverted logic mapping: positive case (1) → "No, cannot be ruled out"
4. Logic: If pneumothorax is present, it cannot be safely excluded from imaging
5. Validate exclusionary reasoning format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Pneumothorax is present with visible pleural line separation and lung collapse, making exclusion impossible and potentially dangerous - critical safety scenario where missing diagnosis could lead to respiratory compromise requiring immediate intervention

### Example 2: Brain CT Stroke Exclusion  
**Original Dataset Context and Annotation Format**: Acute stroke detection dataset with binary labels where 0 = no acute stroke, 1 = acute stroke present  
**Image Presentation Method**: Raw brain CT image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Can acute stroke be ruled out based on this brain CT image?"
- **Answer Choices**: ["Yes, can be ruled out", "No, cannot be ruled out"] 
- **Correct Answer**: "Yes, can be ruled out"  
**Complete Conversion Process Explanation**:
1. Extract binary label "0" from dataset indicating no acute stroke
2. Identify "acute stroke" as condition and "brain CT" as modality from metadata
3. Apply inverted logic mapping: negative case (0) → "Yes, can be ruled out"
4. Logic: If no stroke is present, condition can be safely excluded based on CT findings
5. Verify exclusionary assessment format with single correct answer structure  
**Clinical Rationale**: Normal brain CT with no evidence of acute ischemic changes, hemorrhage, or mass effect, allowing safe exclusion of acute stroke - enables confident clinical decision-making for emergency treatment pathways and thrombolytic therapy eligibility
