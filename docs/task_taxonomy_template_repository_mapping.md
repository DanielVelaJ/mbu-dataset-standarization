# Repository Taxonomy Structure and Template Organization Guide

This document specifies the exact taxonomy structure used in this repository for organizing domain-agnostic medical vision templates. Our structure aligns directly with the **official Medical Vision and Vision–Language Taxonomy** while optimizing for practical template organization.

## 🎯 Taxonomy Alignment Philosophy

Our template organization follows the **official MBU Medical Vision Taxonomy** structure but adapts it for template development efficiency:

- **Exact naming**: Category and subcategory names match the official taxonomy precisely
- **Practical grouping**: Leaf nodes are organized for template development workflow
- **Consistent structure**: All templates follow standardized 8-section format
- **Schema compliance**: Perfect alignment with unified datum schema v1.0

---

## 📁 Template Directory Structure

```
templates/domain-agnostic/
├── classification/                           # "Image-Level Classification" Sub-Category
│   ├── binary/                              # "Binary classification" Leaf Node
│   ├── multiclass/                          # "Multiclass classification" Leaf Node
│   ├── multilabel/                          # "Multilabel classification" Leaf Node
│   └── ordinal/                             # "Ordinal grading" Leaf Node
├── object-and-lesion-detection/             # "Object and Lesion Detection" Sub-Category
│   ├── lesion/                              # "Lesion detection with bounding boxes" Leaf Node
│   ├── anatomy/                             # "Anatomy detection with bounding boxes" Leaf Node
│   └── device/                              # "Device detection with bounding boxes" Leaf Node
├── segmentation/                            # "Segmentation" Sub-Category
│   ├── semantic/                            # "Semantic segmentation" Leaf Node
│   └── instance/                            # "Instance segmentation" Leaf Node
├── anatomical-landmarks-keypoints/         # "Anatomical Landmarks and Keypoints" Sub-Category
│   ├── single/                              # "Single landmark detection" Leaf Node
│   └── multiple/                            # "Multiple landmark detection" Leaf Node
├── counting/                                # "Counting" Sub-Category
│   ├── direct/                              # "Direct count labels" Leaf Node
│   └── density/                             # "Density or point map counting" Leaf Node
└── vision-language/                         # "Vision–Language" Parent Group
    ├── describe/                            # "Describe" Sub-Category
    │   ├── short/                           # "Short medical caption generation" Leaf Node
    │   └── long/                            # "Long clinical report generation" Leaf Node
    ├── ask-and-answer/                      # "Ask and Answer" Sub-Category
    │   ├── open-ended/                      # "Open ended question answering" Leaf Node
    │   ├── multiple-choice/                 # "Multiple choice question answering" Leaf Node
    │   └── visual-reasoning/                # "Visual reasoning question answering" Leaf Node
    ├── ground-and-locate/                   # "Ground and Locate" Sub-Category
    │   ├── bbox/                            # "Referring expression to bounding box" Leaf Node
    │   ├── mask/                            # "Referring expression to segmentation mask" Leaf Node
    │   └── multi-phrase/                    # "Multi phrase grounding" Leaf Node
    └── align-and-retrieve/                  # "Align and Retrieve" Sub-Category
        ├── image-to-text/                   # "Image to text retrieval" Leaf Node
        ├── text-to-image/                   # "Text to image retrieval" Leaf Node
        └── pair-matching/                   # "Image and text pair matching" Leaf Node
```

---

## 🏗️ Taxonomy Mapping

### Vision Parent Group

| **Sub-Category** | **Leaf Nodes** | **Template Folder** | **Status** |
|------------------|-----------------|---------------------|------------|
| **Image-Level Classification** | Binary classification | `classification/binary/` | ✅ **9 templates** |
| | Multiclass classification | `classification/multiclass/` | ✅ **3 templates** |
| | Multilabel classification | `classification/multilabel/` | ✅ **3 templates** |
| | Ordinal grading | `classification/ordinal/` | ❌ **Missing** |
| **Object and Lesion Detection** | Lesion detection with bounding boxes | `object-and-lesion-detection/lesion/` | ✅ **1 template** |
| | Anatomy detection with bounding boxes | `object-and-lesion-detection/anatomy/` | ✅ **1 template** |
| | Device detection with bounding boxes | `object-and-lesion-detection/device/` | ✅ **1 template** |
| **Segmentation** | Semantic segmentation | `segmentation/semantic/` | ✅ **3 templates** |
| | Instance segmentation | `segmentation/instance/` | ✅ **3 templates** |
| **Anatomical Landmarks and Keypoints** | Single landmark detection | `anatomical-landmarks-keypoints/single/` | ❌ **Missing** |
| | Multiple landmark detection | `anatomical-landmarks-keypoints/multiple/` | ❌ **Missing** |
| **Counting** | Direct count labels | `counting/direct/` | ❌ **Missing** |
| | Density or point map counting | `counting/density/` | ❌ **Missing** |

