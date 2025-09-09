# Multi-Label Classification Template 1: Basic Finding Detection

## Template Overview

- **Template ID**: domain-agnostic_classification_multilabel_easy_1
- **Task Type**: Multi-label classification
- **Difficulty**: Easy
- **Pattern**: Multiple medical findings detection with set-based answers
- **Domain**: Domain-agnostic (works across all medical specialties)

## Template Description

This template converts multi-label medical datasets into MCVQA format by asking about what medical findings are present in an image. The template allows for multiple correct findings to be identified simultaneously, where any combination of findings can be true. This approach mirrors clinical image interpretation scenarios where medical professionals must identify all visible pathological findings in a single image.

The template is designed to work with datasets that have multiple binary labels per image, making it suitable for comprehensive medical image analysis across different specialties including radiology, pathology, dermatology, and ophthalmology. Unlike binary or multi-class templates, this template acknowledges that medical images often contain multiple co-occurring conditions or findings.

## Question Generation Pattern

### Question Format
`"Which of the following medical findings are present in this {modality} image?"`

### Answer Format
Set-based answer listing all present findings, with "None of the above" option for negative cases

### Template Variables
- `{modality}`: Imaging modality (e.g., "chest X-ray", "fundus", "dermoscopy", "histopathology")
- `{finding_list}`: List of potential medical findings from the dataset label set
- `{present_findings}`: Set of findings that are actually present in the image

### Example Pattern
```
Question: "Which of the following medical findings are present in this chest X-ray image?"
Options: Pneumonia, Atelectasis, Cardiomegaly, Pleural effusion, Pneumothorax, None of the above
Answer: "Pneumonia, Cardiomegaly" (if both conditions are present)
```

## Mapping to Datum Schema

```json
{
  "questions-and-answers": [
    {
      "qa_id": "1",
      "task": "Classification",
      "question": "Which of the following medical findings are present in this {modality} image?",
      "answer": "{present_findings_list}",
      "answer_type": "multi_label",
      "options": ["{finding_1}", "{finding_2}", "{finding_3}", "{finding_4}", "None of the above"],
      "difficulty": "easy",
      "uncertainty": "certain",
      "answer_confidence": 1.0,
      "rationale": "Multi-label finding detection using original dataset binary labels",
      "provenance": {
        "original_label": "{dataset_multilabel_vector}",
        "rule_id": "domain-agnostic_classification_multilabel_easy_1",
        "annotation_id": null,
        "created_by": "program"
      }
    }
  ]
}
```

## Dataset Requirements

### Essential Requirements
- **Multi-label structure**: Dataset must have multiple binary labels per image (2+ possible findings)
- **Independent labels**: Each finding label must be independently assignable (not mutually exclusive)
- **Medical findings**: Labels must represent distinct medical conditions, pathologies, or abnormalities
- **Imaging data**: Dataset must contain medical images (any modality)

### Compatible Dataset Types
- Chest X-ray datasets with multiple pulmonary findings (CheXpert, MIMIC-CXR)
- Skin lesion datasets with multiple dermatological features
- Fundus datasets with multiple retinal pathologies
- Histopathology datasets with multiple tissue characteristics
- Brain imaging datasets with multiple neurological findings

### Label Format Compatibility
- Binary multi-hot vectors (e.g., [1,0,1,1,0] for 5 possible findings)
- Multiple categorical labels per image
- Set-based annotations with finding lists
- Multi-label datasets from medical vision taxonomy

## Template Usage Rules

### Implementation Guidelines
1. **Comprehensive Assessment**: Include all major findings that can co-occur in the imaging modality
2. **Independent Evaluation**: Ensure each finding can be assessed independently of others
3. **Clinical Relevance**: Use medically meaningful finding combinations
4. **Negative Cases**: Include "None of the above" for images with no target findings

