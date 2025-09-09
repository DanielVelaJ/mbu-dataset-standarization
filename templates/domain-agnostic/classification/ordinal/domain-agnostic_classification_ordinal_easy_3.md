# Ordinal Classification Template 3: Comparative Severity Assessment

## Template Overview

**Template ID**: `classification_ordinal_3`  
**Task Type**: Ordinal Classification  
**Difficulty**: Easy  
**Question Pattern**: Comparative severity assessment with ordered intensity descriptors  

## Template Description

This template converts ordinal classification datasets into MCVQA format by asking about comparative severity levels using descriptive intensity terms. It focuses on relative severity assessment using common clinical descriptors like "mild", "moderate", and "severe", making it suitable for datasets that use intensity-based grading rather than numerical staging.

The template is particularly effective for inflammatory conditions, degenerative diseases, and pathological findings where severity is described using qualitative intensity measures.

## Question Generation Pattern

### Question Format
```
"What level of {condition_severity} is shown in this {modality} image?"
```

### Answer Format
Multiple choice options with ordered severity descriptors:
- A. None/Normal
- B. Minimal/Trace
- C. Mild  
- D. Moderate
- E. Severe/Marked

### Template Variables
- `{condition_severity}`: The medical condition with severity qualifier (e.g., "inflammation", "stenosis", "degeneration", "atrophy", "hypertrophy")
- `{modality}`: The imaging modality (e.g., "MRI", "CT", "ultrasound", "X-ray", "endoscopy")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What level of {condition_severity} is shown in this {modality} image?",
  "answer": "{selected_option_letter}",
  "answer_type": "single_label",
  "options": [
    "A. None (Normal findings)",
    "B. Minimal ({minimal_description})", 
    "C. Mild ({mild_description})",
    "D. Moderate ({moderate_description})",
    "E. Severe ({severe_description})"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Severity assessment based on established intensity grading criteria",
  "provenance": {
    "original_label": "{original_severity_value}",
    "rule_id": "classification_ordinal_3",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Ordinal classification with severity/intensity labels
- **Intensity Grading**: Qualitative severity descriptors (none, mild, moderate, severe)
- **Comparative Assessment**: Relative severity measurements rather than absolute staging
- **Clinical Context**: Conditions commonly assessed using intensity-based grading

## Template Usage Rules

1. **Intensity Progression**: Maintain logical progression from none/minimal to severe
2. **Descriptor Consistency**: Use standard clinical severity terminology
3. **Complete Spectrum**: Include all intensity levels present in the dataset
4. **Clinical Relevance**: Ensure severity levels reflect clinically meaningful distinctions
5. **Comparative Logic**: Options should represent increasing intensity/severity

## Examples

### Example 1: Coronary Artery Stenosis Assessment
**Original Dataset**: Coronary Angiography Stenosis Grading  
**Original Label**: 2 (Moderate stenosis)  
**Generated Q&A**:
- **Question**: "What level of coronary stenosis is shown in this angiography image?"
- **Options**:
  - A. None (Normal coronary arteries)
  - B. Minimal (≤25% stenosis)
  - C. Mild (26-50% stenosis)
  - D. Moderate (51-75% stenosis)
  - E. Severe (76-99% stenosis)
- **Answer**: "D"
- **Rationale**: "Moderate coronary stenosis with 60% luminal narrowing requiring intervention consideration"

### Example 2: Joint Inflammation Assessment
**Original Dataset**: Rheumatoid Arthritis MRI Grading  
**Original Label**: 3 (Severe inflammation)  
**Generated Q&A**:
- **Question**: "What level of joint inflammation is shown in this MRI image?"
- **Options**:
  - A. None (No inflammatory changes)
  - B. Minimal (Trace synovial enhancement)
  - C. Mild (Mild synovial thickening)
  - D. Moderate (Moderate joint effusion)
  - E. Severe (Marked inflammatory changes)
- **Answer**: "E"
- **Rationale**: "Severe joint inflammation with extensive synovial thickening and bone erosion"

### Example 3: Brain Atrophy Assessment
**Original Dataset**: Brain MRI Atrophy Grading  
**Original Label**: 1 (Mild atrophy)  
**Generated Q&A**:
- **Question**: "What level of brain atrophy is shown in this MRI image?"
- **Options**:
  - A. None (Age-appropriate brain volume)
  - B. Minimal (Subtle volume loss)
  - C. Mild (Mild generalized atrophy)
  - D. Moderate (Moderate cortical thinning)
  - E. Severe (Marked brain volume loss)
- **Answer**: "C"
- **Rationale**: "Mild generalized brain atrophy exceeding normal age-related changes"

### Example 4: Fatty Liver Disease Grading
**Original Dataset**: Liver Ultrasound Steatosis Assessment  
**Original Label**: 2 (Moderate steatosis)  
**Generated Q&A**:
- **Question**: "What level of hepatic steatosis is shown in this ultrasound image?"
- **Options**:
  - A. None (Normal liver echogenicity)
  - B. Minimal (Trace fatty infiltration)
  - C. Mild (Grade 1 steatosis)
  - D. Moderate (Grade 2 steatosis)
  - E. Severe (Grade 3 steatosis)
- **Answer**: "D"
- **Rationale**: "Moderate hepatic steatosis with increased echogenicity and posterior acoustic attenuation"

### Example 5: Disc Degeneration Assessment
**Original Dataset**: Spine MRI Disc Degeneration Grading  
**Original Label**: 3 (Severe degeneration)  
**Generated Q&A**:
- **Question**: "What level of disc degeneration is shown in this spine MRI image?"
- **Options**:
  - A. None (Normal disc signal)
  - B. Minimal (Slight signal loss)
  - C. Mild (Mild disc desiccation)
  - D. Moderate (Moderate height loss)
  - E. Severe (Marked disc collapse)
- **Answer**: "E"
- **Rationale**: "Severe disc degeneration with significant height loss and end-plate changes"

## Implementation Notes

### Advantages
- **Intuitive Assessment**: Uses familiar clinical severity descriptors understood across medical specialties
- **Flexible Application**: Applicable to various conditions using intensity-based grading
- **Comparative Evaluation**: Enables relative severity assessment important for treatment decisions
- **Clinical Translation**: Maps naturally to clinical assessment and reporting practices

### Limitations
- **Subjective Interpretation**: Severity descriptors may have some subjective variation between assessors
- **Scale Dependency**: Requires datasets with consistent intensity-based grading criteria
- **Binary vs Continuous**: May oversimplify conditions with more complex or continuous severity measures

### Quality Considerations
- Ensure severity descriptors align with clinical standards and guidelines
- Verify that intensity levels reflect clinically meaningful severity distinctions
- Confirm that comparative terms (mild vs moderate vs severe) are consistently applied
- Validate that severity progression matches clinical understanding of disease intensity
- Check that all severity levels present in the dataset are appropriately represented
