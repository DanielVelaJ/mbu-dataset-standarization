# Dermatology Skin Cancer Type Classification Template

## Template Overview

**Template ID**: `domain-specific_dermatology_classification_multiclass_easy_1`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Question Pattern**: Skin cancer type identification  
**Medical Domain**: Dermatology (skin cancer assessment and oncological dermatology)  
**Domain-knowledge summary**: Requires specialized knowledge of skin cancer types, oncological dermatology, and malignant lesion characteristics. Understanding of different skin cancer categories (melanoma, basal cell carcinoma, squamous cell carcinoma), their distinctive morphological features, risk factors, and clinical presentations. Knowledge of dermatological oncology terminology, cancer staging principles, and differential diagnosis of malignant skin lesions.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking direct questions about specific skin cancer types in dermatological images. This classification is crucial for treatment planning, as different skin cancer types require distinct therapeutic approaches and have varying prognoses.

The template is designed for dermatology datasets where lesions are classified into specific cancer types, testing the model's ability to distinguish between major categories of skin malignancies based on their characteristic features and patterns.

## Question Generation Pattern

### Question Format
```
"What type of skin cancer is most consistent with the features shown?"
```

### Answer Format
Multiclass choice with oncological options:
- A. Melanoma
- B. Basal cell carcinoma
- C. Squamous cell carcinoma
- D. Actinic keratosis
- E. Not cancer

### Template Variables
- `{cancer_features}`: Specific morphological features visible. Used in question construction to provide clinical context and in answer generation to determine the correct skin cancer type based on characteristic features and diagnostic criteria.
- `{anatomical_location}`: Body location (affects cancer prevalence). Incorporated into question assessment and used to guide answer construction based on site-specific cancer patterns and risk factors.
- `{imaging_modality}`: Clinical photography, dermoscopy, or histology. Used to provide clinical context and determine the level of detail available for cancer type assessment.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or annotations. Dermatological images (clinical photography, dermoscopy, histopathology) are displayed as raw images to allow comprehensive assessment of cancer characteristics including morphology, color patterns, surface texture, and overall lesion features. No highlighting, diagnostic overlays, or cancer region marking is added to maintain authentic clinical evaluation conditions for oncological assessment.

### Answer Construction
**Correct Answer Generation**:
- Extract the cancer type from the original dataset (melanoma, BCC, SCC, actinic keratosis, benign)
- Map specific cancer labels to standardized oncological categories
- Use dermatological oncology assessment from dataset annotations focusing on cancer type classification
- Include "Not cancer" option for benign lesions or non-malignant conditions
- Validate answer accuracy against established dermatological oncology criteria and cancer classification guidelines

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification (Vision → Image-Level Classification → Multiclass classification)
- **Label Structure**: Multiple cancer type labels with specific oncological categories per image
- **Image Types**: Dermatological images including clinical photography, dermoscopy, histopathology with clear cancer characteristics
- **Assessment Requirements**: Sufficient image quality for evaluation of cancer morphology and diagnostic features
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include skin cancer classification datasets, ISIC melanoma detection challenges, dermatology oncology atlases, histopathologically confirmed cancer collections, and multi-cancer dermatological databases with expert-validated cancer type annotations

## Template Usage Rules

- **Implementation guidelines**: Use exact dermatological oncology terminology from dataset annotations focusing on cancer type classification and morphological assessment criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format:
  - Cancer type labels "melanoma", "BCC", "SCC", "actinic keratosis" → corresponding cancer category options
  - Benign labels "nevus", "seborrheic keratosis", "normal" → "Not cancer"
  - Always use dataset ground truth labels as definitive cancer classification
- **Conversion Process**: Extract cancer type from original dataset, identify morphological features and anatomical location from metadata, generate questions using oncological assessment terminology, present raw images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of cancer terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with cancer types plus "Not cancer", and includes provenance tracking with original labels and rule_id "domain-specific_dermatology_classification_multiclass_easy_1"

## Examples

### Example 1: Melanoma Classification
**Original Dataset Context and Annotation Format**: Skin cancer classification dataset with oncological labels in CSV format (image_id, cancer_type) where labels include "melanoma", "BCC", "SCC", "actinic_keratosis", "benign"  
**Image Presentation Method**: Raw dermoscopic image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "What type of skin cancer is most consistent with the features shown?"
- **Answer Choices**: ["Melanoma", "Basal cell carcinoma", "Squamous cell carcinoma", "Actinic keratosis", "Not cancer"]
- **Correct Answer**: "Melanoma"  
**Complete Conversion Process Explanation**: 
1. Extract cancer type label "melanoma" from dataset CSV indicating malignant melanoma classification
2. Identify morphological features and imaging modality from dataset metadata
3. Generate question using oncological assessment terminology focused on cancer type identification
4. Map melanoma label to "Melanoma" answer choice based on diagnostic criteria
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Malignant melanoma case requiring recognition of ABCDE criteria including asymmetry, irregular borders, color variation, and diameter characteristics - tests dermatological oncology assessment for cancer type classification based on established criteria for melanoma diagnosis and differential diagnosis from other skin cancer types

### Example 2: Basal Cell Carcinoma Classification  
**Original Dataset Context and Annotation Format**: Dermatology oncology dataset with histopathologically confirmed cancer types where "BCC" classification indicates basal cell carcinoma, stored in annotation file with image names and cancer labels  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, overlays, or diagnostic annotations  
**Generated Question and ALL Answer Choices**:
- **Question**: "What type of skin cancer is most consistent with the features shown?"
- **Answer Choices**: ["Melanoma", "Basal cell carcinoma", "Squamous cell carcinoma", "Actinic keratosis", "Not cancer"] 
- **Correct Answer**: "Basal cell carcinoma"  
**Complete Conversion Process Explanation**:
1. Extract cancer type label "BCC" from dataset annotation indicating basal cell carcinoma classification
2. Map "BCC" to basal cell carcinoma category based on oncological classification
3. Generate question using standardized cancer assessment terminology
4. Convert BCC diagnosis to "Basal cell carcinoma" answer choice following label mapping rules
5. Verify multiclass choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Basal cell carcinoma case demonstrating characteristic pearly, translucent appearance with telangiectasia - tests ability to distinguish BCC from other skin cancer types based on morphological features and oncological classification criteria for accurate cancer type identification