### Quality Requirements
- All finding names must be medically accurate and specific
- Avoid findings that are mutually exclusive (use multi-class template instead)
- Ensure findings are visible and assessable in the given imaging modality
- Verify clinical plausibility of finding combinations

### Domain Adaptation
- **Radiology**: Use modality-appropriate findings (e.g., air space opacities, masses, devices)
- **Pathology**: Include cellular and tissue-level abnormalities
- **Dermatology**: Focus on lesion characteristics and surface features
- **Ophthalmology**: Include retinal, vascular, and optical disc findings

## Examples

### Example 1: Chest X-ray Multi-Label (4 findings)
**Original Dataset**: CheXpert-style multi-finding detection
**Question**: "Which of the following medical findings are present in this chest X-ray image?"
**Options**: Pneumonia, Atelectasis, Cardiomegaly, Pleural effusion, None of the above
**Answer**: "Pneumonia, Cardiomegaly" (if pneumonia=1 and cardiomegaly=1 in ground truth)

### Example 2: Skin Lesion Multi-Label (5 features)
**Original Dataset**: Dermoscopy feature detection
**Question**: "Which of the following dermatological features are present in this dermoscopy image?"
**Options**: Asymmetry, Border irregularity, Color variation, Diameter >6mm, Pigment network, None of the above
**Answer**: "Asymmetry, Color variation, Diameter >6mm" (if multiple features present)

### Example 3: Fundus Multi-Label (3 findings)
**Original Dataset**: Retinal pathology detection
**Question**: "Which of the following retinal findings are present in this fundus image?"
**Options**: Microaneurysms, Hard exudates, Soft exudates, Hemorrhages, None of the above
**Answer**: "Microaneurysms, Hard exudates" (if both findings present)

### Example 4: Brain MRI Multi-Label (3 findings)
**Original Dataset**: Neurological finding detection
**Question**: "Which of the following neurological findings are present in this brain MRI image?"
**Options**: White matter lesions, Atrophy, Edema, Mass effect, None of the above
**Answer**: "White matter lesions, Atrophy" (if both findings present)

### Example 5: Histopathology Multi-Label (4 features)
**Original Dataset**: Tissue characteristic identification
**Question**: "Which of the following histopathological features are present in this tissue image?"
**Options**: Mitotic figures, Nuclear pleomorphism, Necrosis, Invasion, None of the above
**Answer**: "Mitotic figures, Nuclear pleomorphism, Necrosis" (if three features present)

## Implementation Notes

### Advantages
- **Comprehensive Assessment**: Evaluates ability to detect multiple co-occurring conditions
- **Clinical Realism**: Mirrors real-world scenarios where multiple pathologies coexist
- **Flexible Scoring**: Allows partial credit evaluation and detailed performance analysis
- **Information Rich**: Provides more diagnostic information per image than single-label approaches
- **Domain Flexibility**: Applicable across all medical imaging specialties

### Limitations
- **Complexity**: More challenging for models than single-label classification
- **Label Dependencies**: Some findings may be correlated or have dependencies
- **Evaluation Complexity**: Requires more sophisticated evaluation metrics
- **Dataset Requirements**: Needs high-quality multi-label annotations

### Quality Considerations
- **Medical Accuracy**: All finding combinations must be clinically plausible
- **Independent Assessment**: Ensure findings can be evaluated independently
- **Annotation Quality**: Multi-label datasets require careful expert annotation
- **Balanced Representation**: Consider class imbalance across multiple labels
- **Clinical Validation**: Expert review recommended for complex finding combinations

### Implementation Recommendations
- Use established medical finding taxonomies when available
- Consider finding co-occurrence patterns in clinical practice
- Implement appropriate evaluation metrics (F1-score, Hamming loss, subset accuracy)
- Handle negative cases appropriately with "None of the above" option
- Consider confidence scoring for individual findings when available
- Validate finding combinations with medical experts
- Account for inter-observer variability in multi-label scenarios
- Consider hierarchical relationships between findings when relevant
