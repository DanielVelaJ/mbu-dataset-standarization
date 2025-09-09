# Dermatology Inflammatory vs Non-Inflammatory Condition Template

## Template Overview

**Template ID**: `domain-specific_dermatology_classification_binary_easy_2`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Question Pattern**: Inflammatory versus non-inflammatory skin condition assessment  
**Medical Domain**: Dermatology (skin imaging and dermoscopy)  
**Domain-knowledge summary**: Requires specialized knowledge of inflammatory skin conditions and their characteristic features. Understanding of inflammatory markers (erythema, scaling, papules, vesicles), dermatological pathophysiology, immune-mediated skin responses, and differential diagnosis between inflammatory and non-inflammatory conditions. Knowledge of dermatological terminology, treatment implications, and inflammatory dermatoses classification.

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct questions about inflammatory characteristics in dermatological conditions. This assessment is critical for treatment selection, as inflammatory conditions typically require anti-inflammatory approaches while non-inflammatory conditions need different therapeutic strategies.

The template is designed for dermatology datasets where skin conditions are categorized based on the presence or absence of inflammatory features, testing the model's ability to recognize inflammatory markers such as erythema, scaling, papules, and other signs of active inflammation.

## Question Generation Pattern

### Question Format
```
"Does this skin condition show inflammatory characteristics?"
```

### Answer Format
Binary choice with clinical options:
- A. Inflammatory
- B. Non-inflammatory

### Template Variables
- `{condition_type}`: The specific skin condition if available. Used in question construction to provide clinical context and in answer generation to determine inflammatory vs non-inflammatory classification based on dermatological diagnosis.
- `{inflammatory_signs}`: Visible signs of inflammation (erythema, scaling, papules). Incorporated into question assessment and used to guide answer construction based on presence/absence of inflammatory markers.
- `{anatomical_location}`: Body location of the condition. Used to provide clinical context and may influence inflammatory assessment based on site-specific dermatological patterns.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or annotations. Dermatological images (clinical photography, dermoscopy) are displayed as raw images to allow comprehensive assessment of inflammatory characteristics including erythema, scaling, papular changes, and overall tissue response patterns. No highlighting, diagnostic overlays, or inflammatory region marking is added to maintain authentic clinical evaluation conditions.

### Answer Construction
**Correct Answer Generation**:
- Extract the inflammatory status from the original dataset (inflammatory/non-inflammatory, active/inactive, 0/1)
- Map inflammatory cases ("inflammatory", "active", "dermatitis", "eczema", "1") to "Inflammatory"
- Map non-inflammatory cases ("non-inflammatory", "inactive", "stable", "vitiligo", "0") to "Non-inflammatory"
- Use dermatological assessment from dataset annotations focusing on inflammatory markers
- Validate answer accuracy against established dermatological criteria for inflammatory conditions

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels indicating inflammatory/non-inflammatory status per image
- **Image Types**: Dermatological images including clinical photography, dermoscopy showing inflammatory characteristics
- **Assessment Requirements**: Sufficient image quality for evaluation of inflammatory markers (erythema, scaling, papules)
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include inflammatory skin condition datasets, dermatitis classification collections, eczema vs normal skin datasets, and dermatological atlases with expert-validated inflammatory assessments

## Template Usage Rules

- **Implementation guidelines**: Use exact dermatological terminology from dataset annotations focusing on inflammatory markers and clinical assessment criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format:
  - Labels "inflammatory", "dermatitis", "eczema", "psoriasis", "active", "1" → "Inflammatory"
  - Labels "non-inflammatory", "vitiligo", "post-inflammatory", "inactive", "stable", "0" → "Non-inflammatory"
  - Always use dataset ground truth labels as definitive inflammatory classification
- **Conversion Process**: Extract inflammatory status from original dataset, identify condition type and inflammatory markers from metadata, generate questions using clinical inflammatory assessment terminology, present raw images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of inflammatory terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array ["Inflammatory", "Non-inflammatory"], and includes provenance tracking with original labels and rule_id "domain-specific_dermatology_classification_binary_easy_2"

## Examples

### Example 1: Acute Contact Dermatitis
**Original Dataset Context and Annotation Format**: Dermatitis classification dataset with binary labels in CSV format (image_id, inflammatory_status) where 1 = inflammatory condition, 0 = non-inflammatory condition  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Does this skin condition show inflammatory characteristics?"
- **Answer Choices**: ["Inflammatory", "Non-inflammatory"]
- **Correct Answer**: "Inflammatory"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV indicating inflammatory classification
2. Identify "contact dermatitis" as condition type from dataset metadata
3. Generate question using inflammatory assessment terminology focused on visible characteristics
4. Map positive inflammatory label to "Inflammatory" answer based on clinical criteria
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Active contact dermatitis case requiring recognition of inflammatory markers including erythema, vesiculation, scaling, and edema - tests dermatological assessment for inflammatory vs non-inflammatory classification based on established clinical criteria for inflammatory skin conditions

### Example 2: Vitiligo Assessment  
**Original Dataset Context and Annotation Format**: Skin condition classification dataset with diagnostic categories where "vitiligo" classification indicates non-inflammatory condition, stored in annotation file with image names and condition labels  
**Image Presentation Method**: Raw clinical photograph displayed without modifications, overlays, or diagnostic annotations  
**Generated Question and ALL Answer Choices**:
- **Question**: "Does this skin condition show inflammatory characteristics?"
- **Answer Choices**: ["Inflammatory", "Non-inflammatory"] 
- **Correct Answer**: "Non-inflammatory"  
**Complete Conversion Process Explanation**:
1. Extract condition label "vitiligo" from dataset annotation indicating non-inflammatory classification
2. Map "vitiligo" to non-inflammatory category based on dermatological classification
3. Generate question using standardized inflammatory assessment terminology
4. Convert non-inflammatory diagnosis to "Non-inflammatory" answer choice following label mapping rules
5. Verify binary choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Vitiligo case demonstrating non-inflammatory dermatological condition with depigmentation without erythema, scaling, or inflammatory markers - tests ability to distinguish non-inflammatory conditions from inflammatory based on absence of inflammatory signs and presence of characteristic vitiligo patterns

