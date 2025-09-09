# Anatomical Landmarks Template 2: Multiple Landmark Localization

## Template Overview

**Template ID**: `anatomical_landmarks_multiple_1`  
**Task Type**: Anatomical Landmarks & Keypoints (Multiple)  
**Difficulty**: Easy  
**Question Pattern**: Multiple anatomical landmark set selection from coordinate group options  

## Template Description

This template converts anatomical landmark detection datasets into MCVQA format by asking users to identify the correct set of multiple anatomical landmarks from coordinate group options. It is designed for datasets that contain precise (x,y) coordinate annotations for sets of related anatomical structures.

The template focuses on spatial localization of multiple anatomical points simultaneously, testing the ability to recognize and locate collections of anatomical landmarks that work together for comprehensive anatomical analysis.

## Question Generation Pattern

### Question Format
```
"Which set of points correctly identifies the {landmark_set} in this {modality} image?"
```

### Answer Format
Multiple choice options with coordinate sets:
- A. {Correct landmark set with coordinates}
- B. {Alternative landmark set with coordinates}
- C. {Alternative landmark set with coordinates}
- D. {Alternative landmark set with coordinates}

### Template Variables
- `{landmark_set}`: The collection of anatomical landmarks (e.g., "cephalometric landmarks", "cardiac measurement points", "spinal alignment points", "hand joint landmarks")
- `{modality}`: The imaging modality (e.g., "cephalometric X-ray", "echocardiography", "spine X-ray", "hand X-ray")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Landmarks",
  "question": "Which set of points correctly identifies the {landmark_set} in this {modality} image?",
  "answer": "{selected_option_letter}",
  "answer_type": "single_label",
  "options": [
    "A. Set A: [{landmark1}: ({x1}, {y1}), {landmark2}: ({x2}, {y2}), {landmark3}: ({x3}, {y3})]",
    "B. Set B: [{landmark1}: ({x1_alt}, {y1_alt}), {landmark2}: ({x2_alt}, {y2_alt}), {landmark3}: ({x3_alt}, {y3_alt})]", 
    "C. Set C: [{landmark1}: ({x1_alt2}, {y1_alt2}), {landmark2}: ({x2_alt2}, {y2_alt2}), {landmark3}: ({x3_alt2}, {y3_alt2})]",
    "D. Set D: [{landmark1}: ({x1_alt3}, {y1_alt3}), {landmark2}: ({x2_alt3}, {y2_alt3}), {landmark3}: ({x3_alt3}, {y3_alt3})]"
  ],
  "spatial_reference": {
    "landmark_set": "{landmark_set_name}",
    "correct_coordinates": [
      {"{landmark1}": ["{x1_correct}", "{y1_correct}"]},
      {"{landmark2}": ["{x2_correct}", "{y2_correct}"]},
      {"{landmark3}": ["{x3_correct}", "{y3_correct}"]}
    ]
  },
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Multiple anatomical landmark localization based on coordinate set assessment",
  "provenance": {
    "original_landmark_coordinates": "{original_coordinate_array}",
    "rule_id": "anatomical_landmarks_multiple_1",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiple anatomical landmark detection with coordinate sets
- **Coordinate Data**: Multiple (x,y) pixel coordinates for related anatomical landmarks
- **Landmark Collections**: Sets of 3-8 related anatomical points typically used together
- **Clinical Context**: Landmark sets used for comprehensive anatomical or diagnostic analysis

## Template Usage Rules

1. **Coordinate Set Integrity**: Maintain spatial relationships between landmarks in each option
2. **Anatomical Consistency**: Ensure landmark names and positions are anatomically correct
3. **Set Completeness**: Include all landmarks typically used together for the specific analysis
4. **Plausible Alternatives**: Generate alternative sets that are spatially reasonable but incorrect
5. **Clinical Utility**: Focus on landmark sets with established clinical or research applications

## Examples

### Example 1: Cephalometric Analysis Landmarks
**Original Dataset**: Cephalometric Landmark Detection  
**Original Coordinates**: [Nasion: (245, 85), Sella: (220, 120), Menton: (240, 380), Gonion: (180, 320)]  
**Generated Q&A**:
- **Question**: "Which set of points correctly identifies the cephalometric landmarks in this X-ray image?"
- **Options**:
  - A. Set A: [Nasion: (245, 85), Sella: (220, 120), Menton: (240, 380), Gonion: (180, 320)]
  - B. Set B: [Nasion: (260, 100), Sella: (200, 140), Menton: (220, 360), Gonion: (160, 300)]
  - C. Set C: [Nasion: (230, 70), Sella: (240, 100), Menton: (260, 400), Gonion: (200, 340)]
  - D. Set D: [Nasion: (255, 95), Sella: (210, 130), Menton: (230, 370), Gonion: (170, 310)]
- **Answer**: "A"
- **Rationale**: "Standard cephalometric landmarks positioned for comprehensive craniofacial analysis"

### Example 2: Cardiac Measurement Points
**Original Dataset**: Echocardiography Landmark Assessment  
**Original Coordinates**: [Mitral Valve: (180, 200), Aortic Valve: (200, 150), Tricuspid Valve: (220, 210), Apex: (160, 280)]  
**Generated Q&A**:
- **Question**: "Which set of points correctly identifies the cardiac measurement points in this echocardiography image?"
- **Options**:
  - A. Set A: [Mitral: (160, 220), Aortic: (180, 170), Tricuspid: (200, 230), Apex: (140, 300)]
  - B. Set B: [Mitral: (180, 200), Aortic: (200, 150), Tricuspid: (220, 210), Apex: (160, 280)]
  - C. Set C: [Mitral: (200, 180), Aortic: (220, 130), Tricuspid: (240, 190), Apex: (180, 260)]
  - D. Set D: [Mitral: (170, 210), Aortic: (190, 160), Tricuspid: (210, 220), Apex: (150, 290)]
- **Answer**: "B"
- **Rationale**: "Cardiac valve landmarks positioned for comprehensive functional assessment"

### Example 3: Spinal Alignment Assessment Points
**Original Dataset**: Spine Curvature Analysis  
**Original Coordinates**: [C7: (256, 80), T12: (260, 200), L5: (250, 320), S1: (248, 350)]  
**Generated Q&A**:
- **Question**: "Which set of points correctly identifies the spinal alignment points in this spine X-ray image?"
- **Options**:
  - A. Set A: [C7: (240, 90), T12: (245, 210), L5: (235, 330), S1: (233, 360)]
  - B. Set B: [C7: (270, 70), T12: (275, 190), L5: (265, 310), S1: (263, 340)]
  - C. Set C: [C7: (256, 80), T12: (260, 200), L5: (250, 320), S1: (248, 350)]
  - D. Set D: [C7: (250, 85), T12: (254, 205), L5: (244, 325), S1: (242, 355)]
- **Answer**: "C"
- **Rationale**: "Vertebral landmarks positioned for spinal curvature and alignment analysis"

### Example 4: Hand Joint Landmarks
**Original Dataset**: Hand Joint Analysis  
**Original Coordinates**: [MCP Index: (180, 200), PIP Index: (175, 160), DIP Index: (170, 120), MCP Thumb: (220, 240)]  
**Generated Q&A**:
- **Question**: "Which set of points correctly identifies the hand joint landmarks in this hand X-ray image?"
- **Options**:
  - A. Set A: [MCP Index: (190, 210), PIP Index: (185, 170), DIP Index: (180, 130), MCP Thumb: (230, 250)]
  - B. Set B: [MCP Index: (170, 190), PIP Index: (165, 150), DIP Index: (160, 110), MCP Thumb: (210, 230)]
  - C. Set C: [MCP Index: (180, 200), PIP Index: (175, 160), DIP Index: (170, 120), MCP Thumb: (220, 240)]
  - D. Set D: [MCP Index: (185, 205), PIP Index: (180, 165), DIP Index: (175, 125), MCP Thumb: (225, 245)]
- **Answer**: "C"
- **Rationale**: "Digital joint landmarks positioned for comprehensive hand function assessment"

### Example 5: Facial Landmark Set
**Original Dataset**: Facial Analysis Landmarks  
**Original Coordinates**: [Nasion: (256, 120), Left Eye: (220, 140), Right Eye: (290, 140), Nose Tip: (256, 180), Chin: (256, 280)]  
**Generated Q&A**:
- **Question**: "Which set of points correctly identifies the facial landmarks in this facial image?"
- **Options**:
  - A. Set A: [Nasion: (256, 120), Left Eye: (220, 140), Right Eye: (290, 140), Nose Tip: (256, 180), Chin: (256, 280)]
  - B. Set B: [Nasion: (250, 130), Left Eye: (210, 150), Right Eye: (280, 150), Nose Tip: (250, 190), Chin: (250, 290)]
  - C. Set C: [Nasion: (262, 110), Left Eye: (230, 130), Right Eye: (300, 130), Nose Tip: (262, 170), Chin: (262, 270)]
  - D. Set D: [Nasion: (258, 125), Left Eye: (225, 145), Right Eye: (295, 145), Nose Tip: (258, 185), Chin: (258, 285)]
- **Answer**: "A"
- **Rationale**: "Facial landmarks positioned for comprehensive craniofacial assessment and analysis"

## Implementation Notes

### Advantages
- **Comprehensive Assessment**: Tests ability to identify multiple related anatomical landmarks simultaneously
- **Spatial Relationships**: Requires understanding of anatomical spatial relationships between landmarks
- **Clinical Utility**: Supports complete anatomical analyses used in clinical and research settings
- **Measurement Integration**: Enables comprehensive measurement and assessment protocols

### Limitations
- **Complexity Increase**: Multiple landmarks increase complexity compared to single landmark detection
- **Coordinate Set Generation**: Requires careful generation of plausible alternative coordinate sets
- **Anatomical Knowledge**: Demands deeper understanding of anatomical relationships and landmark purposes

### Quality Considerations
- Ensure all landmark sets maintain anatomically plausible spatial relationships
- Verify that landmark names and positions follow established anatomical conventions
- Confirm that alternative coordinate sets are spatially reasonable but clearly incorrect
- Validate that landmark collections are clinically relevant and commonly used together
- Check that coordinate precision is appropriate for the intended clinical or research application
