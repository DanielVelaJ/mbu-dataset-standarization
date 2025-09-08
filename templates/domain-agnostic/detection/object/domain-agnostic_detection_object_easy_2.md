# Object Detection Template 2: Anatomy Detection

## Template Overview

**Template ID**: `domain-agnostic_detection_object_easy_2`  
**Task Type**: Object Detection  
**Difficulty**: Easy  
**Question Pattern**: Anatomical structure identification in highlighted bounding boxes  

## Template Description

This template converts anatomy detection datasets into MCVQA format by asking questions about what anatomical structure or organ is shown in the highlighted bounding box. It is designed for datasets where each image has bounding box annotations identifying specific anatomical structures, organs, or body parts.

## Question Generation Pattern

### Question Format
```
"What anatomical structure is highlighted in the bounding box of this {modality} image?"
```

### Answer Format
- **Single label**: The name of the anatomical structure (e.g., "liver", "heart", "optic disc", "femur")

### Template Variables
- `{modality}`: The imaging modality (e.g., "CT", "MRI", "X-ray", "ultrasound", "fundus")
- `{structure}`: The anatomical structure or organ (derived from detection labels)

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Detection",
  "question": "What anatomical structure is highlighted in the bounding box of this {modality} image?",
  "answer": "{structure_name}",
  "answer_type": "single_label",
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Anatomical structure identification based on bounding box detection annotation",
  "spatial_reference": {
    "reference_type": "bbox",
    "bbox": [0.1, 0.2, 0.3, 0.4],
    "annotation_id": "{original_detection_id}",
    "highlighting_method": "outline",
    "highlight_color": "green",
    "highlight_opacity": 1.0
  },
  "provenance": {
    "original_label": "{original_anatomy_class}",
    "rule_id": "domain-agnostic_detection_object_easy_2",
    "annotation_id": "{detection_bbox_id}",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template works with anatomy detection datasets that have:

- **Medical images** (any modality: CT, MRI, X-ray, ultrasound, fundus photography, etc.)
- **Bounding box annotations** for anatomical structures/organs
- **Anatomical class labels** (e.g., organ names, bone names, anatomical regions)
- **COCO-format or similar** structured detection annotations

**Required Fields**:
- Image files
- Bounding box coordinates (x, y, width, height or x1, y1, x2, y2)
- Anatomical structure class labels
- Optional: anatomical hierarchy, laterality (left/right)

## Template Usage Rules

1. **One question per detected structure**: Each bounding box generates one anatomical identification question
2. **Clear highlighting**: The bounding box must be visually highlighted to indicate which structure is being questioned
3. **Anatomical terminology**: Use clinically accurate anatomical names from standard anatomical atlases
4. **Modality specification**: Include the imaging modality to provide medical context
5. **Answer consistency**: Answers must match the original dataset's anatomical classification scheme

## Examples

### Example 1: Abdominal CT Organ Detection
**Dataset**: Multi-organ Segmentation Challenge (CHAOS)
- **Question**: "What anatomical structure is highlighted in the bounding box of this CT image?"
- **Answer**: "Liver"
- **Modality**: CT
- **Domain**: Radiology

### Example 2: Fundus Optic Disc Detection  
**Dataset**: MESSIDOR Fundus Image Database
- **Question**: "What anatomical structure is highlighted in the bounding box of this fundus image?"
- **Answer**: "Optic disc"
- **Modality**: Fundus photography
- **Domain**: Ophthalmology

### Example 3: Chest X-ray Heart Detection
**Dataset**: CheXpert Chest X-ray Dataset
- **Question**: "What anatomical structure is highlighted in the bounding box of this X-ray image?"
- **Answer**: "Heart"
- **Modality**: Chest X-ray
- **Domain**: Radiology

### Example 4: Blood Cell Detection in Microscopy
**Dataset**: Blood Cell Detection Dataset
- **Question**: "What anatomical structure is highlighted in the bounding box of this microscopy image?"
- **Answer**: "Red blood cell"
- **Modality**: Microscopy
- **Domain**: Hematology

### Example 5: Knee MRI Bone Detection
**Dataset**: OAI (Osteoarthritis Initiative) Dataset
- **Question**: "What anatomical structure is highlighted in the bounding box of this MRI image?"
- **Answer**: "Femur"
- **Modality**: MRI
- **Domain**: Radiology

## Implementation Notes

### Advantages
- **Educational value**: Supports anatomical education and structure recognition training
- **Cross-modal applicability**: Works across multiple imaging modalities and anatomical regions
- **Clinical foundation**: Builds fundamental anatomical recognition skills essential for medical diagnosis
- **Standardized terminology**: Leverages established anatomical nomenclature and classification systems

### Limitations
- **Structure specificity**: Limited by the granularity of anatomical labels in the original dataset
- **Anatomical complexity**: May not capture fine anatomical subdivisions or variations
- **Detection dependency**: Question quality depends on accuracy of original bounding box annotations
- **Context sensitivity**: Some structures may be ambiguous without broader anatomical context

### Quality Considerations
- **Anatomical accuracy**: Ensure structure names follow standard anatomical nomenclature (Terminologia Anatomica)
- **Spatial precision**: Bounding boxes should accurately encompass the anatomical structure
- **Clinical relevance**: Questions should reflect anatomical knowledge relevant to clinical practice
- **Hierarchical consistency**: Maintain appropriate anatomical hierarchy (organ > tissue > cell)

### Best Practices
- **Standard nomenclature**: Use internationally accepted anatomical terminology (SNOMED CT, FMA)
- **Clear boundaries**: Ensure bounding boxes clearly delineate anatomical structures
- **Contextual clarity**: Provide sufficient anatomical context through imaging modality and region
- **Educational alignment**: Structure questions to support anatomical learning objectives
- **Multi-scale awareness**: Consider anatomical structures at appropriate scales for the imaging modality
