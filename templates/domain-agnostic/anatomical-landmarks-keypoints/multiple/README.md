# Multiple Landmark Detection Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Leaf Node**: `Multiple landmark detection — several points`  
**Parent Category**: Vision → Anatomical Landmarks and Keypoints  
**Repository Path**: `templates/domain-agnostic/anatomical-landmarks-keypoints/multiple/`

## 📁 Template Inventory

### **Current Status: ✅ COMPLETE (Task 10 Implementation)**

| Template ID | Difficulty | Purpose | Question Pattern | Status |
|-------------|------------|---------|------------------|---------|
| `domain-agnostic_anatomical-landmarks-keypoints_multiple_easy_1.md` | Easy | Multiple Landmark Localization | "Which set of points correctly identifies the {landmark_set} in this {modality} image?" | ✅ **Implemented** |

### **How This Template Works**:
- **Input**: Medical image with multiple anatomical landmarks
- **Question**: MCVQA format asking to select correct landmark set from coordinate group options
- **Answer**: Single correct coordinate set selected from 4 anatomically meaningful landmark sets
- **Output Examples**:
  - A. "Set A: [Nasion: (245, 85), Sella: (220, 120), Menton: (240, 380), Gonion: (180, 320)]"
  - B. "Set B: [Nasion: (260, 100), Sella: (200, 140), Menton: (220, 360), Gonion: (160, 300)]"
  - C. "Set C: [Nasion: (230, 70), Sella: (240, 100), Menton: (260, 400), Gonion: (200, 340)]"
  - D. "Set D: [Nasion: (255, 95), Sella: (210, 130), Menton: (230, 370), Gonion: (170, 310)]"
- **Clinical Use**: Comprehensive anatomical assessment, spatial relationship evaluation, multi-point localization training

## 📋 Template Functionality

This directory contains domain-agnostic templates for converting multiple anatomical landmark detection datasets into MCVQA format. These templates focus on predicting coordinates of multiple anatomical landmarks in a single image.

## What is Multiple Landmark Detection?

**Definition**: Predict coordinates of multiple anatomical landmarks in a medical image.

**Key Characteristics**:
- **Input**: Medical image
- **Output**: List of (x,y) points
- **Precision**: Point-level accuracy for each landmark
- **Clinical Use**: Comprehensive anatomical mapping and analysis

## Medical Examples

### **Cephalometric Analysis**
- **Orthodontic landmarks**: Skull reference points for treatment planning
- **Growth assessment**: Serial landmark measurement for development tracking
- **Surgical planning**: Multiple anatomical reference points for procedures

### **Surgical Applications**
- **Navigation systems**: Multiple reference points for procedure guidance
- **Anatomical mapping**: Comprehensive point identification for surgery
- **Registration points**: Multiple landmarks for image alignment

### **Research Applications**
- **Biomechanical studies**: Movement analysis using multiple tracking points
- **Shape analysis**: Anatomical variation studies using landmark sets
- **Growth studies**: Development tracking with multiple measurement points

## Template Collection

### 📝 **Planned Templates (High Priority)**
1. **Multiple Landmark Location Set**
   - **Pattern**: "Mark the locations of the {landmark_set} in this {modality} image."
   - **Answer**: List of coordinates [(x1,y1), (x2,y2), ...]
   - **Use Case**: Comprehensive anatomical point identification

### 📝 **Future Templates**
- **Landmark Set Verification**: "Are all the {landmark_set} correctly marked?"
- **Spatial Relationships**: "Which landmark is closest to {reference}?"

## Dataset Compatibility

**Available Datasets** (3 identified):
- **SurgicalVideoEndoNeRFTracking**: Multiple surgical tracking points
- **CT-ScanGaze**: Multiple 3D fixation coordinates with temporal data
- **Subglottal Pressure Experiments**: Multiple laryngeal trajectory points

**Dataset Requirements**:
- **Multiple point annotations**: Precise (x,y) coordinates for multiple landmarks per image
- **Landmark relationships**: Anatomically meaningful point configurations
- **Consistent labeling**: Standardized landmark identification across images

## Clinical Applications

**Primary Uses**:
- **Comprehensive Analysis**: Complete anatomical mapping for detailed assessment
- **Surgical Planning**: Multiple reference points for complex procedures
- **Growth Monitoring**: Serial multi-point assessment over time
- **Biomechanical Research**: Movement and deformation analysis

**Specialized Applications**:
- **Orthodontics**: Cephalometric landmark analysis (20-30 points typically)
- **Surgery**: Anatomical navigation with multiple reference points
- **Research**: Shape analysis and anatomical variation studies
- **Quality Control**: Comprehensive anatomical verification

## Schema Integration

- **Task**: "Landmarks"
- **Answer Type**: List of coordinates [(x,y), ...]
- **Spatial Precision**: Point-level accuracy for each landmark
- **Landmark Relationships**: Maintain anatomical consistency between points

## Template Structure

**Question Format**: Multiple location identification with landmark set specification
**Answer Format**: Ordered list of coordinate pairs
**Spatial Reference**: May highlight target regions for landmark groups
**Clinical Context**: Comprehensive anatomical mapping applications

## Quality Requirements

**Anatomical Consistency**:
- Landmark sets must follow established anatomical protocols
- Maintain spatial relationships between landmarks
- Use standardized landmark nomenclature

**Technical Precision**:
- Each coordinate must meet clinical accuracy standards
- Landmark ordering must be consistent and meaningful
- Handle missing or obscured landmarks appropriately

**Clinical Validity**:
- Landmark sets must serve established clinical purposes
- Support validated measurement and analysis protocols
- Enable meaningful clinical interpretation

## Implementation Challenges

**Complexity Management**:
- Multiple landmarks increase annotation complexity
- Coordinate accuracy requirements multiply with landmark count
- Spatial consistency between landmarks must be maintained

**Clinical Considerations**:
- Not all landmarks may be visible in every image
- Landmark visibility varies with imaging technique and patient anatomy
- Inter-observer variability increases with landmark count

## Evaluation Considerations

**Accuracy Metrics**:
- Individual landmark accuracy assessment
- Overall landmark set accuracy evaluation
- Spatial relationship preservation metrics

**Clinical Validation**:
- Compare with established clinical measurement protocols
- Validate against expert landmark placement
- Assess clinical utility of automated landmark detection

## Future Development

**Advanced Templates**:
- **Dynamic tracking**: Multiple landmarks across time series
- **Multi-view consistency**: Landmark correspondence across imaging views
- **Uncertainty quantification**: Confidence assessment for landmark placement
