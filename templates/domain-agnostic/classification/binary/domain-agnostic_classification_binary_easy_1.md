# Binary Classification Template 1: Presence Detection

## Template Overview

**Template ID**: `domain-agnostic_classification_binary_easy_1`  
**Task Type**: Binary classification  
**Difficulty**: Easy  
**Question Pattern**: Presence/absence detection for medical findings  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires basic understanding of medical terminology and imaging modalities. No specialized domain expertise needed as template works across radiology, pathology, dermatology, and other medical fields using general medical concepts of presence/absence detection.

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct presence/absence questions about medical findings in images. It is designed for datasets where each image has a single binary label indicating whether a specific medical condition, finding, or pathology is present.

The template provides a straightforward approach to binary classification that maps naturally to diagnostic decision-making across medical specialties, making it suitable for screening scenarios and general abnormality detection tasks.

## Question Generation Pattern

### Question Format
```
"Is {finding} present in this {modality} image?"
```

### Answer Format
- **Positive cases**: "Yes"
- **Negative cases**: "No"

### Template Variables
- `{finding}`: The medical condition, pathology, or finding being detected. Used directly in question construction and determines the clinical context for the binary decision.
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus", "skin", "CT", "MRI"). Incorporated into question text to provide clinical context and helps specify the type of medical image being analyzed.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown to the user exactly as captured, allowing for whole-image assessment of the presence or absence of the specified finding.

### Answer Construction
**Correct Answer Generation**:
- Extract the binary label from the original dataset (0/1, positive/negative, true/false)
- Map positive cases (1, "positive", "present", "true") to "Yes"
- Map negative cases (0, "negative", "absent", "false") to "No"

**Answer Format**: Simple binary choice without additional options or distractors, maintaining MCVQA compliance with exactly one correct answer per question.

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Single binary label per image (0/1, positive/negative, yes/no)
- **Image Level**: Whole image classification (not region-specific)
- **Datasets from metadata file**: Compatible datasets include chest X-ray classification datasets (ChestX-ray14), skin lesion datasets (ISIC), fundus photography datasets (EyePACS), and other binary medical image classification datasets available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Use exact medical terminology from dataset label definitions for the finding parameter
- **Label mapping rules**: Convert original dataset annotations as follows:
  - Label "1", "positive", "present", "true" → "Yes"
  - Label "0", "negative", "absent", "false" → "No"
- **Conversion Process**: Extract binary labels from original dataset, map to yes/no format, generate questions using finding and modality from dataset metadata, present raw images without modifications, validate MCVQA compliance with single correct answer
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "yes_no", task "Classification", difficulty "easy", and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_binary_easy_1"

## Examples

### Example 1: Chest X-ray Pneumonia Detection
**Original Dataset Context and Annotation Format**: ChestX-ray14 dataset with binary labels in CSV format (image_id, pneumonia_label) where 1 = pneumonia present, 0 = no pneumonia  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Is pneumonia present in this chest X-ray image?"
- **Answer Choices**: ["Yes", "No"]
- **Correct Answer**: "Yes"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV
2. Map "1" to positive case
3. Insert "pneumonia" as {finding} and "chest X-ray" as {modality} into question template
4. Generate "Yes" answer based on positive label mapping
5. Validate MCVQA compliance with single correct answer  
**Clinical Rationale**: Positive identification based on radiological evidence of consolidation and inflammatory changes consistent with pneumonia diagnosis

### Example 2: Skin Lesion Melanoma Detection  
**Original Dataset Context and Annotation Format**: ISIC dataset with folder-based organization where images in "melanoma" folder have label=1, images in "benign" folder have label=0  
**Image Presentation Method**: Raw dermoscopic image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Is melanoma present in this skin image?"
- **Answer Choices**: ["Yes", "No"] 
- **Correct Answer**: "No"  
**Complete Conversion Process Explanation**:
1. Extract binary label "0" from folder classification (benign folder)
2. Map "0" to negative case
3. Insert "melanoma" as {finding} and "skin" as {modality} into question template
4. Generate "No" answer based on negative label mapping
5. Verify single correct answer for MCVQA compliance  
**Clinical Rationale**: Lesion classified as benign based on symmetric borders, uniform coloration, and lack of ABCDE criteria for malignancy

