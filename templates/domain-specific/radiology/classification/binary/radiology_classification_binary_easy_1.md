# Radiology Pneumonia Detection in Chest X-rays Template

## Template Overview

**Template ID**: `radiology_classification_binary_easy_1`  
**Task Type**: Binary classification  
**Difficulty**: Easy  
**Question Pattern**: Pneumonia presence assessment in chest radiographs  
**Medical Domain**: Radiology (chest imaging)  
**Domain-knowledge summary**: Requires specialized radiological knowledge for chest X-ray interpretation and pneumonia diagnosis. Must understand pulmonary anatomy, consolidation patterns, air bronchogram signs, pleural effusion characteristics, normal versus abnormal chest radiographic findings, and ability to recognize classic pneumonia presentations across different patient populations.

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct questions about pneumonia presence in chest X-ray images. This assessment is critical for emergency department triage and antibiotic decision-making, representing one of the most important diagnostic decisions in emergency radiology.

The template is designed for radiology datasets where chest X-rays are labeled for pneumonia presence, testing the model's ability to recognize classic radiological signs of pulmonary infection including consolidation, air bronchograms, and pleural effusion.

## Question Generation Pattern

### Question Format
```
"Does this chest X-ray show evidence of pneumonia?"
```

### Answer Format
Binary choice with radiological options:
- A. Pneumonia present
- B. No pneumonia

### Template Variables
- `{radiological_signs}`: Specific signs of pneumonia (consolidation, air bronchograms)
- `{anatomical_location}`: Pulmonary lobe or region affected
- `{imaging_view}`: PA, AP, or lateral projection
- `{clinical_context}`: Patient symptoms or presentation if available

### Clinical Context
- **Pneumonia Present**: Consolidation, air bronchograms, pleural effusion, infiltrates
- **No Pneumonia**: Clear lung fields, normal pulmonary vasculature, no consolidation
- **Key Signs**: Airspace opacity, silhouette sign, air bronchograms
- **Clinical Importance**: Guides antibiotic therapy and admission decisions

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Does this chest X-ray show evidence of pneumonia?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Pneumonia present",
    "No pneumonia"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.88,
  "rationale": "Right lower lobe consolidation with air bronchograms consistent with pneumonia",
  "provenance": {
    "original_label": "pneumonia",
    "rule_id": "radiology_classification_binary_easy_1",
    "annotation_id": "pneumonia_detection",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Chest X-ray images (PA, AP, or lateral views)
- **Labels**: Binary pneumonia presence/absence classifications
- **Quality**: Sufficient resolution for pulmonary parenchymal assessment

### Compatible Datasets
- CheXpert pneumonia annotations
- MIMIC-CXR pneumonia labels
- NIH Chest X-ray pneumonia detection
- Chest X-ray pneumonia datasets
- Emergency department chest imaging collections

### Minimum Standards
- **Image Quality**: Clear visualization of pulmonary parenchyma and vasculature
- **Annotation Quality**: Radiologist confirmation of pneumonia presence preferred
- **Data Distribution**: Balanced representation of pneumonia-positive and negative cases

## Template Usage Rules

### Question Construction Rules
1. Focus on "evidence of pneumonia" to emphasize radiological findings
2. Use clinical terminology consistent with emergency radiology
3. Maintain objectivity in question phrasing
4. Align with standard radiological reporting practices

### Answer Assignment Rules
1. Map "pneumonia", "consolidation", "infiltrate" → "Pneumonia present"
2. Map "normal", "clear", "no acute findings" → "No pneumonia"
3. Consider all forms of pneumonia (bacterial, viral, aspiration)
4. Use radiologist interpretation as gold standard when available

### Quality Control Guidelines
1. Verify clinical accuracy with radiology standards
2. Ensure consistency with pneumonia imaging criteria
3. Cross-validate with clinical pneumonia guidelines
4. Review for potential confounding pathologies

## Examples

### Example 1: Right Lower Lobe Pneumonia
**Image**: PA chest X-ray showing right lower lobe consolidation  
**Question**: "Does this chest X-ray show evidence of pneumonia?"  
**Answer**: A. Pneumonia present  
**Rationale**: Dense consolidation in right lower lobe with air bronchograms typical of pneumonia

### Example 2: Normal Chest X-ray
**Image**: PA chest X-ray with clear lung fields and normal heart size  
**Question**: "Does this chest X-ray show evidence of pneumonia?"  
**Answer**: B. No pneumonia  
**Rationale**: Clear lung fields without consolidation, infiltrates, or other signs of pneumonia

### Example 3: Left Upper Lobe Pneumonia
**Image**: PA chest X-ray showing left upper lobe airspace opacity  
**Question**: "Does this chest X-ray show evidence of pneumonia?"  
**Answer**: A. Pneumonia present  
**Rationale**: Left upper lobe consolidation with associated volume loss consistent with pneumonia

### Example 4: Bilateral Lower Lobe Pneumonia
**Image**: AP chest X-ray showing bilateral lower lobe infiltrates  
**Question**: "Does this chest X-ray show evidence of pneumonia?"  
**Answer**: A. Pneumonia present  
**Rationale**: Bilateral lower lobe airspace opacities consistent with pneumonia

### Example 5: Chest X-ray with Atelectasis Only
**Image**: PA chest X-ray showing linear atelectasis without consolidation  
**Question**: "Does this chest X-ray show evidence of pneumonia?"  
**Answer**: B. No pneumonia  
**Rationale**: Linear atelectasis without consolidation or air bronchograms, no evidence of pneumonia

## Implementation Notes

### Technical Considerations
- Optimize for detection of airspace opacities and consolidation
- Implement proper windowing and contrast enhancement
- Consider different chest X-ray projections (PA vs AP)
- Handle varying image quality and patient positioning

### Clinical Validation
- Align with current pneumonia imaging guidelines
- Cross-reference with clinical pneumonia criteria
- Validate against radiologist interpretations
- Consider correlation with clinical symptoms when available

### Dataset-Specific Adaptations
- **CheXpert datasets**: Leverage uncertainty labels for ambiguous cases
- **Emergency datasets**: Focus on acute pneumonia presentations
- **ICU datasets**: Consider ventilator-associated pneumonia patterns
- **Pediatric datasets**: Adapt for age-specific pneumonia presentations

### Quality Assurance
- Regular review by chest radiologists
- Validation against established pneumonia imaging criteria
- Monitoring for consistent pneumonia pattern recognition
- Updates based on evolving pneumonia imaging guidelines
