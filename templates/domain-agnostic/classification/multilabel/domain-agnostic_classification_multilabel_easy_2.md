# Multi-Label Classification Template 2: Anatomical Structure Identification

## Template Overview

- **Template ID**: domain-agnostic_classification_multilabel_easy_2
- **Task Type**: Multi-label classification (anatomical structures)
- **Difficulty**: Easy
- **Pattern**: Multiple anatomical structure identification with set-based answers
- **Domain**: Domain-agnostic (works across all medical specialties)

## Template Description

This template converts multi-label medical datasets into MCVQA format by asking about which anatomical structures or regions are visible in an image. The template allows for multiple anatomical structures to be identified simultaneously, acknowledging that medical images often show multiple organs, tissues, or anatomical landmarks in a single view. This approach mirrors clinical image interpretation where medical professionals must identify all relevant anatomical structures present.

The template is designed to work with datasets that have multiple anatomical structure labels per image, making it suitable for comprehensive anatomical analysis across different imaging modalities and medical specialties. This template is particularly useful for datasets involving cross-sectional imaging, wide-field photography, or panoramic views where multiple structures are naturally visible.

## Question Generation Pattern

### Question Format
`"Which of the following anatomical structures are visible in this {modality} image?"`

### Answer Format
Set-based answer listing all visible anatomical structures, with "None of the above" option when no target structures are visible

### Template Variables
- `{modality}`: Imaging modality (e.g., "CT scan", "MRI", "ultrasound", "fundus photograph", "X-ray")
- `{structure_list}`: List of potential anatomical structures from the dataset label set
- `{visible_structures}`: Set of anatomical structures that are actually visible in the image

### Example Pattern
```
Question: "Which of the following anatomical structures are visible in this abdominal CT scan image?"
Options: Liver, Kidney, Spleen, Pancreas, Gallbladder, None of the above
Answer: "Liver, Kidney, Spleen" (if these three organs are visible in the scan)
```

## Mapping to Datum Schema

```json
{
  "questions-and-answers": [
    {
      "qa_id": "1",
      "task": "Classification",
      "question": "Which of the following anatomical structures are visible in this {modality} image?",
      "answer": "{visible_structures_list}",
      "answer_type": "multi_label",
      "options": ["{structure_1}", "{structure_2}", "{structure_3}", "{structure_4}", "None of the above"],
      "difficulty": "easy",
      "uncertainty": "certain",
      "answer_confidence": 1.0,
      "rationale": "Multi-label anatomical structure identification using original dataset labels",
      "provenance": {
        "original_label": "{dataset_multilabel_anatomy_vector}",
        "rule_id": "domain-agnostic_classification_multilabel_easy_2",
        "annotation_id": null,
        "created_by": "program"
      }
    }
  ]
}
```

## Dataset Requirements

### Essential Requirements
- **Multi-anatomical labels**: Dataset must have multiple anatomical structure labels per image (2+ possible structures)
- **Independent visibility**: Each anatomical structure must be independently visible/assessable
- **Anatomical specificity**: Labels must represent distinct anatomical structures, organs, or tissue types
- **Imaging data**: Dataset must contain medical images showing anatomical structures

### Compatible Dataset Types
- Cross-sectional imaging datasets with multiple organ visibility (CT, MRI)
- Ultrasound datasets with multiple anatomical structures
- Fundus datasets with multiple retinal anatomical features
- Histopathology datasets with multiple tissue types
- Endoscopy datasets with multiple anatomical landmarks
- Whole-body imaging with multiple body regions

### Label Format Compatibility
- Binary multi-hot vectors for anatomical presence (e.g., [1,0,1,1,0] for 5 possible structures)
- Multiple anatomical structure annotations per image
- Set-based anatomical labels
- Multi-label anatomical datasets from medical vision taxonomy

## Template Usage Rules

### Implementation Guidelines
1. **Anatomical Accuracy**: Use standard anatomical nomenclature and terminology
2. **Visibility Assessment**: Include only structures that are actually visible in the imaging modality
3. **Consistent Granularity**: Ensure all anatomical options are at similar levels (organs vs tissues vs regions)
4. **Clinical Relevance**: Focus on clinically relevant anatomical identification tasks