### Vision–Language Parent Group

| **Sub-Category** | **Leaf Nodes** | **Template Folder** | **Status** |
|------------------|-----------------|---------------------|------------|
| **Describe** | Short medical caption generation | `vision-language/describe/short/` | ❌ **Missing** |
| | Long clinical report generation | `vision-language/describe/long/` | ❌ **Missing** |
| **Ask and Answer** | Open ended question answering | `vision-language/ask-and-answer/open-ended/` | ❌ **Missing** |
| | Multiple choice question answering | `vision-language/ask-and-answer/multiple-choice/` | ❌ **Missing** |
| | Visual reasoning question answering | `vision-language/ask-and-answer/visual-reasoning/` | ❌ **Missing** |
| **Ground and Locate** | Referring expression to bounding box | `vision-language/ground-and-locate/bbox/` | ❌ **Missing** |
| | Referring expression to segmentation mask | `vision-language/ground-and-locate/mask/` | ❌ **Missing** |
| | Multi phrase grounding | `vision-language/ground-and-locate/multi-phrase/` | ❌ **Missing** |
| **Align and Retrieve** | Image to text retrieval | `vision-language/align-and-retrieve/image-to-text/` | ❌ **Missing** |
| | Text to image retrieval | `vision-language/align-and-retrieve/text-to-image/` | ❌ **Missing** |
| | Image and text pair matching | `vision-language/align-and-retrieve/pair-matching/` | ❌ **Missing** |

---

## 📋 Template Naming Convention

All templates follow the established naming pattern:

```
{domain}_{task}_{subtype}_{difficulty}_{number}.md
```

### Examples:
- **Vision Tasks**: 
  - `domain-agnostic_classification_binary_easy_1.md`
  - `domain-agnostic_object-and-lesion-detection_lesion_easy_1.md`
  - `domain-agnostic_anatomical-landmarks-keypoints_single_easy_1.md`

- **Vision-Language Tasks**:
  - `domain-agnostic_vision-language_describe_short_easy_1.md`
  - `domain-agnostic_vision-language_ask-and-answer_open-ended_easy_1.md`

### Naming Rules:
1. **Domain**: Always `domain-agnostic` for universal templates
2. **Task**: Matches exact sub-category name (with hyphens for multi-word)
3. **Subtype**: Matches exact leaf node name (shortened for readability)
4. **Difficulty**: `easy`, `medium`, or `hard`
5. **Number**: Sequential numbering within same category/difficulty

---

## 🎯 Coverage Analysis

### ✅ **Complete Coverage (20 templates)**
- **Binary Classification**: 9 templates (easy → hard)
- **Multiclass Classification**: 3 templates (easy)
- **Multilabel Classification**: 3 templates (easy)
- **Object and Lesion Detection**: 3 templates (easy) - 1 per leaf node
- **Semantic Segmentation**: 3 templates (easy)
- **Instance Segmentation**: 3 templates (easy)

### 🔄 **Priority Missing Categories**
1. **Ordinal Grading** (Classification) - 4 available datasets
2. **Vision-Language Describe** - 5+ available datasets
3. **Anatomical Landmarks and Keypoints** - 4 available datasets

### 📝 **Future Expansion Categories**
4. **Vision-Language Ask and Answer** - 3+ available datasets
5. **Vision-Language Ground and Locate** - 1+ available dataset
6. **Vision-Language Align and Retrieve** - 1+ available dataset
7. **Counting** - 0 datasets found (lowest priority)

---

## 🔗 Schema Integration

### Datum Schema Task Types
Templates map to these `task` field values in the unified datum schema:

