# Other-Medical Laboratory Animal Species Identification Template

## Template Overview

**Template ID**: `other-medical_classification_multiclass_easy_4`  
**Task Type**: Multiclass classification  
**Difficulty**: Easy  
**Question Pattern**: Laboratory animal species recognition  
**Medical Domain**: Other-Medical (veterinary and research imaging)  
**Domain-knowledge summary**: Requires general veterinary and research knowledge for laboratory animal identification. Must understand animal anatomy, species characteristics, laboratory animal models, comparative anatomy, and ability to distinguish between different animal species used in biomedical research and veterinary applications.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about laboratory animal species in research imaging. This capability is important for veterinary medicine, biomedical research standardization, and animal model identification applications.

The template is designed for other-medical datasets with animal species annotations, testing the model's ability to identify different laboratory animal species used in biomedical research and veterinary applications.

## Question Generation Pattern

### Question Format
```
"What laboratory animal species is shown in this research imaging?"
```

### Answer Format
Multiclass choice with animal species options:
- A. Mouse
- B. Rat
- C. Rabbit
- D. Non-human primate
- E. Zebrafish
- F. Dog
- G. Pig
- H. Other rodent

### Template Variables
- `{anatomical_features}`: Species-specific anatomical characteristics and proportions
- `{size_scale}`: Relative size and scaling references
- `{research_context}`: Laboratory or veterinary imaging setting
- `{morphological_markers}`: Distinctive species identification features

### Clinical Context
- **Research Applications**: Animal model identification for biomedical studies
- **Veterinary Medicine**: Species identification for clinical care
- **Regulatory Compliance**: Proper species documentation for research protocols
- **Comparative Medicine**: Cross-species research and translational studies

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What laboratory animal species is shown in this research imaging?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Mouse",
    "Rat",
    "Rabbit",
    "Non-human primate",
    "Zebrafish",
    "Dog",
    "Pig",
    "Other rodent"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Animal shows characteristic mouse anatomy with appropriate size scale and morphological features",
  "provenance": {
    "original_label": "mouse",
    "rule_id": "other-medical_classification_multiclass_easy_4",
    "annotation_id": "animal_species_identification",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Laboratory animal imaging from research or veterinary contexts
- **Labels**: Animal species annotations with research context
- **Quality**: Clear visualization of species-specific anatomical features

### Compatible Datasets
- Laboratory animal research datasets
- Veterinary imaging collections
- Animal model identification databases
- Comparative medicine imaging archives
- Research animal welfare datasets

### Minimum Standards
- **Image Quality**: Sufficient detail for species identification and differentiation
- **Annotation Quality**: Expert validation by veterinarians or animal researchers
- **Data Distribution**: Representative examples of common laboratory animal species

## Template Usage Rules

### Question Construction Rules
1. Focus on laboratory and research animal species identification
2. Use standard veterinary and research terminology
3. Consider anatomical features and research context
4. Emphasize biomedical research and veterinary applications

### Answer Assignment Rules
1. Map small rodents with characteristic mouse features → "Mouse"
2. Map larger rodents with rat characteristics → "Rat"
3. Map lagomorphs with long ears → "Rabbit"
4. Map primates with human-like features → "Non-human primate"
5. Map aquatic vertebrates → "Zebrafish"
6. Map canines → "Dog"
7. Map swine → "Pig"
8. Map other small rodent species → "Other rodent"

### Quality Control Guidelines
1. Ensure accurate species identification based on anatomical features
2. Verify consistency with veterinary and research animal standards
3. Cross-validate with expert veterinarian or animal researcher assessment
4. Review for research and educational applications

## Examples

### Example 1: Laboratory Mouse
**Image**: Research imaging showing small rodent with characteristic mouse features  
**Question**: "What laboratory animal species is shown in this research imaging?"  
**Answer**: A. Mouse  
**Rationale**: Animal displays characteristic mouse anatomy with appropriate size, ear shape, and body proportions

### Example 2: Research Rat
**Image**: Laboratory imaging showing larger rodent with rat characteristics  
**Question**: "What laboratory animal species is shown in this research imaging?"  
**Answer**: B. Rat  
**Rationale**: Animal shows typical rat features including larger size compared to mouse and characteristic body proportions

### Example 3: Laboratory Rabbit
**Image**: Research imaging showing lagomorph with long ears  
**Question**: "What laboratory animal species is shown in this research imaging?"  
**Answer**: C. Rabbit  
**Rationale**: Animal demonstrates characteristic rabbit anatomy with long ears, body size, and lagomorph features

### Example 4: Zebrafish Model
**Image**: Research imaging showing small striped fish in laboratory setting  
**Question**: "What laboratory animal species is shown in this research imaging?"  
**Answer**: E. Zebrafish  
**Rationale**: Image shows characteristic zebrafish with striped pattern and aquatic vertebrate anatomy used in research

### Example 5: Primate Research Model
**Image**: Laboratory imaging showing non-human primate  
**Question**: "What laboratory animal species is shown in this research imaging?"  
**Answer**: D. Non-human primate  
**Rationale**: Animal displays primate characteristics with human-like features used in biomedical research applications

## Implementation Notes

### Technical Considerations
- Implement species-specific anatomical feature recognition
- Consider size scaling and proportional relationships
- Account for different imaging modalities and research contexts
- Handle varying animal positions and orientations

### Clinical Validation
- Align with veterinary medicine and research animal standards
- Cross-reference with laboratory animal identification guides
- Validate against expert veterinarian and animal researcher assessment
- Consider research protocol and regulatory requirements

### Dataset-Specific Adaptations
- **Research datasets**: Focus on common laboratory animal models
- **Veterinary datasets**: Include clinical care and diagnostic applications
- **Comparative datasets**: Emphasize cross-species research applications
- **Regulatory datasets**: Support protocol compliance and documentation

### Quality Assurance
- Regular validation by veterinarians and animal research specialists
- Cross-reference with laboratory animal identification standards
- Monitoring for accuracy across different animal species and research contexts
- Updates based on evolving research animal use and welfare standards
