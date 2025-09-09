# Dermatology Skin Condition Category Assessment Template

## Template Overview

**Template ID**: `domain-specific_dermatology_classification_multiclass_easy_3`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Question Pattern**: Dermatological condition category identification  
**Medical Domain**: Dermatology (morphological classification and diagnostic categorization)  
**Domain-knowledge summary**: Requires specialized knowledge of dermatological condition categories and morphological classification systems. Understanding of major dermatological categories (inflammatory, infectious, neoplastic, autoimmune), morphological pattern recognition, diagnostic categorization principles, and systematic approach to dermatological diagnosis. Knowledge of dermatological nosology, condition classification systems, and category-specific characteristics.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking direct questions about dermatological condition categories. This high-level diagnostic categorization is essential for differential diagnosis, as it groups conditions based on morphological characteristics and helps guide systematic diagnostic approaches.

The template is designed for dermatology datasets where skin conditions are classified into broad morphological categories, testing the model's ability to recognize fundamental dermatological patterns that form the basis of clinical diagnosis.

## Question Generation Pattern

### Question Format
```
"Which dermatological condition category best describes this presentation?"
```

### Answer Format
Multiclass choice with morphological category options:
- A. Eczematous dermatitis
- B. Papulosquamous disorder
- C. Vesiculobullous disease
- D. Infectious condition
- E. Neoplastic lesion

### Template Variables
- `{morphological_features}`: Key morphological characteristics visible. Used in question construction to provide clinical context and in answer generation to determine the correct dermatological category based on morphological classification criteria.
- `{distribution_pattern}`: How the condition is distributed anatomically. Incorporated into question assessment and used to guide answer construction based on category-specific distribution patterns.
- `{primary_lesions}`: Type of primary skin lesions present. Used to provide clinical context and determine category classification in answer rationale.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or annotations. Dermatological images (clinical photography, close-up views) are displayed as raw images to allow comprehensive assessment of morphological characteristics including lesion type, distribution patterns, surface changes, and overall condition features. No highlighting, categorization overlays, or diagnostic region marking is added to maintain authentic clinical evaluation conditions for morphological assessment.

### Answer Construction
**Correct Answer Generation**:
- Extract the dermatological category from the original dataset (eczematous, papulosquamous, vesiculobullous, infectious, neoplastic)
- Map specific condition labels to standardized dermatological categories
- Use morphological assessment from dataset annotations focusing on category classification
- Validate answer accuracy against established dermatological categorization criteria
- Ensure clinical relevance of morphological terminology and category descriptions

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification (Vision → Image-Level Classification → Multiclass classification)
- **Label Structure**: Multiple dermatological category labels with specific morphological classifications per image
- **Image Types**: Clinical dermatological photographs with clear morphological features and sufficient detail for category assessment
- **Assessment Requirements**: Sufficient image quality for evaluation of morphological characteristics and categorical classification
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include general dermatology condition databases, morphological pattern classification collections, clinical dermatology atlases, educational dermatology datasets, and multi-condition dermatological databases with expert categorization validation

## Template Usage Rules

- **Implementation guidelines**: Use exact dermatological terminology from dataset annotations focusing on morphological classification and categorical assessment criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format:
  - Category labels "eczematous", "dermatitis", "inflammatory" → "Eczematous dermatitis"
  - Category labels "papulosquamous", "scaly plaques", "psoriasis" → "Papulosquamous disorder"
  - Category labels "vesiculobullous", "blisters", "bullae" → "Vesiculobullous disease"
  - Category labels "infectious", "bacterial", "fungal", "viral" → "Infectious condition"
  - Category labels "neoplastic", "tumor", "growth", "lesion" → "Neoplastic lesion"
  - Always use dataset ground truth labels as definitive category classification
- **Conversion Process**: Extract dermatological category from original dataset, identify morphological features and condition characteristics from metadata, generate questions using categorical assessment terminology, present raw images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of morphological terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with dermatological categories, and includes provenance tracking with original labels and rule_id "domain-specific_dermatology_classification_multiclass_easy_3"

## Examples

### Example 1: Eczematous Dermatitis Category Classification
**Original Dataset Context and Annotation Format**: Dermatological condition category dataset with morphological labels in CSV format (image_id, category_type) where labels include "eczematous", "papulosquamous", "vesiculobullous", "infectious", "neoplastic"  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, annotations, or morphological highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Which dermatological condition category best describes this presentation?"
- **Answer Choices**: ["Eczematous dermatitis", "Papulosquamous disorder", "Vesiculobullous disease", "Infectious condition", "Neoplastic lesion"]
- **Correct Answer**: "Eczematous dermatitis"  
**Complete Conversion Process Explanation**: 
1. Extract category label "eczematous" from dataset CSV indicating inflammatory dermatitis classification
2. Identify morphological features and condition characteristics from dataset metadata
3. Generate question using categorical assessment terminology focused on morphological classification
4. Map eczematous label to "Eczematous dermatitis" answer choice based on morphological criteria
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Eczematous dermatitis case requiring recognition of inflammatory characteristics including erythema, scaling, and inflammatory changes - tests dermatological categorical assessment for eczematous vs other category classification based on established criteria for morphological pattern recognition and dermatological categorization

### Example 2: Papulosquamous Disorder Category Assessment  
**Original Dataset Context and Annotation Format**: Clinical dermatology categorization dataset with expert morphological annotations where "papulosquamous" classification indicates scaling papules and plaques, stored in annotation file with image names and category labels  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, overlays, or categorical annotations  
**Generated Question and ALL Answer Choices**:
- **Question**: "Which dermatological condition category best describes this presentation?"
- **Answer Choices**: ["Eczematous dermatitis", "Papulosquamous disorder", "Vesiculobullous disease", "Infectious condition", "Neoplastic lesion"] 
- **Correct Answer**: "Papulosquamous disorder"  
**Complete Conversion Process Explanation**:
1. Extract category label "papulosquamous" from dataset annotation indicating scaling plaque classification
2. Map "papulosquamous" to papulosquamous disorder category based on morphological characteristics
3. Generate question using standardized categorical assessment terminology
4. Convert papulosquamous diagnosis to "Papulosquamous disorder" answer choice following label mapping rules
5. Verify multiclass choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Papulosquamous disorder case demonstrating well-demarcated plaques with characteristic scaling - tests ability to distinguish papulosquamous patterns from other dermatological categories based on morphological features and categorical classification criteria for accurate condition categorization

