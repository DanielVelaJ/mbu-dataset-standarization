# Binary Classification Template 3: Normal vs Abnormal Assessment

## Template Overview

**Template ID**: `domain-agnostic_classification_binary_easy_3`  
**Task Type**: Binary classification  
**Difficulty**: Easy  
**Question Pattern**: Normal vs abnormal classification for medical screening  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires basic understanding of normal versus abnormal findings in medical imaging. No specialized domain expertise needed as template works across all medical fields using general concepts of screening and abnormality detection.  

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
- `{modality}`: The imaging modality with appropriate descriptors (e.g., "chest X-ray", "fundus photograph", "skin lesion", "brain MRI"). Incorporated into question text to provide clinical context and specify the type of medical examination being performed.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, allowing for comprehensive assessment of overall normalcy versus abnormality.

### Answer Construction
**Correct Answer Generation**:
- Extract the binary label from the original dataset (0/1, normal/abnormal, negative/positive)
- Map normal cases (0, "normal", "healthy", "negative") to "Normal"
- Map abnormal cases (1, "abnormal", "pathological", "positive") to "Abnormal"

**Answer Format**: Binary choice between "Normal" and "Abnormal" options, maintaining MCVQA compliance with exactly one correct answer per question.


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels where 0 = normal/healthy and 1 = abnormal/pathological
- **Clinical Context**: Screening or general abnormality detection scenarios
- **Image Level**: Whole image classification
- **Datasets from metadata file**: Compatible datasets include general screening datasets, chest X-ray screening, fundus photography screening, mammography screening, brain imaging screening, and other normal/abnormal classification datasets available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Use clinically appropriate modality descriptions and maintain consistent terminology with "Normal" and "Abnormal" as the only answer options
- **Label mapping rules**: Convert original dataset annotations as follows:
  - Label "0", "normal", "healthy", "negative" → "Normal"
  - Label "1", "abnormal", "pathological", "positive" → "Abnormal"
- **Conversion Process**: Extract binary labels from original dataset, map to normal/abnormal format, generate questions using modality from dataset metadata, present raw images without modifications, validate MCVQA compliance with single correct answer, best suited for screening datasets rather than specific disease detection
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with 2 choices ["Normal", "Abnormal"], and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_binary_easy_3"

## Examples

### Example 1: Chest X-ray Screening
**Original Dataset Context and Annotation Format**: General chest X-ray screening dataset with binary labels in CSV format (image_id, abnormality_label) where 0 = normal chest, 1 = abnormal findings  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Is this chest X-ray image normal or abnormal?"
- **Answer Choices**: ["Normal", "Abnormal"]
- **Correct Answer**: "Normal"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "0" from dataset CSV indicating normal chest
2. Map "0" to normal case in normal/abnormal framework
3. Insert "chest X-ray" as {modality} into question template
4. Generate "Normal" answer based on negative label mapping
5. Validate MCVQA compliance with single correct answer from two options  
**Clinical Rationale**: Normal chest radiograph with no pathological findings detected, demonstrating clear distinction between normal anatomy and any potential abnormalities that would require clinical attention

### Example 2: Fundus Photography Screening  
**Original Dataset Context and Annotation Format**: Diabetic retinopathy screening dataset with binary labels where 0 = no retinopathy, 1 = any retinopathy present  
**Image Presentation Method**: Raw fundus photograph displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Is this fundus photograph normal or abnormal?"
- **Answer Choices**: ["Normal", "Abnormal"] 
- **Correct Answer**: "Abnormal"  
**Complete Conversion Process Explanation**:
1. Extract binary label "1" from dataset indicating retinopathy presence
2. Map "1" to abnormal case in screening framework
3. Insert "fundus photograph" as {modality} into question template
4. Generate "Abnormal" answer based on positive label mapping
5. Verify single correct answer structure for MCVQA compliance  
**Clinical Rationale**: Abnormal fundus examination showing retinal abnormalities consistent with diabetic retinopathy, requiring further clinical evaluation and management based on screening protocol standards
