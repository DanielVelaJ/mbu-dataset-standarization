# Radiology Radiological Finding Description Template

## Template Overview

**Template ID**: `radiology_vision-language_describe_short_easy_1`  
**Task Type**: Vision-language (describe)  
**Difficulty**: Easy  
**Question Pattern**: Radiological finding description selection  
**Medical Domain**: Radiology (medical imaging)  
**Domain-knowledge summary**: Requires specialized radiological knowledge for medical imaging interpretation and report generation. Must understand radiological anatomy, pathological terminology, imaging findings description, clinical reporting standards, and ability to generate concise, clinically accurate descriptions of radiological findings across multiple imaging modalities.

## Template Description

This template converts vision-language datasets into MCVQA format by asking models to select the most accurate radiological description of primary findings in medical images. This capability tests the model's ability to recognize appropriate medical terminology and structured radiological reporting conventions through multiple choice selection.

The template is designed for radiology datasets with image-text pairs, testing the model's ability to identify clinically accurate, concise descriptions that follow radiological reporting standards.

## Question Generation Pattern

### Question Format
```
"Which statement best describes the primary radiological finding in this image?"
```

### Answer Format
Multiple choice with radiological description options:
- A. [First radiological description option]
- B. [Second radiological description option]  
- C. [Third radiological description option]
- D. [Fourth radiological description option]
- E. No significant radiological findings

### Template Variables
- `{imaging_modality}`: CT, MRI, X-ray, ultrasound, etc.
- `{anatomical_region}`: Specific body system or organ
- `{finding_characteristics}`: Size, shape, density, enhancement pattern
- `{clinical_significance}`: Implications or differential considerations

### Clinical Context
- **Radiological Reporting**: Tests recognition of proper radiology report structure
- **Medical Communication**: Evaluates understanding of professional medical language
- **Educational Value**: Supports radiological training through description recognition
- **Clinical Decision Support**: Validates ability to identify accurate clinical descriptions

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Which statement best describes the primary radiological finding in this image?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "There is a 3.2 cm well-circumscribed hypodense lesion in the right hepatic lobe, consistent with a simple hepatic cyst.",
    "Multiple hyperenhancing lesions throughout the liver consistent with hepatocellular carcinoma.",
    "Diffuse hepatic steatosis with no focal lesions identified.",
    "Normal hepatic parenchyma with no abnormalities detected.",
    "No significant radiological findings"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.88,
  "rationale": "Description includes anatomical location, size, imaging characteristics, and most likely diagnosis",
  "provenance": {
    "original_label": "hepatic_cyst_description",
    "rule_id": "radiology_vision-language_describe_short_easy_1",
    "annotation_id": "finding_description",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Medical imaging studies (CT, MRI, X-ray, ultrasound)
- **Captions**: Radiological descriptions or report excerpts
- **Quality**: Professional radiological language and accurate medical terminology

### Compatible Datasets
- MIMIC-CXR reports and images
- RadGraph structured reporting datasets
- Medical image-caption pairs
- Radiological atlas descriptions
- Educational radiology databases

### Minimum Standards
- **Image Quality**: Diagnostic quality medical images
- **Caption Quality**: Professionally written radiological descriptions
- **Medical Accuracy**: Verified by qualified radiologists

## Template Usage Rules

### Question Construction Rules
1. Ask for the "best" description to emphasize accuracy and clinical appropriateness
2. Focus on "primary finding" to maintain clarity
3. Ensure all options use proper radiological terminology
4. Include clinically relevant differential options

### Description Option Guidelines
1. Correct option should include anatomical location, size, and characteristics
2. Distractors should be clinically plausible but incorrect for the image
3. Use standard radiological terminology and abbreviations consistently
4. Include normal/negative option when appropriate

### Quality Control Guidelines
1. Verify medical accuracy and appropriate terminology
2. Ensure descriptions are clinically relevant and actionable
3. Check for proper anatomical references and measurements
4. Validate diagnostic reasoning and differential considerations

## Examples

### Example 1: Liver Lesion Description
**Image**: Contrast-enhanced CT showing hepatic lesion  
**Question**: "Which statement best describes the primary radiological finding in this image?"  
**Options**: A. There is a 3.2 cm well-circumscribed hypodense lesion in the right hepatic lobe, consistent with a simple hepatic cyst. | B. Multiple hyperenhancing lesions throughout the liver consistent with hepatocellular carcinoma. | C. Diffuse hepatic steatosis with no focal lesions identified. | D. Normal hepatic parenchyma with no abnormalities detected.  
**Answer**: A  
**Rationale**: Correctly describes location, size, imaging characteristics, and most likely diagnosis

### Example 2: Pulmonary Nodule Report
**Image**: Chest CT showing pulmonary nodule  
**Question**: "Which statement best describes the primary radiological finding in this image?"  
**Options**: A. Normal chest CT with clear lung fields. | B. A 1.8 cm spiculated nodule is present in the right upper lobe with associated pleural retraction. | C. Bilateral lower lobe consolidation consistent with pneumonia. | D. Pulmonary embolism in the main pulmonary artery.  
**Answer**: B  
**Rationale**: Accurately details nodule characteristics and associated findings

### Example 3: Brain Hemorrhage Description
**Image**: Non-contrast CT head showing hemorrhage  
**Question**: "Which statement best describes the primary radiological finding in this image?"  
**Options**: A. Normal brain CT with no acute findings. | B. Large ischemic stroke in the middle cerebral artery territory. | C. Acute intraparenchymal hemorrhage in the left basal ganglia with mild surrounding edema. | D. Chronic subdural hematoma with mass effect.  
**Answer**: C  
**Rationale**: Correctly identifies type, location, and secondary changes

### Example 4: Bone Fracture Report
**Image**: X-ray showing femoral fracture  
**Question**: "Which statement best describes the primary radiological finding in this image?"  
**Options**: A. Normal femur with no fractures identified. | B. Comminuted fracture of the mid-shaft femur with moderate displacement and angulation. | C. Simple hairline fracture of the proximal femur. | D. Degenerative joint disease of the hip without fracture.  
**Answer**: B  
**Rationale**: Accurately describes fracture pattern, location, and displacement

### Example 5: Cardiac Finding Description
**Image**: Chest X-ray showing cardiomegaly  
**Question**: "Which statement best describes the primary radiological finding in this image?"  
**Options**: A. Normal cardiac silhouette and clear lung fields. | B. Pneumothorax with collapsed lung. | C. Moderate cardiomegaly with borderline pulmonary vascular congestion. | D. Massive pleural effusion obscuring cardiac borders.  
**Answer**: C  
**Rationale**: Correctly quantifies cardiac enlargement and associated findings

## Implementation Notes

### Technical Considerations
- Implement medical language models trained on radiological texts
- Ensure consistent medical terminology and abbreviation use
- Handle multi-finding images by focusing on primary abnormality
- Consider modality-specific reporting conventions

### Clinical Validation
- Validate descriptions against radiological reporting standards
- Ensure anatomical accuracy and appropriate medical terminology
- Cross-reference with established radiological lexicons
- Verify clinical relevance and diagnostic accuracy

### Dataset-Specific Adaptations
- **MIMIC datasets**: Leverage structured reporting and impression sections
- **Educational datasets**: Focus on classic textbook presentations
- **Research datasets**: Handle novel or complex finding combinations
- **Multi-modal datasets**: Adapt descriptions for different imaging modalities

### Quality Assurance
- Regular review by board-certified radiologists
- Validation against radiological reporting guidelines
- Monitoring for medical terminology accuracy and consistency
- Updates based on evolving radiological communication standards
