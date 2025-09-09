# Binary Classification Template 8: Definition-Based Assessment

## Template Overview

**Template ID**: `domain-agnostic_classification_binary_hard_8`  
**Task Type**: Binary classification  
**Difficulty**: Hard  
**Question Pattern**: Medical definition matching to test knowledge beyond visual pattern recognition  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires deep understanding of medical terminology, pathophysiology, and clinical definitions. Knowledge of precise medical definitions, ability to distinguish between related conditions, and understanding of conceptual differences beyond visual pattern matching.  

## Template Description

This template converts binary classification datasets into MCVQA format by asking which medical definition best describes what is shown in the image. It tests the model's understanding of medical terminology and pathophysiology, requiring both visual recognition and conceptual knowledge. This approach goes beyond simple pattern matching to ensure models truly understand what medical conditions represent.

## Question Generation Pattern

### Question Format
```
"Which definition best describes what is shown in this {modality} image?"
```

### Answer Format
- **Multiple Choice**: Four definition options (A, B, C, D)
- **Positive cases**: Correct definition of target condition + 3 related distractors
- **Negative cases**: 3 plausible but incorrect definitions + "None of the above definitions apply"

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus photograph", "skin lesion"). Incorporated into question text to provide clinical context about the imaging method.
- `{target_definition}`: Accurate medical definition of the target condition. Used as correct answer for positive cases, providing precise clinical terminology and pathophysiology.
- `{distractor_definitions}`: Medically accurate definitions of related but different conditions. Used to create plausible incorrect answer choices that test conceptual understanding.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, requiring conceptual understanding beyond visual cues.

### Answer Construction
**For Positive Cases (original label = 1)**:
- Extract accurate medical definition of target condition from medical literature
- Generate 3 related but distinct condition definitions as distractors
- Create 4-option multiple choice with target definition as correct answer
- Randomize option positioning and validate conceptual accuracy

**For Negative Cases (original label = 0)**:
- Generate 3 plausible but incorrect medical definitions
- Add "None of the above definitions apply" as fourth option
- "None of the above" becomes the correct answer for negative cases
- Ensure all definitions are medically accurate but not applicable to the image


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Medical Context**: Well-defined medical conditions with established clinical definitions and pathophysiology
- **Educational Value**: Conditions where understanding precise medical definitions is clinically important for diagnosis
- **Clear Pathophysiology**: Conditions with distinct pathophysiological mechanisms that can be differentiated conceptually
- **Datasets from metadata file**: Compatible datasets include well-characterized medical conditions with established definitions available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Use medically accurate, textbook-level definitions with established medical terminology, matching definition complexity to clinical context
- **Label mapping rules**: Convert original dataset annotations to definition-based format:
  - Positive cases (1, "positive", "present") → Accurate medical definition of target condition as correct answer with 3 related distractors
  - Negative cases (0, "negative", "absent") →  3 plausible but incorrect definitions plus "None of the above definitions apply" as correct answer
- **Conversion Process**: Extract binary labels from original dataset, identify target condition from metadata, source accurate medical definition from clinical literature, generate 3 related but distinct condition definitions as distractors, create 4-option multiple choice format, present raw images without modifications, validate MCVQA compliance with single correct answer
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "hard", options array with 4 definition choices, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_binary_hard_8"

## Examples

### Example 1: Chest X-ray Pneumonia Detection
**Original Dataset Context and Annotation Format**: ChestX-ray14 dataset with binary labels in CSV format (image_id, pneumonia_label) where 1 = pneumonia present, 0 = no pneumonia  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Which definition best describes what is shown in this chest X-ray image?"
- **Answer Choices**: ["Acute inflammation of lung parenchyma with consolidation and exudate formation", "Collection of air in the pleural space causing lung collapse", "Abnormal accumulation of fluid in the pleural cavity", "Enlargement of the cardiac silhouette beyond normal limits"]
- **Correct Answer**: "Acute inflammation of lung parenchyma with consolidation and exudate formation"  
**Complete Conversion Process Explanation**: 
1. Extract binary label "1" from dataset CSV indicating pneumonia presence
2. Identify "pneumonia" as target condition from dataset metadata
3. Source accurate medical definition of pneumonia from clinical literature: "Acute inflammation of lung parenchyma with consolidation and exudate formation"
4. Generate 3 related respiratory condition definitions as distractors: pneumothorax, pleural effusion, cardiomegaly
5. Create 4-option multiple choice format with pneumonia definition as correct answer, validate MCVQA compliance  
**Clinical Rationale**: Pneumonia case requiring understanding of pathophysiological mechanisms beyond visual recognition - definition emphasizes acute inflammatory process, parenchymal involvement, consolidation pattern, and exudate formation that distinguish pneumonia from other respiratory conditions conceptually

### Example 2: Fundus Normal Case  
**Original Dataset Context and Annotation Format**: Diabetic retinopathy screening dataset with binary labels where 0 = no diabetic retinopathy, 1 = diabetic retinopathy present  
**Image Presentation Method**: Raw fundus photograph displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Which definition best describes what is shown in this fundus photograph?"
- **Answer Choices**: ["Progressive retinal vascular damage due to chronic hyperglycemia", "Optic nerve damage characterized by increased intraocular pressure", "Central retinal degeneration affecting photoreceptor cells", "None of the above definitions apply"] 
- **Correct Answer**: "None of the above definitions apply"  
**Complete Conversion Process Explanation**:
1. Extract binary label "0" from dataset indicating no diabetic retinopathy
2. Since negative case, generate 3 related ophthalmologic condition definitions: diabetic retinopathy, glaucoma, macular degeneration
3. Add "None of the above definitions apply" as fourth option and correct answer for normal fundus
4. Ensure all definitions are medically accurate but not applicable to normal anatomy
5. Validate definition-based format with single correct answer structure for MCVQA compliance  
**Clinical Rationale**: Normal fundus examination requiring conceptual understanding that no pathological definitions apply to healthy retinal anatomy - tests ability to recognize absence of disease conditions while understanding precise medical definitions of common ophthalmologic pathologies
