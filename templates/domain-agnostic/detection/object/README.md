# Domain-Agnostic Object Detection Templates

This directory contains templates for converting object detection datasets into MCVQA (Medical Computer Vision Question Answering) format. These templates are designed to work across all medical domains and imaging modalities.

## Template Collection Overview

**Task Type**: Object Detection  
**Difficulty Level**: Easy  
**Target Datasets**: 66 object detection datasets from MBU metadata  
**Domain Coverage**: Radiology, Pathology, Surgery, Ophthalmology, Dermatology, Other-Medical

## What is Object Detection?

Object detection involves detecting and localizing objects in medical images using rectangular bounding boxes and assigning a class to each detected object. This differs from:
- **Classification**: Provides spatial localization instead of image-level labels
- **Segmentation**: Uses rectangular boxes instead of pixel-accurate masks
- **Landmarks**: Provides class-labeled regions instead of point coordinates

## Available Templates

### 1. Lesion Detection (`domain-agnostic_detection_object_easy_1.md`)
- **Purpose**: Detect and classify pathological findings and lesions
- **Question Pattern**: "What type of lesion is highlighted in the bounding box of this {modality} image?"
- **Target Datasets**: 53 lesion detection datasets
- **Examples**: Pulmonary nodules, melanoma, brain tumors, diabetic retinopathy findings
- **Domains**: Radiology, Dermatology, Ophthalmology, Pathology

### 2. Anatomy Detection (`domain-agnostic_detection_object_easy_2.md`)  
- **Purpose**: Detect and identify anatomical structures and organs
- **Question Pattern**: "What anatomical structure is highlighted in the bounding box of this {modality} image?"
- **Target Datasets**: 9 anatomy detection datasets
- **Examples**: Liver, heart, optic disc, blood cells, bones
- **Domains**: Radiology, Ophthalmology, Hematology

### 3. Device Detection (`domain-agnostic_detection_object_easy_3.md`)
- **Purpose**: Detect and identify medical devices and hardware
- **Question Pattern**: "What medical device is highlighted in the bounding box of this {modality} image?"
- **Target Datasets**: 4 device detection datasets  
- **Examples**: Pacemakers, endotracheal tubes, surgical instruments, implants
- **Domains**: Surgery, Critical Care, Radiology, Orthopedics

## Technical Framework

### Output Format
All templates generate standardized MCVQA question-answer pairs with:
- **Spatial Reference**: Bounding box coordinates with highlighting
- **Single Label Answers**: Device/lesion/anatomy class names
- **Detection Task Type**: Maps to "Detection" in datum schema
- **Easy Difficulty**: Accessible to basic models

### Spatial Reference System
Object detection templates use **bounding box highlighting**:
```json
"spatial_reference": {
  "reference_type": "bbox",
  "bbox": [x1, y1, x2, y2],
  "annotation_id": "detection_001",
  "highlighting_method": "outline",
  "highlight_color": "yellow",
  "highlight_opacity": 1.0
}
```

### Schema Compliance
- **Task**: "Detection" (datum schema)
- **Answer Type**: "single_label"
- **Provenance**: Links to original detection annotations
- **Coordinate Format**: Relative [0,1] coordinates for portability

## Dataset Statistics

**Total Compatible Datasets**: 66 object detection datasets

**By Subtype**:
- Lesion Detection: 53 datasets (80.3%)
- Anatomy Detection: 9 datasets (13.6%)
- Device Detection: 4 datasets (6.1%)

**By Domain**:
- Radiology: 32 datasets (48.5%)
- Pathology: 13 datasets (19.7%)
- Surgery: 8 datasets (12.1%)
- Other-Medical: 7 datasets (10.6%)
- Ophthalmology: 4 datasets (6.1%)
- Dermatology: 2 datasets (3.0%)

**Quality Assessment**:
- Mean Quality Score: 61.3/100
- High Quality (≥80): 4 datasets
- Medium Quality (60-79): 38 datasets
- Lower Quality (<60): 24 datasets

## Usage Guidelines

