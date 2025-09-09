# Dermatology Anatomical Location-Specific Diagnosis Template

## Template Overview

**Template ID**: `domain-specific_dermatology_classification_multiclass_easy_4`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Question Pattern**: Anatomical location-specific dermatological diagnosis  
**Medical Domain**: Dermatology (anatomical site assessment and topographical dermatology)  
**Domain-knowledge summary**: Requires specialized knowledge of anatomical location-specific dermatological characteristics and site-based diagnostic patterns. Understanding of topographical dermatology, body site predilections for different conditions, anatomical variations in skin morphology, site-specific disease patterns, and correlation between anatomical location and diagnostic likelihood. Knowledge of dermatological anatomy, regional skin characteristics, and location-based differential diagnosis principles.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking direct questions about dermatological diagnoses while incorporating anatomical context. This approach reflects clinical practice, where anatomical location significantly influences differential diagnosis due to varying disease prevalence and morphological presentation at different body sites.

The template is designed for dermatology datasets where lesions are classified considering their anatomical location, testing the model's ability to integrate topographical information with morphological features for accurate diagnosis.

## Question Generation Pattern

### Question Format
```
"Given the anatomical location and features, what is the most likely diagnosis?"
```

### Answer Format
Multiclass choice with location-relevant diagnostic options:
- A. Seborrheic keratosis
- B. Solar lentigo
- C. Melanocytic nevus
- D. Dermatofibroma
- E. Sebaceous hyperplasia

### Template Variables
- `{anatomical_site}`: Specific body location (face, trunk, extremities). Used in question construction to provide topographical context and in answer generation to determine location-specific diagnosis based on site predilection patterns.
- `{age_related_factors}`: Age-appropriate differential diagnoses. Incorporated into question assessment and used to guide answer construction based on age-specific dermatological patterns.
- `{morphological_features}`: Lesion characteristics in anatomical context. Used to provide clinical context and determine diagnostic likelihood in answer rationale.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or annotations. Dermatological images (clinical photography showing anatomical context) are displayed as raw images to allow comprehensive assessment of both lesion characteristics and anatomical location context. No highlighting, anatomical marking, or site-specific overlays are added to maintain authentic clinical evaluation conditions for topographical assessment.

### Answer Construction
**Correct Answer Generation**:
- Extract the diagnosis from the original dataset considering anatomical location context
- Map specific condition labels to anatomically-informed diagnostic categories
- Use topographical assessment from dataset annotations focusing on location-specific diagnosis
- Consider anatomical site predilection in diagnostic classification
- Validate answer accuracy against established anatomical dermatology criteria and site-specific diagnostic principles

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Given the anatomical location and features, what is the most likely diagnosis?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Seborrheic keratosis",
    "Solar lentigo",
    "Melanocytic nevus",
    "Dermatofibroma",
    "Sebaceous hyperplasia"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.85,
  "rationale": "Warty, stuck-on lesion on trunk in older adult typical of seborrheic keratosis",
  "provenance": {
    "original_label": "seborrheic_keratosis",
    "rule_id": "dermatology_classification_multiclass_easy_4",
    "annotation_id": "location_specific_diagnosis",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification (Vision → Image-Level Classification → Multiclass classification)
- **Label Structure**: Multiple diagnosis labels with anatomical location context per image
- **Image Types**: Dermatological images with clear anatomical site context and sufficient detail for location-specific assessment
- **Assessment Requirements**: Sufficient image quality for evaluation of both morphological characteristics and anatomical location context
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include location-annotated dermatology databases, anatomical site-specific lesion collections, age-stratified dermatology datasets, sun-exposure related skin lesion databases, and body site-specific dermatological atlases with expert topographical validation

## Template Usage Rules

- **Implementation guidelines**: Use exact dermatological terminology from dataset annotations focusing on anatomical location context and site-specific diagnostic criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format considering anatomical site prevalence:
  - Site-specific condition labels mapped to anatomically-appropriate diagnostic categories
  - Consider anatomical site predilection patterns for each condition
  - Account for age-related and sun-exposure factors in site-specific diagnoses
  - Always use dataset ground truth labels as definitive diagnostic classification
- **Conversion Process**: Extract diagnosis and anatomical location from original dataset, identify site-specific features and morphological characteristics from metadata, generate questions using topographical assessment terminology, present raw images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of location-specific diagnostic terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with anatomically-informed diagnostic categories, and includes provenance tracking with original labels and rule_id "domain-specific_dermatology_classification_multiclass_easy_4"

## Examples

### Example 1: Site-Specific Seborrheic Keratosis Diagnosis
**Original Dataset Context and Annotation Format**: Anatomical location dermatology dataset with site-specific diagnostic labels in CSV format (image_id, anatomical_site, diagnosis) where diagnoses include "seborrheic_keratosis", "solar_lentigo", "melanocytic_nevus", "dermatofibroma", "sebaceous_hyperplasia"  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, annotations, or anatomical site highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Given the anatomical location and features, what is the most likely diagnosis?"
- **Answer Choices**: ["Seborrheic keratosis", "Solar lentigo", "Melanocytic nevus", "Dermatofibroma", "Sebaceous hyperplasia"]
- **Correct Answer**: "Seborrheic keratosis"  
**Complete Conversion Process Explanation**: 
1. Extract diagnosis label "seborrheic_keratosis" and anatomical site "trunk" from dataset CSV indicating site-specific classification
2. Identify morphological features and anatomical context from dataset metadata
3. Generate question using topographical assessment terminology emphasizing anatomical location context
4. Map seborrheic keratosis label to answer choice considering trunk site predilection
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Seborrheic keratosis on trunk case requiring integration of anatomical location (trunk predilection) with morphological features (warty, stuck-on appearance) - tests site-specific diagnostic assessment for anatomical location vs morphological classification based on established criteria for topographical dermatology and anatomical site predilection patterns

### Example 2: Solar Lentigo Location-Specific Assessment  
**Original Dataset Context and Annotation Format**: Site-specific dermatology atlas with expert anatomical annotations where "solar_lentigo" classification on "dorsal_hand" indicates chronic sun exposure lesion, stored in annotation file with image names, anatomical sites, and diagnoses  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, overlays, or site-specific annotations  
**Generated Question and ALL Answer Choices**:
- **Question**: "Given the anatomical location and features, what is the most likely diagnosis?"
- **Answer Choices**: ["Seborrheic keratosis", "Solar lentigo", "Melanocytic nevus", "Dermatofibroma", "Sebaceous hyperplasia"] 
- **Correct Answer**: "Solar lentigo"  
**Complete Conversion Process Explanation**:
1. Extract diagnosis label "solar_lentigo" and site "dorsal_hand" from dataset annotation indicating sun-exposure related classification
2. Map solar lentigo to site-specific diagnostic category based on anatomical predilection
3. Generate question using standardized topographical assessment terminology
4. Convert site-specific diagnosis to "Solar lentigo" answer choice considering hand site predilection
5. Verify multiclass choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Solar lentigo on dorsal hand case demonstrating characteristic anatomical site predilection for chronically sun-exposed areas with flat brown macule morphology - tests ability to integrate anatomical location context with morphological features for accurate site-specific diagnostic classification based on topographical dermatology principles

