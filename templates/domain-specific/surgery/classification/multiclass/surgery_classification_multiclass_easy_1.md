# Surgery Surgical Phase Recognition Template

## Template Overview

**Template ID**: `surgery_classification_multiclass_easy_1`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Surgical phase identification  
**Domain**: Surgery (intraoperative imaging)

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about surgical phases in intraoperative video frames or images. This capability is essential for surgical workflow analysis, training assessment, and automated documentation of procedural progress.

The template is designed for surgery datasets with phase annotations, testing the model's ability to recognize distinct procedural stages and workflow progression in surgical procedures.

## Question Generation Pattern

### Question Format
```
"What surgical phase is currently shown in this surgical video frame?"
```

### Answer Format
Multiclass choice with surgical phase options:
- A. Preparation and setup
- B. Incision and access
- C. Dissection and exposure
- D. Critical view achievement
- E. Resection and removal
- F. Hemostasis and inspection
- G. Closure and finishing

### Template Variables
- `{procedure_type}`: Specific surgical procedure being performed
- `{anatomical_region}`: Body region or organ system involved
- `{surgical_approach}`: Open, laparoscopic, or robotic technique
- `{workflow_stage}`: Position within overall procedural timeline

### Clinical Context
- **Preparation**: Patient positioning, sterile draping, initial setup
- **Incision/Access**: Skin incision, port placement, initial entry
- **Dissection**: Tissue planes, anatomical exposure, structure identification
- **Critical View**: Achievement of safe anatomical landmarks
- **Resection**: Specimen removal, primary therapeutic action
- **Hemostasis**: Bleeding control, inspection for complications
- **Closure**: Layer-by-layer tissue repair, completion

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What surgical phase is currently shown in this surgical video frame?",
  "answer": "C",
  "answer_type": "single_label",
  "options": [
    "Preparation and setup",
    "Incision and access",
    "Dissection and exposure",
    "Critical view achievement",
    "Resection and removal",
    "Hemostasis and inspection",
    "Closure and finishing"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Image shows active tissue dissection with exposure of anatomical structures typical of dissection phase",
  "provenance": {
    "original_label": "dissection",
    "rule_id": "surgery_classification_multiclass_easy_1",
    "annotation_id": "surgical_phase",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Intraoperative video frames or surgical photography
- **Labels**: Surgical phase annotations with procedural context
- **Quality**: Clear visualization of surgical field and instruments

### Compatible Datasets

**Available in MBU Metadata:**
- `connectthapa84/SurgeryVideoQA` - Surgical video Q&A with procedural phase context
- `Raghava1401/surgeryv2` - Surgery image-text pairs for procedural analysis
- `Hensemberk/scared-endoscopy` - Endoscopic procedure images with phase classification

**General Categories:**
- Surgical workflow analysis datasets
- Laparoscopic procedure collections
- Robotic surgery video archives
- Surgical training assessment datasets
- Procedural documentation databases

### Minimum Standards
- **Image Quality**: Sufficient resolution for phase identification
- **Annotation Quality**: Expert surgeon validation of phase classification
- **Data Distribution**: Representative coverage of all surgical phases

## Template Usage Rules

### Question Construction Rules
1. Focus on current procedural phase identification
2. Use standard surgical workflow terminology
3. Reference visual cues and procedural context
4. Maintain consistency across different surgical approaches

### Answer Assignment Rules
1. Map setup and positioning activities → "Preparation and setup"
2. Map initial cutting and entry → "Incision and access"
3. Map tissue separation and exposure → "Dissection and exposure"
4. Map anatomical landmark confirmation → "Critical view achievement"
5. Map specimen or structure removal → "Resection and removal"
6. Map bleeding control activities → "Hemostasis and inspection"
7. Map suturing and completion → "Closure and finishing"

### Quality Control Guidelines
1. Ensure phase identification reflects actual procedural stage
2. Verify consistency with surgical workflow standards
3. Cross-validate with expert surgeon assessments
4. Review for procedure-specific phase variations

## Examples

### Example 1: Laparoscopic Cholecystectomy Dissection
**Image**: Laparoscopic view showing Calot's triangle dissection  
**Question**: "What surgical phase is currently shown in this surgical video frame?"  
**Answer**: C. Dissection and exposure  
**Rationale**: Image shows active dissection of tissue planes around Calot's triangle to expose critical anatomical structures

### Example 2: Initial Port Placement
**Image**: Surgical field showing trocar insertion  
**Question**: "What surgical phase is currently shown in this surgical video frame?"  
**Answer**: B. Incision and access  
**Rationale**: Image demonstrates trocar placement for laparoscopic access, representing the incision and access phase

### Example 3: Gallbladder Removal
**Image**: Laparoscopic view showing gallbladder being placed in extraction bag  
**Question**: "What surgical phase is currently shown in this surgical video frame?"  
**Answer**: E. Resection and removal  
**Rationale**: Image shows gallbladder specimen being prepared for extraction, indicating the resection and removal phase

### Example 4: Critical View of Safety
**Image**: Clear laparoscopic view of hepatocystic triangle  
**Question**: "What surgical phase is currently shown in this surgical video frame?"  
**Answer**: D. Critical view achievement  
**Rationale**: Image demonstrates clear identification of critical anatomical structures confirming safe procedural landmarks

### Example 5: Port Site Closure
**Image**: Surgical field showing fascial layer suturing  
**Question**: "What surgical phase is currently shown in this surgical video frame?"  
**Answer**: G. Closure and finishing  
**Rationale**: Image shows systematic closure of surgical access sites representing the final phase of the procedure

## Implementation Notes

### Technical Considerations
- Implement temporal workflow analysis for phase progression
- Consider procedure-specific phase variations and terminology
- Account for different surgical approaches (open, laparoscopic, robotic)
- Handle varying video quality and camera angles

### Clinical Validation
- Align with established surgical workflow classifications
- Cross-reference with surgical training curricula
- Validate against expert surgeon phase identification
- Consider procedure-specific workflow variations

### Dataset-Specific Adaptations
- **Procedure-specific datasets**: Adapt phases to specific surgical workflows
- **Multi-approach datasets**: Account for open vs minimally invasive differences
- **Training datasets**: Emphasize educational phase progression
- **Assessment datasets**: Focus on critical decision points

### Quality Assurance
- Regular validation by experienced surgeons
- Cross-reference with surgical education standards
- Monitoring for consistency across different procedures
- Updates based on evolving surgical techniques and workflows
