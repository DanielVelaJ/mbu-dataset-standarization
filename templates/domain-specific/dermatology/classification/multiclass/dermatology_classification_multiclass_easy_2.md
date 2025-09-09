# Dermatology Dermoscopic Pattern Recognition Template

## Template Overview

**Template ID**: `dermatology_classification_multiclass_easy_2`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Dermoscopic pattern identification  
**Domain**: Dermatology (dermoscopy imaging)

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking direct questions about dermoscopic patterns in skin lesions. Dermoscopic pattern recognition is essential for lesion evaluation, as specific patterns are associated with different types of lesions and help guide clinical decision-making.

The template is designed for dermoscopy datasets where lesions exhibit distinct dermoscopic patterns, testing the model's ability to recognize and classify the specialized visual patterns visible under dermoscopic examination.

## Question Generation Pattern

### Question Format
```
"What is the primary dermoscopic pattern visible in this lesion?"
```

### Answer Format
Multiclass choice with dermoscopic pattern options:
- A. Reticular pattern
- B. Globular pattern
- C. Homogeneous pattern
- D. Starburst pattern
- E. Multicomponent pattern

### Template Variables
- `{pattern_description}`: Detailed description of the visible pattern
- `{lesion_type}`: Type of lesion showing the pattern
- `{pattern_distribution}`: How the pattern is distributed across the lesion
- `{associated_features}`: Additional dermoscopic features present

### Clinical Context
- **Reticular Pattern**: Network of lines, common in benign nevi
- **Globular Pattern**: Round to oval structures, seen in various lesions
- **Homogeneous Pattern**: Uniform coloration without specific structure
- **Starburst Pattern**: Radial projections, often in Spitz nevi or melanoma
- **Multicomponent Pattern**: Multiple patterns present, concerning for melanoma

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What is the primary dermoscopic pattern visible in this lesion?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Reticular pattern",
    "Globular pattern",
    "Homogeneous pattern", 
    "Starburst pattern",
    "Multicomponent pattern"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.88,
  "rationale": "Well-defined network of brown lines creating reticular pattern typical of benign nevus",
  "provenance": {
    "original_label": "reticular",
    "rule_id": "dermatology_classification_multiclass_easy_2",
    "annotation_id": "dermoscopic_pattern",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: High-quality dermoscopic images with clear pattern visualization
- **Labels**: Dermoscopic pattern classifications by trained dermoscopists
- **Quality**: Sufficient magnification and clarity for pattern recognition

### Compatible Datasets
- Dermoscopy pattern databases
- ISIC dermoscopic challenges
- Melanocytic lesion dermoscopy collections
- Educational dermoscopy atlases
- Pattern-annotated dermoscopy datasets

### Minimum Standards
- **Image Quality**: Clear dermoscopic visualization with proper illumination
- **Annotation Quality**: Expert dermoscopist pattern identification
- **Data Distribution**: Representative examples of each pattern type

## Template Usage Rules

### Question Construction Rules
1. Focus on "primary" pattern when multiple patterns may be present
2. Use standard dermoscopic terminology
3. Emphasize pattern recognition skills
4. Maintain consistency with dermoscopic education standards

### Answer Assignment Rules
1. Map network/pigment network → "Reticular pattern"
2. Map globules/dots → "Globular pattern"
3. Map structureless/diffuse → "Homogeneous pattern"
4. Map streaks/radial → "Starburst pattern"
5. Map multiple patterns → "Multicomponent pattern"

### Quality Control Guidelines
1. Verify alignment with international dermoscopy standards
2. Ensure consistency with dermoscopic pattern terminology
3. Cross-validate with expert dermoscopist assessments
4. Review for proper pattern classification criteria

## Examples

### Example 1: Reticular Pattern Recognition
**Image**: Dermoscopic image showing well-defined brown network  
**Question**: "What is the primary dermoscopic pattern visible in this lesion?"  
**Answer**: A. Reticular pattern  
**Rationale**: Clear network of intersecting brown lines creating classic reticular pattern

### Example 2: Globular Pattern Identification
**Image**: Dermoscopic image with multiple round brown structures  
**Question**: "What is the primary dermoscopic pattern visible in this lesion?"  
**Answer**: B. Globular pattern  
**Rationale**: Multiple round to oval brown globules distributed throughout the lesion

### Example 3: Homogeneous Pattern Assessment
**Image**: Dermoscopic image showing uniform tan coloration without structure  
**Question**: "What is the primary dermoscopic pattern visible in this lesion?"  
**Answer**: C. Homogeneous pattern  
**Rationale**: Uniform, structureless tan pigmentation without specific dermoscopic features

### Example 4: Starburst Pattern Evaluation
**Image**: Dermoscopic image with radial streaming at lesion periphery  
**Question**: "What is the primary dermoscopic pattern visible in this lesion?"  
**Answer**: D. Starburst pattern  
**Rationale**: Radial projections extending from lesion center creating starburst appearance

### Example 5: Multicomponent Pattern Recognition
**Image**: Dermoscopic image showing network, globules, and structureless areas  
**Question**: "What is the primary dermoscopic pattern visible in this lesion?"  
**Answer**: E. Multicomponent pattern  
**Rationale**: Multiple dermoscopic patterns present including network, globular, and homogeneous areas

## Implementation Notes

### Technical Considerations
- Optimize for high-resolution dermoscopic image analysis
- Implement pattern recognition algorithms specific to dermoscopic features
- Consider variable lighting and magnification in dermoscopic images
- Handle overlapping or transitional pattern areas

### Clinical Validation
- Align with international dermoscopy consensus guidelines
- Cross-reference with established dermoscopic pattern criteria
- Validate against expert dermoscopist pattern recognition
- Consider pattern-lesion type correlations

### Dataset-Specific Adaptations
- **Educational datasets**: Emphasize clear, classic pattern examples
- **Clinical datasets**: Handle subtle or mixed pattern presentations
- **Challenge datasets**: Focus on diagnostically relevant patterns
- **Research datasets**: Consider novel or evolving pattern classifications

### Quality Assurance
- Regular review by certified dermoscopists
- Validation against dermoscopic pattern atlases
- Monitoring for consistent pattern recognition across lesion types
- Updates based on evolving dermoscopic terminology and criteria
