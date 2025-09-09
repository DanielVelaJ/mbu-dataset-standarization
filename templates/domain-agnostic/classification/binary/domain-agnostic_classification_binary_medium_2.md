# Binary Classification Template 2: Multiple Choice with Distractors

## Template Overview

**Template ID**: `domain-agnostic_classification_binary_medium_2`  
**Task Type**: Binary classification  
**Difficulty**: Medium  
**Question Pattern**: Multiple choice with one correct answer and relevant medical distractors  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires understanding of medical terminology and ability to generate clinically plausible distractors from the same anatomical domain. Knowledge of related conditions and differential diagnosis concepts needed to create appropriate multiple choice options.  

## Template Description

This template converts binary classification datasets into MCVQA format by presenting the positive condition alongside plausible medical distractors in a multiple choice format. It increases task difficulty by requiring the model to distinguish between the target condition and related medical conditions from the same anatomical domain or clinical context.

## Question Generation Pattern

### Question Format
```
"What condition is shown in this {modality} image?"
```

### Answer Format
- **Multiple Choice**: A, B, C, D options
- **One Correct Answer**: The positive label when true, "None of the above" when false
- **Three Distractors**: Related medical conditions from the same domain

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus", "skin", "CT", "MRI"). Incorporated into question text to provide clinical context.
- `{positive_condition}`: The target medical condition from the original dataset. Used as correct answer for positive cases or omitted for negative cases.
- `{distractor_1}`, `{distractor_2}`, `{distractor_3}`: Related medical conditions from the same anatomical domain. Used to create plausible incorrect answer choices that require medical expertise to distinguish.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, allowing for comprehensive clinical assessment.

### Answer Construction
**For Positive Cases (original label = 1)**:
- Extract positive condition name from dataset labels
- Generate 3 clinically plausible distractors from same anatomical domain
- Create options A-D with positive condition as correct answer
- Select appropriate letter (A-D) based on randomized position

**For Negative Cases (original label = 0)**:
- Generate 3 relevant medical conditions as distractors
- Add "None of the above" as fourth option
- "None of the above" becomes the correct answer
- Maintain MCVQA compliance with single correct choice

### Option Generation Rules

#### For Positive Cases (Original Label = 1):
```
A: {positive_condition}
B: {distractor_1}
C: {distractor_2}  
D: {distractor_3}
```
**Correct Answer**: "A"

#### For Negative Cases (Original Label = 0):
```
A: {distractor_1}
B: {distractor_2}
C: {distractor_3}
D: None of the above
```
**Correct Answer**: "D"

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Single binary label per image (0/1, positive/negative)
- **Domain Knowledge**: Well-defined medical conditions with known related conditions for distractor generation
- **Image Level**: Whole image classification
- **Datasets from metadata file**: Compatible datasets include ChestX-ray14, ISIC skin lesion datasets, fundus photography datasets, brain imaging datasets, and other binary medical classification datasets available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Use precise medical terminology from dataset classifications and generate clinically plausible distractors from the same anatomical domain
- **Label mapping rules**: Convert original dataset annotations to multiple choice format:
  - Positive cases (1, "positive", "present") → Target condition as one option with 3 distractors
  - Negative cases (0, "negative", "absent") → 3 distractors plus "None of the above" as correct answer
- **Conversion Process**: Extract binary labels from original dataset, identify target condition name, generate 3 anatomically related distractors (anatomically related, visually similar, clinically relevant, diagnostically challenging), create multiple choice options with randomized positioning, present raw images without modifications, validate MCVQA compliance with single correct answer
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "medium", options array with 4 choices, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_binary_medium_2"

## Examples

### Example 1: Chest X-ray Pneumonia Detection
**Original Dataset Context and Annotation Format**: ChestX-ray14 dataset with binary labels in CSV format (image_id, pneumonia_label) where 1 = pneumonia present, 0 = no pneumonia  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "What condition is shown in this chest X-ray image?"
- **Answer Choices**: ["Pneumonia", "Pulmonary edema", "Pleural effusion", "Atelectasis"]
- **Correct Answer**: "Pneumonia" (Option A)  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV for pneumonia presence
2. Identify "pneumonia" as target condition from dataset metadata
3. Generate 3 anatomically related respiratory distractors: pulmonary edema, pleural effusion, atelectasis
4. Create multiple choice options with pneumonia as correct answer
5. Randomize option positions and validate MCVQA compliance with single correct answer  
**Clinical Rationale**: Positive identification of pneumonia with plausible respiratory distractors that could appear similar on chest imaging, requiring clinical expertise to differentiate based on consolidation patterns and radiological features

### Example 2: Fundus Diabetic Retinopathy Screening  
**Original Dataset Context and Annotation Format**: Diabetic retinopathy screening dataset with binary labels where 0 = no diabetic retinopathy, 1 = diabetic retinopathy present  
**Image Presentation Method**: Raw fundus photograph displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "What condition is shown in this fundus image?"
- **Answer Choices**: ["Glaucoma", "Age-related macular degeneration", "Hypertensive retinopathy", "None of the above"] 
- **Correct Answer**: "None of the above" (Option D)  
**Complete Conversion Process Explanation**:
1. Extract binary label "0" from dataset indicating no diabetic retinopathy
2. Since negative case, generate 3 ophthalmologic distractors: glaucoma, AMD, hypertensive retinopathy
3. Add "None of the above" as fourth option and correct answer for negative case
4. Create multiple choice format maintaining MCVQA compliance
5. Verify single correct answer structure  
**Clinical Rationale**: Normal fundus examination with ophthalmologic conditions as distractors that affect similar retinal structures but have distinct clinical presentations, testing ability to recognize absence of pathology versus other retinal diseases

