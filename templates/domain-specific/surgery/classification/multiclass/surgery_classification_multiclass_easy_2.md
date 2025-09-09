# Surgery Anatomical Structure Identification Template

## Template Overview

**Template ID**: `surgery_classification_multiclass_easy_2`  
**Task Type**: Multiclass classification  
**Difficulty**: Easy  
**Question Pattern**: Anatomical structure recognition in surgical field  
**Medical Domain**: Surgery (intraoperative imaging)  
**Domain-knowledge summary**: Requires specialized surgical anatomy knowledge for intraoperative structure identification. Must understand regional anatomy, tissue plane relationships, organ identification under surgical conditions, vascular anatomy, nerve locations, and ability to recognize anatomical landmarks during operative exposure across different surgical approaches.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about anatomical structures visible in surgical fields. This capability is critical for safe surgical navigation and avoiding iatrogenic injury during procedures.

The template is designed for surgery datasets with anatomical annotations, testing the model's ability to identify key structures that guide surgical decision-making and ensure procedural safety.

## Question Generation Pattern

### Question Format
```
"What anatomical structure is prominently displayed in this surgical field?"
```

### Answer Format
Multiclass choice with anatomical structure options:
- A. Gallbladder
- B. Liver surface
- C. Common bile duct
- D. Hepatic artery
- E. Portal vein
- F. Cystic artery
- G. Peritoneum
- H. Omentum

### Template Variables
- `{anatomical_region}`: Specific body region or operative field
- `{surgical_approach}`: Visualization method (open, laparoscopic, endoscopic)
- `{structure_characteristics}`: Visual features and anatomical relationships
- `{clinical_significance}`: Importance for surgical navigation and safety

### Clinical Context
- **Gallbladder**: Primary target organ in cholecystectomy procedures
- **Liver Surface**: Reference anatomy for hepatobiliary procedures
- **Common Bile Duct**: Critical structure requiring identification and preservation
- **Hepatic Artery**: Vascular structure essential for liver perfusion
- **Portal Vein**: Major venous structure in hepatic hilum
- **Cystic Artery**: Vessel requiring identification and ligation
- **Peritoneum**: Serosal covering providing anatomical planes
- **Omentum**: Fatty tissue often requiring manipulation or division

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What anatomical structure is prominently displayed in this surgical field?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Gallbladder",
    "Liver surface",
    "Common bile duct",
    "Hepatic artery",
    "Portal vein",
    "Cystic artery",
    "Peritoneum",
    "Omentum"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.95,
  "rationale": "Structure shows characteristic gallbladder morphology with typical position relative to liver surface",
  "provenance": {
    "original_label": "gallbladder",
    "rule_id": "surgery_classification_multiclass_easy_2",
    "annotation_id": "anatomical_structure",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Intraoperative images with clear anatomical visualization
- **Labels**: Anatomical structure annotations with clinical context
- **Quality**: Sufficient detail for structure identification and differentiation

### Compatible Datasets
- Surgical anatomy identification datasets
- Laparoscopic anatomy collections
- Surgical training anatomical references
- Intraoperative navigation datasets
- Anatomical landmark detection sets

### Minimum Standards
- **Image Quality**: Clear visualization of anatomical details and relationships
- **Annotation Quality**: Expert surgeon validation of structure identification
- **Data Distribution**: Representative coverage of critical anatomical structures

## Template Usage Rules

### Question Construction Rules
1. Focus on prominently visible anatomical structures
2. Use precise anatomical terminology
3. Consider surgical context and approach
4. Emphasize structures critical for procedural safety

### Answer Assignment Rules
1. Map primary target organs based on procedure type
2. Consider anatomical relationships and spatial context
3. Prioritize structures with highest clinical significance
4. Use established anatomical nomenclature

### Quality Control Guidelines
1. Ensure anatomical accuracy and proper nomenclature
2. Verify clinical relevance to surgical procedures
3. Cross-validate with surgical anatomy references
4. Review for educational and training value

## Examples

### Example 1: Laparoscopic Cholecystectomy View
**Image**: Clear laparoscopic view of distended gallbladder  
**Question**: "What anatomical structure is prominently displayed in this surgical field?"  
**Answer**: A. Gallbladder  
**Rationale**: Image shows characteristic pear-shaped organ with typical gallbladder wall appearance and anatomical position

### Example 2: Hepatic Surface Exposure
**Image**: Surgical view showing smooth liver parenchyma  
**Question**: "What anatomical structure is prominently displayed in this surgical field?"  
**Answer**: B. Liver surface  
**Rationale**: Image demonstrates smooth hepatic capsule with characteristic liver surface appearance and texture

### Example 3: Calot's Triangle Dissection
**Image**: Detailed view of hepatocystic triangle structures  
**Question**: "What anatomical structure is prominently displayed in this surgical field?"  
**Answer**: C. Common bile duct  
**Rationale**: Image shows tubular structure in Calot's triangle with characteristics consistent with common bile duct

### Example 4: Vascular Structure Identification
**Image**: Surgical view showing arterial vessel with pulsatile characteristics  
**Question**: "What anatomical structure is prominently displayed in this surgical field?"  
**Answer**: D. Hepatic artery  
**Rationale**: Image demonstrates arterial vessel with typical hepatic artery location and appearance in hepatobiliary anatomy

### Example 5: Peritoneal Layer Visualization
**Image**: Surgical view showing smooth serosal surface  
**Question**: "What anatomical structure is prominently displayed in this surgical field?"  
**Answer**: G. Peritoneum  
**Rationale**: Image shows characteristic smooth, shiny serosal covering typical of peritoneal surface

## Implementation Notes

### Technical Considerations
- Implement anatomy-specific feature recognition algorithms
- Consider viewing angle and surgical approach variations
- Account for anatomical variations and pathological changes
- Handle different imaging modalities and lighting conditions

### Clinical Validation
- Align with standard surgical anatomy references
- Cross-reference with surgical training curricula
- Validate against expert surgeon identification
- Consider procedure-specific anatomical priorities

### Dataset-Specific Adaptations
- **Procedure-specific datasets**: Focus on relevant anatomical structures
- **Multi-approach datasets**: Account for visualization differences
- **Training datasets**: Emphasize educationally important structures
- **Safety datasets**: Prioritize structures critical for avoiding injury

### Quality Assurance
- Regular validation by surgical anatomists and experienced surgeons
- Cross-reference with established anatomical atlases
- Monitoring for accuracy across different surgical procedures
- Updates based on evolving surgical techniques and anatomical understanding
