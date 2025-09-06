# Binary Classification Template 6: Clear Evidence Assessment

## Template Overview

**Template ID**: `classification_binary_6`  
**Task Type**: Binary Classification  
**Difficulty**: Easy-Medium  
**Question Pattern**: Evidence-based diagnostic assessment with confidence emphasis  

## Template Description

This template converts binary classification datasets into MCVQA format by asking whether there is clear evidence of a medical condition in imaging studies. It emphasizes the strength and clarity of diagnostic evidence, testing the model's ability to distinguish between definitive findings and uncertain or ambiguous cases. This approach mirrors clinical decision-making where evidence quality is as important as evidence presence.

## Question Generation Pattern

### Question Format
```
"Is there clear evidence of {condition} in this {modality} image?"
```

### Answer Format
- **Positive cases**: "Yes, clear evidence"
- **Negative cases**: "No clear evidence"

### Template Variables
- `{condition}`: The medical condition or finding being assessed for evidence clarity
- `{modality}`: The imaging modality (e.g., "chest X-ray", "MRI scan", "fundus photograph")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Is there clear evidence of {condition} in this {modality} image?",
  "answer": "Yes, clear evidence" | "No clear evidence",
  "answer_type": "single_label",
  "options": ["Yes, clear evidence", "No clear evidence"],
  "difficulty": "medium",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Evidence-based diagnostic assessment with emphasis on clarity",
  "provenance": {
    "original_label": "{original_label_value}",
    "rule_id": "classification_binary_6",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels where evidence quality can be meaningfully assessed
- **Clinical Context**: Diagnostic scenarios where evidence clarity is clinically relevant
- **Image Quality**: Sufficient image quality to assess evidence clarity

## Template Usage Rules

1. **Evidence Mapping**:
   - **Positive Cases (Label = 1)**: "Yes, clear evidence"
   - **Negative Cases (Label = 0)**: "No clear evidence"
2. **Clarity Emphasis**: Focus on the strength and definitiveness of diagnostic evidence
3. **Condition Specificity**: Use specific medical condition names
4. **Conservative Interpretation**: "Clear evidence" should indicate high diagnostic confidence

## Examples

### Example 1: Chest X-ray Pneumonia Evidence
**Original Dataset**: ChestX-ray14 Pneumonia subset  
**Original Label**: 1 (pneumonia present)  
**Generated Q&A**:
- **Question**: "Is there clear evidence of pneumonia in this chest X-ray image?"
- **Answer**: "Yes, clear evidence"
- **Rationale**: "Consolidation and infiltrates provide clear evidence of pneumonia"

### Example 2: Brain MRI Stroke Evidence
**Original Dataset**: Acute stroke detection  
**Original Label**: 0 (no stroke)  
**Generated Q&A**:
- **Question**: "Is there clear evidence of acute stroke in this brain MRI image?"
- **Answer**: "No clear evidence"
- **Rationale**: "MRI shows no clear evidence of acute ischemic changes"

### Example 3: Fundus Diabetic Retinopathy Evidence
**Original Dataset**: Diabetic Retinopathy Detection  
**Original Label**: 1 (diabetic retinopathy present)  
**Generated Q&A**:
- **Question**: "Is there clear evidence of diabetic retinopathy in this fundus photograph?"
- **Answer**: "Yes, clear evidence"
- **Rationale**: "Microaneurysms and hemorrhages provide clear evidence of diabetic retinopathy"

### Example 4: Skin Lesion Melanoma Evidence
**Original Dataset**: ISIC Melanoma Classification  
**Original Label**: 0 (benign lesion)  
**Generated Q&A**:
- **Question**: "Is there clear evidence of melanoma in this skin lesion image?"
- **Answer**: "No clear evidence"
- **Rationale**: "Dermoscopic features do not provide clear evidence of melanoma"

### Example 5: Chest CT Pulmonary Embolism Evidence
**Original Dataset**: Pulmonary embolism detection  
**Original Label**: 1 (pulmonary embolism present)  
**Generated Q&A**:
- **Question**: "Is there clear evidence of pulmonary embolism in this chest CT image?"
- **Answer**: "Yes, clear evidence"
- **Rationale**: "Filling defects in pulmonary arteries provide clear evidence of embolism"

## Implementation Notes

### Advantages
- **Evidence-Based**: Emphasizes the quality and strength of diagnostic evidence
- **Clinical Alignment**: Mirrors how clinicians assess diagnostic confidence
- **Educational Value**: Teaches distinction between presence and clear evidence
- **Confidence Testing**: Tests model's ability to assess diagnostic certainty
- **Conservative Approach**: Encourages high standards for positive diagnosis

### Limitations
- **Subjectivity**: "Clear evidence" may be interpreted differently by different observers
- **Binary Constraint**: May oversimplify cases with moderate or equivocal evidence
- **Context Dependency**: Evidence clarity may vary with clinical setting and urgency
- **Image Quality Dependency**: Poor image quality may affect evidence assessment

### Quality Considerations
- **Evidence Standards**: Establish clear criteria for what constitutes "clear evidence"
- **Clinical Validation**: Ensure evidence thresholds align with expert clinical judgment
- **Consistency**: Maintain consistent evidence standards across similar cases
- **Image Quality**: Consider image quality when assessing evidence clarity

### Clinical Context Guidelines
- **Diagnostic settings**: Most appropriate for formal diagnostic evaluations
- **Evidence-based medicine**: Aligns with evidence-based clinical practice
- **Quality assurance**: Useful for ensuring high diagnostic standards
- **Training applications**: Excellent for teaching evidence assessment skills

### Evidence Assessment Criteria

#### Clear Evidence Indicators:
- **Pathognomonic findings**: Classic, characteristic features of the condition
- **Multiple confirmatory signs**: Several findings supporting the same diagnosis
- **High-quality visualization**: Clear, unambiguous imaging findings
- **Consensus features**: Findings that would be recognized by most experts

#### No Clear Evidence Indicators:
- **Absence of findings**: No diagnostic features present
- **Equivocal findings**: Ambiguous or borderline abnormalities
- **Poor visualization**: Technical factors limiting diagnostic confidence
- **Alternative explanations**: Findings better explained by other conditions

### Implementation Strategy
- **Expert consensus**: Use expert panels to define "clear evidence" criteria
- **Threshold calibration**: Calibrate evidence thresholds using expert annotations
- **Quality control**: Regular review of cases to ensure consistent evidence standards
- **Training focus**: Emphasize evidence quality during model training

### Clinical Decision Support
- **High confidence cases**: "Yes, clear evidence" indicates high diagnostic confidence
- **Uncertain cases**: "No clear evidence" may require additional evaluation
- **Follow-up guidance**: Results should guide need for further testing or specialist referral
- **Risk stratification**: Evidence clarity can inform clinical risk assessment
