# Surgery Domain-Specific Templates

This directory contains MCVQA templates specialized for surgical imaging tasks. These templates work with intraoperative video, surgical photography, and procedural documentation for training and assessment applications.

## Template Organization

### Multiclass Classification (`classification/multiclass/`)
- **Surgical Phase Recognition** - Procedural workflow identification
- **Anatomical Structure Identification** - Surgical navigation support
- **Surgical Instrument Classification** - Tool recognition and tracking
- **Tissue Type Assessment in Surgical Context** - Intraoperative tissue evaluation

### Binary Classification (`classification/binary/`)
- **Critical View of Safety Achievement** - Laparoscopic surgery safety assessment
- **Surgical Complication Detection** - Adverse event identification

### Anatomical Landmarks (`anatomical-landmarks-keypoints/multiple/`)
- **Surgical Landmark Quality Assessment** - Navigation and orientation evaluation (MCVQA format)

### Ordinal Classification (`classification/ordinal/`)
- **Surgical Skill Assessment** - Technical proficiency evaluation

## Example Question Generation

**Template**: `surgery_classification_multiclass_easy_1.md`  
**Question Formula**: "What surgical phase is currently shown in this surgical video frame?"  
**Answer Formula**: A. Preparation and setup | B. Incision and access | C. Dissection and exposure | D. Critical view achievement | E. Resection and removal | F. Hemostasis and inspection | G. Closure and finishing  
**Input**: Laparoscopic video frame showing tissue dissection  
**Generated Answer**: C. Dissection and exposure

## Clinical Context

These templates reflect surgical workflows from procedural planning to skill assessment, supporting AI development for surgical training, workflow analysis, and intraoperative guidance systems.
