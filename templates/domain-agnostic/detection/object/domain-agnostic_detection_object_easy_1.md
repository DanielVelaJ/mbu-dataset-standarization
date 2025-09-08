# Object Detection Template 1: Lesion Detection

## Template Overview

**Template ID**: `domain-agnostic_detection_object_easy_1`  
**Task Type**: Object Detection  
**Difficulty**: Easy  
**Question Pattern**: Lesion classification in highlighted bounding boxes  

## Template Description

This template converts lesion detection datasets into MCVQA format by asking questions about what type of lesion or pathological finding is shown in the highlighted bounding box. It is designed for datasets where each image has bounding box annotations identifying specific lesions, nodules, tumors, or other pathological findings.

## Question Generation Pattern

### Question Format
```
"What type of lesion is highlighted in the bounding box of this {modality} image?"
```

### Answer Format
- **Single label**: The name of the lesion type (e.g., "pulmonary nodule", "melanoma", "brain tumor")

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest X-ray", "MRI", "dermoscopy", "CT", "fundus")
- `{lesion_type}`: The lesion or pathological finding type (derived from detection labels)

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Detection",
  "question": "What type of lesion is highlighted in the bounding box of this {modality} image?",
  "answer": "{lesion_type}",
  "answer_type": "single_label",
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Lesion classification based on bounding box detection annotation",
  "spatial_reference": {
    "reference_type": "bbox",
    "bbox": [0.2, 0.3, 0.4, 0.5],
    "annotation_id": "{original_detection_id}",
    "highlighting_method": "outline",
    "highlight_color": "yellow",
    "highlight_opacity": 1.0
  },
  "provenance": {
    "original_label": "{original_lesion_class}",
    "rule_id": "domain-agnostic_detection_object_easy_1",
    "annotation_id": "{detection_bbox_id}",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template works with lesion detection datasets that have:

- **Medical images** (any modality: X-ray, CT, MRI, dermoscopy, fundus photography, etc.)
- **Bounding box annotations** for lesions/pathological findings
- **Lesion class labels** (e.g., nodule types, tumor categories, pathological findings)
- **COCO-format or similar** structured detection annotations

**Required Fields**:
- Image files
- Bounding box coordinates (x, y, width, height or x1, y1, x2, y2)
- Lesion/pathology class labels
- Optional: confidence scores, severity ratings

## Template Usage Rules

1. **One question per detected lesion**: Each bounding box generates one classification question
2. **Clear highlighting**: The bounding box must be visually highlighted to indicate which lesion is being questioned
3. **Medical terminology**: Use clinically accurate lesion names from the dataset's class vocabulary
4. **Modality specification**: Include the imaging modality to provide medical context
5. **Answer consistency**: Answers must match the original dataset's lesion classification scheme

## Examples

### Example 1: Chest X-ray Pulmonary Nodule Detection
**Dataset**: LIDC-IDRI (Lung Image Database Consortium)
- **Question**: "What type of lesion is highlighted in the bounding box of this chest X-ray image?"
- **Answer**: "Pulmonary nodule"
- **Modality**: Chest X-ray
- **Domain**: Radiology

### Example 2: Dermoscopy Skin Lesion Detection  
**Dataset**: ISIC Skin Lesion Detection Challenge
- **Question**: "What type of lesion is highlighted in the bounding box of this dermoscopy image?"
- **Answer**: "Melanoma"
- **Modality**: Dermoscopy
- **Domain**: Dermatology

### Example 3: Brain MRI Tumor Detection
**Dataset**: BraTS (Brain Tumor Segmentation Challenge)
- **Question**: "What type of lesion is highlighted in the bounding box of this MRI image?"
- **Answer**: "Glioblastoma"
- **Modality**: MRI
- **Domain**: Radiology

### Example 4: Fundus Diabetic Retinopathy Detection
**Dataset**: MESSIDOR Diabetic Retinopathy Detection
- **Question**: "What type of lesion is highlighted in the bounding box of this fundus image?"
- **Answer**: "Microaneurysm"
- **Modality**: Fundus photography
- **Domain**: Ophthalmology

### Example 5: Mammography Mass Detection
**Dataset**: CBIS-DDSM (Curated Breast Imaging Subset of DDSM)
- **Question**: "What type of lesion is highlighted in the bounding box of this mammography image?"
- **Answer**: "Malignant mass"
- **Modality**: Mammography
- **Domain**: Radiology

## Implementation Notes

### Advantages
- **Clinical relevance**: Directly supports diagnostic workflows by identifying pathological findings
- **Spatial precision**: Bounding boxes provide clear spatial context for lesion location
- **Cross-domain applicability**: Works across radiology, dermatology, ophthalmology, and pathology
- **Assessment capability**: Enables evaluation of lesion detection and classification accuracy

### Limitations
- **Single lesion focus**: Each question addresses only one detected lesion (use multiple questions for multiple lesions)
- **Class dependency**: Limited by the original dataset's lesion classification scheme
- **Detection quality**: Question quality depends on accuracy of original bounding box annotations
- **Medical expertise**: Requires medically accurate lesion terminology and classification

### Quality Considerations
- **Medical accuracy**: Ensure lesion names match established medical terminology and diagnostic criteria
- **Spatial clarity**: Bounding boxes must clearly encompass the lesion without excessive background
- **Clinical context**: Questions should reflect real diagnostic scenarios and clinical decision-making processes
- **Answer validation**: Lesion classifications should be verified against medical literature and clinical standards

### Best Practices
- **Consistent terminology**: Use standardized medical vocabulary (ICD-10, SNOMED CT when applicable)
- **Clear visualization**: Ensure bounding box highlighting is prominent and unambiguous
- **Context provision**: Include relevant clinical context through imaging modality specification
- **Quality control**: Validate lesion classifications with medical domain experts when possible
