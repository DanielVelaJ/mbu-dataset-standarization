# Binary Classification Template 7: Detection Capability Assessment

## Template Overview

**Template ID**: `domain-agnostic_classification_binary_medium_7`  
**Task Type**: Binary classification  
**Difficulty**: Medium  
**Question Pattern**: Detection-focused assessment emphasizing visual identification  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires basic visual pattern recognition and medical terminology understanding. Knowledge of what conditions "look like" on different imaging modalities, emphasizing fundamental computer vision detection capabilities for medical imaging.  

## Template Description

This template converts binary classification datasets into MCVQA format by asking whether a medical condition can be detected in imaging studies. It emphasizes the fundamental visual detection capability, testing the model's ability to identify and recognize pathological findings. This approach focuses on the core computer vision task of pattern recognition in medical imaging.

## Question Generation Pattern

### Question Format
```
"Can {condition} be detected in this {modality} image?"
```

### Answer Format
- **Positive cases**: "Yes, detectable"
- **Negative cases**: "No, not detectable"

### Template Variables
- `{condition}`: The medical condition or finding being assessed for detection. Extracted from dataset metadata and used to specify what pathological finding is being evaluated for visual identification.
- `{modality}`: The imaging modality (e.g., "chest X-ray", "CT scan", "fundus photograph"). Incorporated into question text to provide clinical context about the diagnostic imaging method.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, allowing for assessment of natural visual detection capabilities.

### Answer Construction
**For Positive Cases (original label = 1)**:
- Condition is present and visually detectable
- Answer: "Yes, detectable"
- Focuses on whether visual features are sufficient for identification

**For Negative Cases (original label = 0)**:
- Condition is absent and therefore not detectable
- Answer: "No, not detectable"
- Emphasizes absence of visual indicators for the condition


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels where visual detection capability is the primary task focus
- **Visual Clarity**: Conditions that have clearly detectable visual manifestations on imaging
- **Image Quality**: Adequate image quality for reliable visual pattern recognition and identification
- **Datasets from metadata file**: Compatible datasets include detection-focused imaging datasets with clear visual findings available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Emphasize visual pattern recognition capabilities rather than clinical interpretation, using specific and visually detectable medical conditions
- **Label mapping rules**: Convert original dataset annotations to detection-based format:
  - Positive cases (1, "positive", "present") → "Yes, detectable" (condition visible and identifiable)
  - Negative cases (0, "negative", "absent") → "No, not detectable" (condition absent or not visible)
- **Conversion Process**: Extract binary labels from original dataset, identify condition and modality from metadata, map to visual detection framework emphasizing pattern recognition, present raw images without modifications, validate MCVQA compliance with single correct answer, focus on detection capability rather than diagnostic implications
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "medium", options array with 2 detection choices, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_binary_medium_7"

## Examples

### Example 1: Chest X-ray Pneumothorax Detection
**Original Dataset Context and Annotation Format**: Pneumothorax detection dataset with binary labels in CSV format (image_id, pneumothorax_label) where 1 = pneumothorax present, 0 = no pneumothorax  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Can pneumothorax be detected in this chest X-ray image?"
- **Answer Choices**: ["Yes, detectable", "No, not detectable"]
- **Correct Answer**: "Yes, detectable"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV indicating pneumothorax presence
2. Identify "pneumothorax" as condition and "chest X-ray" as modality from dataset metadata
3. Map positive case to visual detection framework based on pattern recognition capability
4. Select "Yes, detectable" for visible pleural line separation and lung collapse patterns
5. Validate detection-focused format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Pneumothorax shows clear visual indicators including visible pleural line, lung collapse, and air space between lung and chest wall - these characteristic patterns provide unambiguous visual markers that enable reliable computer vision detection without requiring complex clinical interpretation

### Example 2: Fundus Microaneurysm Detection  
**Original Dataset Context and Annotation Format**: Diabetic retinopathy screening dataset with binary labels where 0 = no microaneurysms, 1 = microaneurysms present  
**Image Presentation Method**: Raw fundus photograph displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Can microaneurysms be detected in this fundus photograph?"
- **Answer Choices**: ["Yes, detectable", "No, not detectable"] 
- **Correct Answer**: "No, not detectable"  
**Complete Conversion Process Explanation**:
1. Extract binary label "0" from dataset indicating no microaneurysms
2. Identify "microaneurysms" as condition and "fundus photograph" as modality from metadata
3. Map negative case to visual detection framework based on absence of detectable features
4. Select "No, not detectable" for lack of visible small red dots in retinal vasculature
5. Verify detection assessment format with single correct answer structure for MCVQA compliance  
**Clinical Rationale**: Normal fundus with intact retinal vasculature showing no visible microaneurysms (small red dots) - absence of characteristic dot-like hemorrhages and capillary dilatations means no detectable pathological features for computer vision pattern recognition
