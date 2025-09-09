# Binary Classification Template 4: Likelihood Assessment

## Template Overview

**Template ID**: `domain-agnostic_classification_binary_medium_4`  
**Task Type**: Binary classification  
**Difficulty**: Medium  
**Question Pattern**: Probabilistic assessment with text-based likelihood categories  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires understanding of clinical probability and diagnostic confidence levels. Knowledge of how to express medical uncertainty using descriptive likelihood categories that reflect real-world clinical decision-making processes.  

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
- `{condition}`: The medical condition or finding being assessed. Extracted from dataset metadata and incorporated into question text to specify what condition likelihood is being evaluated.
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus photograph", "skin lesion"). Used in question text to provide clinical context about the type of medical examination.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, allowing for comprehensive clinical assessment of condition likelihood.

### Answer Construction
**For Positive Cases (original label = 1)**:
- Map to high confidence categories: "Likely" or "Very likely"
- Selection based on dataset confidence levels or clinical severity
- Higher severity/confidence → "Very likely", moderate → "Likely"

**For Negative Cases (original label = 0)**:
- Map to low confidence categories: "Very unlikely" or "Unlikely"  
- Selection based on how definitively the condition can be excluded
- Clear absence → "Very unlikely", some uncertainty → "Unlikely"


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels that can be mapped to likelihood categories with clinical confidence levels
- **Clinical Context**: Scenarios where probabilistic assessment is clinically meaningful and diagnostically relevant
- **Image Level**: Whole image classification
- **Datasets from metadata file**: Compatible datasets include diagnostic imaging datasets with clear positive/negative classifications available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Use specific medical condition names and appropriate imaging modality descriptions, maintaining consistent likelihood thresholds across similar clinical contexts
- **Label mapping rules**: Convert original dataset annotations to likelihood categories:
  - Positive cases (1, "positive", "present") → "Likely" or "Very likely" based on clinical confidence
  - Negative cases (0, "negative", "absent") → "Very unlikely" or "Unlikely" based on exclusion confidence
- **Conversion Process**: Extract binary labels from original dataset, identify condition name and modality from metadata, map to appropriate likelihood category (Very unlikely 0-25%, Unlikely 25-50%, Likely 50-75%, Very likely 75-100%), present raw images without modifications, validate MCVQA compliance with single correct answer
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "medium", options array with 4 likelihood choices, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_binary_medium_4"

## Examples

### Example 1: Chest X-ray Pneumonia Assessment
**Original Dataset Context and Annotation Format**: ChestX-ray14 dataset with binary labels in CSV format (image_id, pneumonia_label) where 1 = pneumonia present, 0 = no pneumonia  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "What is the likelihood of pneumonia in this chest X-ray image?"
- **Answer Choices**: ["Very unlikely", "Unlikely", "Likely", "Very likely"]
- **Correct Answer**: "Very likely"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV indicating pneumonia presence
2. Identify "pneumonia" as condition from dataset metadata and "chest X-ray" as modality
3. Map positive case to high confidence category based on radiographic evidence strength
4. Select "Very likely" for strong radiographic features supporting pneumonia diagnosis
5. Create 4-option likelihood question maintaining MCVQA compliance with single correct answer  
**Clinical Rationale**: Positive pneumonia case with clear radiographic features (consolidation, air bronchograms, opacity patterns) that strongly suggest pneumonia diagnosis, requiring high confidence likelihood assessment that reflects diagnostic certainty level

### Example 2: Fundus Diabetic Retinopathy Assessment  
**Original Dataset Context and Annotation Format**: Diabetic retinopathy screening dataset with binary labels where 0 = no diabetic retinopathy, 1 = diabetic retinopathy present  
**Image Presentation Method**: Raw fundus photograph displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "What is the likelihood of diabetic retinopathy in this fundus photograph?"
- **Answer Choices**: ["Very unlikely", "Unlikely", "Likely", "Very likely"] 
- **Correct Answer**: "Very unlikely"  
**Complete Conversion Process Explanation**:
1. Extract binary label "0" from dataset indicating no diabetic retinopathy
2. Identify "diabetic retinopathy" as condition and "fundus photograph" as modality from metadata
3. Map negative case to low confidence category based on retinal examination findings
4. Select "Very unlikely" for clear absence of diabetic retinopathy signs (microaneurysms, hemorrhages, exudates)
5. Validate 4-option likelihood format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Normal fundus examination with no signs of diabetic retinopathy (no microaneurysms, dot-blot hemorrhages, hard exudates, or cotton wool spots), warranting very low likelihood assessment that reflects strong evidence against diabetic retinopathy presence
