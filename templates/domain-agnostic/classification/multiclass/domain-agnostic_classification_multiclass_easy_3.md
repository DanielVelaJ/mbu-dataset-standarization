# Multi-Class Classification Template 3: Anatomical Region Identification

## Template Overview

**Template ID**: `domain-agnostic_classification_multiclass_easy_3`  
**Task Type**: Multiclass classification (anatomical region)  
**Difficulty**: Easy  
**Question Pattern**: Anatomical structure or region identification with multiple choice options  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires basic understanding of human anatomy and medical imaging. Knowledge of anatomical structures, organ identification, body regions, and ability to recognize anatomical landmarks on various imaging modalities. No specialized domain expertise required.

## Template Description

This template converts multi-class medical datasets into MCVQA format by asking about what anatomical region, organ, or body part is primarily shown in an image. The template presents multiple anatomical structures as answer options, where exactly one structure represents the primary focus of the image. This approach mirrors clinical image interpretation scenarios where medical professionals must first identify the anatomical context before making diagnostic assessments.

The template is designed to work with datasets that classify medical images based on anatomical regions, organs, body parts, or anatomical views. This includes datasets spanning different imaging modalities and medical specialties, from whole-body region classification to specific organ or tissue identification.

## Question Generation Pattern

### Question Format
`"What anatomical {structure_type} is primarily shown in this {modality} image?"`

### Answer Format
Multiple choice with options A, B, C, D, etc. representing different anatomical structures

### Template Variables
- `{structure_type}`: Type of anatomical classification (e.g., "region", "organ", "body part", "view"). Used in question text to specify the level of anatomical categorization being assessed.
- `{modality}`: Imaging modality (e.g., "X-ray", "CT scan", "MRI", "ultrasound", "histopathology"). Incorporated into question text to provide clinical context about imaging method.
- `{anatomical_list}`: List of specific anatomical structures from the dataset label set. Used to generate multiple choice options with correct anatomy and distractors.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, allowing for comprehensive assessment of anatomical structures and regions.

### Answer Construction
**Anatomical Multiple Choice Format**:
- Extract all anatomical structure labels from dataset metadata
- Use correct anatomical structure as the right answer
- Include other anatomical structures as distractors from the same classification level
- Ensure all options represent anatomically plausible structures for the imaging modality
- Maintain consistent anatomical terminology and classification level

### Example Pattern
```
Question: "What anatomical region is primarily shown in this X-ray image?"
A. Chest
B. Abdomen
C. Pelvis
D. Skull
```


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification with anatomical focus (Vision → Image-Level Classification → Multiclass classification)
- **Label Structure**: 3+ distinct anatomical region/organ labels with one primary anatomical focus per image
- **Medical Context**: Clear anatomical features and structures that can be visually identified across medical imaging modalities
- **Anatomical Level**: Consistent granularity level (organs, regions, body parts, or tissue types)
- **Datasets from metadata file**: Compatible datasets include multi-organ CT/MRI datasets (brain, chest, abdomen, pelvis), body region X-ray classification datasets, histopathology organ/tissue classification, ultrasound organ identification datasets, endoscopy anatomical site classification, retinal anatomical structure identification, and other anatomical classification datasets available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Use standard anatomical terminology and ensure all options are at similar anatomical levels with clear visual distinctions, following established anatomical nomenclature
- **Label mapping rules**: Convert original dataset annotations to anatomical identification format:
  - Extract all anatomical structure labels from dataset metadata
  - Use correct anatomical structure as right answer
  - Include other anatomical structures as distractors from same classification level
  - Ensure mutual exclusivity between anatomical options
- **Conversion Process**: Extract anatomical labels from original dataset, identify all structures from metadata, create anatomical identification question with appropriate structure type and modality, present raw images without modifications, validate MCVQA compliance with single correct answer, ensure appropriate level of anatomical specificity for the dataset
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with 3-8 anatomical choices, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_multiclass_easy_3"

## Examples

### Example 1: Body Region X-ray Classification
**Original Dataset Context and Annotation Format**: Multi-region X-ray dataset with anatomical labels in CSV format (image_id, region_label) where labels include "chest", "abdomen", "pelvis", "extremities"  
**Image Presentation Method**: Raw X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "What anatomical region is primarily shown in this X-ray image?"
- **Answer Choices**: ["Chest", "Abdomen", "Pelvis", "Extremities"]
- **Correct Answer**: "Chest"  
**Complete Conversion Process Explanation**: 
1. Extract multiclass label "chest" from dataset CSV
2. Identify all available anatomical region labels from dataset metadata: chest, abdomen, pelvis, extremities
3. Use "chest" as correct answer and other body regions as distractors
4. Create 4-option multiple choice format ensuring consistent anatomical granularity level
5. Validate anatomical identification format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Chest region identification requiring differentiation from other major body regions (abdomen, pelvis, extremities) - tests fundamental anatomical recognition skills essential for medical image interpretation and demonstrates understanding of basic body region classification used in medical practice and imaging protocols

### Example 2: Abdominal Organ CT Classification  
**Original Dataset Context and Annotation Format**: Abdominal CT organ classification dataset with organ labels where labels include "liver", "kidney", "spleen", "pancreas", "gallbladder"  
**Image Presentation Method**: Raw CT scan image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "What anatomical organ is primarily shown in this CT scan image?"
- **Answer Choices**: ["Liver", "Kidney", "Spleen", "Pancreas", "Gallbladder"] 
- **Correct Answer**: "Kidney"  
**Complete Conversion Process Explanation**:
1. Extract multiclass label "kidney" from dataset annotation file
2. Identify all 5 available organ labels from dataset metadata as answer options
3. Use "kidney" as correct answer with other abdominal organs as distractors
4. Create 5-option multiple choice format maintaining consistent organ-level granularity
5. Verify anatomical organ identification format with single correct answer structure for MCVQA compliance  
**Clinical Rationale**: Kidney identification requiring differentiation from other major abdominal organs including liver, spleen, pancreas, and gallbladder - tests organ-level anatomical recognition critical for CT scan interpretation and demonstrates understanding of abdominal anatomy essential for radiological assessment and clinical correlation
