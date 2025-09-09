# Dermatology Malignant vs Benign Lesion Assessment Template

## Template Overview

**Template ID**: `domain-specific_dermatology_classification_binary_easy_1`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Question Pattern**: Malignant versus benign lesion assessment  
**Medical Domain**: Dermatology (skin imaging and dermoscopy)  
**Domain-knowledge summary**: Requires specialized knowledge of dermatological conditions, dermoscopic pattern recognition, and skin lesion morphology. Understanding of ABCDE criteria (Asymmetry, Border irregularity, Color variation, Diameter >6mm, Evolution), lesion characteristics, malignancy indicators, and differential diagnosis of pigmented and non-pigmented skin lesions. Knowledge of dermatological terminology, skin cancer types (melanoma, basal cell carcinoma, squamous cell carcinoma), and benign lesion characteristics.

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct questions about lesion malignancy in dermatological images. This assessment is fundamental to dermatological practice, representing the core cancer screening decision that affects treatment planning and patient outcomes.

The template is designed for dermatology datasets where lesions are labeled as malignant or benign, testing the model's ability to recognize key dermatological features that distinguish cancerous from non-cancerous skin lesions using established ABCDE criteria.

## Question Generation Pattern

### Question Format
```
"Based on the dermatological features visible, is this lesion malignant or benign?"
```

### Answer Format
Binary choice with clinical options:
- A. Malignant  
- B. Benign

### Template Variables
- `{lesion_type}`: The specific type of lesion if available. Used in question construction to provide clinical context and in answer generation to determine the correct malignant/benign classification based on dermatological diagnosis.
- `{imaging_modality}`: Dermoscopy, clinical photography, or dermatopathology. Incorporated into question text to specify the imaging method and helps determine the level of detail visible for assessment.
- `{anatomical_location}`: Body location of the lesion. Used to provide clinical context in question construction and may influence malignancy risk assessment in answer rationale.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or annotations. Dermatological images (dermoscopy, clinical photography) are displayed as raw images to allow comprehensive assessment of lesion characteristics including symmetry, borders, color variation, and overall morphology. No highlighting, segmentation masks, or diagnostic overlays are added to maintain authentic clinical evaluation conditions.

### Answer Construction
**Correct Answer Generation**:
- Extract the binary malignancy label from the original dataset (malignant/benign, cancer/non-cancer, 0/1)
- Map malignant cases ("malignant", "cancer", "melanoma", "carcinoma", "1") to "Malignant"
- Map benign cases ("benign", "non-cancer", "nevus", "normal", "0") to "Benign"
- Use dermatological diagnosis from dataset annotations as ground truth for malignancy assessment
- Validate answer accuracy against established dermatological diagnostic criteria and ABCDE guidelines

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels indicating malignant/benign status per image  
- **Image Types**: Dermatological images including dermoscopy, clinical photography, or dermatopathology
- **Resolution Requirements**: Sufficient image quality for assessment of dermatological features (ABCDE criteria)
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include ISIC challenges for melanoma detection, HAM10000 skin lesion dataset, skin cancer classification datasets, and dermatology atlases with expert-validated malignancy labels

## Template Usage Rules

- **Implementation guidelines**: Use exact dermatological terminology from dataset annotations and maintain focus on visual assessment of ABCDE criteria and lesion morphology
- **Label mapping rules**: Convert original dataset annotations to MCVQA format:
  - Labels "malignant", "cancer", "melanoma", "carcinoma", "1" → "Malignant"  
  - Labels "benign", "non-cancerous", "nevus", "keratosis", "0" → "Benign"
  - Always use dataset ground truth labels as definitive classification
- **Conversion Process**: Extract binary malignancy labels from original dataset, identify lesion type and imaging modality from metadata, generate questions using dermatological assessment terminology, present raw images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of dermatological terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array ["Malignant", "Benign"], and includes provenance tracking with original labels and rule_id "domain-specific_dermatology_classification_binary_easy_1"

## Examples

### Example 1: Melanoma Detection
**Original Dataset Context and Annotation Format**: ISIC Challenge dataset with binary labels in metadata file (image_id, malignant_label) where 1 = malignant melanoma, 0 = benign lesion  
**Image Presentation Method**: Raw dermoscopic image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Based on the dermatological features visible, is this lesion malignant or benign?"
- **Answer Choices**: ["Malignant", "Benign"]
- **Correct Answer**: "Malignant"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from ISIC dataset metadata indicating malignant classification
2. Identify "melanoma" as lesion type and "dermoscopy" as imaging modality from dataset
3. Generate question using dermatological assessment terminology focused on visual features
4. Map positive malignancy label to "Malignant" answer based on dermatological diagnosis
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Malignant melanoma case requiring recognition of ABCDE criteria including asymmetry, irregular borders, color variation, diameter >6mm, and evolving characteristics - tests dermatological pattern recognition for melanoma diagnosis based on established dermoscopic features

### Example 2: Benign Nevus Assessment  
**Original Dataset Context and Annotation Format**: HAM10000 dataset with diagnostic categories where "nv" (nevus) classification indicates benign lesion, stored in ground truth CSV with image names and diagnosis codes  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, overlays, or diagnostic annotations  
**Generated Question and ALL Answer Choices**:
- **Question**: "Based on the dermatological features visible, is this lesion malignant or benign?"
- **Answer Choices**: ["Malignant", "Benign"] 
- **Correct Answer**: "Benign"  
**Complete Conversion Process Explanation**:
1. Extract diagnosis code "nv" from HAM10000 CSV indicating nevus classification
2. Map "nv" to benign category based on dataset diagnostic guidelines
3. Generate question using standardized dermatological assessment terminology
4. Convert benign diagnosis to "Benign" answer choice following label mapping rules
5. Verify binary choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Benign nevus case demonstrating normal dermatological features including symmetry, regular borders, uniform color distribution, and stable morphology - tests ability to distinguish benign lesions from malignant based on absence of concerning dermatological features and presence of characteristic nevus patterns

