# Dermatology Skin Condition Category Assessment Template

## Template Overview

**Template ID**: `dermatology_classification_multiclass_easy_3`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Dermatological condition category identification  
**Domain**: Dermatology (skin imaging)

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
- `{morphological_features}`: Key morphological characteristics visible
- `{distribution_pattern}`: How the condition is distributed anatomically
- `{primary_lesions}`: Type of primary skin lesions present
- `{secondary_changes}`: Additional features like scaling, crusting, or lichenification

### Clinical Context
- **Eczematous Dermatitis**: Inflammation with erythema, scaling, possible vesiculation
- **Papulosquamous Disorder**: Papules and plaques with scaling (psoriasis, lichen planus)
- **Vesiculobullous Disease**: Fluid-filled lesions (pemphigus, bullous pemphigoid)
- **Infectious Condition**: Signs of bacterial, viral, or fungal infection
- **Neoplastic Lesion**: Abnormal tissue growth, benign or malignant

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Which dermatological condition category best describes this presentation?",
  "answer": "B",
  "answer_type": "single_label",
  "options": [
    "Eczematous dermatitis",
    "Papulosquamous disorder",
    "Vesiculobullous disease",
    "Infectious condition",
    "Neoplastic lesion"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.87,
  "rationale": "Well-demarcated plaques with silvery scale characteristic of papulosquamous disorder",
  "provenance": {
    "original_label": "papulosquamous",
    "rule_id": "dermatology_classification_multiclass_easy_3",
    "annotation_id": "condition_category",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Clinical dermatological photographs showing skin conditions
- **Labels**: Morphological category classifications based on clinical features
- **Quality**: Clear visualization of primary and secondary morphological features

### Compatible Datasets
- General dermatology condition databases
- Morphological pattern classification collections
- Clinical dermatology atlases
- Educational dermatology datasets
- Multi-condition dermatological databases

### Minimum Standards
- **Image Quality**: Sufficient detail for morphological feature assessment
- **Annotation Quality**: Clinical dermatologist categorization preferred
- **Data Distribution**: Representative examples of each morphological category

## Template Usage Rules

### Question Construction Rules
1. Focus on "condition category" to emphasize morphological classification
2. Use "best describes" to acknowledge potential overlap between categories
3. Maintain standard dermatological morphological terminology
4. Emphasize pattern recognition over specific diagnosis

### Answer Assignment Rules
1. Map inflammatory conditions with vesicles/eczema → "Eczematous dermatitis"
2. Map scaly plaques and papules → "Papulosquamous disorder"
3. Map blisters and bullae → "Vesiculobullous disease"
4. Map pustules, impetigo, fungal infections → "Infectious condition"
5. Map tumors, cysts, and abnormal growths → "Neoplastic lesion"

### Quality Control Guidelines
1. Verify alignment with dermatological morphology classification
2. Ensure consistency with clinical pattern recognition principles
3. Cross-validate with established morphological criteria
4. Review for proper categorization based on primary features

## Examples

### Example 1: Eczematous Dermatitis Recognition
**Image**: Clinical photograph of erythematous, scaling patches with inflammation  
**Question**: "Which dermatological condition category best describes this presentation?"  
**Answer**: A. Eczematous dermatitis  
**Rationale**: Erythema, scaling, and inflammatory changes typical of eczematous pattern

### Example 2: Papulosquamous Disorder Identification
**Image**: Clinical photograph of well-demarcated plaques with silvery scale  
**Question**: "Which dermatological condition category best describes this presentation?"  
**Answer**: B. Papulosquamous disorder  
**Rationale**: Well-demarcated plaques with characteristic scaling of papulosquamous disease

### Example 3: Vesiculobullous Disease Assessment
**Image**: Clinical photograph of fluid-filled blisters on erythematous base  
**Question**: "Which dermatological condition category best describes this presentation?"  
**Answer**: C. Vesiculobullous disease  
**Rationale**: Multiple fluid-filled vesicles and bullae characteristic of vesiculobullous disorders

### Example 4: Infectious Condition Evaluation
**Image**: Clinical photograph of pustular lesions with surrounding erythema  
**Question**: "Which dermatological condition category best describes this presentation?"  
**Answer**: D. Infectious condition  
**Rationale**: Pustular lesions with inflammatory response suggestive of infectious etiology

### Example 5: Neoplastic Lesion Classification
**Image**: Clinical photograph of nodular growth with irregular surface  
**Question**: "Which dermatological condition category best describes this presentation?"  
**Answer**: E. Neoplastic lesion  
**Rationale**: Nodular growth with abnormal architecture consistent with neoplastic process

## Implementation Notes

### Technical Considerations
- Optimize for recognition of primary morphological features
- Implement pattern recognition for different lesion distributions
- Consider color and texture analysis for category differentiation
- Handle overlapping morphological characteristics

### Clinical Validation
- Align with established dermatological morphology classification systems
- Cross-reference with clinical pattern recognition principles
- Validate against expert dermatologist categorization
- Consider evolution of morphological patterns over time

### Dataset-Specific Adaptations
- **Educational datasets**: Emphasize classic morphological presentations
- **Clinical datasets**: Handle mixed or evolving morphological patterns
- **Research datasets**: Consider novel or atypical presentations
- **Atlas datasets**: Focus on prototypical examples of each category

### Quality Assurance
- Regular review by dermatologists experienced in morphological classification
- Validation against established dermatological pattern recognition criteria
- Monitoring for consistent categorization across different conditions
- Updates based on evolving understanding of dermatological morphology
