# Dermatology Fitzpatrick Skin Type Assessment Template

## Template Overview

**Template ID**: `dermatology_classification_ordinal_easy_1`  
**Task Type**: Ordinal Classification  
**Difficulty**: Easy  
**Pattern**: Fitzpatrick skin type classification  
**Domain**: Dermatology (skin imaging)

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
- `{skin_tone}`: Observable skin pigmentation level
- `{anatomical_region}`: Body area being assessed (may affect pigmentation)
- `{lighting_conditions}`: Image lighting that may affect skin tone assessment
- `{ethnicity_indicators}`: Morphological features that may suggest skin type

### Clinical Context
- **Type I-II**: Light skin, high sun sensitivity, increased melanoma risk
- **Type III-IV**: Medium skin, moderate sun sensitivity, moderate cancer risk
- **Type V-VI**: Dark skin, low sun sensitivity, lower melanoma risk but higher risk of acral melanoma
- **Clinical Importance**: Guides treatment dosing, sun protection counseling, and cancer screening

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What Fitzpatrick skin type is shown in this image?",
  "answer": "C",
  "answer_type": "single_label",
  "options": [
    "Type I (Always burns, never tans)",
    "Type II (Usually burns, tans minimally)",
    "Type III (Sometimes burns, tans gradually)",
    "Type IV (Burns minimally, tans well)",
    "Type V (Rarely burns, tans darkly)",
    "Type VI (Never burns, deeply pigmented)"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.8,
  "rationale": "Medium skin tone with olive complexion consistent with Type III Fitzpatrick classification",
  "provenance": {
    "original_label": "type_3",
    "rule_id": "dermatology_classification_ordinal_easy_1",
    "annotation_id": "fitzpatrick_assessment",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Clinical photographs showing skin with good color representation
- **Labels**: Fitzpatrick skin type classifications (I-VI scale)
- **Quality**: Accurate color calibration for skin tone assessment

### Compatible Datasets
- Skin type classification datasets
- Dermatology patient population studies
- Phototherapy dosing databases
- Cosmetic dermatology collections
- Skin cancer risk assessment datasets

### Minimum Standards
- **Image Quality**: True color representation without significant color cast
- **Annotation Quality**: Clinical assessment by dermatologists familiar with Fitzpatrick scale
- **Data Distribution**: Representative samples across all Fitzpatrick types

## Template Usage Rules

### Question Construction Rules
1. Use established Fitzpatrick terminology with burn/tan characteristics
2. Focus on constitutive skin color rather than facultative tanning
3. Maintain objectivity in skin tone assessment
4. Include full descriptive text for each type

### Answer Assignment Rules
1. Map very light/pale skin → "Type I"
2. Map light skin with some color → "Type II"
3. Map medium/olive skin → "Type III"
4. Map light brown skin → "Type IV"
5. Map medium brown skin → "Type V"
6. Map dark brown/black skin → "Type VI"

### Quality Control Guidelines
1. Ensure color accuracy and calibration consistency
2. Verify alignment with established Fitzpatrick criteria
3. Consider constitutional vs acquired pigmentation
4. Account for anatomical site variation in pigmentation

## Examples

### Example 1: Fitzpatrick Type I Assessment
**Image**: Clinical photograph of very pale skin with pink undertones  
**Question**: "What Fitzpatrick skin type is shown in this image?"  
**Answer**: A. Type I (Always burns, never tans)  
**Rationale**: Very light skin with pink undertones characteristic of Type I, highest sun sensitivity

### Example 2: Fitzpatrick Type III Evaluation
**Image**: Clinical photograph of olive-toned skin with medium pigmentation  
**Question**: "What Fitzpatrick skin type is shown in this image?"  
**Answer**: C. Type III (Sometimes burns, tans gradually)  
**Rationale**: Medium skin tone with olive complexion typical of Type III Fitzpatrick classification

### Example 3: Fitzpatrick Type V Recognition
**Image**: Clinical photograph of brown skin with rich pigmentation  
**Question**: "What Fitzpatrick skin type is shown in this image?"  
**Answer**: E. Type V (Rarely burns, tans darkly)  
**Rationale**: Medium brown skin tone with rich pigmentation characteristic of Type V

### Example 4: Fitzpatrick Type II Assessment
**Image**: Clinical photograph of light skin with minimal tan capability  
**Question**: "What Fitzpatrick skin type is shown in this image?"  
**Answer**: B. Type II (Usually burns, tans minimally)  
**Rationale**: Light skin tone that shows minimal tanning ability, typical of Type II

### Example 5: Fitzpatrick Type VI Classification
**Image**: Clinical photograph of deeply pigmented dark skin  
**Question**: "What Fitzpatrick skin type is shown in this image?"  
**Answer**: F. Type VI (Never burns, deeply pigmented)  
**Rationale**: Deeply pigmented dark skin with maximal constitutional pigmentation of Type VI

## Implementation Notes

### Technical Considerations
- Implement robust color calibration and standardization
- Account for variable lighting conditions in clinical photography
- Consider impact of image compression on color accuracy
- Handle differences in camera systems and color spaces

### Clinical Validation
- Align with current Fitzpatrick classification criteria
- Consider both constitutive and facultative pigmentation
- Validate against clinical skin type assessments
- Cross-reference with sun sensitivity and burning history when available

### Dataset-Specific Adaptations
- **Clinical datasets**: Incorporate patient-reported sun sensitivity history
- **Research datasets**: Consider genetic markers of pigmentation when available
- **Cosmetic datasets**: Focus on constitutive rather than cosmetic pigmentation
- **Mixed population datasets**: Ensure representative distribution across types

### Quality Assurance
- Regular review by dermatologists experienced in skin type assessment
- Validation against established Fitzpatrick classification standards
- Monitoring for consistent skin type recognition across ethnicities
- Updates based on evolving understanding of skin pigmentation and sun sensitivity
