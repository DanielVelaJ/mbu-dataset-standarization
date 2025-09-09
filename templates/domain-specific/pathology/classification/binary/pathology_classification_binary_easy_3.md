# Pathology High-Grade vs Low-Grade Neoplasm Assessment Template

## Template Overview

**Template ID**: `pathology_classification_binary_easy_3`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Pattern**: High-grade versus low-grade neoplasm differentiation  
**Domain**: Pathology (histopathological imaging)

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct questions about neoplasm grading in histopathological images. This assessment is critical for prognosis and treatment intensity decisions, as tumor grade directly correlates with clinical behavior and patient outcomes.

The template is designed for pathology datasets where neoplasms are graded based on morphological features, testing the model's ability to assess cellular atypia, mitotic activity, and architectural patterns that determine tumor grade.

## Question Generation Pattern

### Question Format
```
"Based on the cellular features, is this a high-grade or low-grade neoplasm?"
```

### Answer Format
Binary choice with grading options:
- A. High-grade
- B. Low-grade

### Template Variables
- `{grading_criteria}`: Specific morphological features used for grading
- `{cellular_atypia}`: Degree of nuclear and cellular abnormalities
- `{mitotic_rate}`: Frequency of mitotic figures
- `{architectural_patterns}`: Tissue organization and differentiation level

### Clinical Context
- **High-Grade**: Aggressive neoplasms with marked atypia, high mitotic rate, poor differentiation
- **Low-Grade**: Indolent neoplasms with minimal atypia, low mitotic rate, good differentiation
- **Grading Systems**: WHO grading criteria, organ-specific grading schemes
- **Clinical Importance**: Grade determines prognosis, treatment intensity, and follow-up protocols

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Based on the cellular features, is this a high-grade or low-grade neoplasm?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "High-grade",
    "Low-grade"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.85,
  "rationale": "Neoplasm shows marked nuclear pleomorphism, high mitotic rate, and poor differentiation consistent with high-grade features",
  "provenance": {
    "original_label": "high_grade",
    "rule_id": "pathology_classification_binary_easy_3",
    "annotation_id": "tumor_grading",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Histopathological sections of graded neoplasms
- **Labels**: Binary labels indicating high-grade/low-grade status
- **Quality**: Sufficient resolution for cellular and nuclear assessment

### Compatible Datasets
- Graded tumor datasets across organ systems
- Cancer grading validation studies
- Histopathological grading collections
- WHO classification validation datasets
- Prognostic grading assessment sets

### Minimum Standards
- **Image Quality**: Clear visualization of cellular morphology and nuclear features
- **Annotation Quality**: Expert pathologist grading validation
- **Data Distribution**: Representative samples across grading spectrum

## Template Usage Rules

### Question Construction Rules
1. Focus on cellular features as primary grading determinants
2. Use established grading terminology (high-grade/low-grade)
3. Reference morphological assessment criteria
4. Maintain consistency with pathological grading systems

### Answer Assignment Rules
1. Map "high-grade", "poorly differentiated", "grade 3", "aggressive" → "High-grade"
2. Map "low-grade", "well differentiated", "grade 1", "indolent" → "Low-grade"
3. Consider nuclear pleomorphism, mitotic rate, and architectural patterns
4. Use established grading criteria as reference standard

### Quality Control Guidelines
1. Ensure consistency with established grading systems
2. Verify correlation between morphological features and grade assignment
3. Cross-validate with expert pathologist assessments
4. Review for grading system-specific criteria

## Examples

### Example 1: High-Grade Sarcoma
**Image**: H&E section showing highly cellular spindle cell tumor  
**Question**: "Based on the cellular features, is this a high-grade or low-grade neoplasm?"  
**Answer**: A. High-grade  
**Rationale**: Neoplasm shows marked nuclear pleomorphism, high cellularity, and numerous mitotic figures consistent with high-grade sarcoma

### Example 2: Low-Grade Adenocarcinoma
**Image**: H&E section showing well-differentiated glandular tumor  
**Question**: "Based on the cellular features, is this a high-grade or low-grade neoplasm?"  
**Answer**: B. Low-grade  
**Rationale**: Neoplasm demonstrates well-formed glandular architecture with minimal nuclear atypia and low mitotic rate

### Example 3: High-Grade Carcinoma
**Image**: H&E section showing poorly differentiated epithelial tumor  
**Question**: "Based on the cellular features, is this a high-grade or low-grade neoplasm?"  
**Answer**: A. High-grade  
**Rationale**: Tumor shows loss of architectural differentiation, marked nuclear pleomorphism, and high mitotic activity

### Example 4: Low-Grade Neuroendocrine Tumor
**Image**: H&E section showing organized neuroendocrine proliferation  
**Question**: "Based on the cellular features, is this a high-grade or low-grade neoplasm?"  
**Answer**: B. Low-grade  
**Rationale**: Tumor demonstrates organized growth pattern with uniform nuclei and rare mitotic figures typical of low-grade neuroendocrine neoplasm

### Example 5: High-Grade Lymphoma
**Image**: H&E section showing large cell lymphoid proliferation  
**Question**: "Based on the cellular features, is this a high-grade or low-grade neoplasm?"  
**Answer**: A. High-grade  
**Rationale**: Lymphoid proliferation shows large cells with prominent nucleoli and high proliferation rate consistent with high-grade lymphoma

## Implementation Notes

### Technical Considerations
- Implement cellular feature analysis for grading assessment
- Consider mitotic counting algorithms for objective assessment
- Account for organ-specific grading variations
- Handle different magnifications and staining protocols

### Clinical Validation
- Align with WHO and organ-specific grading systems
- Cross-reference with established grading criteria
- Validate against expert pathologist consensus
- Consider prognostic correlation studies

### Dataset-Specific Adaptations
- **Organ-specific datasets**: Apply appropriate grading systems (Gleason, Nottingham, etc.)
- **Multi-institutional datasets**: Standardize grading criteria
- **Research datasets**: Focus on well-validated grading examples
- **Clinical datasets**: Emphasize prognostically relevant grading

### Quality Assurance
- Regular review by expert pathologists familiar with grading systems
- Validation against established morphological criteria
- Monitoring for grading consistency across tumor types
- Updates based on evolving grading guidelines and WHO classifications
