# Pathology Tumor vs Normal Tissue Differentiation Template

## Template Overview

**Template ID**: `domain-specific_pathology_classification_binary_easy_2`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Question Pattern**: Tumor versus normal tissue identification  
**Medical Domain**: Pathology (histopathological imaging and neoplasia detection)  
**Domain-knowledge summary**: Requires specialized knowledge of normal tissue architecture and neoplastic changes. Understanding of normal histological patterns, cellular organization, tissue architecture, neoplastic transformation markers, and tumor recognition criteria. Knowledge of pathological terminology for tissue morphology, neoplasia detection, histological pattern recognition, and clinical significance of tumor identification.

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct questions about tumor tissue identification in histopathological images. This assessment is essential for surgical margin evaluation and diagnostic confirmation, helping to distinguish neoplastic from normal tissue architecture.

The template is designed for pathology datasets where tissue samples are labeled as tumor or normal, testing the model's ability to recognize architectural disruption and cellular changes that characterize neoplastic transformation.

## Question Generation Pattern

### Question Format
```
"Does this histopathological section show tumor tissue or normal tissue?"
```

### Answer Format
Binary choice with diagnostic options:
- A. Tumor tissue
- B. Normal tissue

### Template Variables
- `{organ_system}`: Specific organ or tissue type being examined
- `{tumor_characteristics}`: Architectural patterns and cellular features
- `{normal_architecture}`: Expected normal tissue organization
- `{diagnostic_context}`: Clinical setting or specimen type

### Clinical Context
- **Tumor Tissue**: Neoplastic tissue with disrupted architecture and abnormal cellular proliferation
- **Normal Tissue**: Non-neoplastic tissue with preserved architecture and normal cellular organization
- **Architectural Assessment**: Tissue organization, glandular patterns, cellular arrangement
- **Clinical Importance**: Critical for surgical margin assessment and treatment planning

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Does this histopathological section show tumor tissue or normal tissue?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Tumor tissue",
    "Normal tissue"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Tissue shows disrupted architecture with neoplastic cellular proliferation distinct from normal tissue organization",
  "provenance": {
    "original_label": "tumor",
    "rule_id": "pathology_classification_binary_easy_2",
    "annotation_id": "tumor_normal_classification",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Histopathological sections with clear tissue architecture
- **Labels**: Binary labels indicating tumor/normal status
- **Quality**: Sufficient magnification for architectural assessment

### Compatible Datasets
- Surgical margin assessment datasets
- Tumor vs adjacent normal tissue collections
- Cancer detection and localization datasets
- Digital pathology tumor identification sets
- Histopathological normal tissue atlases

### Minimum Standards
- **Image Quality**: Clear visualization of tissue architecture and cellular detail
- **Annotation Quality**: Expert pathologist validation for diagnostic accuracy
- **Data Distribution**: Representative samples of both tumor and normal tissues

## Template Usage Rules

### Question Construction Rules
1. Use clear diagnostic terminology (tumor tissue vs normal tissue)
2. Focus on histopathological section analysis
3. Maintain objectivity in tissue assessment
4. Reference architectural and cellular features

### Answer Assignment Rules
1. Map "tumor", "neoplasm", "cancer", "malignant" → "Tumor tissue"
2. Map "normal", "benign", "non-neoplastic", "healthy" → "Normal tissue"
3. Consider architectural disruption as key distinguishing feature
4. Use expert pathological diagnosis as reference standard

### Quality Control Guidelines
1. Ensure diagnostic accuracy of tissue classification
2. Verify consistency with pathological assessment criteria
3. Cross-validate with established normal tissue patterns
4. Review for potential confounding factors

## Examples

### Example 1: Colonic Adenocarcinoma
**Image**: H&E section showing disrupted glandular architecture  
**Question**: "Does this histopathological section show tumor tissue or normal tissue?"  
**Answer**: A. Tumor tissue  
**Rationale**: Tissue shows irregular glandular formation with loss of normal colonic architecture and neoplastic epithelial changes

### Example 2: Normal Colonic Mucosa
**Image**: H&E section showing organized crypts and surface epithelium  
**Question**: "Does this histopathological section show tumor tissue or normal tissue?"  
**Answer**: B. Normal tissue  
**Rationale**: Tissue demonstrates well-organized colonic crypts with normal epithelial maturation and preserved mucosal architecture

### Example 3: Breast Carcinoma
**Image**: H&E section showing invasive ductal carcinoma  
**Question**: "Does this histopathological section show tumor tissue or normal tissue?"  
**Answer**: A. Tumor tissue  
**Rationale**: Tissue shows invasive malignant glands infiltrating stroma with loss of normal breast ductal architecture

### Example 4: Normal Breast Tissue
**Image**: H&E section showing normal mammary ducts and stroma  
**Question**: "Does this histopathological section show tumor tissue or normal tissue?"  
**Answer**: B. Normal tissue  
**Rationale**: Tissue demonstrates normal mammary ductal architecture with intact basement membrane and organized stromal elements

### Example 5: Lung Adenocarcinoma
**Image**: H&E section showing neoplastic glandular proliferation  
**Question**: "Does this histopathological section show tumor tissue or normal tissue?"  
**Answer**: A. Tumor tissue  
**Rationale**: Tissue shows atypical glandular proliferation with architectural disruption distinct from normal pulmonary parenchyma

## Implementation Notes

### Technical Considerations
- Implement architecture-focused analysis algorithms
- Consider multi-scale assessment for tissue organization
- Account for organ-specific normal architectural patterns
- Handle variations in specimen preparation and orientation

### Clinical Validation
- Align with standard pathological diagnostic criteria
- Cross-reference with normal tissue histology atlases
- Validate against expert pathologist assessments
- Consider context of specimen type and clinical setting

### Dataset-Specific Adaptations
- **Organ-specific datasets**: Account for normal architectural variations
- **Margin assessment datasets**: Focus on tumor-normal tissue boundaries
- **Multi-institutional datasets**: Standardize for preparation variations
- **Research datasets**: Emphasize well-characterized tissue types

### Quality Assurance
- Regular review by expert pathologists
- Validation against established histological criteria
- Monitoring for organ-specific diagnostic accuracy
- Updates based on current pathological knowledge
