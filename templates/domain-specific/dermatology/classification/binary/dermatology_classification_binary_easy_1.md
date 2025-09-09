# Dermatology Malignant vs Benign Lesion Assessment Template

## Template Overview

**Template ID**: `dermatology_classification_binary_easy_1`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Pattern**: Malignant versus benign lesion assessment  
**Domain**: Dermatology (skin imaging)

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct questions about lesion malignancy in dermatological images. This assessment is fundamental to dermatological practice, representing the core cancer screening decision that affects treatment planning and patient outcomes.

The template is designed for dermatology datasets where lesions are labeled as malignant or benign, testing the model's ability to recognize key dermatological features that distinguish cancerous from non-cancerous skin lesions using established ABCDE criteria.

## Question Generation Pattern

### Question Format
```
"Based on the dermatological features visible, is this lesion malignant or benign?"
```

### Answer Format
Binary choice with clinical options:
- A. Malignant
- B. Benign

### Template Variables
- `{lesion_type}`: The specific type of lesion if available
- `{imaging_modality}`: Dermoscopy, clinical photography, or dermatopathology
- `{anatomical_location}`: Body location of the lesion
- `{clinical_context}`: Additional clinical information if available

### Clinical Context
- **Malignant**: Lesions showing characteristics of skin cancer (melanoma, BCC, SCC)
- **Benign**: Non-cancerous lesions (nevi, seborrheic keratoses, dermatofibromas)
- **ABCDE Criteria**: Asymmetry, Border irregularity, Color variation, Diameter >6mm, Evolution
- **Clinical Importance**: Early detection of skin cancer for improved patient outcomes

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Based on the dermatological features visible, is this lesion malignant or benign?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Malignant",
    "Benign"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Lesion shows irregular borders, color variation, and asymmetry consistent with malignant characteristics",
  "provenance": {
    "original_label": "malignant",
    "rule_id": "dermatology_classification_binary_easy_1",
    "annotation_id": "lesion_boundary",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Dermatological images (dermoscopy, clinical photography, dermatopathology)
- **Labels**: Binary labels indicating malignant/benign status
- **Quality**: Sufficient resolution for dermatological feature assessment

### Compatible Datasets
- ISIC challenges (melanoma detection)
- HAM10000 (skin lesion dataset)
- Melanoma detection datasets
- Skin cancer classification datasets
- Dermatology atlases with malignancy labels

### Minimum Standards
- **Image Quality**: High enough resolution to assess dermatological features
- **Annotation Quality**: Expert dermatologist or pathologist validation preferred
- **Data Distribution**: Balanced representation of malignant and benign lesions

## Template Usage Rules

### Question Construction Rules
1. Always reference "dermatological features visible" to focus on visual assessment
2. Use clinical terminology (malignant/benign) rather than generic terms
3. Maintain consistency with dermatological diagnostic workflows
4. Avoid leading questions that bias toward specific answers

### Answer Assignment Rules
1. Map "malignant", "cancer", "melanoma", "carcinoma" → "Malignant"
2. Map "benign", "noncancerous", "nevus", "keratosis" → "Benign"
3. Use original dataset labels as ground truth
4. Handle ambiguous cases by referencing pathological diagnosis when available

### Quality Control Guidelines
1. Verify clinical accuracy of question-answer pairs
2. Ensure terminology aligns with dermatological standards
3. Cross-validate with clinical guidelines (ABCDE criteria)
4. Review for potential bias in question phrasing

## Examples

### Example 1: Melanoma Detection
**Image**: Dermoscopic image of irregular pigmented lesion  
**Question**: "Based on the dermatological features visible, is this lesion malignant or benign?"  
**Answer**: A. Malignant  
**Rationale**: Lesion shows asymmetry, irregular borders, color variation, and diameter >6mm consistent with melanoma

### Example 2: Benign Nevus Assessment
**Image**: Clinical photograph of symmetric mole  
**Question**: "Based on the dermatological features visible, is this lesion malignant or benign?"  
**Answer**: B. Benign  
**Rationale**: Lesion demonstrates symmetry, regular borders, uniform color, and stable appearance typical of benign nevus

### Example 3: Basal Cell Carcinoma
**Image**: Clinical photograph of pearly nodular lesion  
**Question**: "Based on the dermatological features visible, is this lesion malignant or benign?"  
**Answer**: A. Malignant  
**Rationale**: Lesion shows characteristic pearly appearance with telangiectasia consistent with basal cell carcinoma

### Example 4: Seborrheic Keratosis
**Image**: Dermoscopic image of "stuck-on" warty lesion  
**Question**: "Based on the dermatological features visible, is this lesion malignant or benign?"  
**Answer**: B. Benign  
**Rationale**: Lesion demonstrates classic "stuck-on" appearance with surface texture typical of seborrheic keratosis

### Example 5: Squamous Cell Carcinoma
**Image**: Clinical photograph of scaly, irregular lesion  
**Question**: "Based on the dermatological features visible, is this lesion malignant or benign?"  
**Answer**: A. Malignant  
**Rationale**: Lesion shows irregular scaling, induration, and ulceration consistent with squamous cell carcinoma

## Implementation Notes

### Technical Considerations
- Ensure high-quality image preprocessing to maintain dermatological detail
- Consider multi-scale analysis for different imaging modalities
- Implement proper color calibration for dermoscopic images
- Handle varying image orientations and scales

### Clinical Validation
- Cross-reference with established dermatological guidelines
- Validate against pathological diagnosis when available
- Consider inter-observer variability in clinical assessment
- Align with current dermatological diagnostic criteria

### Dataset-Specific Adaptations
- **ISIC datasets**: Leverage metadata for anatomical location and age
- **Clinical datasets**: Incorporate patient history when available
- **Dermoscopy datasets**: Focus on dermoscopic pattern recognition
- **Pathology datasets**: Emphasize histopathological correlation

### Quality Assurance
- Regular review by dermatologists or dermatopathologists
- Validation against multiple expert opinions
- Continuous monitoring of model performance on clinical metrics
- Updates based on evolving dermatological diagnostic criteria
