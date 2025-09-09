# Domain-Agnostic Anatomical Landmarks and Keypoints Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Sub-Category**: `Anatomical Landmarks and Keypoints`  
**Parent Category**: Vision  
**Repository Path**: `templates/domain-agnostic/anatomical-landmarks-keypoints/`

## 📁 Template Inventory

### **Current Status: ❌ MISSING (High Priority)**

| Subdirectory | Leaf Node | Planned Templates | Status |
|--------------|-----------|-------------------|---------|
| `single/` | Single landmark detection — one anatomical point | 1-2 easy templates | 📝 **Planned (Task 10)** |
| `multiple/` | Multiple landmark detection — several points | 1-2 easy templates | 📝 **Planned (Task 10)** |

### **Planned Template Functionality**:
- **Single Landmark**: Point coordinate prediction for single anatomical reference points
- **Multiple Landmarks**: Coordinate set prediction for multiple related anatomical points
- **Question Pattern**: "Identify the location of the {landmark}" or "Mark the locations of {landmark_set}"
- **Answer Format**: (x,y) coordinates or list of coordinates
- **Clinical Use**: Precise measurement, surgical planning, anatomical analysis

## 📋 How These Templates Work

This directory contains domain-agnostic templates for converting anatomical landmark and keypoint detection datasets into MCVQA format. These templates work across all medical specialties for precise point localization of anatomical structures.

## What are Anatomical Landmarks and Keypoints?

**Definition**: Predict precise (x,y) coordinates of anatomical landmarks in medical images for measurement and analysis.

**Key Characteristics**:
- **Input**: One 2D medical image
- **Output**: (x,y) coordinates for single landmark OR list of (x,y) points for multiple landmarks
- **Task Focus**: Precise point localization for measurement and analysis
- **vs Object Detection**: Point coordinates instead of bounding boxes
- **vs Segmentation**: Point locations instead of pixel masks

## Sub-Categories

This directory is organized by the two official taxonomy leaf nodes:

### 1. **Single Landmark Detection** (`single/`)
- **Definition**: Predict coordinates of a single anatomical landmark
- **Output**: One (x,y) coordinate
- **Examples**: Fovea center in fundus, pupil center, specific anatomical point

### 2. **Multiple Landmark Detection** (`multiple/`)
- **Definition**: Predict coordinates of multiple anatomical landmarks
- **Output**: List of (x,y) points
- **Examples**: Cephalometric X-ray landmarks, surgical tracking points, facial landmarks

## Template Collection Status

### 📝 **Currently Missing (High Priority)**
This category is identified as one of the **highest priority missing template categories** with **4 available datasets**.

**Planned Templates**:
1. **Single Landmark Detection**: "Identify the location of the {landmark} in this {modality} image."
2. **Multiple Landmark Detection**: "Mark the locations of the {landmark_set} in this {modality} image."

## Medical Examples

### **Single Landmark Applications**
- **Ophthalmology**: Fovea center detection for retinal analysis
- **Radiology**: Anatomical reference point identification
- **Surgery**: Critical anatomical landmark localization
- **Measurements**: Distance and angle calculations from reference points

### **Multiple Landmark Applications**
- **Cephalometric Analysis**: Skull landmark identification for orthodontic planning
- **Surgical Navigation**: Multiple anatomical reference points for procedures
- **Growth Assessment**: Serial landmark measurement for development tracking
- **Biomechanical Analysis**: Joint and bone landmark mapping

## Key Differences from Object Detection

| **Aspect** | **Landmark Detection** | **Object Detection** |
|------------|----------------------|---------------------|
| **Output Format** | (x,y) coordinates | Bounding boxes [x1,y1,x2,y2] |
| **Clinical Use** | Precise measurement | Identification/localization |
| **Precision Level** | Point-level accuracy | Rectangular approximation |
| **Applications** | Analysis, measurement | Recognition, screening |

## Dataset Compatibility

**Available Datasets** (4 identified):
- **Pupil_Position_in_the_Eye**: Single point pupil localization
- **SurgicalVideoEndoNeRFTracking**: Multiple surgical tracking points
- **CT-ScanGaze**: Multiple 3D fixation coordinates
- **Subglottal Pressure Experiments**: Multiple larynx trajectory points

## Schema Integration

- **Task**: "Landmarks"
- **Answer Type**: Coordinates or list of coordinates
- **Spatial Reference**: Precise (x,y) coordinate system
- **Anatomical ID**: Link to specific anatomical structures

## Clinical Applications

**Primary Uses**:
- **Measurement and Analysis**: Precise anatomical measurements
- **Surgical Planning**: Critical point identification for procedures
- **Growth Monitoring**: Serial landmark assessment over time
- **Biomechanical Studies**: Movement and deformation analysis

**Medical Specialties**:
- Orthodontics (cephalometric landmark analysis)
- Ophthalmology (retinal landmark detection)
- Surgery (anatomical reference points)
- Orthopedics (joint landmark identification)
- Radiology (anatomical measurement points)

## Implementation Notes

**Advantages**:
- Enables precise medical measurements and analysis
- Critical for surgical planning and navigation
- Supports quantitative medical research
- Essential for growth and development studies

**Quality Considerations**:
- **Point-level accuracy**: Requires precise coordinate specification
- **Anatomical knowledge**: Must use correct anatomical landmark names
- **Clinical relevance**: Landmarks must be medically meaningful
- **Measurement standards**: Follow established medical measurement protocols

## Future Template Development

**Easy Difficulty Focus**:
- Basic single point localization
- Standard multiple landmark sets
- Common anatomical measurement points

**Advanced Templates** (Future):
- Dynamic landmark tracking
- Multi-view consistency
- Uncertainty quantification in landmark detection
