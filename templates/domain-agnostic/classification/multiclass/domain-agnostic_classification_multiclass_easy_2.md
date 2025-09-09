# Multi-Class Classification Template 2: Disease Stage/Severity Grading

## Template Overview

**Template ID**: `domain-agnostic_classification_multiclass_easy_2`  
**Task Type**: Multiclass classification (ordinal grading)  
**Difficulty**: Easy  
**Question Pattern**: Disease severity or stage assessment with ordered scale options  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires understanding of medical grading systems and disease progression. Knowledge of established clinical scales, staging systems, and ability to distinguish between severity levels based on visual indicators. Understanding of ordinal relationships in medical assessment.

## Template Description

This template converts multi-class medical datasets with ordered/ordinal labels into MCVQA format by asking about disease severity, staging, or grading. The template presents multiple severity levels or stages as answer options, where exactly one level represents the correct assessment. This approach mirrors clinical grading and staging scenarios where medical professionals must assess disease progression or severity on established scales.

The template is specifically designed for datasets that have ordered classifications such as disease stages (0, I, II, III, IV), severity grades (mild, moderate, severe), or standardized clinical scales (BIRADS 1-5, diabetic retinopathy grades 0-4). The ordered nature of the labels provides clinical meaning where higher grades typically indicate more severe or advanced disease.

## Question Generation Pattern

### Question Format
`"What {assessment_type} is shown in this {modality} image?"`

### Answer Format
Multiple choice with options A, B, C, D, etc. representing ordered severity/stage levels

### Template Variables
- `{assessment_type}`: Type of grading (e.g., "stage", "grade", "severity level", "BIRADS category"). Used in question text to specify the type of clinical assessment being performed.
- `{modality}`: Imaging modality (e.g., "mammography", "fundus", "histopathology", "MRI"). Incorporated into question text to provide clinical context about imaging method.
- `{condition}`: Specific condition being graded (e.g., "diabetic retinopathy", "breast lesion", "cancer"). Used to specify what medical condition is being assessed for severity.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, allowing for comprehensive assessment of disease severity or staging.

### Answer Construction
**Ordinal Multiple Choice Format**:
- Extract all ordinal grades/stages from dataset metadata in natural progression order
- Use correct grade/stage label as the right answer
- Include all other grades/stages as distractors to maintain complete clinical scale
- Present options in order from lowest to highest severity (preserve ordinal relationship)
- Combine numeric grades with descriptive labels when clinically appropriate

### Example Pattern
```
Question: "What diabetic retinopathy severity grade is shown in this fundus image?"
A. No diabetic retinopathy (Grade 0)
B. Mild diabetic retinopathy (Grade 1)
C. Moderate diabetic retinopathy (Grade 2)
D. Severe diabetic retinopathy (Grade 3)
E. Proliferative diabetic retinopathy (Grade 4)
```


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification with ordinal grading (Vision → Image-Level Classification → Multiclass classification)
- **Label Structure**: 3+ ordered stages/grades/severity levels with exactly one grade per image
- **Clinical Context**: Established medical grading scales and staging systems with clinically meaningful distinctions
- **Ordinal Relationship**: Labels must have natural progression order representing disease severity or advancement
- **Datasets from metadata file**: Compatible datasets include diabetic retinopathy grading datasets (grades 0-4), cancer staging datasets (stages I-IV), BIRADS mammography classification (categories 1-5), glaucoma severity grading datasets, Alzheimer's disease staging (CDR scales), osteoarthritis grading (Kellgren-Lawrence grades), and other ordinal medical classification datasets available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Always present options in natural progression order (lowest to highest severity) and use established medical grading terminology, combining numeric grades with descriptive labels when clinically appropriate
- **Label mapping rules**: Convert original dataset annotations to ordinal grading format:
  - Extract all ordinal grades/stages from dataset metadata in natural progression order
  - Use correct grade/stage label as right answer
  - Include all other grades/stages as distractors to maintain complete clinical scale
  - Preserve ordinal relationship in option ordering
- **Conversion Process**: Extract ordinal labels from original dataset, identify all grades/stages from metadata, create grading question with complete severity scale, present raw images without modifications, validate MCVQA compliance with single correct answer, verify ordinal progression is medically accurate and follows established clinical standards
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with 3-8 severity choices in ordinal order, and includes provenance tracking with original labels and rule_id "domain-agnostic_classification_multiclass_easy_2"

## Examples

### Example 1: Diabetic Retinopathy Grading
**Original Dataset Context and Annotation Format**: Fundus diabetic retinopathy classification dataset with ordinal labels in CSV format (image_id, severity_grade) where grades include 0, 1, 2, 3, 4 representing increasing severity levels  
**Image Presentation Method**: Raw fundus photograph displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "What diabetic retinopathy severity grade is shown in this fundus image?"
- **Answer Choices**: ["No diabetic retinopathy (Grade 0)", "Mild nonproliferative diabetic retinopathy (Grade 1)", "Moderate nonproliferative diabetic retinopathy (Grade 2)", "Severe nonproliferative diabetic retinopathy (Grade 3)", "Proliferative diabetic retinopathy (Grade 4)"]
- **Correct Answer**: "Moderate nonproliferative diabetic retinopathy (Grade 2)"  
**Complete Conversion Process Explanation**: 
1. Extract ordinal label "2" from dataset CSV indicating moderate nonproliferative diabetic retinopathy
2. Identify complete severity scale from dataset metadata: grades 0-4 with standard diabetic retinopathy terminology
3. Create 5-option multiple choice presenting all grades in natural progression order (0→4)
4. Use Grade 2 (moderate NPDR) as correct answer with other severity levels as distractors
5. Validate ordinal grading format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Moderate nonproliferative diabetic retinopathy requiring assessment within established clinical grading scale including microaneurysms, dot-blot hemorrhages, and cotton wool spots - tests ability to distinguish severity levels based on retinal vascular changes and progression of diabetic complications

### Example 2: Breast Cancer BIRADS Classification  
**Original Dataset Context and Annotation Format**: Mammography BIRADS assessment dataset with ordinal categories where labels include 1, 2, 3, 4, 5 representing increasing suspicion levels  
**Image Presentation Method**: Raw mammography image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "What BIRADS category is shown in this mammography image?"
- **Answer Choices**: ["BIRADS 1 - Negative", "BIRADS 2 - Benign finding", "BIRADS 3 - Probably benign", "BIRADS 4 - Suspicious abnormality", "BIRADS 5 - Highly suggestive of malignancy"] 
- **Correct Answer**: "BIRADS 4 - Suspicious abnormality"  
**Complete Conversion Process Explanation**:
1. Extract ordinal label "4" from dataset indicating BIRADS category 4 assessment
2. Identify complete BIRADS scale from dataset metadata: categories 1-5 with standard radiological terminology
3. Create 5-option multiple choice presenting all categories in natural progression order (1→5)
4. Use BIRADS 4 as correct answer with other assessment categories as distractors
5. Verify ordinal assessment format with single correct answer structure for MCVQA compliance  
**Clinical Rationale**: BIRADS 4 suspicious abnormality requiring assessment within established breast imaging reporting system - tests ability to categorize mammographic findings by suspicion level using standardized radiological classification that directly impacts clinical management and biopsy recommendations
