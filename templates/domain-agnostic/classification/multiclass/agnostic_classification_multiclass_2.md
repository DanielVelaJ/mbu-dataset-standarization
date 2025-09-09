# Multi-Class Classification Template 2: Disease Stage/Severity Grading

## Template Overview

- **Template ID**: agnostic_classification_multiclass_2
- **Task Type**: Multi-class classification (ordinal grading)
- **Difficulty**: Easy
- **Pattern**: Disease severity or stage assessment with ordered scale options
- **Domain**: Domain-agnostic (works across all medical specialties)

## Template Description

This template converts multi-class medical datasets with ordered/ordinal labels into MCVQA format by asking about disease severity, staging, or grading. The template presents multiple severity levels or stages as answer options, where exactly one level represents the correct assessment. This approach mirrors clinical grading and staging scenarios where medical professionals must assess disease progression or severity on established scales.

The template is specifically designed for datasets that have ordered classifications such as disease stages (0, I, II, III, IV), severity grades (mild, moderate, severe), or standardized clinical scales (BIRADS 1-5, diabetic retinopathy grades 0-4). The ordered nature of the labels provides clinical meaning where higher grades typically indicate more severe or advanced disease.

## Question Generation Pattern

### Question Format
`"What {assessment_type} is shown in this {modality} image?"`

### Answer Format
Multiple choice with options A, B, C, D, etc. representing ordered severity/stage levels

### Template Variables
- `{assessment_type}`: Type of grading (e.g., "stage", "grade", "severity level", "BIRADS category")
- `{modality}`: Imaging modality (e.g., "mammography", "fundus", "histopathology", "MRI")
- `{condition}`: Specific condition being graded (e.g., "diabetic retinopathy", "breast lesion", "cancer")

### Example Pattern
```
Question: "What diabetic retinopathy severity grade is shown in this fundus image?"
A. No diabetic retinopathy (Grade 0)
B. Mild diabetic retinopathy (Grade 1)
C. Moderate diabetic retinopathy (Grade 2)
D. Severe diabetic retinopathy (Grade 3)
E. Proliferative diabetic retinopathy (Grade 4)
```

## Mapping to Datum Schema

```json
{
  "questions-and-answers": [
    {
      "qa_id": "1",
      "task": "Classification",
      "question": "What {assessment_type} is shown in this {modality} image?",
      "answer": "{correct_grade_label}",
      "answer_type": "single_label",
      "options": ["{grade_1}", "{grade_2}", "{grade_3}", "{grade_4}", "{grade_5}"],
      "difficulty": "easy",
      "uncertainty": "certain",
      "answer_confidence": 1.0,
      "rationale": "Disease stage/severity grading using original dataset ordinal labels",
      "provenance": {
        "original_label": "{dataset_original_grade}",
        "rule_id": "agnostic_classification_multiclass_2",
        "annotation_id": null,
        "created_by": "program"
      }
    }
  ]
}
```

## Dataset Requirements

### Essential Requirements
- **Ordinal labels**: Dataset must have 3+ ordered stages/grades/severity levels
- **Single grade per image**: Each image must have exactly one severity/stage label
- **Clinical staging system**: Labels must represent established medical grading scales
- **Imaging data**: Dataset must contain medical images appropriate for grading

### Compatible Dataset Types
- Diabetic retinopathy grading datasets (grades 0-4)
- Cancer staging datasets (stages I-IV)
- BIRADS mammography classification (categories 1-5)
- Glaucoma severity grading datasets
- Alzheimer's disease staging (CDR scales)
- Osteoarthritis grading (Kellgren-Lawrence grades)

### Label Format Compatibility
- Numeric grades (0, 1, 2, 3, 4)
- Roman numeral stages (I, II, III, IV)
- Descriptive severity levels (mild, moderate, severe)
- Standardized clinical scales (BIRADS, CDR, etc.)

## Template Usage Rules

### Implementation Guidelines
1. **Preserve Order**: Always present options in natural progression order (lowest to highest severity)
2. **Include Descriptors**: Combine numeric grades with descriptive labels when available
3. **Clinical Standards**: Use established medical grading terminology and scales
4. **Complete Scale**: Include all possible grades/stages from the dataset

### Quality Requirements
- All grade/stage labels must follow established clinical standards
- Maintain consistent terminology throughout option set
- Ensure each grade represents a clinically meaningful distinction
- Verify that ordinal progression is medically accurate

