# Lesion Detection with Bounding Boxes Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Leaf Node**: `Lesion detection with bounding boxes`  
**Parent Category**: Vision → Object and Lesion Detection  
**Repository Path**: `templates/domain-agnostic/object-and-lesion-detection/lesion/`

## 📁 Template Inventory

### **Current Status: ✅ BASIC COVERAGE (1 template)**

| Template ID | Difficulty | Purpose | Question Pattern | Status |
|-------------|------------|---------|------------------|---------|
| `domain-agnostic_detection_object_easy_1.md` | Easy | Basic lesion classification with highlighting | "What type of lesion is highlighted in the bounding box?" | ✅ **Complete** |

### **How This Template Works**:
- **Input**: Medical image with lesion detection bounding boxes
- **Visual Highlighting**: Template highlights specific lesion with bounding box overlay
- **Question**: Asks for classification of the highlighted lesion
- **Answer**: Single label identifying the lesion type (nodule, mass, lesion, etc.)
- **Clinical Use**: Disease diagnosis and pathology identification

## 📋 Template Functionality

This directory contains domain-agnostic templates for converting lesion detection datasets into MCVQA format. These templates focus specifically on detecting and localizing pathological findings and lesions.

## What is Lesion Detection?

**Definition**: Detect and localize lesions in the image with rectangular boxes and assign a lesion class.

**Key Characteristics**:
- **Input**: Medical image
- **Output**: List of bounding boxes + lesion class per box
- **Clinical Focus**: Pathological findings and disease detection
- **Primary Use**: Diagnostic support and abnormality identification

## Medical Examples
- **Chest X-ray**: Pulmonary nodule detection, pneumonia identification
- **Dermatology**: Skin lesion detection (melanoma, basal cell carcinoma)
- **Brain Imaging**: Tumor detection, stroke lesion identification
- **Mammography**: Mass detection, calcification identification
- **CT Scans**: Liver lesions, lung nodules, bone metastases

## Template Collection

### ✅ **Current Templates**
1. **domain-agnostic_detection_object_easy_1.md**
   - **Pattern**: "What type of lesion is highlighted in the bounding box?"
   - **Use Case**: Basic lesion classification with visual highlighting
   - **Clinical Context**: Disease diagnosis and pathology identification

### 📝 **Future Templates**
- **Medium**: Multi-lesion counting, lesion severity assessment
- **Hard**: Lesion progression analysis, differential diagnosis support

## Dataset Compatibility

**High Priority**: This is the **largest object detection subtype** with **53 available datasets**.

**Dataset Examples**:
- **LIDC-IDRI**: Lung nodule detection (Quality: 85)
- **Dental Condition Detection**: Dental pathology (Quality: 85)
- **Skin lesion datasets**: Various dermatology detection tasks
- **Brain tumor datasets**: Neurological lesion detection

## Clinical Applications

**Primary Uses**:
- **Screening Programs**: Early disease detection in asymptomatic populations
- **Diagnostic Support**: Assisting radiologists in lesion identification
- **Treatment Planning**: Lesion localization for surgical or therapeutic intervention
- **Disease Monitoring**: Tracking lesion progression over time

**Medical Specialties**:
- Radiology (chest, abdominal, neurological imaging)
- Dermatology (skin lesion analysis)
- Pathology (tissue lesion identification)
- Oncology (tumor detection and monitoring)

## Schema Integration

- **Task**: "Detection"
- **Answer Type**: "single_label"
- **Spatial Reference**: Bounding box highlighting with lesion coordinates
- **Clinical Focus**: Pathological finding classification

## Implementation Notes

**Advantages**:
- Critical for medical AI diagnostic support systems
- High dataset availability enables comprehensive evaluation
- Direct clinical applicability for screening and diagnosis

**Quality Considerations**:
- Use precise pathological terminology
- Ensure clinical relevance of lesion categories
- Maintain spatial accuracy for diagnostic applications

## Medical Terminology Standards

Templates use established medical terminology for:
- **Lesion types**: Nodule, mass, lesion, tumor, cyst, calcification
- **Anatomical context**: Organ-specific pathology naming
- **Severity indicators**: When applicable to grading systems
- **Clinical descriptors**: Shape, size, and characteristic terminology
