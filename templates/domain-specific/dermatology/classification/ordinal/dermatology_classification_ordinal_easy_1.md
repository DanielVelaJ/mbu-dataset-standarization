# Dermatology Fitzpatrick Skin Type Assessment Template

## Template Overview

**Template ID**: `domain-specific_dermatology_classification_ordinal_easy_1`  
**Task Type**: Ordinal Classification  
**Difficulty**: Easy  
**Question Pattern**: Fitzpatrick skin type classification  
**Medical Domain**: Dermatology (skin type assessment and phototype classification)  
**Domain-knowledge summary**: Requires specialized knowledge of Fitzpatrick skin type classification system and phototype assessment. Understanding of skin pigmentation characteristics, sun sensitivity patterns, tanning and burning responses, UV exposure reactions, and ordered skin type progression (Type I-VI). Knowledge of dermatological phototype terminology, skin pigmentation assessment, and clinical applications for phototherapy and laser treatment planning.

## Template Description

This template converts ordinal classification datasets into MCVQA format by asking direct questions about Fitzpatrick skin type classification. This assessment is critical for phototherapy dosing, laser treatment planning, and skin cancer risk assessment, as different skin types respond differently to UV exposure and treatments.

The template is designed for dermatology datasets where skin type is classified using the established Fitzpatrick scale, testing the model's ability to assess skin pigmentation and sun sensitivity characteristics in an ordered progression.

## Question Generation Pattern

### Question Format
```
"What Fitzpatrick skin type is shown in this image?"
```

### Answer Format
Ordinal choice with Fitzpatrick classification:
- A. Type I (Always burns, never tans)
- B. Type II (Usually burns, tans minimally)
- C. Type III (Sometimes burns, tans gradually)
- D. Type IV (Burns minimally, tans well)
- E. Type V (Rarely burns, tans darkly)
- F. Type VI (Never burns, deeply pigmented)

### Template Variables
- `{skin_tone}`: Observable skin pigmentation level. Used in question construction to provide phototype context and in answer generation to determine the correct Fitzpatrick type based on skin pigmentation assessment criteria.
- `{anatomical_region}`: Body area being assessed (may affect pigmentation). Incorporated into question assessment and used to guide answer construction based on site-specific pigmentation variations.
- `{ethnicity_indicators}`: Morphological features that may suggest skin type. Used to provide clinical context and determine phototype classification in answer rationale.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or annotations. Dermatological images (clinical photography of skin areas) are displayed as raw images to allow comprehensive assessment of skin pigmentation characteristics including natural skin tone, melanin content, and phototype features. No highlighting, color enhancement, or skin tone marking is added to maintain authentic clinical evaluation conditions for Fitzpatrick skin type assessment.

### Answer Construction
**Correct Answer Generation**:
- Extract the Fitzpatrick skin type from the original dataset (Type I, Type II, Type III, Type IV, Type V, Type VI)
- Map specific skin type labels to standardized Fitzpatrick classification categories
- Use phototype assessment from dataset annotations focusing on ordinal skin type progression
- Maintain ordinal relationship between skin types (I < II < III < IV < V < VI)
- Validate answer accuracy against established Fitzpatrick classification criteria and phototype assessment guidelines

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Ordinal classification (Vision → Image-Level Classification → Ordinal classification)
- **Label Structure**: Ordinal Fitzpatrick skin type labels with meaningful progression (Type I < Type II < Type III < Type IV < Type V < Type VI)
- **Image Types**: Clinical dermatological photographs with accurate color representation for skin tone assessment
- **Assessment Requirements**: Sufficient image quality and color accuracy for evaluation of skin pigmentation and phototype characteristics
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include Fitzpatrick skin type databases, phototype classification collections, dermatology patient photography datasets, skin tone assessment atlases, and ethnicity-specific skin type research datasets with expert dermatologist validation

## Template Usage Rules

- **Implementation guidelines**: Use exact Fitzpatrick skin type terminology from dataset annotations focusing on ordinal skin type progression and phototype assessment criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format maintaining ordinal relationships:
  - Skin type labels mapped to standardized Fitzpatrick classification (Type I through Type VI)
  - Preserve ordinal progression ensuring Type I < Type II < Type III < Type IV < Type V < Type VI
  - Map constitutive skin color assessment to appropriate ordinal category
  - Always use dataset ground truth labels as definitive skin type classification
- **Conversion Process**: Extract Fitzpatrick skin type from original dataset, identify pigmentation characteristics and phototype features from metadata, generate questions using standardized phototype assessment terminology, present raw images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of ordinal skin type terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with ordinal Fitzpatrick skin types, and includes provenance tracking with original labels and rule_id "domain-specific_dermatology_classification_ordinal_easy_1"

## Examples

### Example 1: Ordinal Fitzpatrick Type I Assessment
**Original Dataset Context and Annotation Format**: Fitzpatrick skin type classification dataset with phototype labels in JSON format (image_id, skin_type, clinical_assessment) where skin types include "type_1", "type_2", "type_3", "type_4", "type_5", "type_6" in ordinal progression  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, color adjustments, or skin tone annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "What Fitzpatrick skin type is shown in this image?"
- **Answer Choices**: ["Type I (Always burns, never tans)", "Type II (Usually burns, tans minimally)", "Type III (Sometimes burns, tans gradually)", "Type IV (Burns minimally, tans well)", "Type V (Rarely burns, tans darkly)", "Type VI (Never burns, deeply pigmented)"]
- **Correct Answer**: "Type I (Always burns, never tans)"  
**Complete Conversion Process Explanation**: 
1. Extract Fitzpatrick skin type label "type_1" from dataset JSON indicating lightest phototype classification
2. Identify pigmentation characteristics and phototype features from clinical assessment metadata
3. Generate question using standardized Fitzpatrick assessment terminology
4. Map Type I label to appropriate ordinal category maintaining progression I < II < III < IV < V < VI
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Fitzpatrick Type I classification case requiring assessment of very light skin pigmentation with high sun sensitivity - tests ordinal phototype classification for skin tone assessment based on established criteria for dermatological phototype evaluation and constitutional skin color determination

### Example 2: Ordinal Fitzpatrick Type V Assessment  
**Original Dataset Context and Annotation Format**: Phototype assessment database with expert dermatologist annotations where "type_5" classification indicates brown skin with low sun sensitivity, stored in CSV format with skin_type ordinal values (1-6)  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, color enhancement, or phototype highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "What Fitzpatrick skin type is shown in this image?"
- **Answer Choices**: ["Type I (Always burns, never tans)", "Type II (Usually burns, tans minimally)", "Type III (Sometimes burns, tans gradually)", "Type IV (Burns minimally, tans well)", "Type V (Rarely burns, tans darkly)", "Type VI (Never burns, deeply pigmented)"] 
- **Correct Answer**: "Type V (Rarely burns, tans darkly)"  
**Complete Conversion Process Explanation**:
1. Extract skin type label "type_5" from dataset CSV indicating brown skin phototype classification
2. Map Type V to ordinal skin type category maintaining progression sequence
3. Generate question using standardized Fitzpatrick assessment terminology
4. Convert ordinal skin type to "Type V" answer choice preserving ordinal relationships
5. Verify ordinal classification format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Fitzpatrick Type V assessment demonstrating brown skin pigmentation with low sun sensitivity and high tanning capacity - tests ability to classify ordinal skin types based on constitutional pigmentation for accurate phototype determination according to dermatological assessment criteria

