# Ophthalmology Optic Disc Location Assessment Template

## Template Overview

**Template ID**: `domain-specific_ophthalmology_classification_multiclass_easy_3`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Question Pattern**: Spatial location assessment of optic disc in fundus images  
**Medical Domain**: Ophthalmology (fundus imaging and spatial anatomy assessment)  
**Domain-knowledge summary**: Requires specialized knowledge of optic disc anatomy and spatial orientation in fundus photography. Understanding of retinal quadrant anatomy, optic disc positioning, anatomical landmarks, macula-disc relationship, and fundus orientation. Knowledge of spatial assessment terminology, retinal geography, optic nerve head location patterns, and clinical significance of disc positioning for examination protocols.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about the spatial location of the optic disc within fundus images. It focuses on identifying the anatomical quadrant where the optic disc is positioned, which is essential for proper fundus examination, pathology documentation, and understanding anatomical variations.

The template is designed for ophthalmology datasets where fundus images contain optic discs in various positions, testing the model's ability to understand spatial relationships and anatomical orientation within the retina.

## Question Generation Pattern

### Question Format
```
"In which quadrant of this fundus image is the optic disc located?"
```

### Answer Format
Multiple choice with anatomical quadrant options (A-D):
- A. Superior temporal
- B. Superior nasal
- C. Inferior temporal
- D. Inferior nasal

### Template Variables
- `{quadrant}`: Anatomical quadrant (superior/inferior + temporal/nasal)
- `{modality}`: Always "fundus" for this template
- `{disc_position}`: Relative position of optic disc within the image

### Clinical Context
- **Superior/Inferior**: Vertical positioning relative to horizontal midline
- **Temporal/Nasal**: Horizontal positioning relative to central axis
- **Anatomical Reference**: Based on patient's anatomical orientation
- **Clinical Importance**: Location affects examination approach and pathology interpretation

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "In which quadrant of this fundus image is the optic disc located?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Superior temporal",
    "Superior nasal",
    "Inferior temporal",
    "Inferior nasal"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Spatial assessment of optic disc location for anatomical orientation",
  "provenance": {
    "original_label": "superior_temporal",
    "rule_id": "ophthalmology_classification_multiclass_easy_3",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification (Vision → Image-Level Classification → Multiclass classification)
- **Domain**: Ophthalmology with fundus photography
- **Label Structure**: Categorical labels for optic disc quadrant locations
- **Image Type**: Fundus photographs with visible optic disc
- **Spatial Coverage**: Optic discs in various quadrant positions

### Compatible Datasets
- Wide-field fundus photography datasets
- Optic disc localization datasets
- Anatomical variation studies
- Fundus image quality assessment datasets
- Multi-center ophthalmology collections

## Template Usage Rules

1. **Anatomical Orientation**: Use standard ophthalmological spatial terminology
2. **Quadrant Definition**: Clear division into four anatomical quadrants
3. **Reference Frame**: Maintain consistent anatomical reference system
4. **Disc Identification**: Ensure optic disc is clearly visible and identifiable
5. **Spatial Accuracy**: Precise quadrant assignment based on disc center

## Examples

### Example 1: Superior Temporal Location
**Original Dataset**: Wide-field Fundus Dataset  
**Original Label**: "superior_temporal"  
**Generated Q&A**:
- **Question**: "In which quadrant of this fundus image is the optic disc located?"
- **Answer**: "A" (Superior temporal)
- **Rationale**: "Optic disc is positioned in the upper temporal region of the fundus"

### Example 2: Superior Nasal Location
**Original Dataset**: Optic Disc Localization Dataset  
**Original Label**: "superior_nasal"  
**Generated Q&A**:
- **Question**: "In which quadrant of this fundus image is the optic disc located?"
- **Answer**: "B" (Superior nasal)
- **Rationale**: "Optic disc is located in the upper nasal quadrant of the retina"

### Example 3: Inferior Temporal Location
**Original Dataset**: Anatomical Variation Study  
**Original Label**: "inferior_temporal"  
**Generated Q&A**:
- **Question**: "In which quadrant of this fundus image is the optic disc located?"
- **Answer**: "C" (Inferior temporal)
- **Rationale**: "Optic disc appears in the lower temporal portion of the fundus image"

### Example 4: Inferior Nasal Location
**Original Dataset**: Comprehensive Fundus Collection  
**Original Label**: "inferior_nasal"  
**Generated Q&A**:
- **Question**: "In which quadrant of this fundus image is the optic disc located?"
- **Answer**: "D" (Inferior nasal)
- **Rationale**: "Optic disc is positioned in the lower nasal quadrant of the retina"

### Example 5: Temporal Superior Positioning
**Original Dataset**: Multi-center Ophthalmology Dataset  
**Original Label**: "superior_temporal"  
**Generated Q&A**:
- **Question**: "In which quadrant of this fundus image is the optic disc located?"
- **Answer**: "A" (Superior temporal)
- **Rationale**: "Clear visualization of optic disc in the superior temporal quadrant"

## Implementation Notes

### Advantages
- **Spatial Reasoning**: Tests understanding of anatomical spatial relationships
- **Orientation Skills**: Develops spatial awareness crucial for ophthalmology
- **Clinical Utility**: Relevant for documentation and pathology localization
- **MCVQA Compatible**: Clear multiclass spatial choice format
- **Educational Value**: Builds anatomical orientation competency

### Limitations
- **Disc Visibility**: Requires clear optic disc visualization
- **Border Cases**: Discs near quadrant boundaries may be ambiguous
- **Image Orientation**: Dependent on standard fundus photography positioning
- **Reference Dependency**: Requires consistent anatomical reference frame

### Quality Considerations
- Ensure optic disc is clearly visible and well-defined
- Verify consistent image orientation across dataset
- Consider anatomical variations in disc position
- Account for different fundus camera fields of view
- Validate quadrant assignments against anatomical standards

### Clinical Applications
This template supports:
- **Anatomical Education**: Teaching spatial relationships in fundus examination
- **Documentation Training**: Proper anatomical location recording
- **Image Quality Control**: Ensuring appropriate fundus photograph positioning
- **Pathology Mapping**: Accurate localization of retinal abnormalities
- **Clinical Communication**: Standardized anatomical reference for consultations
