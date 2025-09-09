# Pathology Malignant vs Benign Tissue Classification Template

## Template Overview

**Template ID**: `pathology_classification_binary_easy_1`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Pattern**: Malignant versus benign tissue assessment  
**Domain**: Pathology (histopathological imaging)

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct questions about tissue malignancy in histopathological images. This assessment is fundamental to pathological practice, representing the core cancer diagnosis decision that affects treatment planning and patient prognosis.

The template is designed for pathology datasets where tissue samples are labeled as malignant or benign, testing the model's ability to recognize key histopathological features that distinguish cancerous from non-cancerous tissues using established morphological criteria.

## Question Generation Pattern

### Question Format
```
"Based on the histopathological features, is this tissue malignant or benign?"
```

### Answer Format
Binary choice with clinical options:
- A. Malignant
- B. Benign

### Template Variables
- `{tissue_type}`: The specific type of tissue being examined
- `{staining_method}`: H&E, immunohistochemistry, or special stains
- `{magnification}`: Microscopic magnification level
- `{cellular_features}`: Key morphological characteristics visible

### Clinical Context
- **Malignant**: Tissues showing characteristics of cancer (cellular atypia, invasiveness, mitotic activity)
- **Benign**: Non-cancerous tissues (normal architecture, minimal atypia, regular cell organization)
- **Morphological Criteria**: Nuclear pleomorphism, mitotic rate, tissue architecture disruption
- **Clinical Importance**: Accurate diagnosis guides treatment decisions and prognosis

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Based on the histopathological features, is this tissue malignant or benign?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Malignant",
    "Benign"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Tissue shows nuclear pleomorphism, increased mitotic activity, and architectural disruption consistent with malignancy",
  "provenance": {
    "original_label": "malignant",
    "rule_id": "pathology_classification_binary_easy_1",
    "annotation_id": "tissue_classification",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Histopathological slides (H&E, immunohistochemistry, special stains)
- **Labels**: Binary labels indicating malignant/benign status
- **Quality**: Sufficient resolution for cellular and architectural assessment

### Compatible Datasets

**Available in MBU Metadata:**
- `Alwaly/Breast_Cancer-cancer` - 10,000 breast cancer images with benign/malignant labels
- `akinsanyaayomide/cancer_malignant_benign` - Cancer classification with malignant/benign categories
- `Alwaly/breast_cancer` - Breast cancer histopathology with diagnostic labels

**General Categories:**
- Cancer classification datasets (various organ systems)
- Tumor vs normal tissue datasets
- Histopathological cancer detection collections
- Digital pathology archives with malignancy labels
- Whole slide imaging datasets with diagnostic annotations

### Minimum Standards
- **Image Quality**: High enough resolution to assess cellular morphology
- **Annotation Quality**: Expert pathologist validation preferred
- **Data Distribution**: Balanced representation of malignant and benign tissues

## Template Usage Rules

### Question Construction Rules
1. Always reference "histopathological features" to focus on microscopic assessment
2. Use clinical terminology (malignant/benign) rather than generic terms
3. Maintain consistency with pathological diagnostic workflows
4. Avoid leading questions that bias toward specific answers

### Answer Assignment Rules
1. Map "malignant", "cancer", "carcinoma", "sarcoma" → "Malignant"
2. Map "benign", "normal", "non-cancerous", "reactive" → "Benign"
3. Use original dataset labels as ground truth
4. Handle ambiguous cases by referencing pathological diagnosis when available

### Quality Control Guidelines
1. Verify clinical accuracy of question-answer pairs
2. Ensure terminology aligns with pathological standards
3. Cross-validate with established diagnostic criteria
4. Review for potential bias in question phrasing

## Examples

### Example 1: Adenocarcinoma Detection
**Image**: H&E stained section showing glandular malignancy  
**Question**: "Based on the histopathological features, is this tissue malignant or benign?"  
**Answer**: A. Malignant  
**Rationale**: Tissue shows irregular glandular architecture, nuclear pleomorphism, and increased mitotic activity consistent with adenocarcinoma

### Example 2: Benign Fibrous Tissue
**Image**: H&E stained section showing organized connective tissue  
**Question**: "Based on the histopathological features, is this tissue malignant or benign?"  
**Answer**: B. Benign  
**Rationale**: Tissue demonstrates organized collagenous stroma with mature fibroblasts and no cellular atypia, consistent with benign fibrous tissue

### Example 3: Squamous Cell Carcinoma
**Image**: H&E stained section showing invasive squamous malignancy  
**Question**: "Based on the histopathological features, is this tissue malignant or benign?"  
**Answer**: A. Malignant  
**Rationale**: Tissue shows invasive squamous epithelium with keratin pearl formation and high-grade cellular atypia

### Example 4: Normal Epithelium
**Image**: H&E stained section showing organized epithelial tissue  
**Question**: "Based on the histopathological features, is this tissue malignant or benign?"  
**Answer**: B. Benign  
**Rationale**: Tissue demonstrates well-organized epithelial architecture with normal maturation and no atypia

### Example 5: Sarcoma Identification
**Image**: H&E stained section showing spindle cell malignancy  
**Question**: "Based on the histopathological features, is this tissue malignant or benign?"  
**Answer**: A. Malignant  
**Rationale**: Tissue shows highly cellular spindle cell proliferation with marked nuclear atypia and high mitotic rate consistent with sarcoma

## Implementation Notes

### Technical Considerations
- Ensure high-quality image preprocessing to maintain histological detail
- Consider multi-scale analysis for different magnifications
- Implement proper color normalization for stained sections
- Handle varying slide preparation and staining protocols

### Clinical Validation
- Cross-reference with established pathological guidelines
- Validate against expert pathologist diagnoses when available
- Consider inter-observer variability in pathological assessment
- Align with current histopathological diagnostic criteria

### Dataset-Specific Adaptations
- **Cancer datasets**: Leverage metadata for tumor type and grade
- **Multi-organ datasets**: Consider organ-specific morphological variations
- **Research datasets**: Focus on well-validated diagnostic criteria
- **Clinical datasets**: Emphasize practical diagnostic applications

### Quality Assurance
- Regular review by board-certified pathologists
- Validation against multiple expert opinions
- Continuous monitoring of model performance on diagnostic metrics
- Updates based on evolving pathological diagnostic criteria
