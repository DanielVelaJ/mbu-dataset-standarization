# Ophthalmology Diabetic Retinopathy Grading Template

## Template Overview

**Template ID**: `domain-specific_ophthalmology_classification_ordinal_easy_1`  
**Task Type**: Ordinal Classification  
**Difficulty**: Easy  
**Question Pattern**: Diabetic retinopathy severity grading assessment  
**Medical Domain**: Ophthalmology (fundus imaging and diabetic retinopathy assessment)  
**Domain-knowledge summary**: Requires specialized knowledge of diabetic retinopathy classification and severity grading systems. Understanding of microaneurysms, hemorrhages, hard exudates, cotton wool spots, neovascularization, and proliferative changes. Knowledge of ETDRS grading criteria, severity progression (mild, moderate, severe NPDR, PDR), clinical significance of diabetic changes, and systematic retinal assessment for diabetes complications.

## Template Description

This template converts ordinal diabetic retinopathy classification datasets into MCVQA format by asking direct questions about the severity grade of diabetic retinopathy visible in fundus images. It is specifically designed for ophthalmology datasets where each fundus image has been graded according to the standard diabetic retinopathy severity scale (0-4).

The template uses established clinical terminology and grading systems used in diabetic retinopathy screening programs worldwide, making it highly relevant for real-world clinical applications and model evaluation in ophthalmology.

## Question Generation Pattern

### Question Format
```
"What grade of diabetic retinopathy is shown in this fundus image?"
```

### Answer Format
Multiple choice with ordinal grading options (A-E):
- A. No DR (Grade 0)
- B. Mild NPDR (Grade 1)  
- C. Moderate NPDR (Grade 2)
- D. Severe NPDR (Grade 3)
- E. PDR (Grade 4)

### Template Variables
- `{grade}`: The diabetic retinopathy grade (0-4)
- `{grade_description}`: Clinical description of the grade
- `{modality}`: Always "fundus" for this template

### Clinical Terminology
- **No DR**: No diabetic retinopathy
- **NPDR**: Non-proliferative diabetic retinopathy
- **PDR**: Proliferative diabetic retinopathy

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What grade of diabetic retinopathy is shown in this fundus image?",
  "answer": "C",
  "answer_type": "single_label",
  "options": [
    "No DR (Grade 0)",
    "Mild NPDR (Grade 1)", 
    "Moderate NPDR (Grade 2)",
    "Severe NPDR (Grade 3)",
    "PDR (Grade 4)"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Diabetic retinopathy grading based on standard clinical severity scale",
  "provenance": {
    "original_label": "2",
    "rule_id": "ophthalmology_classification_ordinal_easy_1",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Ordinal classification (Vision → Image-Level Classification → Ordinal grading)
- **Domain**: Ophthalmology with fundus photography
- **Label Structure**: Ordinal grades 0-4 representing diabetic retinopathy severity
- **Image Type**: Color fundus photographs
- **Grading System**: Standard diabetic retinopathy classification

### Compatible Datasets
- EyePACS diabetic retinopathy detection
- APTOS 2019 blindness detection
- DDR (Diabetic Retinopathy Dataset)
- Messidor diabetic retinopathy dataset
- Any fundus dataset with DR grading labels

## Template Usage Rules

1. **Grading System**: Use standard 5-level diabetic retinopathy grading (0-4)
2. **Clinical Terminology**: Always use established medical abbreviations (NPDR, PDR)
3. **Grade Mapping**: 
   - Grade 0 → "No DR (Grade 0)"
   - Grade 1 → "Mild NPDR (Grade 1)"
   - Grade 2 → "Moderate NPDR (Grade 2)"
   - Grade 3 → "Severe NPDR (Grade 3)"
   - Grade 4 → "PDR (Grade 4)"
4. **Order Preservation**: Maintain ordinal relationship in answer options

## Examples

### Example 1: No Diabetic Retinopathy
**Original Dataset**: EyePACS DR Detection  
**Original Label**: 0 (no diabetic retinopathy)  
**Generated Q&A**:
- **Question**: "What grade of diabetic retinopathy is shown in this fundus image?"
- **Answer**: "A" (No DR - Grade 0)
- **Rationale**: "Fundus shows normal retinal vasculature with no diabetic changes"

### Example 2: Mild Non-Proliferative DR
**Original Dataset**: APTOS 2019 Blindness Detection  
**Original Label**: 1 (mild NPDR)  
**Generated Q&A**:
- **Question**: "What grade of diabetic retinopathy is shown in this fundus image?"
- **Answer**: "B" (Mild NPDR - Grade 1)
- **Rationale**: "Mild diabetic retinopathy with microaneurysms present"

### Example 3: Moderate Non-Proliferative DR
**Original Dataset**: DDR Dataset  
**Original Label**: 2 (moderate NPDR)  
**Generated Q&A**:
- **Question**: "What grade of diabetic retinopathy is shown in this fundus image?"
- **Answer**: "C" (Moderate NPDR - Grade 2)
- **Rationale**: "Moderate diabetic retinopathy with hemorrhages and exudates"

### Example 4: Severe Non-Proliferative DR
**Original Dataset**: Messidor Dataset  
**Original Label**: 3 (severe NPDR)  
**Generated Q&A**:
- **Question**: "What grade of diabetic retinopathy is shown in this fundus image?"
- **Answer**: "D" (Severe NPDR - Grade 3)
- **Rationale**: "Severe non-proliferative diabetic retinopathy with extensive hemorrhages and cotton wool spots"

### Example 5: Proliferative Diabetic Retinopathy
**Original Dataset**: EyePACS DR Detection  
**Original Label**: 4 (PDR)  
**Generated Q&A**:
- **Question**: "What grade of diabetic retinopathy is shown in this fundus image?"
- **Answer**: "E" (PDR - Grade 4)
- **Rationale**: "Proliferative diabetic retinopathy with neovascularization visible"

## Implementation Notes

### Advantages
- **Clinical Relevance**: Uses standard diabetic retinopathy grading scale
- **Ordinal Awareness**: Preserves meaningful progression of severity
- **Domain Expertise**: Reflects real ophthalmological workflows
- **MCVQA Compatible**: Clear multiple choice format for automated evaluation
- **Educational Value**: Teaches proper diabetic retinopathy classification

### Limitations
- **Fundus-Specific**: Only works with fundus photography
- **DR-Specific**: Cannot assess other retinal pathologies
- **Grading Dependency**: Requires datasets with proper DR grading labels
- **Clinical Expertise**: Optimal performance requires understanding of DR progression

### Quality Considerations
- Ensure original dataset uses standard DR grading criteria
- Verify clinical accuracy of grade assignments
- Consider inter-grader variability in original dataset annotations
- Validate that image quality supports accurate grading assessment
- Account for potential disagreement between human graders on borderline cases

### Clinical Context
This template mirrors real-world diabetic retinopathy screening workflows where:
- Primary care physicians use automated screening tools
- Ophthalmologists grade fundus photographs for treatment decisions
- Diabetes management programs require regular retinal assessment
- AI systems assist in large-scale population screening
