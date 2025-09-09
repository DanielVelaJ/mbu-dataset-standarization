# Dermatology Pigmented vs Non-Pigmented Lesion Classification Template

## Template Overview

**Template ID**: `dermatology_classification_binary_easy_3`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Pattern**: Pigmented versus non-pigmented lesion classification  
**Domain**: Dermatology (skin imaging)

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
- `{lesion_description}`: Basic morphological description of the lesion
- `{pigment_pattern}`: Type of pigmentation if present (uniform, variegated, network)
- `{color_characteristics}`: Specific colors observed (brown, black, blue-gray)
- `{anatomical_location}`: Body location where pigmentation patterns may vary

### Clinical Context
- **Pigmented**: Lesions containing melanin (nevi, melanoma, seborrheic keratoses)
- **Non-pigmented**: Lesions without significant melanin (basal cell carcinoma, squamous cell carcinoma, dermatofibromas)
- **Pigment Assessment**: Central to dermoscopic evaluation and lesion categorization
- **Clinical Importance**: Guides differential diagnosis and biopsy decisions

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Is this lesion primarily pigmented or non-pigmented?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Pigmented",
    "Non-pigmented"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Lesion shows prominent brown and black pigmentation with melanin deposition",
  "provenance": {
    "original_label": "pigmented",
    "rule_id": "dermatology_classification_binary_easy_3",
    "annotation_id": "lesion_pigmentation",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Dermatological images with clear visualization of pigmentation
- **Labels**: Binary classification of pigmented vs non-pigmented status
- **Quality**: Adequate color representation and resolution for pigment assessment

### Compatible Datasets
- Melanocytic lesion datasets
- Skin lesion classification collections
- Dermoscopy databases
- Pigmented lesion atlases
- General dermatology imaging datasets

### Minimum Standards
- **Image Quality**: True color representation for accurate pigment assessment
- **Annotation Quality**: Dermatologist validation of pigmentation classification
- **Data Distribution**: Representative samples of both pigmented and non-pigmented lesions

## Template Usage Rules

### Question Construction Rules
1. Use "primarily" to acknowledge that some lesions may have mixed characteristics
2. Focus on pigmentation as the key distinguishing feature
3. Maintain objective, descriptive language
4. Align with standard dermatological morphological assessment

### Answer Assignment Rules
1. Map "pigmented", "melanocytic", "brown", "black" → "Pigmented"
2. Map "non-pigmented", "amelanotic", "pink", "flesh-colored" → "Non-pigmented"
3. Consider dominant pigmentation pattern for mixed lesions
4. Use dermoscopic criteria when available

### Quality Control Guidelines
1. Verify color accuracy and calibration
2. Ensure consistency with dermoscopic pigmentation assessment
3. Cross-validate with melanin content when known
4. Review for proper morphological classification

## Examples

### Example 1: Melanocytic Nevus
**Image**: Dermoscopic image of brown, symmetric lesion with network pattern  
**Question**: "Is this lesion primarily pigmented or non-pigmented?"  
**Answer**: A. Pigmented  
**Rationale**: Prominent brown pigmentation with typical melanocytic network pattern

### Example 2: Basal Cell Carcinoma
**Image**: Clinical photograph of pink, pearly nodular lesion  
**Question**: "Is this lesion primarily pigmented or non-pigmented?"  
**Answer**: B. Non-pigmented  
**Rationale**: Lesion shows characteristic pink, pearly appearance without significant pigmentation

### Example 3: Seborrheic Keratosis
**Image**: Clinical photograph of brown, warty lesion with "stuck-on" appearance  
**Question**: "Is this lesion primarily pigmented or non-pigmented?"  
**Answer**: A. Pigmented  
**Rationale**: Well-pigmented brown lesion with characteristic seborrheic keratosis morphology

### Example 4: Dermatofibroma
**Image**: Clinical photograph of firm, brownish-pink nodular lesion  
**Question**: "Is this lesion primarily pigmented or non-pigmented?"  
**Answer**: B. Non-pigmented  
**Rationale**: Predominantly pink with minimal pigmentation, typical of dermatofibroma

### Example 5: Melanoma
**Image**: Dermoscopic image showing variegated brown and black pigmentation  
**Question**: "Is this lesion primarily pigmented or non-pigmented?"  
**Answer**: A. Pigmented  
**Rationale**: Multiple shades of brown and black pigmentation with irregular distribution

## Implementation Notes

### Technical Considerations
- Ensure accurate color reproduction for pigment assessment
- Implement proper white balance and color calibration
- Consider impact of different imaging modalities on pigment visualization
- Handle varying skin tones that may affect pigment perception

### Clinical Validation
- Align with dermoscopic pigmentation assessment criteria
- Consider both clinical and dermoscopic pigmentation patterns
- Validate against histopathological melanin content when available
- Cross-reference with established morphological classification systems

### Dataset-Specific Adaptations
- **Dermoscopy datasets**: Emphasize dermoscopic pigment patterns
- **Clinical photography**: Focus on gross pigmentation characteristics
- **Mixed modality datasets**: Consider consistency across imaging types
- **Pathology correlation**: Incorporate histopathological pigment assessment

### Quality Assurance
- Regular review by dermatologists experienced in pigmented lesions
- Validation against dermoscopic pigmentation criteria
- Monitoring for consistent pigmentation pattern recognition
- Updates based on evolving dermoscopic and morphological standards
