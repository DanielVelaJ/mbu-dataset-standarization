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


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification (Vision → Image-Level Classification → Multiclass classification)
- **Label Structure**: 3+ mutually exclusive condition labels with exactly one correct condition per image
- **Medical Context**: Distinct medical conditions, findings, or diagnoses that can be visually differentiated
- **Image Level**: Whole image classification across any medical imaging modality
- **Datasets from metadata file**: Compatible datasets include chest X-ray datasets with multiple pulmonary conditions, skin lesion datasets with multiple dermatological conditions, fundus datasets with multiple ophthalmological conditions, histopathology datasets with multiple tissue/cancer types, brain imaging datasets with multiple neurological conditions, and other multiclass medical classification datasets available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Use exact medical terminology from original dataset and randomize option order to prevent position bias, including all dataset classes as options (3-8 recommended for readability)
- **Label mapping rules**: Convert original dataset annotations to multiple choice format:
  - Extract all condition labels from dataset metadata
  - Use correct condition label as right answer
  - Include other condition labels as distractors (subset if too many classes)
  - Ensure mutual exclusivity between all options
- **Conversion Process**: Extract multiclass labels from original dataset, identify all condition names from metadata, create multiple choice question with correct condition and plausible distractors from dataset, present raw images without modifications, validate MCVQA compliance with single correct answer, verify clinical relevance of condition combinations
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with 3-8 condition choices, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_multiclass_easy_1"
- **Radiology**: Use anatomically specific condition names (e.g., "pulmonary edema" vs "edema")
- **Pathology**: Include tissue type and grade when relevant (e.g., "adenocarcinoma grade 2")
- **Dermatology**: Use standard dermatological terminology (e.g., "seborrheic keratosis")
- **Ophthalmology**: Include anatomical specificity (e.g., "diabetic macular edema")

## Examples

### Example 1: Chest X-ray Multi-Class Classification
**Original Dataset Context and Annotation Format**: Chest pathology classification dataset with multiclass labels in CSV format (image_id, condition_label) where labels include "pneumonia", "pleural_effusion", "pneumothorax", "normal_chest"  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "What medical condition is shown in this chest X-ray image?"
- **Answer Choices**: ["Pneumonia", "Pleural effusion", "Pneumothorax", "Normal chest"]
- **Correct Answer**: "Pneumonia"  
**Complete Conversion Process Explanation**: 
1. Extract multiclass label "pneumonia" from dataset CSV
2. Identify all available condition labels from dataset metadata: pneumonia, pleural effusion, pneumothorax, normal chest
3. Use "pneumonia" as correct answer and other conditions as distractors
4. Create 4-option multiple choice format with randomized positioning
5. Validate MCVQA compliance with single correct answer from mutually exclusive conditions  
**Clinical Rationale**: Pneumonia case requiring differentiation from other common chest X-ray findings including pleural effusion, pneumothorax, and normal anatomy - tests ability to distinguish between respiratory pathologies based on radiographic patterns and consolidation characteristics

### Example 2: Skin Lesion Classification  
**Original Dataset Context and Annotation Format**: Dermatology multiclass dataset with 5 condition labels where labels include "melanoma", "basal_cell_carcinoma", "seborrheic_keratosis", "actinic_keratosis", "nevus"  
**Image Presentation Method**: Raw dermoscopy image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "What medical condition is shown in this dermoscopy image?"
- **Answer Choices**: ["Melanoma", "Basal cell carcinoma", "Seborrheic keratosis", "Actinic keratosis", "Nevus"] 
- **Correct Answer**: "Seborrheic keratosis"  
**Complete Conversion Process Explanation**:
1. Extract multiclass label "seborrheic_keratosis" from dataset annotation file
2. Identify all 5 available condition labels from dataset metadata as answer options
3. Use "seborrheic keratosis" as correct answer with other skin lesion types as distractors
4. Create 5-option multiple choice format ensuring mutually exclusive conditions
5. Verify multiclass format with single correct answer structure for MCVQA compliance  
**Clinical Rationale**: Seborrheic keratosis case requiring differentiation from malignant lesions (melanoma, basal cell carcinoma) and other benign lesions (nevus, actinic keratosis) - tests dermoscopic pattern recognition and ability to distinguish between benign and malignant skin lesions based on visual characteristics

