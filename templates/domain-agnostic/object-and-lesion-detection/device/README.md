# Device Detection with Bounding Boxes Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Leaf Node**: `Device detection with bounding boxes`  
**Parent Category**: Vision → Object and Lesion Detection  
**Repository Path**: `templates/domain-agnostic/object-and-lesion-detection/device/`

## 📁 Template Inventory

### **Current Status: ✅ BASIC COVERAGE (1 template)**

| Template ID | Difficulty | Purpose | Question Pattern | Status |
|-------------|------------|---------|------------------|---------|
| `domain-agnostic_detection_object_easy_3.md` | Easy | Basic medical device identification | "What medical device is highlighted in the bounding box?" | ✅ **Complete** |

### **How This Template Works**:
- **Input**: Medical image with medical device detection bounding boxes
- **Visual Highlighting**: Template highlights specific medical device with bounding box overlay
- **Question**: Asks for identification of the highlighted medical device
- **Answer**: Single label naming the medical device (pacemaker, tube, catheter, implant, etc.)
- **Clinical Use**: Procedure support and device monitoring

## 📋 Template Functionality

This directory contains domain-agnostic templates for converting medical device detection datasets into MCVQA format. These templates focus specifically on detecting and localizing medical devices and hardware.

## What is Device Detection?

**Definition**: Detect and localize medical devices/hardware with rectangular boxes and assign device class labels.

**Key Characteristics**:
- **Input**: Medical image
- **Output**: Boxes + device class per box
- **Clinical Focus**: Medical device identification and monitoring
- **Primary Use**: Procedure support and device verification

## Medical Examples
- **Chest X-ray**: Pacemaker detection, endotracheal tube placement, central line verification
- **Surgical imaging**: Surgical instrument detection, implant identification
- **ICU monitoring**: Ventilator equipment, monitoring device placement
- **Orthopedic imaging**: Hardware detection (screws, plates, prosthetics)
- **Interventional procedures**: Catheter detection, stent identification

## Template Collection

### ✅ **Current Templates**
1. **domain-agnostic_detection_object_easy_3.md**
   - **Pattern**: "What medical device is highlighted in the bounding box?"
   - **Use Case**: Basic medical device classification with visual highlighting
   - **Clinical Context**: Procedure support and device monitoring

### 📝 **Future Templates**
- **Medium**: Device placement assessment, multi-device identification
- **Hard**: Device malfunction detection, procedural compliance verification

## Dataset Compatibility

**Available Datasets**: **4 datasets** identified in metadata.

**Dataset Examples**:
- **4D-OR**: Surgical device detection in operating room (Quality: 72)
- **HOSPI-Tools Dataset**: Hospital medical device identification (Quality: 70)
- **Medical device datasets**: Various device detection tasks
- **Surgical instrument datasets**: Operating room equipment detection

## Clinical Applications

**Primary Uses**:
- **Procedure Verification**: Confirming proper device placement
- **Safety Monitoring**: Detecting device malposition or displacement
- **Inventory Management**: Automated device tracking in medical facilities
- **Quality Assurance**: Ensuring appropriate device usage

**Medical Specialties**:
- Surgery (instrument and implant detection)
- Radiology (device verification in imaging)
- Critical Care (monitoring equipment detection)
- Cardiology (pacemaker, stent, catheter detection)
- Orthopedics (hardware and prosthetic detection)

## Schema Integration

- **Task**: "Detection"
- **Answer Type**: "single_label"
- **Spatial Reference**: Bounding box highlighting with device coordinates
- **Clinical Focus**: Medical device classification

## Implementation Notes

**Advantages**:
- Critical for procedural safety and quality assurance
- Supports automated medical device monitoring
- Important for regulatory compliance and documentation

**Quality Considerations**:
- Use precise medical device terminology
- Ensure safety-critical accuracy for device identification
- Maintain consistency with medical device standards

## Medical Device Categories

Templates cover standard medical device classifications:

### **Monitoring Devices**
- Electrodes, sensors, probes
- Monitoring leads and cables
- Temperature and pressure monitors

### **Therapeutic Devices**
- Pacemakers, defibrillators
- Infusion pumps, ventilators
- Surgical instruments

### **Diagnostic Devices**
- Catheters, endoscopes
- Biopsy needles, guidewires
- Contrast injection devices

### **Implanted Devices**
- Orthopedic hardware (plates, screws, rods)
- Prosthetic devices
- Stents, filters, coils

## Safety Considerations

Device detection templates must:
- **Prioritize accuracy**: Device misidentification can have serious clinical consequences
- **Follow standards**: Use FDA/CE approved device nomenclature
- **Consider context**: Device detection must align with clinical workflows
- **Enable verification**: Support human oversight and verification processes
