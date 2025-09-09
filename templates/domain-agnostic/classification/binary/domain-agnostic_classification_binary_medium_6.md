# Binary Classification Template 6: Clear Evidence Assessment

## Template Overview

**Template ID**: `domain-agnostic_classification_binary_medium_6`  
**Task Type**: Binary classification  
**Difficulty**: Medium  
**Question Pattern**: Evidence-based diagnostic assessment with confidence emphasis  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires understanding of diagnostic evidence quality and clinical confidence levels. Knowledge of what constitutes "clear evidence" versus ambiguous findings, emphasizing the strength and certainty of diagnostic indicators in medical imaging.  

## Template Description

This template converts binary classification datasets into MCVQA format by asking whether there is clear evidence of a medical condition in imaging studies. It emphasizes the strength and clarity of diagnostic evidence, testing the model's ability to distinguish between definitive findings and uncertain or ambiguous cases. This approach mirrors clinical decision-making where evidence quality is as important as evidence presence.

## Question Generation Pattern

### Question Format
```
"Is there clear evidence of {condition} in this {modality} image?"
```

### Answer Format
- **Positive cases**: "Yes, clear evidence"
- **Negative cases**: "No clear evidence"

### Template Variables
- `{condition}`: The medical condition or finding being assessed for evidence clarity. Extracted from dataset metadata and used to specify what condition is being evaluated for diagnostic evidence.
- `{modality}`: The imaging modality (e.g., "chest X-ray", "MRI scan", "fundus photograph"). Incorporated into question text to provide clinical context about the diagnostic imaging method.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, allowing for comprehensive assessment of evidence clarity and diagnostic confidence.

### Answer Construction
**For Positive Cases (original label = 1)**:
- Condition is present with clear diagnostic evidence
- Answer: "Yes, clear evidence"
- Emphasizes definitive findings that support confident diagnosis

**For Negative Cases (original label = 0)**:
- Condition is absent or findings are ambiguous
- Answer: "No clear evidence"
- Includes both absence of condition and uncertain/borderline cases


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary labels where evidence quality and diagnostic confidence can be meaningfully assessed
- **Clinical Context**: Diagnostic scenarios where evidence clarity is clinically relevant and impacts decision-making
- **Image Quality**: Sufficient image quality to assess evidence clarity and diagnostic features
- **Datasets from metadata file**: Compatible datasets include diagnostic imaging datasets with clear positive/negative findings available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Focus on the strength and definitiveness of diagnostic evidence, using specific medical condition names and conservative interpretation where "clear evidence" indicates high diagnostic confidence
- **Label mapping rules**: Convert original dataset annotations to evidence-based format:
  - Positive cases (1, "positive", "present") → "Yes, clear evidence" (definitive findings supporting diagnosis)
  - Negative cases (0, "negative", "absent") → "No clear evidence" (absence or ambiguous findings)
- **Conversion Process**: Extract binary labels from original dataset, identify condition and modality from metadata, map to evidence clarity framework emphasizing diagnostic confidence, present raw images without modifications, validate MCVQA compliance with single correct answer
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "medium", options array with 2 evidence choices, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_binary_medium_6"

## Examples

### Example 1: Chest X-ray Pneumonia Evidence
**Original Dataset Context and Annotation Format**: ChestX-ray14 dataset with binary labels in CSV format (image_id, pneumonia_label) where 1 = pneumonia present, 0 = no pneumonia  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Is there clear evidence of pneumonia in this chest X-ray image?"
- **Answer Choices**: ["Yes, clear evidence", "No clear evidence"]
- **Correct Answer**: "Yes, clear evidence"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV indicating pneumonia presence
2. Identify "pneumonia" as condition and "chest X-ray" as modality from dataset metadata
3. Map positive case to clear evidence framework based on diagnostic confidence level
4. Select "Yes, clear evidence" for definitive radiographic findings supporting pneumonia
5. Validate evidence-based format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Pneumonia case with definitive radiographic evidence including consolidation, air bronchograms, and infiltrative patterns that provide unambiguous diagnostic indicators - clear pathognomonic findings that would be recognized by clinical experts as definitive evidence requiring confident diagnosis

### Example 2: Brain MRI Stroke Evidence  
**Original Dataset Context and Annotation Format**: Acute stroke detection dataset with binary labels where 0 = no acute stroke, 1 = acute stroke present  
**Image Presentation Method**: Raw brain MRI image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Is there clear evidence of acute stroke in this brain MRI image?"
- **Answer Choices**: ["Yes, clear evidence", "No clear evidence"] 
- **Correct Answer**: "No clear evidence"  
**Complete Conversion Process Explanation**:
1. Extract binary label "0" from dataset indicating no acute stroke
2. Identify "acute stroke" as condition and "brain MRI" as modality from metadata
3. Map negative case to evidence clarity framework based on absence of diagnostic features
4. Select "No clear evidence" for lack of definitive ischemic changes, hemorrhage, or mass effect
5. Verify evidence assessment format with single correct answer structure for MCVQA compliance  
**Clinical Rationale**: Normal brain MRI with no evidence of acute ischemic changes, intracranial hemorrhage, or space-occupying lesions - absence of pathognomonic stroke findings allows confident exclusion with high diagnostic certainty for emergency clinical decision-making
