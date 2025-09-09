# Pathology Cancer Type Classification Template

## Template Overview

**Template ID**: `pathology_classification_multiclass_easy_1`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Specific cancer type identification  
**Domain**: Pathology (histopathological imaging)

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking direct questions about specific cancer types in histopathological images. This classification is crucial for treatment planning, as different cancer types require distinct therapeutic approaches and have varying prognoses.

The template is designed for pathology datasets where malignant tissues are classified into specific cancer types, testing the model's ability to distinguish between major categories of malignancies based on their characteristic histopathological features.

## Question Generation Pattern

### Question Format
```
"What type of cancer is most consistent with these histopathological features?"
```

### Answer Format
Multiclass choice with oncological options:
- A. Adenocarcinoma
- B. Squamous cell carcinoma
- C. Small cell carcinoma
- D. Large cell carcinoma
- E. Sarcoma

### Template Variables
- `{cancer_features}`: Specific morphological features visible
- `{tissue_architecture}`: Architectural patterns and organization
- `{cellular_morphology}`: Cell shape, size, and nuclear characteristics
- `{special_features}`: Diagnostic features unique to cancer types

### Clinical Context
- **Adenocarcinoma**: Glandular architecture, mucin production, epithelial origin
- **Squamous Cell Carcinoma**: Keratin production, intercellular bridges, squamous differentiation
- **Small Cell Carcinoma**: Small cells with scant cytoplasm, high nuclear-to-cytoplasmic ratio
- **Large Cell Carcinoma**: Large cells with prominent nucleoli, undifferentiated features
- **Sarcoma**: Mesenchymal origin, spindle or round cell morphology, stromal proliferation

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What type of cancer is most consistent with these histopathological features?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Adenocarcinoma",
    "Squamous cell carcinoma",
    "Small cell carcinoma",
    "Large cell carcinoma",
    "Sarcoma"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Tissue shows glandular architecture with mucin production consistent with adenocarcinoma",
  "provenance": {
    "original_label": "adenocarcinoma",
    "rule_id": "pathology_classification_multiclass_easy_1",
    "annotation_id": "cancer_type_classification",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Histopathological sections of various cancer types
- **Labels**: Multiclass labels indicating specific cancer types
- **Quality**: Sufficient resolution for morphological differentiation

### Compatible Datasets

**Available in MBU Metadata:**
- `Aliounethegoat/classification-medicale-multi-cancer` - Multi-cancer classification across cancer types
- `Alwaly/Lung_and_Colon_Cancer` - 25,000 images with lung and colon cancer subtypes (colon_aca, colon_bnt, lung_aca, lung_bnt, lung_scc)
- `Alwaly/Lymphoma-cancer` - 15,000 lymphoma images with three subtypes (lymph_cll, lymph_fl, lymph_mcl)

**General Categories:**
- Multi-cancer classification datasets
- Organ-specific cancer typing collections
- Digital pathology cancer archives
- WHO classification validation datasets
- Cancer subtype identification sets

### Minimum Standards
- **Image Quality**: Clear visualization of diagnostic morphological features
- **Annotation Quality**: Expert pathologist validation with WHO classification
- **Data Distribution**: Representative samples across major cancer types

## Template Usage Rules

### Question Construction Rules
1. Focus on histopathological features as diagnostic determinants
2. Use established oncological terminology
3. Reference morphological assessment criteria
4. Maintain consistency with WHO classification systems

### Answer Assignment Rules
1. Map glandular tumors → "Adenocarcinoma"
2. Map keratinizing epithelial tumors → "Squamous cell carcinoma"
3. Map small round cell tumors → "Small cell carcinoma"
4. Map large undifferentiated epithelial tumors → "Large cell carcinoma"
5. Map mesenchymal tumors → "Sarcoma"

### Quality Control Guidelines
1. Ensure consistency with WHO cancer classification
2. Verify correlation between morphological features and cancer type
3. Cross-validate with expert pathologist assessments
4. Review for diagnostic accuracy across cancer types

## Examples

### Example 1: Pulmonary Adenocarcinoma
**Image**: H&E section showing glandular tumor in lung  
**Question**: "What type of cancer is most consistent with these histopathological features?"  
**Answer**: A. Adenocarcinoma  
**Rationale**: Tumor shows well-formed glandular architecture with mucin production typical of pulmonary adenocarcinoma

### Example 2: Squamous Cell Carcinoma
**Image**: H&E section showing keratinizing epithelial tumor  
**Question**: "What type of cancer is most consistent with these histopathological features?"  
**Answer**: B. Squamous cell carcinoma  
**Rationale**: Tumor demonstrates keratin pearl formation and intercellular bridges characteristic of squamous cell carcinoma

### Example 3: Small Cell Lung Cancer
**Image**: H&E section showing small round blue cell tumor  
**Question**: "What type of cancer is most consistent with these histopathological features?"  
**Answer**: C. Small cell carcinoma  
**Rationale**: Tumor shows small cells with high nuclear-to-cytoplasmic ratio and neuroendocrine features typical of small cell carcinoma

### Example 4: Large Cell Carcinoma
**Image**: H&E section showing poorly differentiated large cell tumor  
**Question**: "What type of cancer is most consistent with these histopathological features?"  
**Answer**: D. Large cell carcinoma  
**Rationale**: Tumor displays large cells with prominent nucleoli and lack of specific differentiation features

### Example 5: Soft Tissue Sarcoma
**Image**: H&E section showing spindle cell mesenchymal tumor  
**Question**: "What type of cancer is most consistent with these histopathological features?"  
**Answer**: E. Sarcoma  
**Rationale**: Tumor shows spindle cell morphology with mesenchymal differentiation characteristic of sarcoma

## Implementation Notes

### Technical Considerations
- Implement morphological pattern recognition for cancer classification
- Consider architectural and cellular feature analysis
- Account for organ-specific cancer type variations
- Handle different grades and differentiation levels

### Clinical Validation
- Align with WHO classification of tumors
- Cross-reference with established diagnostic criteria
- Validate against expert pathologist consensus
- Consider immunohistochemical correlation when available

### Dataset-Specific Adaptations
- **Organ-specific datasets**: Focus on relevant cancer types for each organ
- **Multi-institutional datasets**: Standardize classification criteria
- **Research datasets**: Emphasize well-characterized examples
- **Clinical datasets**: Include practical diagnostic challenges

### Quality Assurance
- Regular review by expert pathologists specializing in cancer diagnosis
- Validation against WHO tumor classification guidelines
- Monitoring for diagnostic accuracy across cancer types and organs
- Updates based on evolving cancer classification systems
