# Anatomical Landmarks Template 1: Single Landmark Localization

## Template Overview

**Template ID**: `anatomical_landmarks_single_1`  
**Task Type**: Anatomical Landmarks & Keypoints (Single)  
**Difficulty**: Easy  
**Question Pattern**: Single anatomical landmark location selection from coordinate region options  

## Template Description

This template converts anatomical landmark detection datasets into MCVQA format by asking users to identify the location of a single anatomical landmark from multiple choice coordinate region options. It is designed for datasets that contain precise (x,y) coordinate annotations for specific anatomical structures.

The template focuses on spatial localization of individual anatomical points, testing the ability to recognize and locate specific anatomical landmarks that are clinically important for measurement, diagnosis, or treatment planning.

## Question Generation Pattern

### Question Format
```
"Where is the {landmark} located in this {modality} image?"
```

### Answer Format
Multiple choice options with coordinate regions:
- A. {Region description with approximate coordinates}
- B. {Alternative region with coordinates}
- C. {Alternative region with coordinates}
- D. {Alternative region with coordinates}

### Template Variables
- `{landmark}`: The specific anatomical landmark (e.g., "fovea center", "pupil center", "optic disc center", "anatomical apex")
- `{modality}`: The imaging modality (e.g., "fundus", "chest X-ray", "cephalometric X-ray", "ultrasound")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Landmarks",
  "question": "Where is the {landmark} located in this {modality} image?",
  "answer": "{selected_option_letter}",
  "answer_type": "single_label",
  "options": [
    "A. {region_description_1} ({x1}, {y1})",
    "B. {region_description_2} ({x2}, {y2})", 
    "C. {region_description_3} ({x3}, {y3})",
    "D. {region_description_4} ({x4}, {y4})"
  ],
  "spatial_reference": {
    "correct_region": "{correct_anatomical_region}",
    "approximate_coordinates": ["{x_correct}", "{y_correct}"]
  },
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Anatomical landmark localization based on spatial coordinate assessment",
  "provenance": {
    "original_coordinates": ["{original_x}", "{original_y}"],
    "rule_id": "anatomical_landmarks_single_1",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Anatomical landmark detection with precise coordinate annotations
- **Coordinate Data**: (x,y) pixel coordinates for single anatomical landmarks
- **Anatomical Targets**: Well-defined anatomical structures suitable for point localization
- **Medical Context**: Clinically relevant landmarks used for measurement or diagnosis

## Template Usage Rules

1. **Coordinate Regions**: Convert exact coordinates to approximate anatomical regions for multiple choice
2. **Anatomical Accuracy**: Use correct anatomical terminology for landmark names and regions
3. **Spatial Logic**: Ensure alternative coordinates represent plausible but incorrect locations
4. **Region Descriptions**: Provide meaningful anatomical region descriptions with coordinate ranges
5. **Clinical Relevance**: Focus on landmarks that have clinical or diagnostic significance

## Examples

### Example 1: Fundus Fovea Center Detection
**Original Dataset**: Fundus Fovea Localization  
**Original Coordinates**: (312, 245)  
**Generated Q&A**:
- **Question**: "Where is the fovea center located in this fundus image?"
- **Options**:
  - A. Central macula region (312, 245)
  - B. Temporal retina region (450, 200)
  - C. Nasal retina region (180, 260)
  - D. Superior retina region (310, 120)
- **Answer**: "A"
- **Rationale**: "Fovea centralis located in the central macular region for optimal visual acuity"

### Example 2: Pupil Center Localization
**Original Dataset**: Eye Tracking Pupil Detection  
**Original Coordinates**: (256, 180)  
**Generated Q&A**:
- **Question**: "Where is the pupil center located in this eye image?"
- **Options**:
  - A. Upper eyelid region (260, 120)
  - B. Central iris region (256, 180)
  - C. Lower eyelid region (250, 240)
  - D. Lateral canthus region (320, 180)
- **Answer**: "B"
- **Rationale**: "Pupil center positioned in the central portion of the iris structure"

### Example 3: Cardiac Apex Detection
**Original Dataset**: Echocardiography Landmark Detection  
**Original Coordinates**: (180, 320)  
**Generated Q&A**:
- **Question**: "Where is the cardiac apex located in this echocardiography image?"
- **Options**:
  - A. Base of heart region (200, 150)
  - B. Right heart border (280, 250)
  - C. Cardiac apex region (180, 320)
  - D. Left atrium region (120, 200)
- **Answer**: "C"
- **Rationale**: "Cardiac apex represents the inferolateral tip of the left ventricle"

### Example 4: Cephalometric Nasion Point
**Original Dataset**: Cephalometric Analysis Landmarks  
**Original Coordinates**: (245, 85)  
**Generated Q&A**:
- **Question**: "Where is the nasion point located in this cephalometric X-ray image?"
- **Options**:
  - A. Frontonasal suture region (245, 85)
  - B. Orbital rim region (220, 120)
  - C. Nasal spine region (250, 180)
  - D. Chin prominence region (240, 380)
- **Answer**: "A"
- **Rationale**: "Nasion located at the frontonasal suture intersection for cephalometric analysis"

### Example 5: Spinal Vertebral Center
**Original Dataset**: Spine Alignment Assessment  
**Original Coordinates**: (256, 200)  
**Generated Q&A**:
- **Question**: "Where is the vertebral body center located in this spine X-ray image?"
- **Options**:
  - A. Posterior spinous process (180, 200)
  - B. Vertebral body center (256, 200)
  - C. Transverse process (320, 190)
  - D. Intervertebral disc space (250, 240)
- **Answer**: "B"
- **Rationale**: "Vertebral body center identified for spinal alignment and curvature assessment"

## Implementation Notes

### Advantages
- **Precise Localization**: Tests ability to identify specific anatomical landmark locations
- **Clinical Relevance**: Focuses on landmarks important for medical measurement and diagnosis
- **Spatial Reasoning**: Requires understanding of anatomical spatial relationships
- **Measurement Support**: Enables precise medical measurements and anatomical analysis

### Limitations
- **Coordinate Approximation**: Converting exact coordinates to regions may lose precision
- **Single Point Focus**: Limited to one landmark per question, may miss spatial relationships
- **Anatomical Knowledge**: Requires understanding of anatomical terminology and structure

### Quality Considerations
- Ensure coordinate regions are anatomically meaningful and clinically relevant
- Verify that landmark names match standard anatomical terminology
- Confirm that alternative coordinate options represent plausible anatomical locations
- Validate that spatial regions are appropriate for the specific imaging modality
- Check that coordinate ranges are suitable for clinical measurement applications
