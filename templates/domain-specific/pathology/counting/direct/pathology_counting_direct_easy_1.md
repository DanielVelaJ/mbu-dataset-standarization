# Pathology Mitotic Figure Counting Assessment Template

## Template Overview

**Template ID**: `pathology_counting_direct_easy_1`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Mitotic figure density evaluation  
**Domain**: Pathology (histopathological imaging)

## Template Description

This template converts counting datasets into MCVQA format by asking questions about mitotic figure density in histopathological images. While original counting tasks produce exact integer counts, this template evaluates the model's ability to assess mitotic activity levels through multiple choice questions, which is more clinically relevant for grading purposes.

The template is designed for pathology datasets with mitotic figure annotations, testing the model's understanding of proliferation assessment and tumor grading criteria based on mitotic activity.

## Question Generation Pattern

### Question Format
```
"What best describes the mitotic activity level in this high-power field?"
```

### Answer Format
Multiclass choice with mitotic activity options:
- A. High mitotic activity (>10 mitoses per HPF)
- B. Moderate mitotic activity (5-10 mitoses per HPF)
- C. Low mitotic activity (1-4 mitoses per HPF)
- D. Rare mitotic figures (<1 mitosis per HPF)
- E. No mitotic figures identified

### Template Variables
- `{mitotic_count}`: Number of mitotic figures in the field
- `{field_area}`: High-power field area for standardization
- `{proliferation_pattern}`: Distribution and morphology of mitotic figures
- `{grading_relevance}`: Clinical significance for tumor grading

### Clinical Context
- **Mitotic Count**: Critical component of tumor grading systems (Nottingham, WHO)
- **High-Power Field**: Standardized area (typically 0.237 mm²) for count normalization
- **Grading Significance**: Higher mitotic counts correlate with aggressive tumor behavior
- **Clinical Applications**: Breast cancer grading, sarcoma assessment, lymphoma classification

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What best describes the mitotic activity level in this high-power field?",
  "answer": "B",
  "answer_type": "single_label",
  "options": [
    "High mitotic activity (>10 mitoses per HPF)",
    "Moderate mitotic activity (5-10 mitoses per HPF)",
    "Low mitotic activity (1-4 mitoses per HPF)", 
    "Rare mitotic figures (<1 mitosis per HPF)",
    "No mitotic figures identified"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.85,
  "rationale": "Field contains 7 clearly identifiable mitotic figures corresponding to moderate proliferative activity",
  "provenance": {
    "original_label": "7_mitoses",
    "rule_id": "pathology_counting_direct_easy_1",
    "annotation_id": "mitotic_count_assessment",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: High-power field histopathological images
- **Annotations**: Mitotic figure counts or density information
- **Quality**: Sufficient resolution for mitotic figure identification

### Compatible Datasets
- Mitotic figure counting challenge datasets
- Tumor grading validation collections
- Proliferation index assessment datasets
- Cancer classification with mitotic data
- Digital pathology counting benchmarks

### Minimum Standards
- **Image Quality**: Clear visualization of mitotic morphology
- **Annotation Quality**: Expert pathologist validation of mitotic identification
- **Data Distribution**: Range of mitotic activities from low to high

## Template Usage Rules

### Question Construction Rules
1. Reference high-power field standardization
2. Use clinically relevant mitotic activity categories
3. Focus on proliferation assessment for grading
4. Maintain consistency with established grading systems

### Answer Assignment Rules
1. Map >10 mitoses per HPF → "High mitotic activity"
2. Map 5-10 mitoses per HPF → "Moderate mitotic activity"
3. Map 1-4 mitoses per HPF → "Low mitotic activity"
4. Map <1 mitosis per HPF → "Rare mitotic figures"
5. Map 0 mitoses per HPF → "No mitotic figures identified"

### Quality Control Guidelines
1. Ensure counts reflect actual mitotic activity levels
2. Verify consistency with tumor grading criteria
3. Cross-validate with expert pathologist counts
4. Review for standardized high-power field assessment

## Examples

### Example 1: High-Grade Sarcoma
**Image**: H&E section showing numerous mitotic figures in spindle cell tumor  
**Question**: "What best describes the mitotic activity level in this high-power field?"  
**Answer**: A. High mitotic activity (>10 mitoses per HPF)  
**Rationale**: Field shows 15 clearly identifiable mitotic figures indicating high proliferative activity typical of high-grade sarcoma

### Example 2: Moderate-Grade Carcinoma
**Image**: H&E section showing moderate mitotic activity in epithelial tumor  
**Question**: "What best describes the mitotic activity level in this high-power field?"  
**Answer**: B. Moderate mitotic activity (5-10 mitoses per HPF)  
**Rationale**: Field contains 7 mitotic figures representing moderate proliferative activity in intermediate-grade malignancy

### Example 3: Low-Grade Neoplasm
**Image**: H&E section showing few mitotic figures in well-differentiated tumor  
**Question**: "What best describes the mitotic activity level in this high-power field?"  
**Answer**: C. Low mitotic activity (1-4 mitoses per HPF)  
**Rationale**: Field displays 3 mitotic figures consistent with low proliferative activity in well-differentiated neoplasm

### Example 4: Benign Proliferation
**Image**: H&E section showing minimal mitotic activity  
**Question**: "What best describes the mitotic activity level in this high-power field?"  
**Answer**: D. Rare mitotic figures (<1 mitosis per HPF)  
**Rationale**: Field shows occasional mitotic figure reflecting minimal proliferative activity typical of benign lesions

### Example 5: Quiescent Tissue
**Image**: H&E section showing mature tissue without mitoses  
**Question**: "What best describes the mitotic activity level in this high-power field?"  
**Answer**: E. No mitotic figures identified  
**Rationale**: Field lacks identifiable mitotic figures indicating quiescent tissue with minimal proliferative activity

## Implementation Notes

### Technical Considerations
- Implement mitotic figure recognition and morphological validation
- Consider high-power field standardization across different systems
- Account for staining variations affecting mitotic visibility
- Handle different tumor types and grading systems

### Clinical Validation
- Align with established tumor grading systems (Nottingham, WHO)
- Cross-reference with clinical proliferation indices
- Validate against expert pathologist mitotic counts
- Consider prognostic significance of mitotic activity levels

### Dataset-Specific Adaptations
- **Breast cancer datasets**: Apply Nottingham grading criteria
- **Sarcoma datasets**: Use sarcoma-specific grading systems
- **Lymphoma datasets**: Consider proliferation index requirements
- **Multi-tumor datasets**: Standardize across different grading systems

### Quality Assurance
- Regular validation by pathologists experienced in tumor grading
- Cross-reference with established mitotic counting protocols
- Monitoring for consistency across different tumor types
- Updates based on evolving grading system requirements and digital pathology standards
