# Single Landmark Detection Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Leaf Node**: `Single landmark detection — one anatomical point`  
**Parent Category**: Vision → Anatomical Landmarks and Keypoints  
**Repository Path**: `templates/domain-agnostic/anatomical-landmarks-keypoints/single/`

## 📁 Template Inventory

### **Current Status: ✅ COMPLETE (Task 10 Implementation)**

| Template ID | Difficulty | Purpose | Question Pattern | Status |
|-------------|------------|---------|------------------|---------|
| `domain-agnostic_anatomical-landmarks-keypoints_single_easy_1.md` | Easy | Single Landmark Localization | "Where is the {landmark} located in this {modality} image?" | ✅ **Implemented** |
| `domain-agnostic_anatomical-landmarks-keypoints_single_easy_2.md` | Easy | Surgical/Procedural Landmark Localization | "Where is the optimal {procedure_landmark} located for {procedure_type} in this {modality} image?" | ✅ **Implemented** |

### **How These Templates Work**:
- **Input**: Medical image with single anatomical landmark
- **Question**: MCVQA format asking to select correct landmark location from coordinate region options
- **Answer**: Single correct coordinate region selected from 4 anatomically meaningful options
- **Output Examples**:
  - A. "Central macula region (312, 245)"
  - B. "Temporal retina region (450, 200)"
  - C. "Nasal retina region (180, 260)"
  - D. "Superior retina region (310, 120)"
- **Clinical Use**: Spatial reasoning assessment, anatomical localization training, procedural planning evaluation

## 📋 Template Functionality

This directory contains domain-agnostic templates for converting single anatomical landmark detection datasets into MCVQA format. These templates focus on predicting coordinates of a single anatomical landmark per image.

## What is Single Landmark Detection?

**Definition**: Predict coordinates of a single anatomical landmark in a medical image.

**Key Characteristics**:
- **Input**: Medical image
- **Output**: One (x,y) coordinate
- **Precision**: Point-level accuracy required
- **Clinical Use**: Precise measurement and reference point identification

## Medical Examples

### **Ophthalmology**
- **Fovea center detection**: Critical reference point for retinal analysis
- **Optic disc center**: Central point of optic nerve head
- **Pupil center**: Reference for eye tracking and measurement

### **Radiology**
- **Anatomical reference points**: Specific landmark identification in CT/MRI
- **Measurement origins**: Starting points for distance calculations
- **Surgical targets**: Critical points for procedure planning

### **Other Specialties**
- **Cardiac imaging**: Heart reference points for measurement
- **Orthopedics**: Joint center identification
- **Neurology**: Brain landmark identification

## Template Collection

### 📝 **Planned Templates (High Priority)**
1. **Basic Single Landmark Location**
   - **Pattern**: "Identify the location of the {landmark} in this {modality} image."
   - **Answer**: (x,y) coordinates
   - **Use Case**: Direct anatomical point localization

### 📝 **Future Templates**
- **Landmark Verification**: "Is the marked location correctly positioned at the {landmark}?"
- **Relative Positioning**: "Where is the {landmark} located relative to {reference}?"

## Dataset Compatibility

**Available Dataset**:
- **Pupil_Position_in_the_Eye**: Single point pupil localization in eye images

**Dataset Requirements**:
- **Single point annotations**: Precise (x,y) coordinates for one landmark per image
- **Medical images**: Clear visualization of target anatomical landmark
- **Consistent landmark definition**: Anatomically meaningful and reproducible points

## Clinical Applications

**Primary Uses**:
- **Measurement Origin**: Starting point for distance and angle measurements
- **Reference Point**: Anatomical coordinate system establishment  
- **Quality Assessment**: Verification of proper anatomical visualization
- **Surgical Planning**: Critical point identification for procedures

**Measurement Applications**:
- **Ophthalmology**: Retinal distance measurements from fovea
- **Cardiology**: Cardiac dimension measurements from chamber centers
- **Orthopedics**: Joint space measurements from bone landmarks
- **Radiology**: Anatomical distance and angle calculations

## Schema Integration

- **Task**: "Landmarks"
- **Answer Type**: Coordinates (x,y)
- **Spatial Precision**: Point-level accuracy
- **Coordinate System**: Relative [0,1] normalized coordinates

## Template Structure

**Question Format**: Location identification with anatomical precision
**Answer Format**: Precise coordinate pairs
**Spatial Reference**: May include highlighting of target region
**Clinical Context**: Anatomical measurement and reference applications

## Quality Requirements

**Anatomical Accuracy**:
- Use precise anatomical landmark terminology
- Follow established anatomical reference standards
- Ensure cross-cultural applicability of landmark definitions

**Technical Precision**:
- Coordinate accuracy must be clinically meaningful
- Reproducible landmark identification
- Clear landmark definition criteria

**Clinical Relevance**:
- Landmarks must serve meaningful clinical purposes
- Support established medical measurement protocols
- Enable quantitative medical analysis

## Implementation Notes

**Advantages**:
- Essential for quantitative medical analysis
- Supports precision medicine applications
- Enables automated measurement systems

**Challenges**:
- Requires high anatomical expertise
- Coordinate precision critical for clinical utility
- Landmark visibility may vary across images

**Evaluation Considerations**:
- Distance-based accuracy metrics
- Clinical significance of coordinate errors
- Inter-observer reliability validation
