# Domain-Agnostic Semantic Segmentation Templates

This directory contains templates for converting semantic segmentation datasets into MCVQA (Medical Computer Vision Question Answering) format. These templates work across all medical domains and focus on pixel-level anatomical structure and tissue type identification.

## What is Semantic Segmentation?

**Semantic segmentation** assigns a class to each pixel in medical images, with instances of the same class not separated. Unlike image-level classification that labels entire images, semantic segmentation provides precise pixel-level delineation of anatomical structures, tissues, and pathologies.

**Key Characteristics:**
- **Input**: Medical image (any modality)
- **Output**: Pixel-wise mask or multi-class encoding
- **Focus**: Region identification and boundary delineation
- **Clinical Application**: Anatomical structure outlining, tissue classification, pathology localization

## Template Collection Overview

### Easy Difficulty Templates (3 total)

#### 1. **Region Identification** (`domain-agnostic_segmentation_semantic_easy_1.md`)
- **Pattern**: "What anatomical structure is highlighted in the segmented region of this {modality} image?"
- **Purpose**: Basic anatomical structure identification
- **Answer Type**: Single label (structure name)
- **Spatial Reference**: Polygon overlay with red highlighting
- **Use Cases**: Organ segmentation, anatomical landmark identification

#### 2. **Segmentation Verification** (`domain-agnostic_segmentation_semantic_easy_2.md`)
- **Pattern**: "Is the {structure} correctly segmented in this {modality} image?"
- **Purpose**: Quality assessment of segmentation accuracy
- **Answer Type**: Yes/No verification
- **Spatial Reference**: Polygon outline with blue highlighting
- **Use Cases**: Segmentation validation, quality control

#### 3. **Regional Assessment** (`domain-agnostic_segmentation_semantic_easy_3.md`)
- **Pattern**: "What type of {assessment_category} is identified in the segmented region of this {modality} image?"
- **Purpose**: Tissue type and pathology classification
- **Answer Type**: Single label (tissue/pathology type)
- **Spatial Reference**: Polygon fill with yellow highlighting
- **Use Cases**: Tissue characterization, pathology identification

## Domain Applications

### Radiology
- **CT**: Organ segmentation (liver, kidneys, lungs)
- **MRI**: Brain tissue classification, cardiac segmentation
- **X-ray**: Anatomical structure identification

### Pathology
- **Histopathology**: Tissue type classification, tumor segmentation
- **Cytology**: Cell component identification

### Ophthalmology
- **Fundus**: Optic disc, vessel segmentation
- **OCT**: Retinal layer identification

### Dermatology
- **Dermoscopy**: Lesion boundary segmentation
- **Clinical Photography**: Skin region classification

### Cardiology
- **Cardiac MRI**: Chamber segmentation, myocardium identification
- **Echocardiography**: Cardiac structure delineation

## Compatible Dataset Types

These templates work with semantic segmentation datasets that have:

### Required Components
- ✅ **Medical images** (any modality: CT, MRI, X-ray, microscopy, etc.)
- ✅ **Pixel-level annotations** (masks, segmentation maps)
- ✅ **Class labels** for segmented regions
- ✅ **Anatomical/pathological targets** with clear definitions

### Dataset Examples
- **Medical Segmentation Decathlon**: Multi-organ segmentation
- **BraTS**: Brain tumor segmentation
- **ACDC**: Cardiac segmentation
- **DRIVE**: Retinal vessel segmentation
- **ISIC**: Skin lesion segmentation
- **BreakHis**: Histopathology tissue segmentation

## Schema Integration

### Answer Types Used
- **single_label**: For structure identification and tissue classification
- **yes_no**: For segmentation verification questions

### Spatial Reference System
All templates include **spatial_reference** fields that link questions to specific segmented regions:

#### Template 1: Region Identification
- **Highlighting**: `overlay` method with red color and 30% opacity
- **Purpose**: Highlight the anatomical structure being identified
- **Coordinate Source**: Original segmentation mask polygons