### Quality Requirements
- All anatomical structure names must be medically accurate and current
- Avoid structures that cannot coexist in the same anatomical view
- Ensure structures are appropriately visible in the given imaging modality
- Use standardized anatomical terminology when possible

### Domain Adaptation
- **Radiology**: Focus on organs and structures visible in cross-sectional imaging
- **Pathology**: Include tissue types and cellular structures visible in microscopy
- **Ophthalmology**: Include retinal structures (vessels, disc, macula, etc.)
- **Surgery**: Focus on anatomical landmarks relevant to surgical procedures

## Examples

### Example 1: Abdominal CT Multi-Label (5 organs)
**Original Dataset**: Multi-organ abdominal imaging
**Question**: "Which of the following anatomical structures are visible in this abdominal CT scan image?"
**Options**: Liver, Kidney, Spleen, Pancreas, Gallbladder, None of the above
**Answer**: "Liver, Kidney, Spleen" (if these organs are visible in the slice)

### Example 2: Fundus Multi-Label (4 structures)
**Original Dataset**: Retinal anatomical structure detection
**Question**: "Which of the following anatomical structures are visible in this fundus image?"
**Options**: Optic disc, Macula, Retinal vessels, Fovea, None of the above
**Answer**: "Optic disc, Retinal vessels, Fovea" (if these structures are visible)

### Example 3: Chest X-ray Multi-Label (3 structures)
**Original Dataset**: Thoracic anatomical identification
**Question**: "Which of the following anatomical structures are visible in this chest X-ray image?"
**Options**: Heart, Lungs, Diaphragm, Ribs, None of the above
**Answer**: "Heart, Lungs, Diaphragm, Ribs" (if all structures are visible)

### Example 4: Histopathology Multi-Label (4 tissue types)
**Original Dataset**: Multi-tissue histological analysis
**Question**: "Which of the following tissue types are visible in this histopathology image?"
**Options**: Epithelial tissue, Connective tissue, Blood vessels, Inflammatory cells, None of the above
**Answer**: "Epithelial tissue, Connective tissue, Blood vessels" (if these tissues are present)

### Example 5: Brain MRI Multi-Label (5 structures)
**Original Dataset**: Brain anatomical region identification
**Question**: "Which of the following brain structures are visible in this MRI image?"
**Options**: Cerebral cortex, White matter, Ventricles, Cerebellum, Brainstem, None of the above
**Answer**: "Cerebral cortex, White matter, Ventricles" (if these structures are visible in the slice)

## Implementation Notes

### Advantages
- **Comprehensive Anatomical Assessment**: Evaluates complete anatomical structure recognition
- **Educational Value**: Reinforces anatomical knowledge across multiple structures simultaneously
- **Clinical Relevance**: Mirrors real anatomical identification tasks in medical practice
- **Cross-Modal Applicability**: Works across different imaging modalities and views
- **Foundation Knowledge**: Tests basic anatomical recognition essential for medical AI

### Limitations
- **View Dependency**: Some anatomical structures may only be visible in specific views or orientations
- **Resolution Limitations**: Small structures may not be visible in all imaging conditions
- **Overlap Complexity**: Some structures may overlap or obscure others
- **Modality Constraints**: Different imaging modalities show different anatomical details

### Quality Considerations
- **Anatomical Accuracy**: All structure identifications must be anatomically correct
- **Visibility Validation**: Ensure structures are actually visible and identifiable in the images
- **Terminological Consistency**: Use standardized anatomical nomenclature
- **Clinical Context**: Consider anatomical relationships and spatial organization
- **Expert Validation**: Consider review by anatomists or imaging specialists

### Implementation Recommendations
- Use standardized anatomical terminology (Terminologia Anatomica when applicable)
- Consider imaging modality capabilities and limitations for structure visibility
- Ensure consistent anatomical granularity across all options
- Include anatomical orientation and positioning context when relevant
- Validate structure combinations against anatomical atlases
- Consider developmental and pathological anatomical variations
- Account for normal anatomical variants that may affect structure visibility
- Ensure structures are at appropriate scales for the imaging resolution
- Consider cultural and linguistic variations in anatomical terminology for international datasets
