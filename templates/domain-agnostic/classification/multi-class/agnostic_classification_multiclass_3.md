# Multi-Class Classification Template 3: Anatomical Region Identification

## Template Overview

- **Template ID**: agnostic_classification_multiclass_3
- **Task Type**: Multi-class classification (anatomical region)
- **Difficulty**: Easy
- **Pattern**: Anatomical structure or region identification with multiple choice options
- **Domain**: Domain-agnostic (works across all medical specialties)

## Template Description

This template converts multi-class medical datasets into MCVQA format by asking about what anatomical region, organ, or body part is primarily shown in an image. The template presents multiple anatomical structures as answer options, where exactly one structure represents the primary focus of the image. This approach mirrors clinical image interpretation scenarios where medical professionals must first identify the anatomical context before making diagnostic assessments.

The template is designed to work with datasets that classify medical images based on anatomical regions, organs, body parts, or anatomical views. This includes datasets spanning different imaging modalities and medical specialties, from whole-body region classification to specific organ or tissue identification.

## Question Generation Pattern

### Question Format
`"What anatomical {structure_type} is primarily shown in this {modality} image?"`

### Answer Format
Multiple choice with options A, B, C, D, etc. representing different anatomical structures

### Template Variables
- `{structure_type}`: Type of anatomical classification (e.g., "region", "organ", "body part", "view")
- `{modality}`: Imaging modality (e.g., "X-ray", "CT scan", "MRI", "ultrasound", "histopathology")
- `{anatomical_list}`: List of specific anatomical structures from the dataset label set

### Example Pattern
```
Question: "What anatomical region is primarily shown in this X-ray image?"
A. Chest
B. Abdomen
C. Pelvis
D. Skull
```

## Mapping to Datum Schema

```json
{
  "questions-and-answers": [
    {
      "qa_id": "1",
      "task": "Classification",
      "question": "What anatomical {structure_type} is primarily shown in this {modality} image?",
      "answer": "{correct_anatomy_label}",
      "answer_type": "single_label",
      "options": ["{anatomy_1}", "{anatomy_2}", "{anatomy_3}", "{anatomy_4}"],
      "difficulty": "easy",
      "uncertainty": "certain",
      "answer_confidence": 1.0,
      "rationale": "Anatomical region identification using original dataset labels",
      "provenance": {
        "original_label": "{dataset_original_anatomy}",
        "rule_id": "agnostic_classification_multiclass_3",
        "annotation_id": null,
        "created_by": "program"
      }
    }
  ]
}
```

## Dataset Requirements

### Essential Requirements
- **Anatomical labels**: Dataset must have 3+ distinct anatomical region/organ labels
- **Single primary region**: Each image must show one primary anatomical focus
- **Clear anatomical distinction**: Labels must represent clearly distinguishable anatomical structures
- **Imaging data**: Dataset must contain medical images showing anatomical structures

### Compatible Dataset Types
- Multi-organ CT/MRI datasets (brain, chest, abdomen, pelvis)
- Body region X-ray classification datasets
- Histopathology organ/tissue classification
- Ultrasound organ identification datasets
- Endoscopy anatomical site classification
- Retinal anatomical structure identification

### Label Format Compatibility
- Anatomical region names (chest, abdomen, brain)
- Organ names (heart, liver, kidney, lung)
- Body part classifications (head, neck, extremities)
- Tissue type classifications (muscle, bone, soft tissue)

## Template Usage Rules

### Implementation Guidelines
1. **Anatomical Accuracy**: Use standard anatomical terminology (avoid colloquial terms)
2. **Consistent Granularity**: Ensure all options are at similar anatomical levels
3. **Clear Distinctions**: Choose anatomical structures that are visually distinguishable
4. **Medical Standards**: Follow established anatomical nomenclature when possible

### Quality Requirements
- All anatomical terms must be medically accurate and current
- Avoid ambiguous or overlapping anatomical classifications
- Ensure mutual exclusivity between anatomical options
- Use appropriate level of anatomical specificity for the dataset

