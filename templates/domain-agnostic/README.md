# Domain-Agnostic Medical Vision Templates

## 🎯 Overview

This directory contains **domain-agnostic templates** that work across all medical specialties for converting medical vision datasets into MCVQA format. Our organization follows the **official Medical Vision and Vision–Language Taxonomy** precisely.

## 📁 Directory Structure & Coverage

### ✅ **Complete Coverage** (20 templates)

| Category | Sub-Category | Leaf Nodes | Templates | Status |
|----------|--------------|------------|-----------|---------|
| **Classification** | Image-Level Classification | Binary, Multiclass, Multilabel | 15 templates | ✅ **Complete** |
| **Object Detection** | Object and Lesion Detection | Lesion, Anatomy, Device | 3 templates | ✅ **Basic Coverage** |
| **Segmentation** | Segmentation | Semantic, Instance | 6 templates | ✅ **Basic Coverage** |

### 📝 **High Priority Missing** (Task 10)

| Category | Sub-Category | Leaf Nodes | Available Datasets | Priority |
|----------|--------------|------------|-------------------|----------|
| **Classification** | Image-Level Classification | Ordinal grading | 4 datasets | 🔥 **Highest** |
| **Vision-Language** | Describe | Short/Long caption generation | 5+ datasets | 🔥 **Highest** |
| **Landmarks** | Anatomical Landmarks and Keypoints | Single/Multiple landmark detection | 4 datasets | 🔥 **High** |

### 🚀 **Future Expansion**

| Category | Sub-Category | Available Datasets | Priority |
|----------|--------------|-------------------|----------|
| **Vision-Language** | Ask and Answer | 3+ datasets | 📈 **High** |
| **Vision-Language** | Ground and Locate | 1+ dataset | 📈 **Medium** |
| **Vision-Language** | Align and Retrieve | 1+ dataset | 📈 **Medium** |
| **Counting** | Counting | 0 datasets | 📉 **Low** |

## 🏗️ Taxonomy Alignment

Our structure **perfectly aligns** with the official Medical Vision and Vision–Language Taxonomy:

```
📂 templates/domain-agnostic/
├── 📁 classification/
│   ├── 📁 binary/ (9 templates) ✅
│   ├── 📁 multiclass/ (3 templates) ✅
│   ├── 📁 multilabel/ (3 templates) ✅
│   └── 📁 ordinal/ ❌ Missing
├── 📁 object-and-lesion-detection/
│   ├── 📁 lesion/ (1 template) ✅
│   ├── 📁 anatomy/ (1 template) ✅
│   └── 📁 device/ (1 template) ✅
├── 📁 segmentation/
│   ├── 📁 semantic/ (3 templates) ✅
│   └── 📁 instance/ (3 templates) ✅
├── 📁 anatomical-landmarks-keypoints/
│   ├── 📁 single/ ❌ Missing
│   └── 📁 multiple/ ❌ Missing
├── 📁 counting/
│   ├── 📁 direct/ ❌ Missing (no datasets)
│   └── 📁 density/ ❌ Missing (no datasets)
└── 📁 vision-language/
    ├── 📁 describe/
    │   ├── 📁 short/ ❌ Missing
    │   └── 📁 long/ ❌ Missing
    ├── 📁 ask-and-answer/
    │   ├── 📁 open-ended/ ❌ Missing
    │   ├── 📁 multiple-choice/ ❌ Missing
    │   └── 📁 visual-reasoning/ ❌ Missing
    ├── 📁 ground-and-locate/
    │   ├── 📁 bbox/ ❌ Missing
    │   ├── 📁 mask/ ❌ Missing
    │   └── 📁 multi-phrase/ ❌ Missing
    └── 📁 align-and-retrieve/
        ├── 📁 image-to-text/ ❌ Missing
        ├── 📁 text-to-image/ ❌ Missing
        └── 📁 pair-matching/ ❌ Missing
```

## 📋 Template Standards

### **Naming Convention**
```
{domain}_{task}_{subtype}_{difficulty}_{number}.md
```

**Examples**:
- `domain-agnostic_classification_binary_easy_1.md`
- `domain-agnostic_object-and-lesion-detection_lesion_easy_1.md`
- `domain-agnostic_vision-language_describe_short_easy_1.md`

### **8-Section Structure**
All templates follow standardized documentation:
1. Template Overview
2. Template Description
3. Question Generation Pattern
4. Mapping to Datum Schema
5. Dataset Requirements
6. Template Usage Rules
7. Examples (5 concrete examples)
8. Implementation Notes

### **Quality Standards**
- ✅ **Medical Accuracy**: Correct medical terminology
- ✅ **Schema Compliance**: Perfect alignment with unified datum schema v1.0
- ✅ **Clinical Relevance**: Real diagnostic workflows
- ✅ **Cross-Domain**: Work across medical specialties

## 🎯 Quick Reference

### **Need a Template?**
1. **Classification**: Use `classification/` directory
   - Binary: `binary/` (9 options available)
   - Multiclass: `multiclass/` (3 options available)
   - Multilabel: `multilabel/` (3 options available)
   - Ordinal: `ordinal/` (⚠️ planned in Task 10)

2. **Object Detection**: Use `object-and-lesion-detection/`
   - Lesions: `lesion/` (1 template available)
   - Anatomy: `anatomy/` (1 template available)
   - Devices: `device/` (1 template available)

3. **Segmentation**: Use `segmentation/`
   - Semantic: `semantic/` (3 templates available)
   - Instance: `instance/` (3 templates available)

4. **Landmarks**: Use `anatomical-landmarks-keypoints/` (⚠️ planned in Task 10)

5. **Vision-Language**: Use `vision-language/` (⚠️ planned in Task 10)

### **Each Directory Contains**:
- 📄 **README.md**: Comprehensive index with taxonomy mapping and template inventory
- 📄 **Template files**: Actual template implementations with examples
- 🏷️ **Clear taxonomy mapping**: Connection to official medical vision taxonomy
- 📊 **Status tracking**: What's complete vs missing vs planned

## 🔗 Documentation

- **Taxonomy Structure**: `docs/taxonomy_structure_mapping.md`
- **Task Instructions**: `instructions/task_10_priority_missing_templates.md`
- **General Guidelines**: `instructions/general_instructions.md`

---

*This directory provides comprehensive coverage of the medical vision domain with templates aligned to the official Medical Vision and Vision–Language Taxonomy.*
