# Surgery Surgical Instrument Classification Template

## Template Overview

**Template ID**: `surgery_classification_multiclass_easy_3`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Surgical instrument identification  
**Domain**: Surgery (intraoperative imaging)

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about surgical instruments being used in operative images. This capability is important for surgical training, workflow analysis, and instrument tracking during procedures.

The template is designed for surgery datasets with instrument annotations, testing the model's ability to recognize and identify different surgical tools and their applications in clinical settings.

## Question Generation Pattern

### Question Format
```
"What surgical instrument is being used in this image?"
```

### Answer Format
Multiclass choice with surgical instrument options:
- A. Grasper
- B. Scissors
- C. Clip applier
- D. Electrocautery
- E. Suction/irrigation
- F. Trocar
- G. Needle holder
- H. Retractor

### Template Variables
- `{instrument_type}`: Specific category and function of surgical tool
- `{surgical_context}`: Procedural phase and clinical application
- `{visual_characteristics}`: Shape, size, and identifying features
- `{functional_purpose}`: Intended use and mechanism of action

### Clinical Context
- **Grasper**: Tissue manipulation and specimen handling
- **Scissors**: Cutting and dissection activities
- **Clip Applier**: Hemostatic clipping and vessel occlusion
- **Electrocautery**: Electrical cutting and coagulation
- **Suction/Irrigation**: Fluid management and field clearing
- **Trocar**: Port placement and access creation
- **Needle Holder**: Suturing and needle manipulation
- **Retractor**: Tissue retraction and exposure

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What surgical instrument is being used in this image?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Grasper",
    "Scissors",
    "Clip applier",
    "Electrocautery",
    "Suction/irrigation",
    "Trocar",
    "Needle holder",
    "Retractor"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Instrument shows characteristic grasping jaws and articulation mechanism typical of laparoscopic grasper",
  "provenance": {
    "original_label": "grasper",
    "rule_id": "surgery_classification_multiclass_easy_3",
    "annotation_id": "surgical_instrument",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Intraoperative images showing surgical instruments in use
- **Labels**: Instrument type annotations with functional context
- **Quality**: Clear visualization of instrument characteristics and usage

### Compatible Datasets

**Available in MBU Metadata:**
- `introvoyz041/ORBIT-surgical` - Surgical imagery with instrument recognition context
- `introvoyz041/surgicalSAM` - Surgical segmentation with instrument analysis
- `connectthapa84/SurgeryVideoQA` - Surgical video analysis including instrument usage

**General Categories:**
- Surgical instrument detection datasets
- Laparoscopic tool identification collections
- Surgical training instrument databases
- Workflow analysis instrument tracking sets
- Robotic surgery tool recognition data

### Minimum Standards
- **Image Quality**: Sufficient detail for instrument identification and differentiation
- **Annotation Quality**: Expert validation by surgical personnel
- **Data Distribution**: Representative coverage of commonly used surgical instruments

## Template Usage Rules

### Question Construction Rules
1. Focus on clearly visible instruments in active use
2. Use standard surgical instrument terminology
3. Consider functional context and application
4. Emphasize instruments critical for procedural success

### Answer Assignment Rules
1. Map tissue manipulation tools → "Grasper"
2. Map cutting instruments → "Scissors"
3. Map hemostatic devices → "Clip applier"
4. Map electrical devices → "Electrocautery"
5. Map fluid management tools → "Suction/irrigation"
6. Map access devices → "Trocar"
7. Map suturing tools → "Needle holder"
8. Map exposure tools → "Retractor"

### Quality Control Guidelines
1. Ensure accurate instrument identification and nomenclature
2. Verify functional context matches instrument type
3. Cross-validate with surgical instrument references
4. Review for educational and training accuracy

## Examples

### Example 1: Laparoscopic Grasping
**Image**: Laparoscopic view showing grasping forceps manipulating gallbladder  
**Question**: "What surgical instrument is being used in this image?"  
**Answer**: A. Grasper  
**Rationale**: Image shows characteristic laparoscopic grasping forceps with articulating jaws for tissue manipulation

### Example 2: Surgical Cutting
**Image**: Intraoperative view showing curved scissors cutting tissue  
**Question**: "What surgical instrument is being used in this image?"  
**Answer**: B. Scissors  
**Rationale**: Image demonstrates surgical scissors with characteristic curved blades performing tissue dissection

### Example 3: Hemostatic Clipping
**Image**: Surgical view showing clip being applied to vessel  
**Question**: "What surgical instrument is being used in this image?"  
**Answer**: C. Clip applier  
**Rationale**: Image shows clip applier device placing hemostatic clip on vascular structure for bleeding control

### Example 4: Electrocautery Use
**Image**: Surgical field showing electrical cautery with tissue effect  
**Question**: "What surgical instrument is being used in this image?"  
**Answer**: D. Electrocautery  
**Rationale**: Image demonstrates electrocautery device with characteristic electrical cutting and coagulation effects

### Example 5: Field Irrigation
**Image**: Surgical view showing irrigation and suction of operative field  
**Question**: "What surgical instrument is being used in this image?"  
**Answer**: E. Suction/irrigation  
**Rationale**: Image shows suction-irrigation device clearing fluid from surgical field for improved visualization

## Implementation Notes

### Technical Considerations
- Implement instrument shape and feature recognition algorithms
- Consider different surgical approaches and instrument variations
- Account for partial occlusion and varying viewing angles
- Handle different instrument manufacturers and designs

### Clinical Validation
- Align with standard surgical instrument classifications
- Cross-reference with surgical training materials
- Validate against experienced surgical personnel
- Consider procedure-specific instrument requirements

### Dataset-Specific Adaptations
- **Procedure-specific datasets**: Focus on relevant instruments for each procedure
- **Multi-approach datasets**: Account for open vs laparoscopic vs robotic instruments
- **Training datasets**: Emphasize educationally important instruments
- **Workflow datasets**: Include instruments used throughout procedural phases

### Quality Assurance
- Regular validation by surgical technologists and surgeons
- Cross-reference with surgical instrument catalogs and references
- Monitoring for accuracy across different surgical specialties
- Updates based on evolving surgical technology and instrument design