### Template Selection
1. **Lesion Detection**: Use for pathological findings, abnormalities, disease markers
2. **Anatomy Detection**: Use for organs, structures, anatomical landmarks
3. **Device Detection**: Use for medical equipment, implants, surgical tools

### Implementation Requirements
- **Bounding Box Data**: COCO-format or similar detection annotations required
- **Class Labels**: Medically accurate object classification schemes
- **Highlighting**: Visual indication of which detection is being questioned
- **Medical Terminology**: Clinically validated vocabulary for answers

### Best Practices
- **Clear Visualization**: Ensure bounding box highlighting is prominent and unambiguous
- **Medical Accuracy**: Validate object classifications with domain experts
- **Context Provision**: Include imaging modality for clinical context
- **Standardized Terminology**: Use established medical vocabularies (SNOMED CT, ICD-10)

## Clinical Applications

### Diagnostic Support
- **Lesion Screening**: Automated detection of pathological findings
- **Anatomical Assessment**: Structure identification and localization
- **Device Monitoring**: Safety verification and positioning assessment

### Educational Use
- **Medical Training**: Teaching object recognition across medical specialties
- **Benchmark Development**: Standardized evaluation of detection models
- **Quality Assurance**: Validation of automated detection systems

### Research Applications
- **Model Evaluation**: Cross-domain assessment of detection capabilities
- **Clinical Validation**: Testing detection accuracy in real clinical scenarios
- **Workflow Integration**: Automated detection in clinical decision support

## Quality Considerations

### Medical Accuracy
- Use clinically validated object classifications
- Ensure questions reflect real diagnostic workflows
- Validate examples with medical domain expertise

### Technical Quality
- Bounding boxes must accurately encompass objects
- Highlighting must clearly indicate target objects
- Coordinates must correspond to actual object locations

### Cross-Domain Applicability  
- Templates work across multiple medical specialties
- Avoid domain-specific terminology that limits use
- Scale appropriately across imaging modalities

## Examples by Domain

### Radiology
- **Chest X-ray**: Pulmonary nodules, pacemakers, heart detection
- **CT Scans**: Organ detection, tumor localization, anatomy identification
- **MRI**: Brain tumors, anatomical structures, implant detection

### Surgery
- **Surgical Video**: Instrument detection, anatomy identification
- **Fluoroscopy**: Device positioning, anatomical landmarks
- **OR Imaging**: Tool tracking, anatomy recognition

### Pathology
- **Microscopy**: Cell detection, tissue identification
- **Histopathology**: Tumor detection, cellular structures
- **Cytology**: Abnormal cell identification

### Ophthalmology
- **Fundus Photography**: Optic disc, diabetic retinopathy lesions
- **OCT**: Retinal structures, pathological findings
- **Slit Lamp**: Anterior segment anatomy

## Template Development History

- **Created**: Task 9 - Object Detection Templates
- **Pattern**: Follows established template structure from tasks 3,5,6,7
- **Analysis Base**: 66 datasets identified from MBU metadata analysis
- **Design Decision**: 3 separate templates for different object semantics
- **Schema**: Aligned with unified datum schema v1.0

## Future Enhancements

### Medium Difficulty (Planned)
- Multi-object counting questions
- Spatial relationship analysis
- Comparative object assessment

### Hard Difficulty (Planned)
- Detection quality assessment
- Complex spatial reasoning
- Multi-criteria evaluation

### Additional Subtypes (Future)
- Multi-object detection templates
- Object property assessment
- Detection validation templates

## Contributing

When creating new object detection templates or modifying existing ones:

1. **Follow 8-section structure**: Overview, Description, Pattern, Schema, Requirements, Rules, Examples, Notes
2. **Maintain medical accuracy**: Validate terminology and clinical relevance
3. **Ensure schema compliance**: Align with unified datum schema requirements
4. **Provide diverse examples**: Cover multiple domains and imaging modalities
5. **Document limitations**: Clearly state template constraints and dependencies

For questions about object detection template development or integration, refer to the Task 9 instructions document.
