# Anatomy Detection with Bounding Boxes Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Leaf Node**: `Anatomy detection with bounding boxes`  
**Parent Category**: Vision → Object and Lesion Detection  
**Repository Path**: `templates/domain-agnostic/object-and-lesion-detection/anatomy/`

## 📁 Template Inventory

### **Current Status: ✅ BASIC COVERAGE (1 template)**

| Template ID | Difficulty | Purpose | Question Pattern | Status |
|-------------|------------|---------|------------------|---------|
| `domain-agnostic_detection_object_easy_2.md` | Easy | Basic anatomical structure identification | "What anatomical structure is highlighted in the bounding box?" | ✅ **Complete** |

### **How This Template Works**:
- **Input**: Medical image with anatomical structure detection bounding boxes
- **Visual Highlighting**: Template highlights specific anatomical structure with bounding box overlay
- **Question**: Asks for identification of the highlighted anatomical structure
- **Answer**: Single label naming the anatomical structure (organ, bone, tissue type, etc.)
- **Clinical Use**: Structure identification and anatomical assessment

## 📋 Template Functionality

This directory contains domain-agnostic templates for converting anatomy detection datasets into MCVQA format. These templates focus specifically on detecting and localizing anatomical structures.

## What is Anatomy Detection?

**Definition**: Detect and localize anatomical structures with rectangular boxes and assign anatomical class labels.

**Key Characteristics**:
- **Input**: Medical image
- **Output**: Boxes + anatomical class per box
- **Clinical Focus**: Structure identification and anatomical assessment
- **Primary Use**: Anatomical recognition and medical education

## Medical Examples
- **Fundus imaging**: Optic disc detection, macula identification
- **Chest X-ray**: Heart boundary detection, lung field identification
- **CT imaging**: Organ detection (liver, kidney, spleen)
- **Bone imaging**: Joint detection, bone structure identification
- **Ultrasound**: Fetal anatomy detection, organ boundary identification

## Template Collection

### ✅ **Current Templates**
1. **domain-agnostic_detection_object_easy_2.md**
   - **Pattern**: "What anatomical structure is highlighted in the bounding box?"
   - **Use Case**: Basic anatomical structure classification with visual highlighting
   - **Clinical Context**: Structure identification and anatomical assessment

### 📝 **Future Templates**
- **Medium**: Multi-structure identification, anatomical relationship questions
- **Hard**: Complex anatomical reasoning, spatial relationship analysis

## Dataset Compatibility

**Available Datasets**: **9 datasets** identified in metadata.

**Dataset Examples**:
- **LeukemiaAttri**: Blood cell anatomical feature detection (Quality: 75)
- **Blood Cell Detection**: Cellular structure identification (Quality: 65)
- **Ophthalmology datasets**: Fundus anatomical structure detection
- **Radiology datasets**: Organ and bone structure detection

## Clinical Applications

**Primary Uses**:
- **Medical Education**: Teaching anatomical recognition skills
- **Image Analysis**: Automated anatomical structure identification
- **Quality Control**: Ensuring proper anatomical visualization in medical images
- **Treatment Planning**: Anatomical landmark identification for procedures

**Medical Specialties**:
- Ophthalmology (retinal structure identification)
- Radiology (organ and bone detection)
- Cardiology (cardiac structure identification)
- Obstetrics (fetal anatomy detection)
- Pathology (tissue structure identification)

## Schema Integration

- **Task**: "Detection"
- **Answer Type**: "single_label"
- **Spatial Reference**: Bounding box highlighting with anatomical coordinates
- **Clinical Focus**: Normal anatomical structure classification

## Implementation Notes

**Advantages**:
- Fundamental for medical AI systems requiring anatomical awareness
- Essential for medical education and training applications
- Provides baseline anatomical recognition capabilities

**Quality Considerations**:
- Use precise anatomical terminology following medical standards
- Ensure cross-cultural applicability of anatomical naming
- Maintain consistency with medical education standards

## Anatomical Terminology Standards

Templates use established anatomical terminology for:
- **Major organs**: Heart, liver, kidney, lung, brain, etc.
- **Bone structures**: Femur, tibia, skull, vertebrae, ribs
- **Specialized structures**: Optic disc, macula, cardiac chambers
- **Tissue types**: When relevant to detection context
- **Regional anatomy**: Anatomical position and orientation terms

## Educational Value

These templates support:
- **Medical student training**: Basic anatomical recognition
- **Resident education**: Cross-sectional anatomy understanding  
- **Continuing education**: Anatomical refresher and assessment
- **AI system validation**: Ensuring proper anatomical understanding in medical AI
