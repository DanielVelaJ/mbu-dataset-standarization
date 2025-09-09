# Object Detection Template 3: Device Detection

## Template Overview

**Template ID**: `domain-agnostic_detection_object_easy_3`  
**Task Type**: Object detection  
**Difficulty**: Easy  
**Question Pattern**: Medical device identification in highlighted bounding boxes  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires understanding of medical device terminology and ability to identify medical devices and instruments within highlighted bounding boxes. Knowledge of medical equipment, implants, surgical instruments, and diagnostic devices across different imaging modalities, but does not require specialized domain expertise.  

## Template Description

This template converts medical device detection datasets into MCVQA format by asking questions about what medical device or hardware is shown in the highlighted bounding box. It is designed for datasets where each image has bounding box annotations identifying specific medical devices, surgical instruments, implants, or monitoring equipment.

## Question Generation Pattern

### Question Format
```
"What medical device is highlighted in the bounding box of this {modality} image?"
```

### Answer Format
- **Single label**: The name of the medical device (e.g., "pacemaker", "endotracheal tube", "central line")

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fluoroscopy", "surgical video", "CT")
- `{device}`: The medical device or hardware (derived from detection labels)

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Detection",
  "question": "What medical device is highlighted in the bounding box of this {modality} image?",
  "answer": "{device_name}",
  "answer_type": "single_label",
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Medical device identification based on bounding box detection annotation",
  "spatial_reference": {
    "reference_type": "bbox",
    "bbox": [0.3, 0.1, 0.5, 0.3],
    "annotation_id": "{original_detection_id}",
    "highlighting_method": "outline",
    "highlight_color": "blue",
    "highlight_opacity": 1.0
  },
  "provenance": {
    "original_label": "{original_device_class}",
    "rule_id": "domain-agnostic_detection_object_easy_3",
    "annotation_id": "{detection_bbox_id}",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template works with medical device detection datasets that have:

- **Medical images** (any modality: X-ray, CT, fluoroscopy, surgical video, ultrasound, etc.)
- **Bounding box annotations** for medical devices/hardware
- **Device class labels** (e.g., tube types, implant names, instrument categories)
- **COCO-format or similar** structured detection annotations

**Required Fields**:
- Image files
- Bounding box coordinates (x, y, width, height or x1, y1, x2, y2)
- Medical device class labels
- Optional: device status, position assessment, manufacturer information

## Template Usage Rules

1. **One question per detected device**: Each bounding box generates one device identification question
2. **Clear highlighting**: The bounding box must be visually highlighted to indicate which device is being questioned
3. **Medical device terminology**: Use clinically accurate device names from medical device databases
4. **Modality specification**: Include the imaging modality to provide procedural context
5. **Answer consistency**: Answers must match the original dataset's device classification scheme

## Examples

### Example 1: Chest X-ray Pacemaker Detection
**Dataset**: CheXpert with Device Annotations
- **Question**: "What medical device is highlighted in the bounding box of this chest X-ray image?"
- **Answer**: "Pacemaker"
- **Modality**: Chest X-ray
- **Domain**: Radiology

### Example 2: ICU Endotracheal Tube Detection  
**Dataset**: MIMIC-CXR with Tube Annotations
- **Question**: "What medical device is highlighted in the bounding box of this chest X-ray image?"
- **Answer**: "Endotracheal tube"
- **Modality**: Chest X-ray
- **Domain**: Critical Care

### Example 3: Surgical Instrument Detection
**Dataset**: 4D-OR Surgical Video Dataset
- **Question**: "What medical device is highlighted in the bounding box of this surgical video image?"
- **Answer**: "Laparoscopic grasper"
- **Modality**: Surgical video
- **Domain**: Surgery

### Example 4: Central Line Detection
**Dataset**: HOSPI-Tools Dataset
- **Question**: "What medical device is highlighted in the bounding box of this chest X-ray image?"
- **Answer**: "Central venous catheter"
- **Modality**: Chest X-ray
- **Domain**: Critical Care

### Example 5: Orthopedic Implant Detection
**Dataset**: Hip Prosthesis X-ray Dataset
- **Question**: "What medical device is highlighted in the bounding box of this X-ray image?"
- **Answer**: "Hip prosthesis"
- **Modality**: X-ray
- **Domain**: Orthopedics

## Implementation Notes

### Advantages
- **Procedural safety**: Supports verification of device placement and positioning
- **Clinical workflow integration**: Aligns with device monitoring and quality assurance protocols
- **Multi-domain applicability**: Works across surgery, radiology, critical care, and other specialties
- **Quality control**: Enables automated device detection for safety and compliance monitoring

### Limitations
- **Device specificity**: Limited by the granularity of device classifications in the original dataset
- **Positioning assessment**: Does not evaluate correctness of device placement (only identification)
- **Temporal constraints**: Single-frame detection may miss device movement or dynamic positioning
- **Technical expertise**: Requires knowledge of medical device terminology and clinical applications

### Quality Considerations
- **Device accuracy**: Ensure device names match FDA classifications and medical device databases
- **Clinical relevance**: Questions should reflect real device monitoring and safety assessment needs
- **Spatial precision**: Bounding boxes should accurately encompass the medical device
- **Safety implications**: Consider clinical safety implications of device detection accuracy

### Best Practices
- **Standard terminology**: Use FDA device classifications and UMLS medical device concepts
- **Clinical context**: Provide procedural context through imaging modality and clinical setting
- **Safety awareness**: Structure questions to support clinical safety and quality assurance goals
- **Multi-specialty coverage**: Include devices from surgery, radiology, critical care, and other domains
- **Temporal considerations**: Consider device stability and positioning over time in video sequences
