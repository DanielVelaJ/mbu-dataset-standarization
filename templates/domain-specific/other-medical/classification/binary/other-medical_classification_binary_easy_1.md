# Other-Medical Normal vs Abnormal Cell Morphology Template

## Template Overview

**Template ID**: `other-medical_classification_binary_easy_1`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Pattern**: Cell morphology normality assessment  
**Domain**: Other-Medical (cellular microscopy)

## Template Description

This template converts binary classification datasets into MCVQA format by asking questions about cell morphology normality in microscopic images. This assessment is fundamental for research applications, quality control, and cellular analysis in biomedical research contexts.

The template is designed for other-medical datasets with cellular morphology annotations, testing the model's ability to distinguish normal from abnormal cellular characteristics at the microscopic level.

## Question Generation Pattern

### Question Format
```
"Does this cell show normal or abnormal morphology under microscopic examination?"
```

### Answer Format
Binary choice with morphology assessment options:
- A. Normal morphology
- B. Abnormal morphology

### Template Variables
- `{cellular_features}`: Shape, size, and structural characteristics
- `{nuclear_characteristics}`: Nucleus size, shape, and chromatin pattern
- `{cytoplasmic_features}`: Cytoplasm appearance and organelle distribution
- `{pathological_indicators}`: Signs of cellular damage or dysfunction

### Clinical Context
- **Research Quality Control**: Cell culture monitoring and validation
- **Experimental Assessment**: Cellular response to treatments or conditions
- **Biomedical Research**: Normal vs pathological cellular states
- **Drug Testing**: Cellular toxicity and morphological changes

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Does this cell show normal or abnormal morphology under microscopic examination?",
  "answer": "B",
  "answer_type": "single_label",
  "options": [
    "Normal morphology",
    "Abnormal morphology"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.85,
  "rationale": "Cell shows morphological alterations including nuclear irregularities and cytoplasmic changes consistent with abnormal morphology",
  "provenance": {
    "original_label": "abnormal",
    "rule_id": "other-medical_classification_binary_easy_1",
    "annotation_id": "cell_morphology_assessment",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: High-resolution microscopic images of individual cells
- **Labels**: Binary labels indicating normal/abnormal morphology status
- **Quality**: Sufficient magnification for cellular detail assessment

### Compatible Datasets
- Cell culture quality control datasets
- Cellular toxicity assessment collections
- Normal vs pathological cell databases
- Drug response morphology datasets
- Cellular research validation sets

### Minimum Standards
- **Image Quality**: Clear visualization of cellular and subcellular structures
- **Annotation Quality**: Expert validation by cell biologists or research scientists
- **Data Distribution**: Balanced representation of normal and abnormal cells

## Template Usage Rules

### Question Construction Rules
1. Focus on microscopic morphological assessment
2. Use standard cell biology terminology
3. Emphasize research and quality control applications
4. Consider cellular health and viability indicators

### Answer Assignment Rules
1. Map healthy, typical cellular appearance → "Normal morphology"
2. Map altered, damaged, or atypical cellular features → "Abnormal morphology"
3. Consider nuclear irregularities, cytoplasmic changes, membrane damage
4. Use established cellular morphology criteria

### Quality Control Guidelines
1. Ensure accurate morphological assessment based on cellular biology standards
2. Verify consistency with cell culture and research protocols
3. Cross-validate with expert cell biologist assessment
4. Review for research and quality control applications

## Examples

### Example 1: Healthy Cell Culture
**Image**: Microscopic view showing cell with normal nuclear and cytoplasmic features  
**Question**: "Does this cell show normal or abnormal morphology under microscopic examination?"  
**Answer**: A. Normal morphology  
**Rationale**: Cell demonstrates normal cellular architecture with regular nucleus, healthy cytoplasm, and intact membrane

### Example 2: Damaged Cell
**Image**: Microscopic view showing cell with nuclear fragmentation and cytoplasmic blebbing  
**Question**: "Does this cell show normal or abnormal morphology under microscopic examination?"  
**Answer**: B. Abnormal morphology  
**Rationale**: Cell shows signs of damage including nuclear fragmentation and membrane blebbing indicating abnormal morphology

### Example 3: Normal Fibroblast
**Image**: Microscopic view of typical fibroblast with characteristic spindle shape  
**Question**: "Does this cell show normal or abnormal morphology under microscopic examination?"  
**Answer**: A. Normal morphology  
**Rationale**: Fibroblast displays characteristic normal morphology with spindle shape and healthy cellular features

### Example 4: Apoptotic Cell
**Image**: Microscopic view showing cell with condensed chromatin and membrane changes  
**Question**: "Does this cell show normal or abnormal morphology under microscopic examination?"  
**Answer**: B. Abnormal morphology  
**Rationale**: Cell demonstrates apoptotic features including chromatin condensation and membrane alterations

### Example 5: Healthy Epithelial Cell
**Image**: Microscopic view of epithelial cell with normal polarization and junctions  
**Question**: "Does this cell show normal or abnormal morphology under microscopic examination?"  
**Answer**: A. Normal morphology  
**Rationale**: Epithelial cell shows normal morphological features with appropriate polarization and cellular organization

## Implementation Notes

### Technical Considerations
- Implement cellular feature analysis algorithms
- Consider different cell types and their normal morphological ranges
- Account for varying microscopy techniques and staining methods
- Handle different magnifications and imaging conditions

### Clinical Validation
- Align with established cell biology and morphology standards
- Cross-reference with cellular research protocols
- Validate against expert cell biologist assessment
- Consider research application requirements

### Dataset-Specific Adaptations
- **Research datasets**: Focus on cell types relevant to specific research applications
- **Quality control datasets**: Emphasize cell culture validation criteria
- **Drug testing datasets**: Include treatment-induced morphological changes
- **Toxicity datasets**: Focus on damage indicators and cellular stress responses

### Quality Assurance
- Regular validation by cell biologists and microscopy experts
- Cross-reference with established cellular morphology standards
- Monitoring for accuracy across different cell types and experimental conditions
- Updates based on advancing cell biology knowledge and imaging techniques
