# Other-Medical Brain Region Identification Template

## Template Overview

**Template ID**: `other-medical_classification_multiclass_easy_2`  
**Task Type**: Multiclass classification  
**Difficulty**: Easy  
**Question Pattern**: Brain region identification in neuroimaging  
**Medical Domain**: Other-Medical (neuroscience imaging)  
**Domain-knowledge summary**: Requires general neuroscience knowledge for brain anatomy and neuroimaging interpretation. Must understand basic neuroanatomy, brain region identification, neuroimaging modalities, anatomical landmarks, and ability to recognize different brain structures and regions across various neuroimaging techniques for research applications.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about brain regions in neuroimaging slices. This capability is important for neuroscience research, brain mapping, and neurological assessment applications.

The template is designed for other-medical datasets with brain region annotations, testing the model's ability to identify anatomical brain structures and neuroanatomical regions based on imaging characteristics.

## Question Generation Pattern

### Question Format
```
"Which brain region is primarily visible in this neuroimaging slice?"
```

### Answer Format
Multiclass choice with brain region options:
- A. Frontal cortex
- B. Parietal cortex
- C. Temporal cortex
- D. Occipital cortex
- E. Cerebellum
- F. Brainstem
- G. Hippocampus
- H. Basal ganglia

### Template Variables
- `{anatomical_landmarks}`: Distinctive structural features and reference points
- `{cortical_patterns}`: Gray and white matter organization and appearance
- `{regional_characteristics}`: Shape, size, and positioning relative to other structures
- `{imaging_modality}`: MRI, CT, or other neuroimaging technique used

### Clinical Context
- **Neuroscience Research**: Brain structure analysis and functional mapping
- **Neurological Assessment**: Anatomical evaluation for neurological conditions
- **Brain Mapping**: Spatial localization and anatomical reference
- **Educational Applications**: Neuroanatomy teaching and training

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Which brain region is primarily visible in this neuroimaging slice?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Frontal cortex",
    "Parietal cortex", 
    "Temporal cortex",
    "Occipital cortex",
    "Cerebellum",
    "Brainstem",
    "Hippocampus",
    "Basal ganglia"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Image shows anterior brain regions with characteristic frontal lobe anatomy and cortical organization",
  "provenance": {
    "original_label": "frontal_cortex",
    "rule_id": "other-medical_classification_multiclass_easy_2",
    "annotation_id": "brain_region_identification",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Brain imaging slices (MRI, CT) showing distinct anatomical regions
- **Labels**: Brain region annotations with anatomical context
- **Quality**: Sufficient resolution for neuroanatomical structure identification

### Compatible Datasets
- Brain atlas and mapping datasets
- Neuroimaging research collections
- Neuroanatomy reference databases
- Brain structure identification sets
- Neuroscience research imaging archives

### Minimum Standards
- **Image Quality**: Clear visualization of brain structures and anatomical landmarks
- **Annotation Quality**: Expert validation by neuroanatomists or neuroscientists
- **Data Distribution**: Representative coverage of major brain regions

## Template Usage Rules

### Question Construction Rules
1. Focus on primary brain region identification based on anatomical features
2. Use standard neuroanatomical terminology
3. Consider imaging characteristics and anatomical landmarks
4. Emphasize neuroscience research and educational applications

### Answer Assignment Rules
1. Map anterior cerebral regions → "Frontal cortex"
2. Map superior posterior cerebral regions → "Parietal cortex"
3. Map lateral middle cerebral regions → "Temporal cortex"
4. Map posterior cerebral regions → "Occipital cortex"
5. Map posterior fossa structures → "Cerebellum"
6. Map central brain structures → "Brainstem"
7. Map medial temporal structures → "Hippocampus"
8. Map deep brain nuclei → "Basal ganglia"

### Quality Control Guidelines
1. Ensure accurate neuroanatomical identification and nomenclature
2. Verify consistency with brain atlas references
3. Cross-validate with expert neuroanatomist assessment
4. Review for educational and research applications

## Examples

### Example 1: Frontal Lobe MRI
**Image**: Sagittal MRI slice showing anterior brain regions  
**Question**: "Which brain region is primarily visible in this neuroimaging slice?"  
**Answer**: A. Frontal cortex  
**Rationale**: Image shows characteristic frontal lobe anatomy with prefrontal and motor cortical regions

### Example 2: Cerebellar Anatomy
**Image**: MRI slice showing posterior fossa structures  
**Question**: "Which brain region is primarily visible in this neuroimaging slice?"  
**Answer**: E. Cerebellum  
**Rationale**: Image demonstrates characteristic cerebellar folial pattern and posterior fossa location

### Example 3: Temporal Lobe Structure
**Image**: Coronal MRI slice showing lateral brain regions  
**Question**: "Which brain region is primarily visible in this neuroimaging slice?"  
**Answer**: C. Temporal cortex  
**Rationale**: Image shows temporal lobe anatomy with characteristic lateral positioning and hippocampal structures

### Example 4: Brainstem Visualization
**Image**: Sagittal MRI showing central brain structures  
**Question**: "Which brain region is primarily visible in this neuroimaging slice?"  
**Answer**: F. Brainstem  
**Rationale**: Image demonstrates brainstem structures including midbrain, pons, and medulla

### Example 5: Hippocampal Formation
**Image**: Coronal MRI slice showing medial temporal structures  
**Question**: "Which brain region is primarily visible in this neuroimaging slice?"  
**Answer**: G. Hippocampus  
**Rationale**: Image shows characteristic hippocampal formation with curved structure in medial temporal lobe

## Implementation Notes

### Technical Considerations
- Implement neuroanatomical landmark recognition algorithms
- Consider different imaging modalities and slice orientations
- Account for individual anatomical variations
- Handle different image contrast and resolution parameters

### Clinical Validation
- Align with standard neuroanatomical atlases and references
- Cross-reference with neuroscience education materials
- Validate against expert neuroanatomist identification
- Consider research application requirements

### Dataset-Specific Adaptations
- **Research datasets**: Focus on regions relevant to specific neuroscience studies
- **Clinical datasets**: Emphasize clinically important brain structures
- **Educational datasets**: Include comprehensive anatomical coverage
- **Atlas datasets**: Provide standardized anatomical references

### Quality Assurance
- Regular validation by neuroanatomists and neuroscience researchers
- Cross-reference with established brain atlas standards
- Monitoring for accuracy across different imaging modalities
- Updates based on advancing neuroanatomical knowledge and imaging techniques
