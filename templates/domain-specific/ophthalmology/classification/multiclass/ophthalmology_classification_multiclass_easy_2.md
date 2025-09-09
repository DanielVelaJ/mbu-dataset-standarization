# Ophthalmology OCT Retinal Pathology Analysis Template

## Template Overview

**Template ID**: `domain-specific_ophthalmology_classification_multiclass_easy_2`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Question Pattern**: Retinal pathology identification in OCT imaging  
**Medical Domain**: Ophthalmology (OCT retinal imaging and pathology assessment)  
**Domain-knowledge summary**: Requires specialized knowledge of OCT imaging and retinal pathology. Understanding of retinal layer anatomy, pathological changes, diabetic maculopathy, age-related macular degeneration, choroidal neovascularization, and retinal detachment patterns. Knowledge of OCT interpretation, cross-sectional retinal analysis, pathological feature recognition, and clinical correlation with retinal diseases.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about retinal pathologies visible in OCT (Optical Coherence Tomography) images. It focuses on identifying the most evident pathological finding, which is crucial for retinal disease diagnosis and treatment planning.

The template is designed for ophthalmology datasets where OCT images are labeled based on primary retinal pathologies, testing the model's ability to recognize layer-specific abnormalities and structural changes characteristic of common retinal diseases.

## Question Generation Pattern

### Question Format
```
"Which retinal pathology is most evident in this OCT image?"
```

### Answer Format
Multiple choice with pathology options (A-E):
- A. Diabetic macular edema
- B. Age-related macular degeneration
- C. Retinal detachment
- D. Normal retina
- E. Epiretinal membrane

### Template Variables
- `{pathology}`: Primary retinal pathology identified
- `{modality}`: Always "OCT" for this template
- `{layer_involvement}`: Specific retinal layers affected

### Clinical Context
- **Diabetic Macular Edema**: Fluid accumulation in macula due to diabetes
- **Age-related Macular Degeneration**: Drusen deposits or neovascularization
- **Retinal Detachment**: Separation of neurosensory retina from RPE
- **Normal Retina**: Intact retinal architecture with clear layer definition
- **Epiretinal Membrane**: Fibrous tissue on retinal surface

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Which retinal pathology is most evident in this OCT image?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Diabetic macular edema",
    "Age-related macular degeneration",
    "Retinal detachment",
    "Normal retina",
    "Epiretinal membrane"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "OCT-based retinal pathology identification for treatment planning",
  "provenance": {
    "original_label": "diabetic_macular_edema",
    "rule_id": "ophthalmology_classification_multiclass_easy_2",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification (Vision → Image-Level Classification → Multiclass classification)
- **Domain**: Ophthalmology with OCT retinal imaging
- **Label Structure**: Categorical labels for retinal pathologies
- **Image Type**: OCT cross-sectional retinal scans
- **Pathology Coverage**: Common retinal diseases and normal variants

### Compatible Datasets
- OCT retinal pathology datasets
- Macular disease classification datasets
- Diabetic retinopathy OCT collections
- Age-related macular degeneration datasets
- Multi-center OCT databases

## Template Usage Rules

1. **Pathology Specificity**: Use established clinical diagnostic criteria
2. **Layer Awareness**: Consider which retinal layers are affected
3. **Clinical Terminology**: Use standard ophthalmological pathology names
4. **Severity Neutrality**: Focus on pathology type rather than severity
5. **OCT Interpretation**: Maintain relevance to OCT imaging capabilities

## Examples

### Example 1: Diabetic Macular Edema
**Original Dataset**: Diabetic OCT Dataset  
**Original Label**: "diabetic_macular_edema"  
**Generated Q&A**:
- **Question**: "Which retinal pathology is most evident in this OCT image?"
- **Answer**: "A" (Diabetic macular edema)
- **Rationale**: "Cystoid spaces and retinal thickening characteristic of diabetic macular edema"

### Example 2: Age-Related Macular Degeneration
**Original Dataset**: AMD OCT Collection  
**Original Label**: "amd"  
**Generated Q&A**:
- **Question**: "Which retinal pathology is most evident in this OCT image?"
- **Answer**: "B" (Age-related macular degeneration)
- **Rationale**: "Drusen deposits and RPE changes consistent with age-related macular degeneration"

### Example 3: Retinal Detachment
**Original Dataset**: Retinal Detachment OCT Dataset  
**Original Label**: "retinal_detachment"  
**Generated Q&A**:
- **Question**: "Which retinal pathology is most evident in this OCT image?"
- **Answer**: "C" (Retinal detachment)
- **Rationale**: "Clear separation between neurosensory retina and retinal pigment epithelium"

### Example 4: Normal Retinal Architecture
**Original Dataset**: Control OCT Dataset  
**Original Label**: "normal"  
**Generated Q&A**:
- **Question**: "Which retinal pathology is most evident in this OCT image?"
- **Answer**: "D" (Normal retina)
- **Rationale**: "Intact retinal layers with normal foveal contour and thickness"

### Example 5: Epiretinal Membrane
**Original Dataset**: Vitreoretinal Interface Dataset  
**Original Label**: "epiretinal_membrane"  
**Generated Q&A**:
- **Question**: "Which retinal pathology is most evident in this OCT image?"
- **Answer**: "E" (Epiretinal membrane)
- **Rationale**: "Hyperreflective tissue on the retinal surface causing distortion"

## Implementation Notes

### Advantages
- **OCT-Specific**: Tailored to high-resolution retinal imaging
- **Pathology Focus**: Tests disease recognition capabilities
- **Layer Analysis**: Utilizes OCT's unique cross-sectional view
- **MCVQA Compatible**: Clear multiclass diagnostic choices
- **Clinical Relevance**: Directly applicable to retinal subspecialty practice

### Limitations
- **OCT-Dependent**: Requires familiarity with OCT imaging characteristics
- **Pathology Subset**: Limited to common retinal diseases
- **Severity Agnostic**: Does not assess disease staging or severity
- **Static Assessment**: Cannot evaluate disease progression

### Quality Considerations
- Ensure OCT images have adequate quality and resolution
- Verify pathology labels against clinical diagnostic criteria
- Consider normal anatomical variations and artifacts
- Account for different OCT machine types and scanning protocols
- Validate pathological findings with retinal subspecialists when possible

### Clinical Applications
This template supports:
- **Retinal Disease Screening**: Automated OCT interpretation for common pathologies
- **Educational Training**: Teaching OCT interpretation to ophthalmology residents
- **Telemedicine**: Remote OCT analysis for underserved populations
- **Clinical Decision Support**: AI-assisted diagnosis in retinal clinics
- **Research Applications**: Standardized pathology classification for clinical studies