### Domain Adaptation
- **Ophthalmology**: Use standard scales (DR severity, glaucoma staging)
- **Oncology**: Follow TNM staging or histological grading systems
- **Radiology**: Apply modality-specific grading scales (BIRADS, PI-RADS)
- **Pathology**: Use histological grading standards (tumor grades, fibrosis stages)

## Examples

### Example 1: Diabetic Retinopathy Grading (5 stages)
**Original Dataset**: Fundus diabetic retinopathy classification
**Question**: "What diabetic retinopathy severity grade is shown in this fundus image?"
**Options**:
- A. No diabetic retinopathy (Grade 0)
- B. Mild nonproliferative diabetic retinopathy (Grade 1)
- C. Moderate nonproliferative diabetic retinopathy (Grade 2)
- D. Severe nonproliferative diabetic retinopathy (Grade 3)
- E. Proliferative diabetic retinopathy (Grade 4)
**Answer**: "C" (if moderate NPDR is the ground truth)

### Example 2: Breast Cancer BIRADS Classification (5 categories)
**Original Dataset**: Mammography BIRADS assessment
**Question**: "What BIRADS category is shown in this mammography image?"
**Options**:
- A. BIRADS 1 - Negative
- B. BIRADS 2 - Benign finding
- C. BIRADS 3 - Probably benign
- D. BIRADS 4 - Suspicious abnormality
- E. BIRADS 5 - Highly suggestive of malignancy
**Answer**: "D" (if BIRADS 4 is the ground truth)

### Example 3: Glaucoma Severity Staging (4 stages)
**Original Dataset**: Optic disc glaucoma staging
**Question**: "What glaucoma severity stage is shown in this fundus image?"
**Options**:
- A. No glaucoma (Stage 0)
- B. Early glaucoma (Stage 1)
- C. Moderate glaucoma (Stage 2)
- D. Advanced glaucoma (Stage 3)
**Answer**: "B" (if early glaucoma is the ground truth)

### Example 4: Alzheimer's Disease CDR Staging (3 stages)
**Original Dataset**: Brain MRI dementia staging
**Question**: "What Clinical Dementia Rating (CDR) stage is shown in this brain MRI image?"
**Options**:
- A. CDR 0 - Normal cognition
- B. CDR 0.5 - Very mild dementia
- C. CDR 1 - Mild dementia
- D. CDR 2 - Moderate dementia
**Answer**: "C" (if CDR 1 is the ground truth)

### Example 5: Osteoarthritis Kellgren-Lawrence Grading (5 grades)
**Original Dataset**: Knee X-ray osteoarthritis classification
**Question**: "What Kellgren-Lawrence grade is shown in this knee X-ray image?"
**Options**:
- A. Grade 0 - No osteoarthritis
- B. Grade 1 - Doubtful osteoarthritis
- C. Grade 2 - Minimal osteoarthritis
- D. Grade 3 - Moderate osteoarthritis
- E. Grade 4 - Severe osteoarthritis
**Answer**: "D" (if Grade 3 is the ground truth)

## Implementation Notes

### Advantages
- **Clinical Standardization**: Maps directly to established medical grading systems
- **Ordinal Information**: Preserves meaningful progression/severity relationships
- **Prognostic Value**: Grades often correlate with treatment decisions and outcomes
- **Expert Alignment**: Mirrors how medical professionals assess disease severity
- **Cross-Domain Applicability**: Works across multiple medical specialties

### Limitations
- **Single Dimension**: Cannot capture multi-dimensional severity assessments
- **Subjective Boundaries**: Grade boundaries may be subjective or variable between observers
- **No Localization**: Does not assess regional or spatial distribution of disease
- **Scale Dependency**: Requires datasets with established clinical grading systems

### Quality Considerations
- **Clinical Validity**: All grades must represent clinically meaningful distinctions
- **Scale Consistency**: Use consistent terminology and numbering throughout
- **Expert Validation**: Consider validation by specialists familiar with the grading system
- **Inter-observer Reliability**: Acknowledge that some grading systems have inherent variability
- **Progression Logic**: Ensure ordinal progression makes clinical sense

### Implementation Recommendations
- Always present grades in natural order (normal → mild → moderate → severe)
- Include both numeric and descriptive labels when clinically standard
- Use established medical grading systems rather than ad-hoc severity scales
- Consider including brief descriptions of grade criteria when space permits
- Validate grade terminology against current clinical guidelines
- Be aware that some conditions may skip certain grades (e.g., no "mild" cancer stage)
- Consider domain-specific medical expert review for complex grading systems