### Domain Adaptation
- **Radiology**: Use imaging-appropriate anatomical terms (e.g., "thorax" vs "chest")
- **Pathology**: Include tissue-level classifications (epithelial, connective, nervous)
- **Surgery**: Use surgical anatomical landmarks and approaches
- **Ophthalmology**: Include retinal anatomical structures (macula, disc, vessels)

## Examples

### Example 1: Body Region X-ray Classification (4 regions)
**Original Dataset**: Multi-region X-ray dataset
**Question**: "What anatomical region is primarily shown in this X-ray image?"
**Options**:
- A. Chest
- B. Abdomen
- C. Pelvis
- D. Extremities
**Answer**: "A" (if chest is the ground truth label)

### Example 2: Abdominal Organ CT Classification (5 organs)
**Original Dataset**: Abdominal CT organ segmentation
**Question**: "What anatomical organ is primarily shown in this CT scan image?"
**Options**:
- A. Liver
- B. Kidney
- C. Spleen
- D. Pancreas
- E. Gallbladder
**Answer**: "B" (if kidney is the ground truth label)

### Example 3: Histopathology Tissue Classification (4 tissue types)
**Original Dataset**: Multi-organ histopathology dataset
**Question**: "What anatomical tissue type is primarily shown in this histopathology image?"
**Options**:
- A. Epithelial tissue
- B. Connective tissue
- C. Muscle tissue
- D. Nervous tissue
**Answer**: "C" (if muscle tissue is the ground truth label)

### Example 4: Brain MRI Region Classification (6 regions)
**Original Dataset**: Brain anatomical region dataset
**Question**: "What anatomical brain region is primarily shown in this MRI image?"
**Options**:
- A. Frontal lobe
- B. Parietal lobe
- C. Temporal lobe
- D. Occipital lobe
- E. Cerebellum
- F. Brainstem
**Answer**: "E" (if cerebellum is the ground truth label)

### Example 5: Ultrasound Organ Identification (3 organs)
**Original Dataset**: Abdominal ultrasound classification
**Question**: "What anatomical organ is primarily shown in this ultrasound image?"
**Options**:
- A. Liver
- B. Gallbladder
- C. Kidney
**Answer**: "A" (if liver is the ground truth label)

## Implementation Notes

### Advantages
- **Foundation Knowledge**: Tests basic anatomical recognition essential for medical AI
- **Cross-Modal Applicability**: Works across different imaging modalities
- **Educational Value**: Reinforces anatomical knowledge and medical terminology
- **Preprocessing Utility**: Can help categorize datasets by anatomical focus
- **Clinical Relevance**: Mirrors anatomical identification in medical practice

### Limitations
- **No Pathological Assessment**: Does not evaluate disease or abnormality detection
- **Single Region Focus**: Cannot handle images with multiple equally prominent regions
- **No Spatial Relationships**: Does not assess understanding of anatomical relationships
- **View Dependency**: Some anatomical structures may be view-specific

### Quality Considerations
- **Anatomical Accuracy**: All anatomical terms must be correct and current
- **Terminological Consistency**: Use standardized anatomical nomenclature
- **Visual Clarity**: Ensure anatomical structures are clearly visible in dataset images
- **Clinical Context**: Consider imaging modality appropriateness for anatomical visualization
- **Expert Validation**: Consider review by anatomists or relevant medical specialists

### Implementation Recommendations
- Use standardized anatomical nomenclature (Terminologia Anatomica when applicable)
- Ensure consistent granularity across anatomical options (organs vs regions vs tissues)
- Consider imaging modality limitations (e.g., soft tissue visibility on X-rays)
- Include anatomical orientation information when relevant (anterior, posterior, etc.)
- Validate anatomical classifications against medical atlases or references
- Consider cultural/linguistic variations in anatomical terminology for international datasets
- Ensure anatomical options reflect realistic clinical distinctions
- Be aware of anatomical variations that may complicate classification
