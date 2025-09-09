# Ophthalmology Anatomical Structure Identification Template

## Template Overview

**Template ID**: `domain-specific_ophthalmology_classification_multiclass_easy_1`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Question Pattern**: Primary anatomical structure identification in fundus images  
**Medical Domain**: Ophthalmology (fundus imaging and retinal anatomy assessment)  
**Domain-knowledge summary**: Requires specialized knowledge of retinal anatomy and fundus examination techniques. Understanding of optic nerve, macula, retinal vessels, fovea, and peripheral retinal landmarks. Knowledge of fundus photography interpretation, anatomical structure recognition, spatial relationships, and clinical significance of retinal anatomy. Expertise in ophthalmological terminology for retinal structures and fundus examination principles.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about primary anatomical structures visible in fundus images. It focuses on identifying the central or most prominent anatomical feature, which is essential for proper fundus examination and pathology localization.

The template is designed for ophthalmology datasets where fundus images are labeled based on the primary anatomical structure in focus, testing the model's ability to recognize and differentiate key retinal landmarks that are crucial for clinical assessment.

## Question Generation Pattern

### Question Format
```
"What is the primary anatomical structure visible in the center of this fundus image?"
```

### Answer Format
Multiple choice with anatomical structure options (A-D):
- A. Optic disc
- B. Macula/fovea
- C. Retinal vessels
- D. Peripheral retina

### Template Variables
- `{structure}`: Primary anatomical structure in focus
- `{modality}`: Always "fundus" for this template
- `{location}`: Anatomical location within the retina

### Clinical Context
- **Optic Disc**: Optic nerve head, typically bright yellowish oval structure
- **Macula/Fovea**: Central retina responsible for detailed vision
- **Retinal Vessels**: Blood vessels emanating from optic disc
- **Peripheral Retina**: Outer retinal areas beyond the posterior pole

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What is the primary anatomical structure visible in the center of this fundus image?",
  "answer": "B",
  "answer_type": "single_label",
  "options": [
    "Optic disc",
    "Macula/fovea",
    "Retinal vessels",
    "Peripheral retina"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Anatomical structure identification for fundus examination",
  "provenance": {
    "original_label": "macula",
    "rule_id": "ophthalmology_classification_multiclass_easy_1",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification (Vision → Image-Level Classification → Multiclass classification)
- **Domain**: Ophthalmology with fundus photography
- **Label Structure**: Categorical labels for primary anatomical structures
- **Image Type**: Color fundus photographs with clear anatomical landmarks
- **Anatomical Coverage**: Images centered on different retinal structures

### Compatible Datasets
- Anatomical structure detection datasets
- Fundus image analysis collections
- Retinal landmark identification datasets
- Ophthalmology training image sets
- Multi-center fundus photography databases

## Template Usage Rules

1. **Central Focus**: Identify the structure occupying the central portion of the image
2. **Anatomical Accuracy**: Use correct ophthalmological terminology
3. **Primary Structure**: Focus on the most prominent anatomical feature
4. **Clinical Relevance**: Maintain connection to examination workflows
5. **Landmark Recognition**: Emphasize structures critical for clinical assessment

## Examples

### Example 1: Optic Disc Centered Image
**Original Dataset**: Optic Disc Analysis Dataset  
**Original Label**: "optic_disc"  
**Generated Q&A**:
- **Question**: "What is the primary anatomical structure visible in the center of this fundus image?"
- **Answer**: "A" (Optic disc)
- **Rationale**: "Optic nerve head is the central focus with characteristic bright appearance"

### Example 2: Macular-Centered Image
**Original Dataset**: Macular Disease Dataset  
**Original Label**: "macula"  
**Generated Q&A**:
- **Question**: "What is the primary anatomical structure visible in the center of this fundus image?"
- **Answer**: "B" (Macula/fovea)
- **Rationale**: "Central retinal area showing macular region and foveal reflex"

### Example 3: Vascular Pattern Focus
**Original Dataset**: Retinal Vessel Analysis Dataset  
**Original Label**: "retinal_vessels"  
**Generated Q&A**:
- **Question**: "What is the primary anatomical structure visible in the center of this fundus image?"
- **Answer**: "C" (Retinal vessels)
- **Rationale**: "Major retinal blood vessels are the dominant feature in this view"

### Example 4: Peripheral Retinal View
**Original Dataset**: Wide-field Fundus Dataset  
**Original Label**: "peripheral_retina"  
**Generated Q&A**:
- **Question**: "What is the primary anatomical structure visible in the center of this fundus image?"
- **Answer**: "D" (Peripheral retina)
- **Rationale**: "Peripheral retinal tissue beyond the posterior pole is shown"

### Example 5: Optic Disc with Vessels
**Original Dataset**: Comprehensive Fundus Collection  
**Original Label**: "optic_disc"  
**Generated Q&A**:
- **Question**: "What is the primary anatomical structure visible in the center of this fundus image?"
- **Answer**: "A" (Optic disc)
- **Rationale**: "Optic disc is centrally located with emerging retinal vessels"

## Implementation Notes

### Advantages
- **Anatomical Foundation**: Tests fundamental retinal anatomy knowledge
- **Clinical Utility**: Relevant for all fundus examinations
- **Structure Recognition**: Essential for pathology localization
- **MCVQA Compatible**: Clear multiclass choice format
- **Educational Value**: Builds anatomical recognition skills

### Limitations
- **Centering Dependency**: Requires structures to be centrally positioned
- **Basic Level**: Does not assess pathological changes
- **Binary Distinctions**: Some structures may overlap or coexist
- **Image Quality**: Dependent on fundus photograph clarity

### Quality Considerations
- Ensure clear visibility and central positioning of target structures
- Verify anatomical accuracy of structure labels
- Consider normal anatomical variations
- Account for different fundus camera types and magnifications
- Validate consistency across different imaging protocols

### Clinical Applications
This template supports:
- **Fundus Examination Training**: Teaching anatomical landmark recognition
- **Image Quality Assessment**: Ensuring proper centering and focus
- **Automated Screening**: Identifying appropriate image types for specific analyses
- **Educational Programs**: Building foundational ophthalmological knowledge
- **Clinical Documentation**: Systematic cataloging of fundus photography
