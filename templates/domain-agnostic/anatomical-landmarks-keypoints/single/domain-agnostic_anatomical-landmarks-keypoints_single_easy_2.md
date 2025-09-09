# Anatomical Landmarks Template 3: Surgical/Procedural Landmark Localization

## Template Overview

**Template ID**: `anatomical_landmarks_single_2`  
**Task Type**: Anatomical Landmarks & Keypoints (Single)  
**Difficulty**: Easy  
**Question Pattern**: Surgical/procedural landmark location selection for intervention planning  

## Template Description

This template converts anatomical landmark detection datasets into MCVQA format by asking users to identify the location of surgical or procedural landmarks from multiple choice coordinate region options. It is designed for datasets that contain precise (x,y) coordinate annotations for anatomical structures relevant to surgical planning, interventional procedures, or medical device placement.

The template focuses on procedurally relevant anatomical points, testing the ability to recognize and locate specific landmarks that are critical for surgical navigation, intervention guidance, or treatment planning.

## Question Generation Pattern

### Question Format
```
"Where is the optimal {procedure_landmark} located for {procedure_type} in this {modality} image?"
```

### Answer Format
Multiple choice options with procedural coordinate regions:
- A. {Optimal procedure region with coordinates}
- B. {Suboptimal region with coordinates}
- C. {Contraindicated region with coordinates}
- D. {Alternative anatomical region with coordinates}

### Template Variables
- `{procedure_landmark}`: The surgical/procedural target point (e.g., "entry point", "target site", "insertion point", "access route")
- `{procedure_type}`: The specific procedure (e.g., "needle biopsy", "catheter insertion", "screw placement", "injection")
- `{modality}`: The imaging modality (e.g., "CT", "ultrasound", "fluoroscopy", "MRI")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Landmarks",
  "question": "Where is the optimal {procedure_landmark} located for {procedure_type} in this {modality} image?",
  "answer": "{selected_option_letter}",
  "answer_type": "single_label",
  "options": [
    "A. {optimal_region_description} ({x1}, {y1})",
    "B. {suboptimal_region_description} ({x2}, {y2})", 
    "C. {contraindicated_region_description} ({x3}, {y3})",
    "D. {alternative_region_description} ({x4}, {y4})"
  ],
  "spatial_reference": {
    "procedure_target": "{procedure_landmark}",
    "optimal_coordinates": ["{x_optimal}", "{y_optimal}"],
    "safety_considerations": "{safety_notes}"
  },
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Procedural landmark localization for safe and effective intervention",
  "provenance": {
    "original_coordinates": ["{original_x}", "{original_y}"],
    "rule_id": "anatomical_landmarks_single_2",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Procedural/surgical landmark detection with intervention relevance
- **Coordinate Data**: (x,y) pixel coordinates for procedurally relevant anatomical points
- **Clinical Context**: Landmarks used for surgical planning, interventional procedures, or device placement
- **Safety Considerations**: Annotations that consider procedural safety and efficacy

## Template Usage Rules

1. **Procedural Accuracy**: Ensure landmark positions are clinically appropriate for the specified procedure
2. **Safety Awareness**: Include options that represent safe vs potentially hazardous locations
3. **Anatomical Precision**: Use correct anatomical terminology relevant to the procedure
4. **Clinical Relevance**: Focus on landmarks that are actually used in clinical practice
5. **Risk Assessment**: Consider procedural risks when generating alternative coordinate options

## Examples

### Example 1: Liver Biopsy Target Site
**Original Dataset**: CT-guided Liver Biopsy Planning  
**Original Coordinates**: (280, 190)  
**Generated Q&A**:
- **Question**: "Where is the optimal entry point located for liver biopsy in this CT image?"
- **Options**:
  - A. Safe liver parenchyma region (280, 190)
  - B. Near major hepatic vessels (285, 180)
  - C. Close to gallbladder (260, 170)
  - D. Superficial subcutaneous area (270, 120)
- **Answer**: "A"
- **Rationale**: "Safe biopsy path avoiding major vessels and adjacent organs for successful tissue sampling"

### Example 2: Lumbar Puncture Entry Point
**Original Dataset**: Spinal Procedure Planning MRI  
**Original Coordinates**: (256, 280)  
**Generated Q&A**:
- **Question**: "Where is the optimal insertion point located for lumbar puncture in this MRI image?"
- **Options**:
  - A. L3-L4 interspinous space (256, 280)
  - B. L2 vertebral body center (260, 240)
  - C. L5-S1 disc space (250, 320)
  - D. Posterior spinal muscle (200, 290)
- **Answer**: "A"
- **Rationale**: "Optimal interspinous space for safe cerebrospinal fluid access below conus medullaris"

### Example 3: Central Line Insertion Site
**Original Dataset**: Ultrasound-guided Vascular Access  
**Original Coordinates**: (180, 150)  
**Generated Q&A**:
- **Question**: "Where is the optimal insertion point located for central line placement in this ultrasound image?"
- **Options**:
  - A. Internal jugular vein access (180, 150)
  - B. Carotid artery region (175, 145)
  - C. External jugular vein (160, 130)
  - D. Subclavian region (220, 180)
- **Answer**: "A"
- **Rationale**: "Safe internal jugular access avoiding arterial puncture and minimizing complications"

### Example 4: Joint Injection Target
**Original Dataset**: Knee Injection Guidance Ultrasound  
**Original Coordinates**: (200, 180)  
**Generated Q&A**:
- **Question**: "Where is the optimal injection point located for knee joint injection in this ultrasound image?"
- **Options**:
  - A. Suprapatellar joint space (200, 180)
  - B. Patellar tendon insertion (190, 220)
  - C. Lateral meniscus region (240, 200)
  - D. Subcutaneous fat layer (180, 140)
- **Answer**: "A"
- **Rationale**: "Optimal joint space access for effective intra-articular medication delivery"

### Example 5: Pedicle Screw Placement
**Original Dataset**: Spine Surgery Planning CT  
**Original Coordinates**: (230, 200)  
**Generated Q&A**:
- **Question**: "Where is the optimal entry point located for pedicle screw placement in this CT image?"
- **Options**:
  - A. Pedicle entry zone (230, 200)
  - B. Facet joint center (210, 190)
  - C. Transverse process tip (260, 185)
  - D. Spinal canal region (235, 205)
- **Answer**: "A"
- **Rationale**: "Safe pedicle trajectory avoiding spinal canal and neural structures for secure fixation"

## Implementation Notes

### Advantages
- **Procedural Relevance**: Focuses on clinically important landmarks for interventional procedures
- **Safety Emphasis**: Incorporates procedural safety considerations in landmark selection
- **Practical Application**: Tests skills directly relevant to clinical intervention planning
- **Risk Awareness**: Teaches recognition of safe vs potentially hazardous anatomical locations

### Limitations
- **Procedure Specificity**: Limited to specific procedural contexts and may not generalize broadly
- **Clinical Knowledge**: Requires understanding of procedural techniques and safety considerations
- **Context Dependency**: Landmark appropriateness may depend on patient-specific factors not visible in images

### Quality Considerations
- Ensure all procedural landmarks align with established clinical guidelines and safety protocols
- Verify that coordinate options represent realistic procedural scenarios and risks
- Confirm that anatomical terminology matches surgical and interventional standards
- Validate that safety considerations are appropriately reflected in option generation
- Check that procedural contexts are commonly encountered in clinical practice
