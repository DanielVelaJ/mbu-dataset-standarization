# Dermatology Inflammatory vs Non-Inflammatory Condition Template

## Template Overview

**Template ID**: `dermatology_classification_binary_easy_2`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Pattern**: Inflammatory versus non-inflammatory skin condition assessment  
**Domain**: Dermatology (skin imaging)

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
- `{condition_type}`: The specific skin condition if available
- `{inflammatory_signs}`: Visible signs of inflammation (erythema, scaling, papules)
- `{anatomical_location}`: Body location of the condition
- `{severity}`: Degree of inflammation if assessable

### Clinical Context
- **Inflammatory**: Conditions with active inflammation (dermatitis, psoriasis, eczema)
- **Non-inflammatory**: Conditions without inflammatory response (vitiligo, post-inflammatory hyperpigmentation)
- **Key Signs**: Erythema (redness), scaling, papules, vesicles, induration
- **Clinical Importance**: Determines treatment approach and medication selection

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Does this skin condition show inflammatory characteristics?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Inflammatory",
    "Non-inflammatory"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.85,
  "rationale": "Visible erythema, scaling, and papular changes indicate active inflammatory process",
  "provenance": {
    "original_label": "inflammatory",
    "rule_id": "dermatology_classification_binary_easy_2",
    "annotation_id": "inflammatory_region",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Clinical dermatological photographs showing skin conditions
- **Labels**: Binary classification of inflammatory vs non-inflammatory status
- **Quality**: Clear visualization of skin surface changes and inflammatory signs

### Compatible Datasets
- Dermatitis and eczema datasets
- Psoriasis severity datasets
- Inflammatory skin disease collections
- Clinical dermatology atlases
- Skin condition classification datasets

### Minimum Standards
- **Image Quality**: Sufficient resolution to assess inflammatory changes
- **Annotation Quality**: Clinical dermatologist validation preferred
- **Data Distribution**: Representative mix of inflammatory and non-inflammatory conditions

## Template Usage Rules

### Question Construction Rules
1. Focus on "inflammatory characteristics" to guide clinical assessment
2. Use standard dermatological terminology
3. Maintain objectivity in question phrasing
4. Align with clinical diagnostic workflows

### Answer Assignment Rules
1. Map "inflammatory", "dermatitis", "eczema", "psoriasis" → "Inflammatory"
2. Map "non-inflammatory", "vitiligo", "post-inflammatory" → "Non-inflammatory"
3. Consider acute vs chronic inflammatory patterns
4. Evaluate based on visible inflammatory markers

### Quality Control Guidelines
1. Verify clinical accuracy with dermatological standards
2. Ensure consistency with inflammatory disease classification
3. Cross-validate with clinical inflammatory markers
4. Review for proper inflammatory assessment criteria

## Examples

### Example 1: Acute Dermatitis
**Image**: Clinical photograph showing erythematous, scaling patches  
**Question**: "Does this skin condition show inflammatory characteristics?"  
**Answer**: A. Inflammatory  
**Rationale**: Visible erythema, scaling, and edema indicate acute inflammatory dermatitis

### Example 2: Vitiligo
**Image**: Clinical photograph of depigmented patches without erythema  
**Question**: "Does this skin condition show inflammatory characteristics?"  
**Answer**: B. Non-inflammatory  
**Rationale**: Depigmentation without erythema, scaling, or other inflammatory signs characteristic of vitiligo

### Example 3: Psoriatic Plaques
**Image**: Clinical photograph of well-demarcated erythematous plaques with silvery scale  
**Question**: "Does this skin condition show inflammatory characteristics?"  
**Answer**: A. Inflammatory  
**Rationale**: Classic psoriatic plaques show erythema, scaling, and induration indicating chronic inflammation

### Example 4: Post-Inflammatory Hyperpigmentation
**Image**: Clinical photograph of darkened skin patches without active inflammation  
**Question**: "Does this skin condition show inflammatory characteristics?"  
**Answer**: B. Non-inflammatory  
**Rationale**: Hyperpigmentation without current erythema or scaling represents post-inflammatory changes

### Example 5: Contact Dermatitis
**Image**: Clinical photograph of vesicular, erythematous eruption  
**Question**: "Does this skin condition show inflammatory characteristics?"  
**Answer**: A. Inflammatory  
**Rationale**: Vesicles, erythema, and acute changes consistent with active contact dermatitis

## Implementation Notes

### Technical Considerations
- Optimize color representation for erythema detection
- Consider lighting conditions that may affect inflammation visibility
- Implement proper skin tone calibration
- Handle varying degrees of inflammatory severity

### Clinical Validation
- Align with dermatological inflammation assessment criteria
- Consider both acute and chronic inflammatory patterns
- Validate against clinical inflammatory markers
- Cross-reference with dermatologist assessments

### Dataset-Specific Adaptations
- **Dermatitis datasets**: Focus on acute inflammatory changes
- **Psoriasis datasets**: Emphasize chronic inflammatory patterns
- **Mixed condition datasets**: Consider spectrum of inflammatory severity
- **Clinical datasets**: Incorporate patient history when available

### Quality Assurance
- Regular review by dermatologists
- Validation against inflammatory disease classification systems
- Monitoring for consistent inflammatory pattern recognition
- Updates based on evolving understanding of inflammatory skin diseases
