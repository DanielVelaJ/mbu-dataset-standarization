# Ordinal Classification Template 2: Stage Progression Assessment

## Template Overview

**Template ID**: `classification_ordinal_2`  
**Task Type**: Ordinal Classification  
**Difficulty**: Easy  
**Question Pattern**: Disease staging and progression assessment with ordered multiple choice options  

## Template Description

This template converts ordinal classification datasets into MCVQA format by asking about disease stages or progression levels with ordered multiple choice options. It focuses specifically on temporal progression and disease advancement, making it ideal for cancer staging, disease progression monitoring, and pathological staging systems.

The template emphasizes the progressive nature of disease stages, supporting clinical workflows that require understanding of disease advancement for treatment planning and prognosis assessment.

## Question Generation Pattern

### Question Format
```
"Which stage of {condition} is demonstrated in this {modality} image?"
```

### Answer Format
Multiple choice options with ordered stage progression:
- A. {Stage I/Early description}
- B. {Stage II/Moderate description}
- C. {Stage III/Advanced description}  
- D. {Stage IV/Late description}
- E. {Stage V/End-stage description} (if applicable)

### Template Variables
- `{condition}`: The medical condition or disease being staged (e.g., "cancer", "kidney disease", "heart failure", "liver disease")
- `{modality}`: The imaging modality (e.g., "CT", "MRI", "ultrasound", "chest X-ray", "PET scan")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Which stage of {condition} is demonstrated in this {modality} image?",
  "answer": "{selected_option_letter}",
  "answer_type": "single_label",
  "options": [
    "A. Stage I ({early_description})",
    "B. Stage II ({moderate_description})", 
    "C. Stage III ({advanced_description})",
    "D. Stage IV ({late_description})",
    "E. Stage V ({end_stage_description})"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Disease staging based on established clinical staging criteria",
  "provenance": {
    "original_label": "{original_stage_value}",
    "rule_id": "classification_ordinal_2",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Ordinal classification with disease staging or progression labels
- **Staging Systems**: Established clinical staging criteria (TNM, AJCC, CKD stages, etc.)
- **Progressive Labels**: Clear progression from early to late stages
- **Medical Context**: Disease conditions with recognized staging systems

## Template Usage Rules

1. **Stage Ordering**: Maintain correct chronological/severity progression in options
2. **Clinical Terminology**: Use standard medical staging terminology and criteria
3. **Complete Staging**: Include all relevant stages present in the dataset
4. **Clear Descriptions**: Provide meaningful stage descriptions that clinicians recognize
5. **Progression Logic**: Ensure stage progression reflects actual disease advancement

## Examples

### Example 1: Lung Cancer TNM Staging
**Original Dataset**: Lung Cancer CT Staging  
**Original Label**: 3 (Stage III)  
**Generated Q&A**:
- **Question**: "Which stage of lung cancer is demonstrated in this chest CT image?"
- **Options**:
  - A. Stage I (Early localized cancer)
  - B. Stage II (Locally advanced cancer)
  - C. Stage III (Regional lymph node involvement)
  - D. Stage IV (Distant metastases)
- **Answer**: "C"
- **Rationale**: "Stage III lung cancer with mediastinal lymph node involvement but no distant metastases"

### Example 2: Chronic Kidney Disease Progression
**Original Dataset**: Renal Ultrasound CKD Staging  
**Original Label**: 4 (Stage 4 CKD)  
**Generated Q&A**:
- **Question**: "Which stage of chronic kidney disease is demonstrated in this renal ultrasound image?"
- **Options**:
  - A. Stage 1 (Normal kidney function)
  - B. Stage 2 (Mild dysfunction)
  - C. Stage 3 (Moderate dysfunction)
  - D. Stage 4 (Severe dysfunction)
  - E. Stage 5 (Kidney failure)
- **Answer**: "D"
- **Rationale**: "Severe reduction in kidney function with significant parenchymal changes"

### Example 3: Alzheimer's Disease Progression
**Original Dataset**: Brain MRI Alzheimer's Staging  
**Original Label**: 2 (Moderate cognitive decline)  
**Generated Q&A**:
- **Question**: "Which stage of Alzheimer's disease is demonstrated in this brain MRI image?"
- **Options**:
  - A. Stage 1 (No cognitive decline)
  - B. Stage 2 (Mild cognitive decline)
  - C. Stage 3 (Moderate cognitive decline)
  - D. Stage 4 (Severe cognitive decline)
- **Answer**: "C"
- **Rationale**: "Moderate hippocampal atrophy consistent with moderate Alzheimer's progression"

### Example 4: Liver Cirrhosis Child-Pugh Classification
**Original Dataset**: Liver CT Cirrhosis Staging  
**Original Label**: 2 (Child-Pugh B)  
**Generated Q&A**:
- **Question**: "Which stage of liver cirrhosis is demonstrated in this abdominal CT image?"
- **Options**:
  - A. Child-Pugh A (Compensated cirrhosis)
  - B. Child-Pugh B (Moderately decompensated)
  - C. Child-Pugh C (Severely decompensated)
- **Answer**: "B"
- **Rationale**: "Moderately decompensated cirrhosis with ascites and portal hypertension"

### Example 5: Breast Cancer Staging
**Original Dataset**: Breast MRI Cancer Staging  
**Original Label**: 1 (Stage I)  
**Generated Q&A**:
- **Question**: "Which stage of breast cancer is demonstrated in this breast MRI image?"
- **Options**:
  - A. Stage 0 (Carcinoma in situ)
  - B. Stage I (Small invasive cancer)
  - C. Stage II (Locally advanced cancer)
  - D. Stage III (Regional spread)
  - E. Stage IV (Distant metastases)
- **Answer**: "B"
- **Rationale**: "Small invasive ductal carcinoma confined to breast tissue without lymph node involvement"

## Implementation Notes

### Advantages
- **Progression Awareness**: Captures temporal and severity progression essential for clinical decision-making
- **Staging Compatibility**: Aligns with established medical staging systems used in clinical practice
- **Treatment Planning**: Supports clinical workflows requiring stage-based treatment decisions
- **Prognosis Assessment**: Enables severity-based prognosis and outcome prediction

### Limitations
- **Staging System Dependency**: Requires datasets with established staging criteria
- **Complexity Variation**: Different staging systems may have varying complexity levels
- **Temporal Requirements**: Best suited for diseases with clear progression patterns

### Quality Considerations
- Ensure stage progression accurately reflects clinical disease advancement
- Use terminology consistent with established medical staging guidelines
- Verify that stage descriptions match clinical definitions and criteria
- Confirm that options cover the full range of stages present in the dataset
- Validate compatibility with specific staging systems used in different medical domains
