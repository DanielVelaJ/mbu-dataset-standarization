# Dermatology Skin Cancer Type Classification Template

## Template Overview

**Template ID**: `dermatology_classification_multiclass_easy_1`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Skin cancer type identification  
**Domain**: Dermatology (skin imaging)

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
- `{cancer_features}`: Specific morphological features visible
- `{anatomical_location}`: Body location (affects cancer prevalence)
- `{patient_demographics}`: Age/skin type if available
- `{imaging_modality}`: Clinical photography, dermoscopy, or histology

### Clinical Context
- **Melanoma**: Most dangerous, arises from melanocytes, ABCDE criteria
- **Basal Cell Carcinoma**: Most common, locally invasive, pearly appearance
- **Squamous Cell Carcinoma**: Second most common, can metastasize, scaly/keratotic
- **Actinic Keratosis**: Precancerous, rough/scaly texture, sun-exposed areas
- **Clinical Importance**: Accurate classification guides treatment urgency and approach

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What type of skin cancer is most consistent with the features shown?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Melanoma",
    "Basal cell carcinoma", 
    "Squamous cell carcinoma",
    "Actinic keratosis",
    "Not cancer"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.85,
  "rationale": "Asymmetric lesion with irregular borders and color variation consistent with melanoma",
  "provenance": {
    "original_label": "melanoma",
    "rule_id": "dermatology_classification_multiclass_easy_1",
    "annotation_id": "cancer_classification",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: High-quality dermatological images showing skin lesions
- **Labels**: Specific cancer type classifications with histopathological confirmation
- **Quality**: Sufficient detail for morphological assessment and cancer typing

### Compatible Datasets
- ISIC melanoma detection challenges
- Skin cancer classification datasets
- Dermatology oncology atlases
- Histopathologically confirmed cancer datasets
- Multi-cancer dermatology collections

### Minimum Standards
- **Image Quality**: Clear visualization of lesion morphology and characteristics
- **Annotation Quality**: Pathologist or dermatologist confirmation of cancer type
- **Data Distribution**: Representative samples of each cancer type

## Template Usage Rules

### Question Construction Rules
1. Focus on "features shown" to emphasize visual assessment
2. Use "most consistent with" to acknowledge diagnostic uncertainty
3. Include "Not cancer" option for benign lesions
4. Maintain clinical terminology and diagnostic approach

### Answer Assignment Rules
1. Map specific cancer diagnoses to appropriate categories
2. Handle "carcinoma in situ" as appropriate cancer type
3. Map "atypical nevus" or "dysplastic nevus" based on clinical context
4. Use histopathological diagnosis as gold standard when available

### Quality Control Guidelines
1. Verify alignment with oncological classification systems
2. Ensure consistency with dermatopathology standards
3. Cross-validate with cancer staging and grading systems
4. Review for proper cancer type differentiation

## Examples

### Example 1: Melanoma Identification
**Image**: Dermoscopic image of asymmetric, multicolored lesion  
**Question**: "What type of skin cancer is most consistent with the features shown?"  
**Answer**: A. Melanoma  
**Rationale**: Asymmetry, irregular borders, multiple colors, and diameter >6mm consistent with melanoma

### Example 2: Basal Cell Carcinoma Recognition
**Image**: Clinical photograph of pearly, translucent nodule with telangiectasia  
**Question**: "What type of skin cancer is most consistent with the features shown?"  
**Answer**: B. Basal cell carcinoma  
**Rationale**: Classic pearly, translucent appearance with surface telangiectasia typical of BCC

### Example 3: Squamous Cell Carcinoma Assessment
**Image**: Clinical photograph of hyperkeratotic, indurated lesion  
**Question**: "What type of skin cancer is most consistent with the features shown?"  
**Answer**: C. Squamous cell carcinoma  
**Rationale**: Hyperkeratotic surface with induration and ulceration characteristic of SCC

### Example 4: Actinic Keratosis Evaluation
**Image**: Clinical photograph of rough, scaly lesion on sun-exposed area  
**Question**: "What type of skin cancer is most consistent with the features shown?"  
**Answer**: D. Actinic keratosis  
**Rationale**: Rough, scaly texture on sun-exposed skin typical of actinic keratosis

### Example 5: Benign Lesion Assessment
**Image**: Clinical photograph of symmetric, uniform brown lesion  
**Question**: "What type of skin cancer is most consistent with the features shown?"  
**Answer**: E. Not cancer  
**Rationale**: Symmetric, uniform appearance without malignant features suggests benign lesion

## Implementation Notes

### Technical Considerations
- Optimize for detailed morphological feature recognition
- Implement multi-scale analysis for different lesion sizes
- Consider color and texture analysis for cancer differentiation
- Handle varying image qualities and modalities

### Clinical Validation
- Align with current oncological classification systems
- Cross-reference with histopathological standards
- Validate against cancer staging and grading criteria
- Consider inter-observer variability in cancer diagnosis

### Dataset-Specific Adaptations
- **ISIC datasets**: Leverage challenge-specific cancer classifications
- **Pathology datasets**: Emphasize histopathological correlation
- **Clinical datasets**: Consider patient demographics and history
- **Mixed datasets**: Ensure consistency across different cancer types

### Quality Assurance
- Regular review by dermatopathologists and dermatologists
- Validation against established cancer classification systems
- Monitoring for accurate cancer type differentiation
- Updates based on evolving oncological diagnostic criteria
