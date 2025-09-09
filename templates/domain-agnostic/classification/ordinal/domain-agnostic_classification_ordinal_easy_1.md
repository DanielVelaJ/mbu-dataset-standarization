# Ordinal Classification Template 1: Basic Severity Assessment

## Template Overview

**Template ID**: `domain-agnostic_classification_ordinal_easy_1`  
**Task Type**: Ordinal classification  
**Difficulty**: Easy  
**Question Pattern**: Severity/stage assessment with ordered multiple choice options  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires understanding of medical grading systems and disease progression. Knowledge of ordinal relationships in medical assessment, staging criteria, and ability to distinguish between severity levels based on visual indicators across different medical domains.  

## Template Description

This template converts ordinal classification datasets into MCVQA format by asking about severity grades or disease stages with ordered multiple choice options. It is designed for datasets where images have ordered labels representing progression of severity, stage, or grade (e.g., Grade 0 < Grade 1 < Grade 2 < Grade 3).

The template preserves the ordering relationship inherent in medical grading systems, making it suitable for clinical assessment tasks where the sequence of severity matters for diagnosis and treatment planning.

## Question Generation Pattern

### Question Format
```
"What {severity_type} is shown in this {modality} image?"
```

### Answer Format
Multiple choice options with ordered severity levels:
- A. {Grade/Stage 0 description}
- B. {Grade/Stage 1 description}
- C. {Grade/Stage 2 description}
- D. {Grade/Stage 3 description}
- E. {Grade/Stage 4 description} (if applicable)

### Template Variables
- `{severity_type}`: The specific grading system being assessed (e.g., "diabetic retinopathy grade", "BI-RADS category", "liver fibrosis stage")
- `{modality}`: The imaging modality (e.g., "fundus", "mammography", "ultrasound", "CT", "MRI")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What {severity_type} is shown in this {modality} image?",
  "answer": "{selected_option_letter}",
  "answer_type": "single_label",
  "options": [
    "A. Grade 0 (No {condition})",
    "B. Grade 1 (Mild {condition})", 
    "C. Grade 2 (Moderate {condition})",
    "D. Grade 3 (Severe {condition})",
    "E. Grade 4 (Advanced {condition})"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Ordinal classification based on established medical grading scale",
  "provenance": {
    "original_label": "{original_ordinal_value}",
    "rule_id": "classification_ordinal_1",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Ordinal classification with ordered severity/stage labels
- **Label Structure**: Ordered categorical labels (3-8 levels typical)
- **Medical Grading**: Established clinical grading systems (BI-RADS, diabetic retinopathy, fibrosis staging, etc.)
- **Clear Progression**: Meaningful order between categories representing increasing severity

## Template Usage Rules

1. **Preserve Order**: Options must maintain the correct ordering of severity levels
2. **Medical Terminology**: Use established medical grading terminology from the dataset
3. **Complete Scale**: Include all severity levels present in the dataset
4. **Option Format**: Use clear letter labels (A, B, C, D, E) with descriptive text
5. **Label Mapping**: Map original ordinal values to appropriate option letters maintaining order

## Examples

### Example 1: Diabetic Retinopathy Grading
**Original Dataset**: EyePACS Diabetic Retinopathy Detection  
**Original Label**: 2 (Moderate NPDR)  
**Generated Q&A**:
- **Question**: "What diabetic retinopathy grade is shown in this fundus image?"
- **Options**: 
  - A. Grade 0 (No DR)
  - B. Grade 1 (Mild NPDR)
  - C. Grade 2 (Moderate NPDR)
  - D. Grade 3 (Severe NPDR)  
  - E. Grade 4 (Proliferative DR)
- **Answer**: "C"
- **Rationale**: "Moderate non-proliferative diabetic retinopathy identified with microaneurysms and hemorrhages"

### Example 2: BI-RADS Mammography Assessment
**Original Dataset**: Mammography BI-RADS Classification  
**Original Label**: 4 (Suspicious abnormality)  
**Generated Q&A**:
- **Question**: "What BI-RADS category is shown in this mammography image?"
- **Options**:
  - A. BI-RADS 1 (Negative)
  - B. BI-RADS 2 (Benign finding)
  - C. BI-RADS 3 (Probably benign)
  - D. BI-RADS 4 (Suspicious abnormality)
  - E. BI-RADS 5 (Highly suspicious)
- **Answer**: "D"
- **Rationale**: "Suspicious mammographic findings requiring tissue sampling for diagnosis"

### Example 3: Liver Fibrosis Staging
**Original Dataset**: Liver Fibrosis Ultrasound Assessment  
**Original Label**: 3 (Advanced fibrosis)  
**Generated Q&A**:
- **Question**: "What liver fibrosis stage is shown in this ultrasound image?"
- **Options**:
  - A. F0 (No fibrosis)
  - B. F1 (Minimal fibrosis)
  - C. F2 (Moderate fibrosis)
  - D. F3 (Advanced fibrosis)
  - E. F4 (Cirrhosis)
- **Answer**: "D"
- **Rationale**: "Advanced hepatic fibrosis with significant architectural distortion"

### Example 4: Heart Failure Severity Assessment
**Original Dataset**: Echocardiography Heart Failure Grading  
**Original Label**: 1 (Mild heart failure)  
**Generated Q&A**:
- **Question**: "What heart failure severity is shown in this echocardiography image?"
- **Options**:
  - A. Grade 0 (Normal function)
  - B. Grade 1 (Mild heart failure)
  - C. Grade 2 (Moderate heart failure)
  - D. Grade 3 (Severe heart failure)
- **Answer**: "B"
- **Rationale**: "Mild systolic dysfunction with preserved ejection fraction"

### Example 5: Osteoarthritis Joint Degeneration
**Original Dataset**: Knee X-ray Osteoarthritis Grading  
**Original Label**: 2 (Moderate OA)  
**Generated Q&A**:
- **Question**: "What osteoarthritis grade is shown in this knee X-ray image?"
- **Options**:
  - A. Grade 0 (Normal joint)
  - B. Grade 1 (Mild OA)
  - C. Grade 2 (Moderate OA)
  - D. Grade 3 (Severe OA)
  - E. Grade 4 (End-stage OA)
- **Answer**: "C"
- **Rationale**: "Moderate joint space narrowing with osteophyte formation"

## Implementation Notes

### Advantages
- **Clinically Meaningful**: Preserves medical grading relationships essential for staging and prognosis
- **Ordered Assessment**: Maintains severity progression crucial for treatment decisions
- **Standardized Scales**: Uses established medical grading systems familiar to clinicians
- **Cross-Domain**: Applicable across medical specialties with ordinal grading systems

### Limitations
- **Requires Ordinal Data**: Not suitable for nominal categorical or binary classification
- **Scale Dependency**: Limited to datasets with established medical grading systems
- **Order Sensitivity**: Incorrect option ordering would compromise clinical validity

### Quality Considerations
- Ensure option ordering correctly reflects medical severity progression
- Use exact terminology from established clinical grading scales
- Verify all severity levels from the dataset are represented in options
- Validate that generated questions align with clinical assessment practices
- Confirm answer mappings preserve the ordinal relationship
