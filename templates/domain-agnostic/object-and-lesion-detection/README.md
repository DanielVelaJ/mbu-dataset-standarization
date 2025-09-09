# Domain-Agnostic Object and Lesion Detection Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Sub-Category**: `Object and Lesion Detection`  
**Parent Category**: Vision  
**Repository Path**: `templates/domain-agnostic/object-and-lesion-detection/`

## 📁 Template Inventory

### **Current Status: ✅ BASIC COVERAGE (3 easy templates)**

| Subdirectory | Leaf Node | Template File | Purpose | Status |
|--------------|-----------|---------------|---------|---------|
| `lesion/` | Lesion detection with bounding boxes | `domain-agnostic_detection_object_easy_1.md` | Pathological finding classification | ✅ **Complete** |
| `anatomy/` | Anatomy detection with bounding boxes | `domain-agnostic_detection_object_easy_2.md` | Anatomical structure identification | ✅ **Complete** |
| `device/` | Device detection with bounding boxes | `domain-agnostic_detection_object_easy_3.md` | Medical device recognition | ✅ **Complete** |

### **Template Functionality Summary**:
- **All templates**: Use bounding box highlighting to focus on specific detected objects
- **Question Pattern**: "What type of {object_type} is highlighted in the bounding box?"
- **Answer Format**: Single label classification of the highlighted object
- **Clinical Context**: Real diagnostic and identification workflows

## 📋 How These Templates Work

This directory contains domain-agnostic templates for converting object and lesion detection datasets into MCVQA format. These templates work across all medical specialties for detecting and localizing objects using bounding boxes.

## What is Object and Lesion Detection?

**Definition**: Detect and localize objects in the image with rectangular bounding boxes and assign a class to each detected object.

**Key Characteristics**:
- **Input**: One 2D medical image
- **Output**: List of bounding boxes + object class per box
- **Task Focus**: Object localization and classification at bounding box level
- **vs Classification**: Object-level localization instead of image-level labeling
- **vs Segmentation**: Rectangular boxes instead of pixel-accurate masks

## Sub-Categories

This directory is organized by the three official taxonomy leaf nodes:

### 1. **Lesion Detection** (`lesion/`)
- **Purpose**: Detect and localize pathological findings/lesions
- **Examples**: CXR nodule detection, dermatology lesion detection, brain tumor detection
- **Dataset Count**: **53 datasets** in our metadata (largest subtype)

### 2. **Anatomy Detection** (`anatomy/`)
- **Purpose**: Detect and localize anatomical structures
- **Examples**: Fundus optic disc detection, organ detection in CT, bone detection in X-rays
- **Dataset Count**: **9 datasets** in our metadata

### 3. **Device Detection** (`device/`)
- **Purpose**: Detect and localize medical devices/hardware
- **Examples**: CXR pacemaker detection, ETT tube detection, surgical instrument detection
- **Dataset Count**: **4 datasets** in our metadata

## Template Collection Status

### ✅ **Current Templates (3 easy templates)**
- ✅ **Lesion Detection**: 1 template (domain-agnostic_detection_object_easy_1.md)
- ✅ **Anatomy Detection**: 1 template (domain-agnostic_detection_object_easy_2.md)
- ✅ **Device Detection**: 1 template (domain-agnostic_detection_object_easy_3.md)

### 📝 **Future Expansion**
- **Medium/Hard Templates**: Multi-object detection, spatial relationships, detection validation
- **Advanced Reasoning**: "How many objects are detected?", "Which detected object is closest to X?"

## Key Features

- **Bounding Box Integration**: Visual highlighting using rectangular regions
- **Multi-Object Support**: Can handle multiple objects of same/different classes
- **Clinical Context Aware**: Questions reflect real diagnostic workflows
- **Cross-Domain**: Work across radiology, pathology, surgery, dermatology, ophthalmology

## Dataset Requirements

Templates work with datasets that have:
- **Medical images** (any modality: CT, MRI, X-ray, microscopy, photography, etc.)
- **Bounding box annotations** (rectangular object localizations)
- **Class labels** for detected objects
- **COCO-format or similar** structured annotations

## Schema Integration

- **Task**: "Detection"
- **Answer Type**: "single_label", "number", "yes_no"
- **Spatial Reference**: Bounding box coordinates and highlighting specifications
- **Highlighting Method**: Outline for individual object identification

## Compatible Datasets

**Dataset Statistics**: 66 total object detection datasets
- **Domain Distribution**: Radiology (32), Pathology (13), Surgery (8), Other-Medical (7), Ophthalmology (4), Dermatology (2)
- **Quality Range**: Mean quality score 61.3, with 4 high-quality datasets (≥80)

**Example High-Quality Datasets**:
- **Lesion**: Dataset for Automating Dental Condition Detection (Quality: 85), LIDC-IDRI (Quality: 85)
- **Anatomy**: LeukemiaAttri (Quality: 75), Blood Cell Detection (Quality: 65)
- **Device**: 4D-OR (Quality: 72), HOSPI-Tools Dataset (Quality: 70)

## Implementation Notes

**Technical Approach**:
- Templates share identical technical structure (bbox + class) but differ in semantic contexts
- More practical than separate template categories for each object type
- Enables efficient template reuse across object detection domains

**Clinical Applications**:
- Disease diagnosis and pathology identification (lesions)
- Structure identification and anatomical assessment (anatomy)
- Procedure support and device monitoring (devices)

**Quality Considerations**:
- Use correct medical terminology for all object types
- Ensure questions reflect real clinical workflows
- Provide precise spatial localization with proper coordinate systems
