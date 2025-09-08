# Multi-Label Classification Template 3: Clinical Assessment with Multiple Criteria

## Template Overview

- **Template ID**: domain-agnostic_classification_multilabel_easy_3
- **Task Type**: Multi-label classification (clinical assessment)
- **Difficulty**: Easy
- **Pattern**: Multiple clinical criteria or feature assessment with set-based answers
- **Domain**: Domain-agnostic (works across all medical specialties)

## Template Description

This template converts multi-label medical datasets into MCVQA format by asking about which clinical assessment criteria or image features are met or present in a medical image. The template allows for multiple clinical criteria to be evaluated simultaneously, acknowledging that medical assessment often involves checking multiple independent criteria or features. This approach mirrors clinical decision-making where medical professionals must evaluate multiple characteristics or criteria to make comprehensive assessments.

The template is designed to work with datasets that have multiple binary assessment criteria per image, making it suitable for comprehensive clinical evaluation tasks across different medical specialties. This template is particularly valuable for quality assessment, diagnostic criteria evaluation, and systematic clinical feature analysis.

## Question Generation Pattern

### Question Format
`"Which of the following {assessment_type} are present in this {modality} image?"`

### Answer Format
Set-based answer listing all present criteria or features, with "None of the above" option when no target criteria are met

### Template Variables
- `{assessment_type}`: Type of clinical assessment (e.g., "diagnostic criteria", "image quality features", "clinical signs", "pathological features")
- `{modality}`: Imaging modality (e.g., "chest X-ray", "mammography", "fundus", "histopathology")
- `{criteria_list}`: List of clinical criteria or features from the dataset label set
- `{present_criteria}`: Set of criteria or features that are actually present/met in the image

### Example Pattern
```
Question: "Which of the following image quality criteria are met in this chest X-ray image?"
Options: Adequate inspiration, Proper positioning, Good contrast, Absence of motion artifacts, None of the above
Answer: "Adequate inspiration, Good contrast" (if these criteria are met)
```

## Mapping to Datum Schema

```json
{
  "questions-and-answers": [
    {
      "qa_id": "1",
      "task": "Classification",
      "question": "Which of the following {assessment_type} are present in this {modality} image?",
      "answer": "{present_criteria_list}",
      "answer_type": "multi_label",
      "options": ["{criterion_1}", "{criterion_2}", "{criterion_3}", "{criterion_4}", "None of the above"],
      "difficulty": "easy",
      "uncertainty": "certain",
      "answer_confidence": 1.0,
      "rationale": "Multi-label clinical assessment using original dataset criteria labels",
      "provenance": {
        "original_label": "{dataset_multilabel_criteria_vector}",
        "rule_id": "domain-agnostic_classification_multilabel_easy_3",
        "annotation_id": null,
        "created_by": "program"
      }
    }
  ]
}
```

## Dataset Requirements

### Essential Requirements
- **Multi-criteria labels**: Dataset must have multiple assessment criteria labels per image (2+ possible criteria)
- **Independent assessment**: Each criterion must be independently evaluable
- **Clinical relevance**: Labels must represent meaningful clinical assessment criteria or features
- **Imaging data**: Dataset must contain medical images suitable for clinical assessment

### Compatible Dataset Types
- Image quality assessment datasets with multiple quality criteria
- Diagnostic criteria datasets with multiple clinical signs
- Pathological feature assessment with multiple characteristics
- Technical imaging parameter evaluation datasets
- Clinical scoring systems with multiple components
- Radiological reporting datasets with multiple findings

### Label Format Compatibility
- Binary multi-hot vectors for criteria presence (e.g., [1,0,1,1,0] for 5 possible criteria)
- Multiple clinical assessment annotations per image
- Set-based clinical criteria labels
- Multi-label clinical assessment datasets

## Template Usage Rules

### Implementation Guidelines
1. **Clinical Validity**: Use established clinical criteria and assessment standards
2. **Independent Evaluation**: Ensure each criterion can be assessed independently
3. **Objective Assessment**: Focus on objectively assessable features when possible
4. **Comprehensive Coverage**: Include all relevant criteria for the clinical assessment domain