| **Template Category** | **Schema Task Value** | **Answer Types** |
|----------------------|----------------------|------------------|
| Classification | `"Classification"` | `"yes_no"`, `"single_label"`, `"multi_label"` |
| Object and Lesion Detection | `"Detection"` | `"single_label"`, `"bbox"`, `"number"` |
| Segmentation | `"Segmentation"` | `"single_label"`, `"yes_no"` |
| Anatomical Landmarks and Keypoints | `"Landmarks"` | Coordinates, list of coordinates |
| Counting | `"Counting"` | `"number"`, coordinates |
| Vision-Language Describe | `"Describe"` | `"span"` (free text) |
| Vision-Language Ask and Answer | `"Ask&Answer"` | `"span"`, `"single_label"` |
| Vision-Language Ground and Locate | `"Grounding"` | `"bbox"`, masks |
| Vision-Language Align and Retrieve | `"Retrieval"` | Rankings, matches |

### Special Schema Considerations:
- **Ordinal Grading**: Uses `"single_label"` with ordered options
- **Vision-Language**: May require new task types for complex interactions
- **Spatial References**: Leverage enhanced spatial reference system for highlighting

---

## 📊 Dataset Compatibility Matrix

### High Compatibility (4+ datasets available):
- ✅ **Ordinal Grading**: EyePACS (diabetic retinopathy), Fundus-MMBench
- ✅ **Vision-Language Describe**: MIMIC chest X-ray reports, brain-tumor-captions
- ✅ **Anatomical Landmarks**: Pupil position, surgical tracking, cephalometric

### Medium Compatibility (1-3 datasets available):
- **Vision-Language Ask & Answer**: Combined_MRI_ChestXray_QA, Fundus-MMBench
- **Vision-Language Ground & Locate**: retinal_oct_analysis2
- **Vision-Language Align & Retrieve**: retinal_oct_analysis2

### Low Compatibility (0 datasets found):
- **Counting**: No direct count datasets identified in metadata

---

## 🚀 Implementation Roadmap

### Phase 1: High-Priority Missing Templates
1. **Task 10**: Create ordinal grading, vision-language describe, and landmark detection templates
2. **Folder Structure**: ✅ **Complete** - All directories created
3. **Template Development**: Focus on easy difficulty templates first

### Phase 2: Vision-Language Expansion
4. **Ask and Answer**: Create open-ended, multiple-choice, and visual reasoning templates
5. **Ground and Locate**: Create bbox, mask, and multi-phrase grounding templates
6. **Align and Retrieve**: Create image-to-text, text-to-image, and pair matching templates

### Phase 3: Advanced Templates
7. **Medium/Hard Difficulty**: Expand existing categories with more complex templates
8. **Counting Templates**: Add when relevant datasets become available
9. **Domain-Specific**: Consider domain-specific extensions for major medical specialties

---

## ✅ Quality Assurance

### Template Standards:
- **Medical Accuracy**: All templates use correct medical terminology
- **Schema Compliance**: Perfect alignment with unified datum schema v1.0
- **Clinical Relevance**: Questions reflect real diagnostic workflows
- **Cross-Domain Applicability**: Work across medical specialties
- **8-Section Structure**: Standardized documentation format

### Folder Organization Standards:
- **Exact Taxonomy Names**: Match official medical vision taxonomy precisely
- **Consistent Hierarchy**: Clear parent-group → sub-category → leaf-node structure
- **Logical Grouping**: Related leaf nodes grouped under appropriate sub-categories
- **Scalable Structure**: Easy to add new templates and categories

### Documentation Standards:
- **Complete Mapping**: Every official taxonomy node mapped to folder structure
- **Status Tracking**: Clear indication of completed vs missing templates
- **Priority Ranking**: Based on dataset availability and clinical importance
- **Implementation Guidance**: Clear next steps and development roadmap

---

## 📚 References

1. **Official Source**: `context/about_dataset_metadata/mbu_medical_vision_taxonomy_table.md`
2. **Datum Schema**: `instructions/datum_schema.md` and `src/mbu_dataset_standardization/datum.py`
3. **Template Standards**: Established in `instructions/task_2_binary_classification_template.md`
4. **Dataset Metadata**: `data/dataset_metadata/datasets_metadata.csv`

---

*This taxonomy structure ensures our template collection comprehensively covers the medical vision domain while maintaining practical organization for development and deployment.*
