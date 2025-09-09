# Ophthalmology Comparative Fundus Analysis Template

## Template Overview

**Template ID**: `domain-specific_ophthalmology_classification_multiclass_easy_4`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Question Pattern**: Comparative pathology assessment between retinal quadrants  
**Medical Domain**: Ophthalmology (fundus imaging and comparative pathology assessment)  
**Domain-knowledge summary**: Requires specialized knowledge of retinal pathology distribution and comparative assessment techniques. Understanding of retinal quadrant anatomy, pathological pattern recognition, disease distribution patterns, hemorrhage classification, exudate patterns, and comparative analysis methodology. Knowledge of retinal pathology terminology, quadrant-specific disease predilection, and clinical significance of pathological distribution patterns.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about comparative pathology assessment between different quadrants of the fundus. It focuses on identifying which region shows more severe pathological changes, which is crucial for disease staging, treatment planning, and monitoring progression.

The template is designed for ophthalmology datasets where fundus images contain pathology with varying severity across different retinal regions, testing the model's ability to perform spatial comparisons and assess relative disease severity.

## Question Generation Pattern

### Question Format
```
"Comparing the temporal and nasal quadrants, which shows more severe pathology in this fundus image?"
```

### Answer Format
Multiple choice with comparative assessment options (A-D):
- A. Temporal quadrant more severe
- B. Nasal quadrant more severe
- C. Equal severity in both
- D. No pathology visible

### Template Variables
- `{comparison_result}`: Relative severity between regions
- `{quadrants}`: Anatomical regions being compared (temporal vs nasal)
- `{pathology_type}`: Type of pathological changes present

### Clinical Context
- **Temporal Quadrant**: Lateral aspect of the retina (toward the ear)
- **Nasal Quadrant**: Medial aspect of the retina (toward the nose)
- **Severity Assessment**: Relative degree of pathological involvement
- **Clinical Importance**: Regional assessment guides treatment decisions

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Comparing the temporal and nasal quadrants, which shows more severe pathology in this fundus image?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Temporal quadrant more severe",
    "Nasal quadrant more severe",
    "Equal severity in both",
    "No pathology visible"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Comparative pathology assessment for treatment planning",
  "provenance": {
    "original_label": "temporal_more_severe",
    "rule_id": "ophthalmology_classification_multiclass_easy_4",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification (Vision → Image-Level Classification → Multiclass classification)
- **Domain**: Ophthalmology with fundus photography showing pathology
- **Label Structure**: Categorical labels for comparative severity assessment
- **Image Type**: Fundus photographs with regional pathology variations
- **Pathology Distribution**: Varying severity across different retinal quadrants

### Compatible Datasets
- Diabetic retinopathy progression datasets
- Regional pathology assessment collections
- Disease severity grading datasets
- Multi-quadrant pathology studies
- Retinal disease monitoring databases

## Template Usage Rules

1. **Comparative Assessment**: Focus on relative rather than absolute severity
2. **Anatomical Reference**: Use standard temporal vs nasal orientation
3. **Pathology Awareness**: Consider various types of retinal pathology
4. **Clinical Relevance**: Maintain connection to treatment decision-making
5. **Severity Gradation**: Account for subtle differences in pathological involvement

## Examples

### Example 1: Temporal Quadrant More Severe
**Original Dataset**: Diabetic Retinopathy Regional Assessment  
**Original Label**: "temporal_more_severe"  
**Generated Q&A**:
- **Question**: "Comparing the temporal and nasal quadrants, which shows more severe pathology in this fundus image?"
- **Answer**: "A" (Temporal quadrant more severe)
- **Rationale**: "Greater concentration of hemorrhages and exudates in temporal retina"

### Example 2: Nasal Quadrant More Severe
**Original Dataset**: Regional Pathology Study  
**Original Label**: "nasal_more_severe"  
**Generated Q&A**:
- **Question**: "Comparing the temporal and nasal quadrants, which shows more severe pathology in this fundus image?"
- **Answer**: "B" (Nasal quadrant more severe)
- **Rationale**: "More extensive pathological changes visible in nasal retinal region"

### Example 3: Equal Severity
**Original Dataset**: Symmetric Pathology Dataset  
**Original Label**: "equal_severity"  
**Generated Q&A**:
- **Question**: "Comparing the temporal and nasal quadrants, which shows more severe pathology in this fundus image?"
- **Answer**: "C" (Equal severity in both)
- **Rationale**: "Similar degree of pathological involvement in both temporal and nasal quadrants"

### Example 4: No Pathology Visible
**Original Dataset**: Normal Fundus Control Dataset  
**Original Label**: "no_pathology"  
**Generated Q&A**:
- **Question**: "Comparing the temporal and nasal quadrants, which shows more severe pathology in this fundus image?"
- **Answer**: "D" (No pathology visible)
- **Rationale**: "Normal retinal appearance with no pathological changes detected"

### Example 5: Asymmetric Disease Pattern
**Original Dataset**: Unilateral Pathology Collection  
**Original Label**: "temporal_more_severe"  
**Generated Q&A**:
- **Question**: "Comparing the temporal and nasal quadrants, which shows more severe pathology in this fundus image?"
- **Answer**: "A" (Temporal quadrant more severe)
- **Rationale**: "Asymmetric distribution with predominant temporal involvement"

## Implementation Notes

### Advantages
- **Comparative Reasoning**: Tests spatial comparison and analysis skills
- **Clinical Relevance**: Mirrors real-world severity assessment workflows
- **Regional Assessment**: Develops understanding of disease distribution patterns
- **MCVQA Compatible**: Clear multiclass comparative choice format
- **Treatment Planning**: Directly applicable to therapeutic decision-making

### Limitations
- **Subjective Assessment**: Severity comparison may be subjective
- **Pathology Dependency**: Requires presence of pathological changes
- **Binary Comparison**: Limited to two-region comparison
- **Expertise Requirement**: Optimal assessment requires clinical knowledge

### Quality Considerations
- Ensure clear visibility of both temporal and nasal quadrants
- Verify consistency in severity assessment criteria
- Consider inter-observer variability in pathology grading
- Account for different types and patterns of retinal pathology
- Validate comparative assessments against clinical standards

### Clinical Applications
This template supports:
- **Disease Monitoring**: Tracking regional progression of retinal pathology
- **Treatment Planning**: Guiding targeted therapeutic interventions
- **Clinical Documentation**: Systematic recording of disease distribution
- **Educational Training**: Teaching comparative pathology assessment skills
- **Research Applications**: Standardized regional severity analysis for studies