### Quality Requirements
- All clinical criteria must be medically valid and evidence-based
- Avoid criteria that are mutually exclusive (use appropriate classification type instead)
- Ensure criteria are assessable from the given imaging modality and view
- Use standardized clinical terminology and assessment scales

### Domain Adaptation
- **Radiology**: Focus on image quality criteria and radiological signs
- **Pathology**: Include histological features and cellular characteristics
- **Dermatology**: Use dermatological assessment criteria (ABCDE criteria, etc.)
- **Ophthalmology**: Include retinal assessment criteria and image quality factors

## Examples

### Example 1: Chest X-ray Quality Assessment (4 criteria)
**Original Dataset**: Radiographic quality evaluation
**Question**: "Which of the following image quality criteria are met in this chest X-ray image?"
**Options**: Adequate inspiration, Proper positioning, Good contrast, Absence of motion artifacts, None of the above
**Answer**: "Adequate inspiration, Good contrast, Absence of motion artifacts" (if these criteria are met)

### Example 2: Skin Lesion ABCDE Assessment (5 criteria)
**Original Dataset**: Melanoma risk assessment
**Question**: "Which of the following ABCDE criteria are present in this dermoscopy image?"
**Options**: Asymmetry, Border irregularity, Color variation, Diameter >6mm, Evolving characteristics, None of the above
**Answer**: "Asymmetry, Border irregularity, Color variation" (if these criteria are present)

### Example 3: Mammography BI-RADS Features (4 features)
**Original Dataset**: Breast imaging assessment
**Question**: "Which of the following BI-RADS imaging features are present in this mammography image?"
**Options**: Mass, Calcifications, Architectural distortion, Asymmetry, None of the above
**Answer**: "Mass, Calcifications" (if these features are present)

### Example 4: Fundus Image Quality Assessment (3 criteria)
**Original Dataset**: Retinal imaging quality control
**Question**: "Which of the following image quality criteria are met in this fundus image?"
**Options**: Adequate illumination, Sharp focus, Complete optic disc visibility, None of the above
**Answer**: "Adequate illumination, Sharp focus, Complete optic disc visibility" (if all criteria are met)

### Example 5: Histopathology Tumor Grading Features (4 features)
**Original Dataset**: Cancer grading assessment
**Question**: "Which of the following histological features are present in this tissue image?"
**Options**: High mitotic activity, Nuclear pleomorphism, Tubule formation, Necrosis, None of the above
**Answer**: "High mitotic activity, Nuclear pleomorphism" (if these features are present)

## Implementation Notes

### Advantages
- **Systematic Assessment**: Enables comprehensive evaluation of multiple clinical criteria
- **Clinical Decision Support**: Mirrors real clinical assessment workflows
- **Quality Control**: Useful for image quality and technical assessment tasks
- **Educational Value**: Teaches systematic clinical evaluation approaches
- **Objective Evaluation**: Can focus on objectively measurable criteria

### Limitations
- **Subjectivity**: Some clinical criteria may have inter-observer variability
- **Context Dependency**: Some criteria may require clinical context not visible in the image
- **Complexity**: Multiple criteria assessment can be more challenging than single assessments
- **Training Requirements**: May require specialized medical knowledge for accurate assessment

### Quality Considerations
- **Clinical Validity**: All criteria must be clinically meaningful and evidence-based
- **Assessment Objectivity**: Prefer objective over subjective criteria when possible
- **Inter-observer Reliability**: Consider criteria with good inter-observer agreement
- **Clinical Context**: Ensure criteria are appropriate for the clinical context and imaging modality
- **Expert Validation**: Consider validation by relevant medical specialists

### Implementation Recommendations
- Use established clinical assessment criteria and guidelines when available
- Consider international standards and consensus guidelines for criteria definition
- Implement appropriate scoring and weighting for different criteria when relevant
- Account for normal variations and edge cases in criteria assessment
- Provide clear definitions for subjective or complex criteria
- Consider confidence scoring for individual criteria when appropriate
- Validate criteria combinations against clinical practice patterns
- Ensure criteria are appropriate for the target clinical application
- Consider training requirements for accurate criteria assessment
