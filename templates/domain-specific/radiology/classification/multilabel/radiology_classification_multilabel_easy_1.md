# Radiology Chest X-ray Primary Finding Assessment Template

## Template Overview

**Template ID**: `radiology_classification_multilabel_easy_1`  
**Task Type**: Multilabel classification  
**Difficulty**: Easy  
**Question Pattern**: Primary radiological finding identification in chest X-rays  
**Medical Domain**: Radiology (chest imaging)  
**Domain-knowledge summary**: Requires specialized radiological knowledge for chest X-ray interpretation and finding prioritization. Must understand multiple pulmonary pathologies, clinical significance hierarchy, differential diagnosis principles, and ability to identify the most clinically important finding when multiple abnormalities are present in chest radiographs.

## Template Description

This template converts multilabel classification datasets into MCVQA format by asking questions about the most prominent or primary finding in chest X-ray images. When multiple findings are present, this focuses on identifying the most clinically significant or dominant abnormality, which is essential for prioritizing clinical decision-making and treatment planning.

The template is designed for radiology datasets where chest X-rays may show multiple concurrent findings, testing the model's ability to recognize and prioritize the most important radiological abnormality among those present.

## Question Generation Pattern

### Question Format
```
"What is the most prominent radiological finding in this chest X-ray?"
```

### Answer Format
Single choice with radiological finding options:
- A. Atelectasis
- B. Cardiomegaly
- C. Pleural effusion
- D. Pneumonia
- E. Pneumothorax
- F. Pulmonary edema
- G. Mass or nodule
- H. Consolidation
- I. No significant findings

### Template Variables
- `{finding_combinations}`: Specific combinations of findings present
- `{anatomical_locations}`: Pulmonary regions affected by each finding
- `{severity_indicators}`: Degree or extent of each finding
- `{view_type}`: PA, AP, or lateral chest X-ray projection

### Clinical Context
- **Primary Finding**: Most clinically significant or prominent abnormality requiring immediate attention
- **Clinical Prioritization**: Helps focus initial management on the most important pathology
- **Diagnostic Hierarchy**: Identifies the leading diagnosis when multiple findings coexist
- **Clinical Importance**: Primary finding identification guides immediate treatment decisions and urgency assessment

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What is the most prominent radiological finding in this chest X-ray?",
  "answer": "B",
  "answer_type": "single_label",
  "options": [
    "Atelectasis",
    "Cardiomegaly", 
    "Pleural effusion",
    "Pneumonia",
    "Pneumothorax",
    "Pulmonary edema",
    "Mass or nodule",
    "Consolidation",
    "No significant findings"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.85,
  "rationale": "Enlarged cardiac silhouette is the most prominent finding requiring immediate clinical attention",
  "provenance": {
    "original_label": "cardiomegaly",
    "rule_id": "radiology_classification_multilabel_easy_1",
    "annotation_id": "multiple_findings",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Chest X-ray images with comprehensive finding annotations
- **Labels**: Multilabel annotations indicating all present findings
- **Quality**: Sufficient resolution for detailed radiological assessment

### Compatible Datasets
- CheXpert multilabel annotations
- MIMIC-CXR comprehensive labeling
- PadChest multilabel chest findings
- NIH Chest X-ray comprehensive labels
- Multi-finding chest radiograph datasets

### Minimum Standards
- **Image Quality**: Clear visualization of cardiac, pulmonary, and pleural structures
- **Annotation Quality**: Comprehensive radiologist review with all findings labeled
- **Data Distribution**: Representative mix of single and multiple finding cases

## Template Usage Rules

### Question Construction Rules
1. Focus on identifying the most prominent or clinically significant finding
2. Include comprehensive list of common chest X-ray findings
3. Maintain standard radiological terminology
4. Include "No significant findings" option for normal or near-normal cases

### Answer Assignment Rules
1. Map the most prominent finding to the corresponding option
2. Use clinical judgment to prioritize when multiple findings are present
3. Consider severity and clinical significance in determining primary finding
4. Use "No significant findings" only when chest X-ray shows no clinically important abnormalities

### Quality Control Guidelines
1. Verify completeness of finding identification
2. Ensure consistency with radiological finding definitions
3. Cross-validate with established chest X-ray finding criteria
4. Review for potential missed findings

## Examples

### Example 1: Congestive Heart Failure Pattern
**Image**: PA chest X-ray showing enlarged heart, pulmonary edema, and pleural effusion  
**Question**: "What is the most prominent radiological finding in this chest X-ray?"  
**Answer**: B. Cardiomegaly  
**Rationale**: While multiple CHF findings are present, cardiomegaly is the most prominent and clinically significant finding

### Example 2: Post-operative Chest
**Image**: AP chest X-ray showing small atelectasis and large pneumothorax with surgical clips  
**Question**: "What is the most prominent radiological finding in this chest X-ray?"  
**Answer**: E. Pneumothorax  
**Rationale**: Pneumothorax is the most urgent finding requiring immediate attention in this post-surgical patient

### Example 3: COPD with Pneumonia
**Image**: PA chest X-ray showing hyperinflation and prominent right lower lobe consolidation  
**Question**: "What is the most prominent radiological finding in this chest X-ray?"  
**Answer**: H. Consolidation  
**Rationale**: While background COPD changes are present, the acute consolidation is the most prominent and clinically urgent finding

### Example 4: Normal Chest X-ray
**Image**: PA chest X-ray with clear lung fields and normal cardiac silhouette  
**Question**: "What is the most prominent radiological finding in this chest X-ray?"  
**Answer**: I. No significant findings  
**Rationale**: Normal chest X-ray without any clinically significant abnormalities

### Example 5: Lung Cancer with Complications
**Image**: PA chest X-ray showing large right upper lobe mass with small pleural effusion  
**Question**: "What is the most prominent radiological finding in this chest X-ray?"  
**Answer**: G. Mass or nodule  
**Rationale**: The lung mass is the most prominent and clinically significant finding requiring immediate oncological evaluation

## Implementation Notes

### Technical Considerations
- Implement comprehensive finding detection algorithms
- Handle overlapping or co-occurring pathologies
- Consider finding severity and extent assessment
- Optimize for systematic radiological evaluation

### Clinical Validation
- Align with established chest X-ray finding definitions
- Cross-reference with radiological society guidelines
- Validate against comprehensive radiologist assessments
- Consider inter-observer variability in complex cases

### Dataset-Specific Adaptations
- **CheXpert datasets**: Handle uncertainty labels and impression extraction
- **MIMIC datasets**: Incorporate temporal changes and clinical context
- **Research datasets**: Consider novel finding combinations
- **Educational datasets**: Emphasize classic finding presentations

### Quality Assurance
- Regular review by board-certified radiologists
- Validation against comprehensive finding checklists
- Monitoring for systematic finding omissions
- Updates based on evolving chest imaging interpretation standards
