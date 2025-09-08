# Semantic Segmentation Template 1: Region Identification

## Template Overview

**Template ID**: `domain-agnostic_segmentation_semantic_easy_1`  
**Task Type**: Semantic Segmentation  
**Difficulty**: Easy  
**Question Pattern**: Anatomical structure identification in segmented regions  

## Template Description

This template converts semantic segmentation datasets into MCVQA format by asking questions about what anatomical structure or tissue type is shown in the segmented region. It is designed for datasets where each image has pixel-level annotations identifying specific anatomical structures, organs, or tissue types.

## Question Generation Pattern

### Question Format
```
"What anatomical structure is highlighted in the segmented region of this {modality} image?"
```

### Answer Format
- **Single label**: The name of the anatomical structure (e.g., "liver", "optic disc", "skin lesion")

### Template Variables
- `{modality}`: The imaging modality (e.g., "CT", "MRI", "fundus", "X-ray", "microscopy")
- `{structure}`: The anatomical structure being segmented (derived from segmentation labels)

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Segmentation",
  "question": "What anatomical structure is highlighted in the segmented region of this {modality} image?",
  "answer": "{structure_name}",
  "answer_type": "single_label",
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Anatomical structure identification based on pixel-level segmentation mask",
  "provenance": {
    "original_label": "{segmentation_class_label}",
    "rule_id": "domain-agnostic_segmentation_semantic_easy_1",
    "annotation_id": "{mask_id}",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Semantic segmentation (Vision → Segmentation → Semantic segmentation)
- **Annotation Structure**: Pixel-level masks or class labels for anatomical structures
- **Clear Labels**: Well-defined anatomical structure names or tissue type classifications
- **Medical Context**: Anatomical structures relevant to medical diagnosis

## Template Usage Rules

1. **Structure Names**: Use standard anatomical terminology from the dataset's class definitions
2. **Modality Specification**: Include the imaging modality to provide clinical context
3. **Consistent Terminology**: Use medically accurate anatomical structure names
4. **Single Structure**: Each question focuses on one segmented structure per image
5. **Label Mapping**: Map segmentation class IDs to anatomical structure names

## Examples

### Example 1: Liver Segmentation in Abdominal CT
**Original Dataset**: Medical Segmentation Decathlon - Liver  
**Original Label**: Liver segmentation mask  
**Generated Q&A**:
- **Question**: "What anatomical structure is highlighted in the segmented region of this CT image?"
- **Answer**: "Liver"
- **Rationale**: "Liver region identified and segmented based on CT imaging characteristics"

### Example 2: Optic Disc Segmentation in Fundus Images
**Original Dataset**: DRIVE Retinal Vessel Segmentation  
**Original Label**: Optic disc segmentation mask  
**Generated Q&A**:
- **Question**: "What anatomical structure is highlighted in the segmented region of this fundus image?"
- **Answer**: "Optic disc"
- **Rationale**: "Optic disc region delineated in retinal fundus photography"

### Example 3: Skin Lesion Segmentation in Dermoscopy
**Original Dataset**: ISIC Skin Lesion Segmentation  
**Original Label**: Lesion boundary segmentation  
**Generated Q&A**:
- **Question**: "What anatomical structure is highlighted in the segmented region of this dermoscopy image?"
- **Answer**: "Skin lesion"
- **Rationale**: "Lesion boundary accurately segmented for dermatological analysis"

### Example 4: Heart Segmentation in Cardiac MRI
**Original Dataset**: Cardiac MRI Segmentation Challenge  
**Original Label**: Left ventricle segmentation mask  
**Generated Q&A**:
- **Question**: "What anatomical structure is highlighted in the segmented region of this MRI image?"
- **Answer**: "Left ventricle"
- **Rationale**: "Left ventricle chamber segmented for cardiac function assessment"

### Example 5: Cell Nuclei Segmentation in Histopathology
**Original Dataset**: MoNuSeg Nuclei Segmentation  
**Original Label**: Cell nuclei segmentation masks  
**Generated Q&A**:
- **Question**: "What anatomical structure is highlighted in the segmented region of this microscopy image?"
- **Answer**: "Cell nuclei"
- **Rationale**: "Individual cell nuclei segmented for histopathological analysis"

## Implementation Notes

### Advantages
- **Anatomical Focus**: Tests fundamental knowledge of medical anatomy
- **Clear Evaluation**: Straightforward structure identification with definitive answers
- **Cross-Domain**: Works across radiology, pathology, ophthalmology, and dermatology
- **Educational Value**: Reinforces anatomical knowledge in medical AI systems

### Limitations
- **Single Structure**: Only handles one anatomical structure per question
- **No Spatial Relations**: Does not test relationships between multiple structures
- **No Quality Assessment**: Does not evaluate segmentation accuracy or boundary quality
- **Basic Level**: Limited to simple structure identification without clinical reasoning

### Quality Considerations
- Ensure anatomical structure names are medically accurate and standardized
- Verify that segmentation masks correspond to the named anatomical structures
- Use appropriate anatomical terminology for the target medical domain
- Confirm that the imaging modality context is clinically relevant
- Validate that segmented regions are clearly identifiable and well-defined
