# Dermatology Pigmented vs Non-Pigmented Lesion Classification Template

## Template Overview

**Template ID**: `domain-specific_dermatology_classification_binary_easy_3`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Question Pattern**: Pigmented versus non-pigmented lesion classification  
**Medical Domain**: Dermatology (skin imaging and dermoscopy)  
**Domain-knowledge summary**: Requires specialized knowledge of pigmented skin lesions and melanin distribution patterns. Understanding of dermatological pigmentation mechanisms, lesion color assessment, differential diagnosis between pigmented and non-pigmented conditions, and recognition of various pigmentation patterns including melanocytic and non-melanocytic lesions. Knowledge of dermatological terminology and pigmentation-related pathology.

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct questions about pigmentation characteristics in dermatological lesions. This fundamental morphological distinction affects diagnostic approach, as pigmented and non-pigmented lesions have different differential diagnoses and follow distinct evaluation pathways.

The template is designed for dermatology datasets where lesions are categorized based on the presence or absence of pigmentation, testing the model's ability to recognize melanin content and pigment pattern variations that are crucial for dermatological assessment.

## Question Generation Pattern

### Question Format
```
"Is this lesion primarily pigmented or non-pigmented?"
```

### Answer Format
Binary choice with morphological options:
- A. Pigmented
- B. Non-pigmented

### Template Variables
- `{lesion_description}`: Basic morphological description of the lesion. Used in question construction to provide clinical context and in answer generation to determine pigmented vs non-pigmented classification based on dermatological assessment.
- `{pigment_pattern}`: Type of pigmentation if present (uniform, variegated, network). Incorporated into question assessment and used to guide answer construction based on presence/absence of melanin patterns.
- `{color_characteristics}`: Specific colors observed (brown, black, blue-gray). Used to provide clinical context and determine pigmentation status in answer rationale.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or annotations. Dermatological images (clinical photography, dermoscopy) are displayed as raw images to allow comprehensive assessment of pigmentation characteristics including melanin distribution, color patterns, and overall lesion coloration. No highlighting, color enhancement, or pigmentation region marking is added to maintain authentic clinical evaluation conditions for pigment assessment.

### Answer Construction
**Correct Answer Generation**:
- Extract the pigmentation status from the original dataset (pigmented/non-pigmented, melanocytic/non-melanocytic, 0/1)
- Map pigmented cases ("pigmented", "melanocytic", "brown", "black", "1") to "Pigmented"
- Map non-pigmented cases ("non-pigmented", "non-melanocytic", "flesh-colored", "erythematous", "0") to "Non-pigmented"
- Use dermatological assessment from dataset annotations focusing on melanin presence
- Validate answer accuracy against established dermatological criteria for pigmentation classification

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels indicating pigmented/non-pigmented status per image
- **Image Types**: Dermatological images including clinical photography, dermoscopy with clear pigmentation visualization
- **Assessment Requirements**: Sufficient image quality and color representation for evaluation of melanin content and pigment patterns
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include melanocytic lesion classification datasets, skin lesion datasets with pigmentation labels, dermoscopy collections with pigmented/non-pigmented annotations, and dermatological atlases with expert-validated pigmentation assessments

## Template Usage Rules

- **Implementation guidelines**: Use exact dermatological terminology from dataset annotations focusing on pigmentation assessment and melanin content evaluation criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format:
  - Labels "pigmented", "melanocytic", "brown", "black", "1" → "Pigmented"
  - Labels "non-pigmented", "amelanotic", "pink", "flesh-colored", "0" → "Non-pigmented"
  - Always use dataset ground truth labels as definitive pigmentation classification
- **Conversion Process**: Extract pigmentation status from original dataset, identify lesion type and color characteristics from metadata, generate questions using pigmentation assessment terminology, present raw images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of pigmentation terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array ["Pigmented", "Non-pigmented"], and includes provenance tracking with original labels and rule_id "domain-specific_dermatology_classification_binary_easy_3"

## Examples

### Example 1: Pigmented Melanocytic Nevus
**Original Dataset Context and Annotation Format**: Dermoscopy dataset with pigmentation labels in CSV format (image_id, pigmentation_status) where 1 = pigmented lesion, 0 = non-pigmented lesion  
**Image Presentation Method**: Raw dermoscopic image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Is this lesion primarily pigmented or non-pigmented?"
- **Answer Choices**: ["Pigmented", "Non-pigmented"]
- **Correct Answer**: "Pigmented"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV indicating pigmented classification
2. Identify "melanocytic nevus" as lesion type and "dermoscopy" as imaging modality from dataset
3. Generate question using pigmentation assessment terminology focused on melanin content
4. Map positive pigmentation label to "Pigmented" answer based on visual characteristics
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Pigmented melanocytic nevus case requiring recognition of melanin distribution patterns including brown pigmentation and network characteristics - tests dermatological assessment for pigmented vs non-pigmented classification based on established criteria for melanin content and dermoscopic pigmentation patterns

### Example 2: Non-Pigmented Basal Cell Carcinoma  
**Original Dataset Context and Annotation Format**: Skin lesion classification dataset with morphological categories where "non-pigmented BCC" classification indicates absence of significant melanin, stored in annotation file with image names and pigmentation labels  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, overlays, or diagnostic annotations  
**Generated Question and ALL Answer Choices**:
- **Question**: "Is this lesion primarily pigmented or non-pigmented?"
- **Answer Choices**: ["Pigmented", "Non-pigmented"] 
- **Correct Answer**: "Non-pigmented"  
**Complete Conversion Process Explanation**:
1. Extract pigmentation label "non-pigmented" from dataset annotation indicating absence of melanin
2. Map "non-pigmented BCC" to non-pigmented category based on dermatological morphology
3. Generate question using standardized pigmentation assessment terminology
4. Convert non-pigmented diagnosis to "Non-pigmented" answer choice following label mapping rules
5. Verify binary choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Non-pigmented basal cell carcinoma case demonstrating lesion without significant melanin content showing characteristic pearly, pink appearance - tests ability to distinguish non-pigmented lesions from pigmented based on absence of melanin and presence of characteristic non-pigmented morphological features