#### Template 2: Segmentation Verification  
- **Highlighting**: `outline` method with blue color and full opacity
- **Purpose**: Emphasize segmentation boundaries for quality assessment
- **Coordinate Source**: Segmentation mask being validated

#### Template 3: Regional Assessment
- **Highlighting**: `fill` method with yellow color and 40% opacity
- **Purpose**: Clearly identify tissue region being classified
- **Coordinate Source**: Tissue classification mask coordinates

### Spatial Reference Benefits
- **Explicit region linking**: Questions clearly reference specific image regions
- **Visual highlighting**: Different methods for different question types
- **Coordinate traceability**: Links back to original annotations
- **Cross-modal compatibility**: Works with any segmentation format

### Segmentation-Specific Fields
```json
{
  "task": "Segmentation",
  "spatial_reference": {
    "reference_type": "polygon",
    "polygon": [[x, y], ...],
    "annotation_id": "segmentation_mask_001",
    "highlighting_method": "overlay",
    "highlight_color": "red",
    "highlight_opacity": 0.3
  },
  "geometry": {
    "polygons": [[[x, y], ...]],
    "image_size": [W, H]
  },
  "provenance": {
    "annotation_id": "{original_annotation_id}"
  }
}
```

## Template Selection Guide

### Choose Template 1 (Region Identification) when:
- Dataset has clear anatomical structure labels
- Goal is basic anatomical recognition
- Single structure per segmentation mask

### Choose Template 2 (Segmentation Verification) when:
- Dataset includes quality validation information
- Expert-reviewed segmentations available
- Focus on segmentation accuracy assessment

### Choose Template 3 (Regional Assessment) when:
- Dataset classifies tissue types or pathologies
- Multiple tissue/pathology categories available
- Goal is tissue characterization

## Implementation Guidelines

### Medical Terminology
- Use standard anatomical nomenclature
- Employ appropriate tissue classification terms
- Maintain consistency with clinical practice

### Quality Considerations
- Verify segmentation mask accuracy
- Ensure anatomical structure names are medically correct
- Validate tissue type classifications against medical standards
- Confirm imaging modality context is clinically appropriate

### Cross-Domain Compatibility
- Templates work across medical specialties
- Modality-agnostic question patterns
- Adaptable to different anatomical systems

## Evaluation Considerations

### Metrics for Semantic Segmentation MCVQA
- **Anatomical Accuracy**: Correct structure identification
- **Tissue Classification**: Accurate tissue type recognition
- **Segmentation Quality**: Assessment of boundary accuracy
- **Medical Relevance**: Clinical applicability of questions

### Special Considerations
- Pixel-level precision vs. image-level understanding
- Spatial reasoning about anatomical regions
- Integration of segmentation masks with question answering
- Medical domain expertise requirements

## Future Expansions

### Potential Additional Templates
- **Multi-Structure Recognition**: Questions about multiple anatomical structures
- **Spatial Relationships**: Questions about structure positions and relationships
- **Quantitative Assessment**: Questions about area, volume, or size measurements
- **Comparative Analysis**: Questions comparing segmentation quality or characteristics

### Difficulty Progressions
- **Medium Difficulty**: Multi-structure questions, spatial relationships
- **Hard Difficulty**: Complex anatomical reasoning, quantitative assessments

## Usage Notes

### Template Compatibility
- All templates follow the standardized 8-section structure
- Schema-compliant with unified datum schema v1.0
- Cross-compatible with domain-agnostic approach

### Implementation Support
- Clear documentation for each template
- Comprehensive examples across medical domains
- Detailed usage rules and quality considerations
- Medical accuracy validation guidelines

---

*These templates enable systematic evaluation of semantic segmentation capabilities in medical AI systems, providing comprehensive assessment across anatomical recognition, tissue classification, and segmentation quality domains.*
