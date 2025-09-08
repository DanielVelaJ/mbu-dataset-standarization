# MBU Datum Schema & Spatial Reference Guide

## Table of Contents
1. [Overview](#overview)
2. [Datum Schema Structure](#datum-schema-structure)
3. [Spatial Reference System](#spatial-reference-system)
4. [Implementation Examples](#implementation-examples)
5. [Template Integration](#template-integration)
6. [Best Practices](#best-practices)
7. [FAQ](#faq)

## Overview

The MBU (Medical Benchmark Unified) datum schema is designed to convert medical datasets into a standardized MCVQA (Medical Computer Vision Question Answering) format. This schema supports:

- **Multiple question types**: Classification, segmentation, detection, landmarks, etc.
- **Spatial awareness**: Questions can reference specific regions in images
- **Cross-domain compatibility**: Works across radiology, pathology, dermatology, ophthalmology
- **Rich metadata**: Complete provenance tracking and quality information

### Key Innovation: Spatial Reference System

Our schema includes a sophisticated spatial reference system that enables questions like:
- "What anatomical structure is highlighted in the segmented region?"
- "What type of cell is shown in the highlighted instance?"
- "How many lesions are highlighted in this image?"

## Datum Schema Structure

### Complete Schema Overview

```json
{
  "header": {
    "image_id": "P_0000001.jpg",
    "image_name": "P_0000001.jpg", 
    "domain": "Radiology",
    "subdomain": "Chest imaging",
    "category": "pneumonia"
  },
  "dataset": {
    "name": "ChestX-ray14",
    "dataset_id": "nih-chest-xray",
    "tasks": ["Classification"],
    "split": "train",
    "institution": "NIH Clinical Center",
    "license": "CC0",
    "path": "chest_xray/images/00000001_000.png"
  },
  "quality": {
    "expert_involved": "yes",
    "qc_passed": "yes", 
    "notes": "Radiologist-reviewed annotations"
  },
  "imaging": {
    "modality": "CXR",
    "submodality": "PA",
    "frames": 1,
    "view": "PA",
    "body_part": "chest"
  },
  "geometry": {
    "bbox": [[0.1, 0.2, 0.9, 0.8]],
    "polygons": [[[0.1, 0.2], [0.9, 0.2], [0.9, 0.8], [0.1, 0.8]]],
    "image_size": [1024, 1024]
  },
  "questions-and-answers": [
    {
      "qa_id": "1",
      "task": "Classification",
      "question": "Is pneumonia present in this chest X-ray?",
      "answer": "Yes",
      "answer_type": "yes_no",
      "difficulty": "easy",
      "uncertainty": "certain",
      "answer_confidence": 0.95,
      "rationale": "Consolidation visible in right lower lobe",
      "spatial_reference": {
        "reference_type": "bbox",
        "bbox": [0.6, 0.5, 0.9, 0.8],
        "highlighting_method": "outline",
        "highlight_color": "red"
      },
      "provenance": {
        "original_label": "pneumonia_positive",
        "rule_id": "domain-agnostic_classification_binary_easy_1",
        "annotation_id": "finding_001",
        "created_by": "program"
      }
    }
  ],
  "version": "v1.0"
}
```

### Required Sections

#### 1. Header Section
Contains basic image identification and medical domain classification.

```python
class DatumHeader(BaseModel):
    image_id: str                    # Unique identifier
    image_name: str                  # Original filename
    domain: Literal[...]             # Medical domain (Radiology, Pathology, etc.)
    subdomain: Optional[str] = None  # Subspecialty (e.g., "Chest imaging")
    category: Optional[str] = None   # Primary label for classification
```

#### 2. Dataset Section
Metadata about the source dataset.

```python
class DatumDataset(BaseModel):
    name: str                        # Dataset name
    dataset_id: str                  # Unique dataset identifier
    tasks: List[Literal[...]]        # Supported tasks
    split: Literal[...]              # train/val/test/other
    institution: Optional[str]       # Source institution
    license: Optional[str]           # Usage license
    path: str                        # Relative path to image
```

#### 3. Quality Section
Quality control and validation information.

```python
class DatumQuality(BaseModel):
    expert_involved: Literal["yes", "no", "unknown"]
    qc_passed: Literal["yes", "no", "unknown"] 
    notes: Optional[str] = None
```

#### 4. Imaging Section
Technical imaging parameters.

```python
class DatumImaging(BaseModel):
    modality: Literal["CXR", "CT", "MRI", ...]  # Imaging modality
    submodality: Optional[str] = None           # Technical details
    frames: int = 1                             # Number of frames
    view: Optional[str] = None                  # Imaging view
    body_part: Optional[Literal[...]] = None    # Anatomical region
    eye_part: Optional[str] = None              # Ophthalmology specific
```

#### 5. Geometry Section
Spatial annotations (bounding boxes, polygons, etc.).

```python
class DatumGeometry(BaseModel):
    bbox: Optional[List[List[float]]] = None      # [[x1,y1,x2,y2], ...]
    polygons: Optional[List[List[List[float]]]] = None  # [[[x,y], ...], ...]
    image_size: Optional[List[int]] = None        # [width, height]
```

#### 6. Questions and Answers Section
Array of question-answer pairs with spatial references.

```python
class QuestionAnswer(BaseModel):
    qa_id: str                           # Unique question identifier
    task: Literal[...]                   # Task type
    question: str                        # Question text
    answer: Union[str, int, List[str]]   # Answer content
    answer_type: Literal[...]            # Answer format type
    spatial_reference: Optional[SpatialReference] = None  # NEW: Spatial link
    provenance: Optional[DatumProvenance] = None
```

## Spatial Reference System

### Core Concept

The `SpatialReference` class explicitly links questions to specific spatial regions in images, enabling precise spatial reasoning in MCVQA tasks.

### **Polygon vs Mask Relationship**

**Important**: In medical datasets, the same segmented region can be represented in two ways:
- **Mask files**: Binary/labeled images (PNG, TIFF) from original dataset
- **Polygon coordinates**: Vector representation extracted from mask boundaries

**Our Approach**:
1. **Original dataset**: Provides mask files (e.g., `liver_001.png`)
2. **Conversion process**: Extracts polygon coordinates from mask boundaries  
3. **MCVQA format**: Uses polygons for spatial_reference, keeps annotation_id for traceability
4. **annotation_id**: References the original annotation (not the mask file itself)

### **Why This Design?**
- **Polygons**: Compact, scalable, JSON-friendly for spatial questions
- **annotation_id**: Maintains traceability back to source dataset
- **Flexibility**: Supports both raster (masks) and vector (polygons) workflows

### SpatialReference Structure

```python
class SpatialReference(BaseModel):
    # Type of spatial reference
    reference_type: Literal["bbox", "polygon", "mask", "point", "multiple_regions"]
    
    # Single region coordinates (relative [0,1])
    bbox: Optional[List[float]] = None          # [x1, y1, x2, y2]
    polygon: Optional[List[List[float]]] = None # [[x, y], ...]
    point: Optional[List[float]] = None         # [x, y]
    
    # Multiple regions (for instance segmentation)
    multiple_bboxes: Optional[List[List[float]]] = None
    multiple_polygons: Optional[List[List[List[float]]]] = None
    
    # Annotation references
    annotation_id: Optional[str] = None         # Original annotation identifier  
    instance_ids: Optional[List[str]] = None    # Multiple instance IDs (instance segmentation)
    
    # Visual highlighting specification
    highlighting_method: Literal["overlay", "outline", "fill", "arrow", "none"] = "overlay"
    highlight_color: Optional[str] = None       # e.g., "red", "#FF0000"
    highlight_opacity: Optional[float] = None   # 0.0 to 1.0
```

### Highlighting Methods

#### 1. **Overlay** (`highlighting_method: "overlay"`)
- **Use**: Semi-transparent mask over region
- **Best for**: Semantic segmentation, large regions
- **Example**: Liver segmentation with 30% red overlay

#### 2. **Outline** (`highlighting_method: "outline"`)
- **Use**: Border highlighting around region boundary
- **Best for**: Object detection, instance boundaries
- **Example**: Cell nucleus outlined in yellow

#### 3. **Fill** (`highlighting_method: "fill"`)
- **Use**: Solid color fill of entire region
- **Best for**: Small regions, clear visibility
- **Example**: Multiple cells filled with blue

#### 4. **Arrow** (`highlighting_method: "arrow"`)
- **Use**: Pointing arrow to specific location
- **Best for**: Landmark detection, point annotations
- **Example**: Arrow pointing to fovea center

#### 5. **None** (`highlighting_method: "none"`)
- **Use**: Question references region without visual highlighting
- **Best for**: When original annotations provide sufficient context

## Implementation Examples

### 1. Semantic Segmentation

**Scenario**: Liver segmentation in abdominal CT

```json
{
  "qa_id": "1",
  "task": "Segmentation",
  "question": "What anatomical structure is highlighted in the segmented region of this CT image?",
  "answer": "Liver",
  "answer_type": "single_label",
  "spatial_reference": {
    "reference_type": "polygon",
    "polygon": [
      [0.2, 0.3], [0.8, 0.3], [0.8, 0.7], [0.6, 0.9], [0.2, 0.7]
    ],
    "annotation_id": "liver_segmentation_001",
    "highlighting_method": "overlay",
    "highlight_color": "red",
    "highlight_opacity": 0.3
  },
  "provenance": {
    "rule_id": "domain-agnostic_segmentation_semantic_easy_1",
    "annotation_id": "liver_mask_001"
  }
}
```

### 2. Instance Segmentation

**Scenario**: Multiple cell nuclei in histopathology

**Single Instance Question:**
```json
{
  "qa_id": "2",
  "task": "Segmentation",
  "question": "What type of cell is shown in the highlighted segmented instance?",
  "answer": "Epithelial cell",
  "answer_type": "single_label",
  "spatial_reference": {
    "reference_type": "polygon",
    "polygon": [[0.3, 0.4], [0.5, 0.4], [0.5, 0.6], [0.3, 0.6]],
    "annotation_id": "cell_instance_07",
    "highlighting_method": "outline",
    "highlight_color": "yellow",
    "highlight_opacity": 1.0
  }
}
```

**Multiple Instance Question:**
```json
{
  "qa_id": "3", 
  "task": "Segmentation",
  "question": "How many cell nuclei are highlighted in this histopathology image?",
  "answer": "5",
  "answer_type": "number",
  "spatial_reference": {
    "reference_type": "multiple_regions",
    "multiple_polygons": [
      [[0.1, 0.1], [0.2, 0.1], [0.2, 0.2], [0.1, 0.2]],
      [[0.3, 0.3], [0.4, 0.3], [0.4, 0.4], [0.3, 0.4]],
      [[0.5, 0.5], [0.6, 0.5], [0.6, 0.6], [0.5, 0.6]],
      [[0.7, 0.1], [0.8, 0.1], [0.8, 0.2], [0.7, 0.2]],
      [[0.1, 0.7], [0.2, 0.7], [0.2, 0.8], [0.1, 0.8]]
    ],
    "instance_ids": ["nucleus_01", "nucleus_02", "nucleus_03", "nucleus_04", "nucleus_05"],
    "highlighting_method": "fill",
    "highlight_color": "blue",
    "highlight_opacity": 0.4
  }
}
```

### 3. Object Detection with Bounding Boxes

**Scenario**: Medical device detection in chest X-ray

```json
{
  "qa_id": "4",
  "task": "Detection", 
  "question": "What medical device is shown in the highlighted bounding box?",
  "answer": "Pacemaker",
  "answer_type": "single_label",
  "spatial_reference": {
    "reference_type": "bbox",
    "bbox": [0.2, 0.3, 0.6, 0.7],
    "annotation_id": "pacemaker_detection_001",
    "highlighting_method": "outline",
    "highlight_color": "green",
    "highlight_opacity": 1.0
  },
  "provenance": {
    "rule_id": "domain-agnostic_detection_bbox_easy_1",
    "annotation_id": "pacemaker_bbox_001"
  }
}
```

### 4. Landmark Detection

**Scenario**: Anatomical landmark in fundus image

```json
{
  "qa_id": "5",
  "task": "Landmarks",
  "question": "What anatomical landmark is highlighted in this fundus image?",
  "answer": "Fovea center", 
  "answer_type": "single_label",
  "spatial_reference": {
    "reference_type": "point",
    "point": [0.5, 0.6],
    "annotation_id": "fovea_landmark_001",
    "highlighting_method": "arrow",
    "highlight_color": "red"
  }
}
```

### 5. Multiple Questions per Image

**Scenario**: Same CT image with multiple analysis types

```json
{
  "header": {"image_id": "ct_001", "domain": "Radiology"},
  "questions-and-answers": [
    {
      "qa_id": "1",
      "task": "Classification",
      "question": "Is a liver tumor present in this CT image?",
      "answer": "Yes",
      "answer_type": "yes_no",
      "spatial_reference": {
        "reference_type": "bbox", 
        "bbox": [0.4, 0.3, 0.7, 0.6],
        "highlighting_method": "outline",
        "highlight_color": "red"
      }
    },
    {
      "qa_id": "2",
      "task": "Segmentation",
      "question": "What anatomical structure is highlighted in the segmented region?",
      "answer": "Liver",
      "answer_type": "single_label", 
      "spatial_reference": {
        "reference_type": "polygon",
        "polygon": [[0.2, 0.2], [0.8, 0.2], [0.8, 0.8], [0.2, 0.8]],
        "highlighting_method": "overlay",
        "highlight_color": "blue",
        "highlight_opacity": 0.2
      }
    },
    {
      "qa_id": "3",
      "task": "Segmentation",
      "question": "What type of pathology is identified in the segmented region?",
      "answer": "Tumor",
      "answer_type": "single_label",
      "spatial_reference": {
        "reference_type": "polygon",
        "polygon": [[0.45, 0.35], [0.65, 0.35], [0.65, 0.55], [0.45, 0.55]],
        "highlighting_method": "fill",
        "highlight_color": "yellow",
        "highlight_opacity": 0.5
      }
    }
  ]
}
```

## Template Integration

### Template Design Guidelines

#### 1. **Specify Spatial Requirements**
Templates should clearly indicate when spatial references are needed:

```markdown
## Spatial Reference Requirements

This template generates questions that reference specific regions in the image:
- **Required**: `spatial_reference` with polygon coordinates
- **Highlighting**: Overlay method recommended
- **Coordinates**: Use relative [0,1] format
```

#### 2. **Include Spatial Examples**
All spatial templates should include complete `spatial_reference` examples:

```json
{
  "spatial_reference": {
    "reference_type": "polygon",
    "polygon": "{coordinates_from_segmentation_mask}",
    "annotation_id": "{original_annotation_id}",
    "highlighting_method": "overlay",
    "highlight_color": "red",
    "highlight_opacity": 0.3
  }
}
```

#### 3. **Support Multiple Annotation Types**
Templates should specify which annotation types they support:

- **Semantic Segmentation**: Single polygons, overlay highlighting
- **Instance Segmentation**: Multiple polygons, outline/fill highlighting
- **Object Detection**: Bounding boxes, outline highlighting
- **Landmark Detection**: Points, arrow highlighting

### Updated Template Structure

```markdown
# Template Title

## Spatial Reference Integration

### Supported Annotation Types
- Semantic segmentation masks
- Instance segmentation masks  
- Bounding box annotations
- Point/landmark annotations

### Highlighting Specifications
- **Default Method**: overlay
- **Recommended Colors**: red, blue, yellow
- **Opacity Range**: 0.2-0.5 for overlays, 1.0 for outlines

### Implementation Example
[Include complete JSON with spatial_reference]
```

## Best Practices

### 1. **Coordinate Systems**
- **Always use relative coordinates** [0,1] for portability
- **Include image_size** in geometry section when available
- **Validate coordinate ranges** (0 ≤ x,y ≤ 1)

### 2. **Spatial Reference Usage**
- **Required for region-specific questions** ("highlighted region", "segmented area")
- **Optional for global questions** ("Is pneumonia present?")
- **Use appropriate highlighting methods** for different annotation types

### 3. **Multiple Questions Strategy**
- **Different spatial_reference per question** even for same region
- **Vary highlighting colors** to distinguish between questions
- **Use descriptive annotation_id values** for traceability

### 4. **Template Compatibility**
- **Check annotation type compatibility** before applying templates
- **Graceful degradation** when spatial references unavailable
- **Clear error messages** for unsupported spatial types

### 5. **Quality Assurance**
- **Validate spatial coordinates** against image boundaries
- **Verify annotation_id references** exist in original annotations
- **Test highlighting visualization** with sample images

## FAQ

### Q: When should I use spatial references?
**A:** Use spatial references whenever your question refers to a specific region ("highlighted", "segmented", "outlined", "shown in the box"). Don't use for global image questions.

### Q: Can I have multiple questions with different spatial references for the same image?
**A:** Yes! This is encouraged. Use different highlighting colors and methods to distinguish between questions.

### Q: What coordinate system should I use?
**A:** Always use relative coordinates [0,1]. This ensures portability across different image sizes.

### Q: How do I handle instance segmentation with many instances?
**A:** Use `reference_type: "multiple_regions"` with `multiple_polygons` and `instance_ids` arrays.

### Q: What if my dataset doesn't have polygon coordinates, only class labels?
**A:** For semantic segmentation without coordinates, use `highlighting_method: "none"` and reference the region conceptually in the question.

### Q: Can I reference the same spatial region from multiple templates?
**A:** Yes, but use different `qa_id` values and potentially different highlighting to distinguish the questions.

### Q: How do I validate that my spatial references are correct?
**A:** Implement coordinate validation (0 ≤ x,y ≤ 1) and verify that `annotation_id` references exist in your original dataset annotations.

---

## Summary

The MBU datum schema with spatial reference system provides:

- ✅ **Complete spatial awareness** for region-specific questions
- ✅ **Cross-modal compatibility** (segmentation, detection, landmarks)
- ✅ **Rich metadata** with full provenance tracking
- ✅ **Multiple question support** per image
- ✅ **Flexible highlighting** for different visualization needs
- ✅ **Standard coordinate system** for portability

This schema enables sophisticated MCVQA tasks that closely mirror real medical diagnostic workflows, where spatial reasoning and region identification are crucial for accurate assessment.
