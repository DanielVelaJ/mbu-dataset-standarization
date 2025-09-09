# Dermatology Anatomical Location-Specific Diagnosis Template

## Template Overview

**Template ID**: `dermatology_classification_multiclass_easy_4`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Anatomical location-specific dermatological diagnosis  
**Domain**: Dermatology (skin imaging)

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
- `{anatomical_site}`: Specific body location (face, trunk, extremities)
- `{age_related_factors}`: Age-appropriate differential diagnoses
- `{sun_exposure_history}`: Chronic vs acute sun damage indicators
- `{morphological_features}`: Lesion characteristics in anatomical context

### Clinical Context
- **Seborrheic Keratosis**: Common on trunk/face in older adults, "stuck-on" appearance
- **Solar Lentigo**: Sun-exposed areas, flat brown macules, age-related
- **Melanocytic Nevus**: Common on trunk/extremities, symmetric pigmented lesions
- **Dermatofibroma**: Often on legs, firm nodular lesions, may follow trauma
- **Sebaceous Hyperplasia**: Facial, yellowish papules with central depression

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

### Primary Requirements
- **Images**: Dermatological images with anatomical location metadata
- **Labels**: Specific diagnoses with anatomical site information
- **Quality**: Clear visualization of lesion characteristics and anatomical context

### Compatible Datasets
- Location-annotated dermatology databases
- Anatomical site-specific lesion collections
- Age-stratified dermatology datasets
- Sun-exposure related skin lesion databases
- Body site-specific dermatological atlases

### Minimum Standards
- **Image Quality**: Sufficient detail for morphological and contextual assessment
- **Annotation Quality**: Clinical diagnosis with anatomical site specification
- **Data Distribution**: Representative lesions across different anatomical locations

## Template Usage Rules

### Question Construction Rules
1. Explicitly reference "anatomical location and features" to emphasize context
2. Use "most likely diagnosis" to acknowledge differential diagnosis considerations
3. Incorporate location-specific disease prevalence in answer options
4. Maintain clinical diagnostic reasoning approach

### Answer Assignment Rules
1. Consider anatomical site prevalence for each condition
2. Match age-appropriate diagnoses for given locations
3. Account for sun exposure patterns by anatomical site
4. Use histopathological confirmation when available

### Quality Control Guidelines
1. Verify location-diagnosis correlations with clinical epidemiology
2. Ensure age-appropriate differential diagnoses
3. Cross-validate with anatomical site-specific disease prevalence
4. Review for proper integration of morphological and topographical features

## Examples

### Example 1: Seborrheic Keratosis on Trunk
**Image**: Clinical photograph of warty, brown lesion on chest of elderly patient  
**Question**: "Given the anatomical location and features, what is the most likely diagnosis?"  
**Answer**: A. Seborrheic keratosis  
**Rationale**: Warty, "stuck-on" appearance on trunk in older adult classic for seborrheic keratosis

### Example 2: Solar Lentigo on Hand
**Image**: Clinical photograph of flat brown macule on dorsal hand  
**Question**: "Given the anatomical location and features, what is the most likely diagnosis?"  
**Answer**: B. Solar lentigo  
**Rationale**: Flat brown macule on chronically sun-exposed dorsal hand typical of solar lentigo

### Example 3: Melanocytic Nevus on Back
**Image**: Clinical photograph of symmetric brown lesion on upper back  
**Question**: "Given the anatomical location and features, what is the most likely diagnosis?"  
**Answer**: C. Melanocytic nevus  
**Rationale**: Symmetric pigmented lesion on trunk with regular features consistent with benign nevus

### Example 4: Dermatofibroma on Leg
**Image**: Clinical photograph of firm, brown nodule on lower leg  
**Question**: "Given the anatomical location and features, what is the most likely diagnosis?"  
**Answer**: D. Dermatofibroma  
**Rationale**: Firm nodular lesion on leg with characteristic morphology of dermatofibroma

### Example 5: Sebaceous Hyperplasia on Face
**Image**: Clinical photograph of yellowish papule with central depression on forehead  
**Question**: "Given the anatomical location and features, what is the most likely diagnosis?"  
**Answer**: E. Sebaceous hyperplasia  
**Rationale**: Yellowish facial papule with central depression characteristic of sebaceous hyperplasia

## Implementation Notes

### Technical Considerations
- Incorporate anatomical site metadata in analysis
- Consider age-related disease prevalence patterns
- Implement location-specific feature weighting
- Handle variable image quality across anatomical sites

### Clinical Validation
- Align with epidemiological data for anatomical site disease prevalence
- Cross-reference with age-specific disease patterns
- Validate against clinical anatomical pathology correlations
- Consider environmental exposure patterns by body site

### Dataset-Specific Adaptations
- **Age-stratified datasets**: Emphasize age-appropriate differential diagnoses
- **Sun exposure databases**: Focus on chronically exposed vs protected sites
- **Population-specific datasets**: Consider ethnic and geographic disease patterns
- **Clinical datasets**: Incorporate patient demographics and history

### Quality Assurance
- Regular review by dermatologists familiar with anatomical site patterns
- Validation against established epidemiological disease distributions
- Monitoring for accurate integration of morphological and topographical features
- Updates based on evolving understanding of anatomical site-specific disease patterns
