# Surgery Tissue Type Assessment in Surgical Context Template

## Template Overview

**Template ID**: `surgery_classification_multiclass_easy_4`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Intraoperative tissue condition evaluation  
**Domain**: Surgery (intraoperative imaging)

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about tissue conditions and types visible in surgical fields. This assessment is critical for surgical decision-making and tissue handling strategies during procedures.

The template is designed for surgery datasets with tissue condition annotations, testing the model's ability to evaluate tissue characteristics relevant to surgical manipulation and clinical outcomes.

## Question Generation Pattern

### Question Format
```
"What type of tissue condition is being manipulated in this surgical field?"
```

### Answer Format
Multiclass choice with tissue condition options:
- A. Healthy tissue
- B. Inflamed tissue
- C. Fibrotic tissue
- D. Necrotic tissue
- E. Tumor tissue
- F. Infected tissue
- G. Hemorrhagic tissue

### Template Variables
- `{tissue_characteristics}`: Visual appearance and morphological features
- `{pathological_changes}`: Disease-related tissue alterations
- `{surgical_implications}`: Impact on surgical technique and handling
- `{clinical_context}`: Underlying pathology and patient condition

### Clinical Context
- **Healthy Tissue**: Normal appearance, good vascularity, appropriate texture
- **Inflamed Tissue**: Erythema, edema, hypervascularity, friable texture
- **Fibrotic Tissue**: Dense, white, contracted appearance with poor vascularity
- **Necrotic Tissue**: Discolored, devitalized tissue requiring debridement
- **Tumor Tissue**: Abnormal growth with altered vascularity and texture
- **Infected Tissue**: Purulent material, abnormal coloration, poor viability
- **Hemorrhagic Tissue**: Active bleeding, hematoma formation, vascular injury

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What type of tissue condition is being manipulated in this surgical field?",
  "answer": "B",
  "answer_type": "single_label",
  "options": [
    "Healthy tissue",
    "Inflamed tissue",
    "Fibrotic tissue",
    "Necrotic tissue",
    "Tumor tissue",
    "Infected tissue",
    "Hemorrhagic tissue"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.85,
  "rationale": "Tissue shows erythema, edema, and hypervascularity consistent with inflammatory changes",
  "provenance": {
    "original_label": "inflamed",
    "rule_id": "surgery_classification_multiclass_easy_4",
    "annotation_id": "tissue_condition",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Intraoperative images showing tissue with various pathological conditions
- **Labels**: Tissue condition annotations with pathological context
- **Quality**: Clear visualization of tissue characteristics and abnormalities

### Compatible Datasets
- Surgical pathology assessment datasets
- Intraoperative tissue evaluation collections
- Disease-specific surgical datasets
- Pathological tissue recognition sets
- Surgical decision-making databases

### Minimum Standards
- **Image Quality**: Sufficient detail for tissue condition assessment
- **Annotation Quality**: Expert validation by surgeons and pathologists
- **Data Distribution**: Representative coverage of common tissue conditions

## Template Usage Rules

### Question Construction Rules
1. Focus on tissue characteristics relevant to surgical decision-making
2. Use clinical terminology describing tissue conditions
3. Consider pathological context and surgical implications
4. Emphasize conditions affecting surgical technique

### Answer Assignment Rules
1. Map normal-appearing tissue → "Healthy tissue"
2. Map erythematous, edematous tissue → "Inflamed tissue"
3. Map dense, white, contracted tissue → "Fibrotic tissue"
4. Map discolored, devitalized tissue → "Necrotic tissue"
5. Map abnormal growths → "Tumor tissue"
6. Map purulent, infected areas → "Infected tissue"
7. Map bleeding, vascular injury → "Hemorrhagic tissue"

### Quality Control Guidelines
1. Ensure accurate tissue condition assessment
2. Verify clinical relevance to surgical decision-making
3. Cross-validate with expert surgical and pathological opinion
4. Review for educational and training value

## Examples

### Example 1: Acute Cholecystitis
**Image**: Laparoscopic view showing erythematous, edematous gallbladder wall  
**Question**: "What type of tissue condition is being manipulated in this surgical field?"  
**Answer**: B. Inflamed tissue  
**Rationale**: Gallbladder shows characteristic signs of acute inflammation with erythema, edema, and hypervascularity

### Example 2: Normal Hepatic Parenchyma
**Image**: Surgical view showing smooth, well-vascularized liver surface  
**Question**: "What type of tissue condition is being manipulated in this surgical field?"  
**Answer**: A. Healthy tissue  
**Rationale**: Liver tissue demonstrates normal color, texture, and vascularity without pathological changes

### Example 3: Chronic Adhesions
**Image**: Surgical view showing dense, white fibrous bands  
**Question**: "What type of tissue condition is being manipulated in this surgical field?"  
**Answer**: C. Fibrotic tissue  
**Rationale**: Tissue shows characteristic dense, white, fibrotic adhesions requiring careful dissection techniques

### Example 4: Hepatic Tumor
**Image**: Surgical view showing abnormal mass with altered vascularity  
**Question**: "What type of tissue condition is being manipulated in this surgical field?"  
**Answer**: E. Tumor tissue  
**Rationale**: Tissue demonstrates abnormal growth pattern with altered vascularity and texture consistent with neoplasm

### Example 5: Active Bleeding
**Image**: Surgical field showing active hemorrhage from tissue surface  
**Question**: "What type of tissue condition is being manipulated in this surgical field?"  
**Answer**: G. Hemorrhagic tissue  
**Rationale**: Tissue shows active bleeding requiring immediate hemostatic intervention and careful handling

## Implementation Notes

### Technical Considerations
- Implement tissue texture and color analysis algorithms
- Consider lighting variations and camera settings
- Account for different pathological processes and presentations
- Handle varying degrees of tissue alteration

### Clinical Validation
- Align with surgical pathology standards
- Cross-reference with intraoperative assessment guidelines
- Validate against expert surgeon and pathologist evaluation
- Consider clinical correlation with patient history

### Dataset-Specific Adaptations
- **Disease-specific datasets**: Focus on relevant pathological conditions
- **Emergency datasets**: Emphasize acute conditions requiring immediate recognition
- **Cancer datasets**: Include various tumor presentations and characteristics
- **Inflammatory datasets**: Cover acute and chronic inflammatory changes

### Quality Assurance
- Regular validation by surgeons experienced in intraoperative assessment
- Cross-reference with pathological diagnosis when available
- Monitoring for accuracy across different pathological conditions
- Updates based on evolving understanding of tissue pathology and surgical techniques
