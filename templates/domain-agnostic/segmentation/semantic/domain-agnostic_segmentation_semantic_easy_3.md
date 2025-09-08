# Semantic Segmentation Template 3: Regional Assessment

## Template Overview

**Template ID**: `domain-agnostic_segmentation_semantic_easy_3`  
**Task Type**: Semantic Segmentation  
**Difficulty**: Easy  
**Question Pattern**: Tissue type or regional characteristic identification in segmented areas  

## Template Description

This template converts semantic segmentation datasets into MCVQA format by asking questions about the type of tissue, pathology, or regional characteristic identified in the segmented area. It is designed for datasets where pixel-level annotations classify different tissue types, pathological regions, or anatomical characteristics.

## Question Generation Pattern

### Question Format
```
"What type of {assessment_category} is identified in the segmented region of this {modality} image?"
```

### Answer Format
- **Single classification**: The tissue type, pathology name, or regional characteristic (e.g., "healthy tissue", "tumor", "gray matter")

### Template Variables
- `{assessment_category}`: The type of assessment being made (e.g., "tissue", "pathology", "brain matter", "cardiac tissue")
- `{modality}`: The imaging modality (e.g., "CT", "MRI", "histopathology", "ultrasound")
- `{tissue_type}`: The specific classification result (derived from segmentation labels)

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Segmentation",
  "question": "What type of {assessment_category} is identified in the segmented region of this {modality} image?",
  "answer": "{tissue_type}",
  "answer_type": "single_label",
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Tissue type or pathology classification based on segmented region analysis",
  "spatial_reference": {
    "reference_type": "polygon",
    "polygon": "{tissue_region_polygon_coordinates}",
    "annotation_id": "{tissue_classification_annotation_id}",
    "highlighting_method": "fill",
    "highlight_color": "yellow",
    "highlight_opacity": 0.4
  },
  "provenance": {
    "original_label": "{segmentation_class_id}",
    "rule_id": "domain-agnostic_segmentation_semantic_easy_3",
    "annotation_id": "{region_assessment_id}",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Semantic segmentation (Vision → Segmentation → Semantic segmentation)
- **Tissue Classification**: Labels that classify tissue types, pathologies, or regional characteristics
- **Spatial Information**: Polygon coordinates for classified tissue regions
- **Medical Context**: Classifications relevant to medical diagnosis or research
- **Multi-Class Labels**: Multiple tissue/pathology types to distinguish between

## Spatial Reference Integration

This template generates **tissue classification questions** that reference specific segmented regions:

### Spatial Requirements
- **Required**: Polygon coordinates of the classified tissue region
- **Coordinate Format**: Relative [0,1] coordinates
- **Highlighting Method**: Fill (solid color highlighting)
- **Visual Properties**: Yellow fill with 40% opacity (recommended)

### Tissue Classification Focus
- Spatial reference shows the **specific tissue region being classified**
- Fill highlighting provides **clear region identification**
- Enables **detailed tissue characterization**
- Supports **pathology assessment workflows**

### Implementation Notes
- Extract coordinates from tissue classification masks
- Use "fill" highlighting for clear region visualization
- Link spatial_reference.annotation_id to tissue classification annotations
- Yellow color provides good contrast for tissue identification
- Moderate opacity (0.4) allows underlying tissue details to remain visible

## Template Usage Rules

1. **Category Specification**: Choose appropriate assessment category (tissue, pathology, etc.)
2. **Medical Terminology**: Use standard medical/scientific terminology for tissue types
3. **Modality Context**: Include imaging modality for clinical context
4. **Single Classification**: Each question focuses on one segmented region type
5. **Consistent Mapping**: Map segmentation class labels to medical terminology

## Examples

### Example 1: Brain Tissue Segmentation in MRI
**Original Dataset**: BraTS Brain Tumor Segmentation  
**Original Label**: Gray matter segmentation mask  
**Generated Q&A**:
- **Question**: "What type of brain tissue is identified in the segmented region of this MRI image?"
- **Answer**: "Gray matter"
- **Rationale**: "Gray matter region accurately segmented based on T1-weighted MRI characteristics"

### Example 2: Cardiac Tissue Segmentation in MRI
**Original Dataset**: ACDC Cardiac Segmentation  
**Original Label**: Myocardium segmentation mask  
**Generated Q&A**:
- **Question**: "What type of cardiac tissue is identified in the segmented region of this MRI image?"
- **Answer**: "Myocardium"
- **Rationale**: "Myocardial tissue segmented for cardiac function assessment"

### Example 3: Liver Pathology Segmentation in CT
**Original Dataset**: Liver Tumor Segmentation Challenge  
**Original Label**: Tumor tissue segmentation mask  
**Generated Q&A**:
- **Question**: "What type of pathology is identified in the segmented region of this CT image?"
- **Answer**: "Tumor"
- **Rationale**: "Hepatic tumor tissue identified and segmented for oncological assessment"

### Example 4: Breast Tissue Classification in Histopathology
**Original Dataset**: BreakHis Histopathology  
**Original Label**: Ductal carcinoma segmentation  
**Generated Q&A**:
- **Question**: "What type of tissue is identified in the segmented region of this histopathology image?"
- **Answer**: "Ductal carcinoma"
- **Rationale**: "Invasive ductal carcinoma tissue identified through histopathological analysis"

### Example 5: Retinal Layer Segmentation in OCT
**Original Dataset**: Duke OCT Retinal Layer Segmentation  
**Original Label**: Inner nuclear layer segmentation  
**Generated Q&A**:
- **Question**: "What type of retinal layer is identified in the segmented region of this OCT image?"
- **Answer**: "Inner nuclear layer"
- **Rationale**: "Inner nuclear layer of retina accurately segmented in optical coherence tomography"

## Implementation Notes

### Advantages
- **Tissue-Specific**: Tests knowledge of tissue types and pathological classifications
- **Medical Relevance**: Directly applicable to diagnostic pathology and radiology
- **Flexible Categories**: Can adapt to different medical domains and tissue types
- **Educational Value**: Teaches tissue recognition across imaging modalities

### Limitations
- **Domain Knowledge Required**: Needs understanding of medical tissue classifications
- **Single Region Focus**: Only handles one tissue type per question
- **No Spatial Context**: Does not consider relationships between different tissue types
- **Basic Classification**: Limited to simple tissue type identification

### Quality Considerations
- Ensure tissue type names are medically accurate and standardized
- Use appropriate assessment categories for the medical domain
- Verify that segmentation labels correspond to correct tissue classifications
- Confirm that imaging modality context matches clinical practice
- Validate that tissue types are clinically relevant and distinguishable
