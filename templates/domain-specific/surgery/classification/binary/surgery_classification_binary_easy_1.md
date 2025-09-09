# Surgery Critical View of Safety Achievement Template

## Template Overview

**Template ID**: `surgery_classification_binary_easy_1`  
**Task Type**: Binary classification  
**Difficulty**: Easy  
**Question Pattern**: Critical view of safety assessment  
**Medical Domain**: Surgery (laparoscopic cholecystectomy)  
**Domain-knowledge summary**: Requires specialized surgical knowledge of laparoscopic cholecystectomy anatomy and safety protocols. Must understand Calot's triangle anatomy, critical view of safety criteria (clear identification of hepatocystic triangle with only two structures - cystic artery and cystic duct - entering the gallbladder), and ability to assess surgical safety landmarks to prevent bile duct injury during gallbladder removal.

## Template Description

This template converts binary classification datasets into MCVQA format by asking questions about the achievement of critical view of safety in laparoscopic cholecystectomy images. This assessment is essential for preventing bile duct injury, representing a fundamental safety checkpoint in gallbladder surgery.

The template is designed for surgery datasets with critical view annotations, testing the model's ability to recognize the specific anatomical criteria required for safe gallbladder dissection.

## Question Generation Pattern

### Question Format
```
"Has the critical view of safety been achieved in this laparoscopic cholecystectomy image?"
```

### Answer Format
Binary choice with safety assessment options:
- A. Critical view achieved
- B. Critical view not achieved

### Template Variables
- `{anatomical_landmarks}`: Specific structures required for critical view
- `{dissection_quality}`: Completeness of tissue plane development
- `{visibility_criteria}`: Clear identification of required structures
- `{safety_confirmation}`: Verification of safe anatomical relationships

### Clinical Context
- **Critical View Criteria**: Clear view of hepatocystic triangle, identification of only two structures entering gallbladder, liver bed clearance
- **Safety Importance**: Prevents bile duct injury, ensures proper structure identification
- **Anatomical Requirements**: Calot's triangle cleared, artery and duct isolated, no extra structures
- **Clinical Standard**: Gold standard safety checkpoint in laparoscopic cholecystectomy

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Has the critical view of safety been achieved in this laparoscopic cholecystectomy image?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Critical view achieved",
    "Critical view not achieved"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.95,
  "rationale": "Image shows clear hepatocystic triangle with only two structures entering gallbladder and cleared liver bed, meeting critical view criteria",
  "provenance": {
    "original_label": "critical_view_achieved",
    "rule_id": "surgery_classification_binary_easy_1",
    "annotation_id": "critical_view_assessment",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Laparoscopic cholecystectomy images showing hepatocystic triangle
- **Labels**: Binary labels indicating critical view achievement status
- **Quality**: Clear visualization of anatomical structures and dissection planes

### Compatible Datasets
- Laparoscopic cholecystectomy safety datasets
- Critical view assessment collections
- Surgical safety training databases
- Gallbladder surgery evaluation sets
- Hepatobiliary surgery safety archives

### Minimum Standards
- **Image Quality**: Sufficient resolution for anatomical detail assessment
- **Annotation Quality**: Expert surgeon validation familiar with critical view criteria
- **Data Distribution**: Representative examples of achieved and non-achieved states

## Template Usage Rules

### Question Construction Rules
1. Reference specific critical view of safety terminology
2. Focus on laparoscopic cholecystectomy context
3. Emphasize safety assessment and injury prevention
4. Use established surgical safety standards

### Answer Assignment Rules
1. Map complete critical view criteria → "Critical view achieved"
2. Map incomplete or unclear criteria → "Critical view not achieved"
3. Require all three criteria: cleared triangle, two structures only, liver bed visibility
4. Use conservative assessment for patient safety

### Quality Control Guidelines
1. Ensure strict adherence to established critical view criteria
2. Verify anatomical accuracy and safety assessment
3. Cross-validate with expert laparoscopic surgeons
4. Review for educational and safety training value

## Examples

### Example 1: Complete Critical View
**Image**: Clear laparoscopic view showing perfectly dissected Calot's triangle  
**Question**: "Has the critical view of safety been achieved in this laparoscopic cholecystectomy image?"  
**Answer**: A. Critical view achieved  
**Rationale**: Image demonstrates cleared hepatocystic triangle with only cystic artery and duct visible entering gallbladder, with clear liver bed view

### Example 2: Incomplete Dissection
**Image**: Laparoscopic view with partially dissected triangle and unclear structures  
**Question**: "Has the critical view of safety been achieved in this laparoscopic cholecystectomy image?"  
**Answer**: B. Critical view not achieved  
**Rationale**: Hepatocystic triangle dissection is incomplete with unclear structure identification and persistent tissue obscuring anatomy

### Example 3: Optimal Safety View
**Image**: Laparoscopic image showing textbook critical view anatomy  
**Question**: "Has the critical view of safety been achieved in this laparoscopic cholecystectomy image?"  
**Answer**: A. Critical view achieved  
**Rationale**: Perfect demonstration of critical view with clear identification of only two structures and completely cleared liver bed

### Example 4: Inadequate Exposure
**Image**: Laparoscopic view with poor visualization and multiple unclear structures  
**Question**: "Has the critical view of safety been achieved in this laparoscopic cholecystectomy image?"  
**Answer**: B. Critical view not achieved  
**Rationale**: Poor anatomical exposure with multiple structures in triangle area preventing safe identification of critical anatomy

### Example 5: Borderline Assessment
**Image**: Laparoscopic view with mostly adequate but not perfect critical view  
**Question**: "Has the critical view of safety been achieved in this laparoscopic cholecystectomy image?"  
**Answer**: B. Critical view not achieved  
**Rationale**: While dissection is advanced, not all critical view criteria are completely satisfied, requiring further dissection for safety

## Implementation Notes

### Technical Considerations
- Implement specific anatomical feature recognition for critical view criteria
- Consider viewing angle and laparoscopic camera positioning
- Account for individual anatomical variations
- Handle different laparoscopic equipment and image quality

### Clinical Validation
- Align with Society of American Gastrointestinal and Endoscopic Surgeons (SAGES) guidelines
- Cross-reference with established critical view teaching materials
- Validate against expert laparoscopic surgeon assessment
- Consider international surgical safety standards

### Dataset-Specific Adaptations
- **Training datasets**: Emphasize clear examples of achieved vs non-achieved states
- **Safety datasets**: Focus on injury prevention and risk reduction
- **Assessment datasets**: Include challenging cases requiring expert judgment
- **Educational datasets**: Provide comprehensive examples for surgical training

### Quality Assurance
- Regular validation by experienced laparoscopic surgeons
- Cross-reference with surgical safety literature and guidelines
- Monitoring for consistency with established safety standards
- Updates based on evolving surgical safety recommendations and techniques
