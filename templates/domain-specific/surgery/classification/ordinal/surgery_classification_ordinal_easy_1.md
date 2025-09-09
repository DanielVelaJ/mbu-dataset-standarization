# Surgery Surgical Skill Assessment Template

## Template Overview

**Template ID**: `surgery_classification_ordinal_easy_1`  
**Task Type**: Ordinal classification  
**Difficulty**: Easy  
**Question Pattern**: Surgical skill level evaluation  
**Medical Domain**: Surgery (surgical education and assessment)  
**Domain-knowledge summary**: Requires specialized surgical education knowledge and assessment expertise. Must understand surgical competency metrics, technical skill progression, instrument handling proficiency, suturing quality, tissue manipulation techniques, and ability to evaluate surgical performance levels from novice to expert based on visual assessment criteria.

## Template Description

This template converts ordinal classification datasets into MCVQA format by asking questions about surgical skill levels demonstrated in procedural segments. This assessment is important for surgical training evaluation and competency assessment, using established skill assessment criteria.

The template is designed for surgery datasets with skill level annotations, testing the model's ability to evaluate technical proficiency, efficiency, and quality of surgical performance based on visual assessment.

## Question Generation Pattern

### Question Format
```
"Rate the surgical skill level demonstrated in this procedural segment."
```

### Answer Format
Ordinal choice with skill level progression:
- A. Novice (1) - Basic movements, hesitant technique
- B. Advanced beginner (2) - Improving coordination, some confidence
- C. Competent (3) - Adequate technique, reasonable efficiency  
- D. Proficient (4) - Smooth technique, good efficiency
- E. Expert (5) - Masterful technique, optimal efficiency

### Template Variables
- `{technical_precision}`: Accuracy and control of surgical movements
- `{procedural_efficiency}`: Speed and workflow optimization
- `{tissue_handling}`: Quality of tissue manipulation and respect
- `{instrument_use}`: Proficiency with surgical instruments and techniques

### Clinical Context
- **Skill Assessment**: Systematic evaluation of surgical competency and proficiency
- **Training Applications**: Objective assessment for surgical education programs
- **Competency Evaluation**: Standardized assessment for certification and credentialing
- **Quality Improvement**: Performance monitoring and skill development tracking

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Rate the surgical skill level demonstrated in this procedural segment.",
  "answer": "D",
  "answer_type": "single_label",
  "options": [
    "Novice (1) - Basic movements, hesitant technique",
    "Advanced beginner (2) - Improving coordination, some confidence",
    "Competent (3) - Adequate technique, reasonable efficiency",
    "Proficient (4) - Smooth technique, good efficiency", 
    "Expert (5) - Masterful technique, optimal efficiency"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.8,
  "rationale": "Demonstration shows smooth, coordinated movements with good efficiency and appropriate tissue handling typical of proficient skill level",
  "provenance": {
    "original_label": "proficient",
    "rule_id": "surgery_classification_ordinal_easy_1",
    "annotation_id": "surgical_skill_assessment",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Surgical video segments or images showing technical performance
- **Labels**: Skill level annotations based on established assessment criteria
- **Quality**: Clear visualization of surgical technique and instrument handling

### Compatible Datasets
- Surgical training assessment datasets
- Skill evaluation video collections
- Competency assessment databases
- Surgical education video libraries
- Performance evaluation archives

### Minimum Standards
- **Image Quality**: Sufficient detail for technique assessment and evaluation
- **Annotation Quality**: Expert validation by surgical educators and experienced surgeons
- **Data Distribution**: Representative examples across all skill levels

## Template Usage Rules

### Question Construction Rules
1. Reference established surgical skill assessment criteria
2. Use progressive skill level terminology
3. Focus on observable technical performance indicators
4. Maintain consistency with surgical education standards

### Answer Assignment Rules
1. Map basic, hesitant movements → "Novice (1)"
2. Map improving coordination → "Advanced beginner (2)"
3. Map adequate technique → "Competent (3)"
4. Map smooth, efficient performance → "Proficient (4)"
5. Map masterful technique → "Expert (5)"

### Quality Control Guidelines
1. Ensure assessment reflects established skill evaluation criteria
2. Verify consistency with surgical education standards
3. Cross-validate with expert surgical educator assessment
4. Review for educational and training application validity

## Examples

### Example 1: Expert Level Performance
**Image**: Surgical video showing masterful technique with optimal efficiency  
**Question**: "Rate the surgical skill level demonstrated in this procedural segment."  
**Answer**: E. Expert (5) - Masterful technique, optimal efficiency  
**Rationale**: Performance demonstrates exceptional technical mastery with optimal workflow, precision, and efficiency

### Example 2: Novice Level Technique
**Image**: Surgical video showing hesitant movements and basic technique  
**Question**: "Rate the surgical skill level demonstrated in this procedural segment."  
**Answer**: A. Novice (1) - Basic movements, hesitant technique  
**Rationale**: Performance shows basic movements with hesitation and limited coordination typical of early learning stage

### Example 3: Competent Performance
**Image**: Surgical video showing adequate technique with reasonable efficiency  
**Question**: "Rate the surgical skill level demonstrated in this procedural segment."  
**Answer**: C. Competent (3) - Adequate technique, reasonable efficiency  
**Rationale**: Performance demonstrates adequate technical skills with reasonable efficiency and appropriate task completion

### Example 4: Proficient Skill Display
**Image**: Surgical video showing smooth, coordinated technique  
**Question**: "Rate the surgical skill level demonstrated in this procedural segment."  
**Answer**: D. Proficient (4) - Smooth technique, good efficiency  
**Rationale**: Performance shows smooth, well-coordinated movements with good efficiency and confident technique execution

### Example 5: Advanced Beginner Level
**Image**: Surgical video showing improving coordination with some confidence  
**Question**: "Rate the surgical skill level demonstrated in this procedural segment."  
**Answer**: B. Advanced beginner (2) - Improving coordination, some confidence  
**Rationale**: Performance demonstrates improving coordination and growing confidence beyond basic novice level

## Implementation Notes

### Technical Considerations
- Implement movement analysis and technique assessment algorithms
- Consider temporal aspects of surgical performance and workflow
- Account for different procedures and complexity levels
- Handle varying video quality and camera angles

### Clinical Validation
- Align with established surgical skill assessment frameworks (OSATS, GOALS)
- Cross-reference with surgical education competency standards
- Validate against expert surgical educator assessments
- Consider specialty-specific skill requirements

### Dataset-Specific Adaptations
- **Training datasets**: Include clear examples of each skill level
- **Assessment datasets**: Focus on discriminative features between skill levels
- **Multi-procedure datasets**: Account for procedure-specific skill requirements
- **Longitudinal datasets**: Track skill progression over time

### Quality Assurance
- Regular validation by surgical educators and training program directors
- Cross-reference with established skill assessment literature
- Monitoring for consistency across different surgical procedures and specialties
- Updates based on evolving surgical education standards and assessment methodologies
