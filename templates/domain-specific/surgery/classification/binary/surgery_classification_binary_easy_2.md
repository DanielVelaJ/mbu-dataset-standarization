# Surgery Surgical Complication Detection Template

## Template Overview

**Template ID**: `surgery_classification_binary_easy_2`  
**Task Type**: Binary classification  
**Difficulty**: Easy  
**Question Pattern**: Intraoperative complication identification  
**Medical Domain**: Surgery (intraoperative imaging)  
**Domain-knowledge summary**: Requires specialized surgical knowledge of intraoperative complications and tissue pathology. Must understand normal versus abnormal tissue characteristics, bleeding patterns, tissue perforation signs, instrument-related injuries, and ability to recognize surgical complications requiring immediate intervention during operative procedures.

## Template Description

This template converts binary classification datasets into MCVQA format by asking questions about surgical complications visible in intraoperative images. Early detection of complications is critical for immediate intervention and optimal patient outcomes.

The template is designed for surgery datasets with complication annotations, testing the model's ability to recognize adverse events and abnormal findings that require immediate surgical attention.

## Question Generation Pattern

### Question Format
```
"Does this intraoperative image show evidence of a surgical complication?"
```

### Answer Format
Binary choice with complication assessment options:
- A. Complication present
- B. No complication

### Template Variables
- `{complication_type}`: Specific type of adverse event or abnormality
- `{severity_indicators}`: Visual signs of complication severity
- `{anatomical_involvement}`: Structures affected by the complication
- `{intervention_urgency}`: Need for immediate corrective action

### Clinical Context
- **Complications**: Bleeding, perforation, thermal injury, vascular injury, organ damage
- **Early Recognition**: Critical for immediate intervention and damage control
- **Visual Signs**: Abnormal tissue appearance, unexpected bleeding, perforation, thermal damage
- **Clinical Impact**: Affects patient safety, procedural outcome, and recovery

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Does this intraoperative image show evidence of a surgical complication?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Complication present",
    "No complication"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Image shows active bleeding and tissue damage consistent with surgical complication requiring immediate intervention",
  "provenance": {
    "original_label": "complication",
    "rule_id": "surgery_classification_binary_easy_2",
    "annotation_id": "complication_detection",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Intraoperative images showing normal procedures and complications
- **Labels**: Binary labels indicating presence or absence of complications
- **Quality**: Clear visualization of surgical field and any abnormalities

### Compatible Datasets
- Surgical complication databases
- Adverse event documentation collections
- Surgical safety and quality datasets
- Intraoperative error recognition sets
- Surgical training complication examples

### Minimum Standards
- **Image Quality**: Sufficient detail for complication identification
- **Annotation Quality**: Expert validation by experienced surgeons
- **Data Distribution**: Balanced representation of complicated and uncomplicated cases

## Template Usage Rules

### Question Construction Rules
1. Focus on visible evidence of surgical complications
2. Use general complication terminology applicable across procedures
3. Emphasize immediate recognition and intervention needs
4. Consider patient safety and quality improvement applications

### Answer Assignment Rules
1. Map visible adverse events → "Complication present"
2. Map normal procedural appearance → "No complication"
3. Include bleeding, perforation, thermal injury, organ damage
4. Use conservative assessment for patient safety

### Quality Control Guidelines
1. Ensure accurate complication identification and classification
2. Verify clinical significance and intervention requirements
3. Cross-validate with expert surgical assessment
4. Review for educational and quality improvement value

## Examples

### Example 1: Active Hemorrhage
**Image**: Surgical field showing significant active bleeding from tissue  
**Question**: "Does this intraoperative image show evidence of a surgical complication?"  
**Answer**: A. Complication present  
**Rationale**: Image demonstrates active hemorrhage requiring immediate hemostatic intervention and surgical control

### Example 2: Bowel Perforation
**Image**: Laparoscopic view showing inadvertent intestinal injury  
**Question**: "Does this intraoperative image show evidence of a surgical complication?"  
**Answer**: A. Complication present  
**Rationale**: Image shows bowel perforation with visible defect requiring immediate repair and possible conversion

### Example 3: Normal Procedure
**Image**: Standard laparoscopic view with appropriate hemostasis and tissue handling  
**Question**: "Does this intraoperative image show evidence of a surgical complication?"  
**Answer**: B. No complication  
**Rationale**: Surgical field appears normal with appropriate tissue handling and no evidence of adverse events

### Example 4: Thermal Injury
**Image**: Surgical field showing tissue damage from electrocautery  
**Question**: "Does this intraoperative image show evidence of a surgical complication?"  
**Answer**: A. Complication present  
**Rationale**: Image demonstrates thermal injury to adjacent tissue from electrocautery, requiring assessment and possible intervention

### Example 5: Routine Dissection
**Image**: Standard surgical dissection with controlled tissue planes  
**Question**: "Does this intraoperative image show evidence of a surgical complication?"  
**Answer**: B. No complication  
**Rationale**: Image shows routine surgical dissection with appropriate tissue handling and hemostasis

## Implementation Notes

### Technical Considerations
- Implement abnormality detection algorithms for various complication types
- Consider different surgical approaches and anatomical regions
- Account for varying severity levels and presentation patterns
- Handle emergency scenarios requiring immediate recognition

### Clinical Validation
- Align with established complication classification systems
- Cross-reference with surgical quality and safety standards
- Validate against expert surgeon complication assessment
- Consider malpractice and quality improvement implications

### Dataset-Specific Adaptations
- **Procedure-specific datasets**: Focus on relevant complications for each procedure type
- **Emergency datasets**: Emphasize immediate recognition and intervention needs
- **Training datasets**: Include educational examples of common complications
- **Quality datasets**: Support quality improvement and safety initiatives

### Quality Assurance
- Regular validation by experienced surgeons across multiple specialties
- Cross-reference with surgical complication literature and guidelines
- Monitoring for accuracy across different complication types and procedures
- Updates based on evolving understanding of surgical complications and prevention strategies
