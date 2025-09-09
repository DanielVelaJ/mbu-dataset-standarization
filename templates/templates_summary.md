# Medical Image Analysis Templates Summary

## Overview

This document provides a comprehensive summary of all available templates in the MBU Dataset Standardization project. Templates convert medical datasets into MCVQA (Multiple Choice Visual Question Answering) format for standardized evaluation. All templates follow the standardized 6-section structure as defined in the template guidelines.

**Total Templates**: 73 active templates  
**Domains**: Domain-Agnostic (30) + Domain-Specific (43)  
**Last Updated**: Based on current template structure analysis

---

## Template Structure Summary

Each template includes:
- **Template Name**: Descriptive title and purpose
- **Task Type**: Classification, Detection, Segmentation, Landmarks, Counting, Vision-Language
- **Difficulty**: Easy, Medium, Hard
- **Question Pattern**: Template for question generation
- **Answer Format**: MCVQA-compliant response structure
- **Answer Choices**: Multiple choice options or specific formats
- **Compatible Datasets**: References to datasets in metadata file
- **Template ID**: Unique identifier
- **File Location**: Path within templates directory

---

# Domain-Agnostic Templates

## Classification Templates

### Binary Classification (9 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Binary Classification Template 1: Presence Detection | Easy | "Is {finding} present in this {modality} image?" | Yes/No | `domain-agnostic_classification_binary_easy_1` | `domain-agnostic/classification/binary/` |
| Binary Classification Template 3: Quality Assessment | Easy | "Is this {modality} image of diagnostic quality?" | Diagnostic Quality/Poor Quality | `domain-agnostic_classification_binary_easy_3` | `domain-agnostic/classification/binary/` |
| Binary Classification Template 2: Comparison Assessment | Medium | "Is this {modality} image {comparison_criteria}?" | Yes/No | `domain-agnostic_classification_binary_medium_2` | `domain-agnostic/classification/binary/` |
| Binary Classification Template 4: Temporal Assessment | Medium | "Does this {modality} image show {temporal_pattern}?" | Yes/No | `domain-agnostic_classification_binary_medium_4` | `domain-agnostic/classification/binary/` |
| Binary Classification Template 5: Severity Assessment | Medium | "Is this {finding} classified as {severity_level}?" | Yes/No | `domain-agnostic_classification_binary_medium_5` | `domain-agnostic/classification/binary/` |
| Binary Classification Template 6: Treatment Response | Medium | "Does this {modality} image show {response_type}?" | Yes/No | `domain-agnostic_classification_binary_medium_6` | `domain-agnostic/classification/binary/` |
| Binary Classification Template 7: Progression Assessment | Medium | "Does this {modality} image show {progression_status}?" | Yes/No | `domain-agnostic_classification_binary_medium_7` | `domain-agnostic/classification/binary/` |
| Binary Classification Template 8: Complex Feature Assessment | Hard | "Based on multiple criteria, is this {finding} present?" | Yes/No | `domain-agnostic_classification_binary_hard_8` | `domain-agnostic/classification/binary/` |
| Binary Classification Template 9: Meta-Assessment | Hard | "Is this diagnostic assessment {assessment_quality}?" | Yes/No | `domain-agnostic_classification_binary_hard_9` | `domain-agnostic/classification/binary/` |

### Multiclass Classification (3 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Multi-Class Classification Template 1: Basic Condition Identification | Easy | "What medical condition is shown in this {modality} image?" | Multiple condition options (A-D/E) | `domain-agnostic_classification_multiclass_easy_1` | `domain-agnostic/classification/multiclass/` |
| Multi-Class Classification Template 2: Disease Stage/Severity Grading | Easy | "What {assessment_type} is shown in this {modality} image?" | Multiple severity/stage levels (A-D/E) | `domain-agnostic_classification_multiclass_easy_2` | `domain-agnostic/classification/multiclass/` |
| Multi-Class Classification Template 3: Anatomical Region Identification | Easy | "What anatomical {structure_type} is primarily shown in this {modality} image?" | Multiple anatomical structures (A-D/E) | `domain-agnostic_classification_multiclass_easy_3` | `domain-agnostic/classification/multiclass/` |

### Multilabel Classification (3 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Multi-Label Classification Template 1: Multiple Finding Detection | Easy | "Which of the following findings are present?" | Multiple simultaneous selections | `domain-agnostic_classification_multilabel_easy_1` | `domain-agnostic/classification/multilabel/` |
| Multi-Label Classification Template 2: Anatomical Region Assessment | Easy | "Which anatomical regions show abnormalities?" | Multiple region selections | `domain-agnostic_classification_multilabel_easy_2` | `domain-agnostic/classification/multilabel/` |
| Multi-Label Classification Template 3: Pathology Pattern Recognition | Easy | "Which pathological patterns are visible?" | Multiple pattern selections | `domain-agnostic_classification_multilabel_easy_3` | `domain-agnostic/classification/multilabel/` |

### Ordinal Classification (3 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Ordinal Classification Template 1: Severity Grading | Easy | "What is the severity grade of {finding}?" | Ordered severity levels (Grade 1-5) | `domain-agnostic_classification_ordinal_easy_1` | `domain-agnostic/classification/ordinal/` |
| Ordinal Classification Template 2: Stage Assessment | Easy | "What stage is demonstrated in this {modality} image?" | Ordered stage progression | `domain-agnostic_classification_ordinal_easy_2` | `domain-agnostic/classification/ordinal/` |
| Ordinal Classification Template 3: Quality Scoring | Easy | "What quality score best describes this image?" | Ordered quality levels (1-5) | `domain-agnostic_classification_ordinal_easy_3` | `domain-agnostic/classification/ordinal/` |

## Object and Lesion Detection Templates

### Lesion Detection (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Object Detection Template 1: Lesion Localization | Easy | "Where is the {lesion_type} located in this image?" | Bounding box coordinates | `domain-agnostic_detection_object_easy_1` | `domain-agnostic/object-and-lesion-detection/lesion/` |

### Anatomy Detection (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Object Detection Template 2: Anatomical Structure Localization | Easy | "Where is the {anatomical_structure} located?" | Bounding box coordinates | `domain-agnostic_detection_object_easy_2` | `domain-agnostic/object-and-lesion-detection/anatomy/` |

### Device Detection (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Object Detection Template 3: Medical Device Localization | Easy | "Where is the {medical_device} located?" | Bounding box coordinates | `domain-agnostic_detection_object_easy_3` | `domain-agnostic/object-and-lesion-detection/device/` |

## Segmentation Templates

### Instance Segmentation (3 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Instance Segmentation Template 1: Instance Counting | Easy | "How many {object_type} are segmented in this image?" | Numerical count | `domain-agnostic_segmentation_instance_easy_1` | `domain-agnostic/segmentation/instance/` |
| Instance Segmentation Template 2: Instance Properties | Easy | "What is the {property} of the highlighted {object_type}?" | Property value options | `domain-agnostic_segmentation_instance_easy_2` | `domain-agnostic/segmentation/instance/` |
| Instance Segmentation Template 3: Instance Relationships | Easy | "What is the spatial relationship between instances?" | Relationship options | `domain-agnostic_segmentation_instance_easy_3` | `domain-agnostic/segmentation/instance/` |

### Semantic Segmentation (3 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Semantic Segmentation Template 1: Region Classification | Easy | "What type of tissue is shown in the highlighted region?" | Tissue type options | `domain-agnostic_segmentation_semantic_easy_1` | `domain-agnostic/segmentation/semantic/` |
| Semantic Segmentation Template 2: Area Assessment | Easy | "What percentage of the image shows {tissue_type}?" | Percentage ranges | `domain-agnostic_segmentation_semantic_easy_2` | `domain-agnostic/segmentation/semantic/` |
| Semantic Segmentation Template 3: Region Properties | Easy | "What property characterizes the segmented region?" | Property options | `domain-agnostic_segmentation_semantic_easy_3` | `domain-agnostic/segmentation/semantic/` |

## Anatomical Landmarks Templates

### Single Landmark (2 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Single Landmark Template 1: Point Localization | Easy | "Where is the {landmark_name} located?" | X,Y coordinates | `domain-agnostic_anatomical-landmarks-keypoints_single_easy_1` | `domain-agnostic/anatomical-landmarks-keypoints/single/` |
| Single Landmark Template 2: Landmark Identification | Easy | "What landmark is indicated at the marked location?" | Landmark name options | `domain-agnostic_anatomical-landmarks-keypoints_single_easy_2` | `domain-agnostic/anatomical-landmarks-keypoints/single/` |

### Multiple Landmarks (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Multiple Landmarks Template 1: Multi-Point Assessment | Easy | "How many {landmark_type} landmarks are visible?" | Numerical count | `domain-agnostic_anatomical-landmarks-keypoints_multiple_easy_1` | `domain-agnostic/anatomical-landmarks-keypoints/multiple/` |

## Vision-Language Templates

### Description - Short (2 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Vision-Language Description Template 1: Short Medical Caption Selection | Easy | "Which best describes this {modality} image?" | Multiple caption options | `domain-agnostic_vision-language_describe_short_easy_1` | `domain-agnostic/vision-language/describe/short/` |
| Vision-Language Description Template 2: Findings Description | Easy | "Which statement best describes the findings?" | Finding description options | `domain-agnostic_vision-language_describe_short_easy_2` | `domain-agnostic/vision-language/describe/short/` |

### Description - Long (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Vision-Language Description Template 1: Comprehensive Medical Report Selection | Easy | "Which report best describes this image?" | Multiple detailed report options | `domain-agnostic_vision-language_describe_long_easy_1` | `domain-agnostic/vision-language/describe/long/` |

---

# Domain-Specific Templates

## Dermatology Domain (8 templates)

### Binary Classification (3 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Dermatology Malignant vs Benign Lesion Assessment | Easy | "Based on dermatological features, is this lesion malignant or benign?" | Malignant/Benign | `domain-specific_dermatology_classification_binary_easy_1` | `domain-specific/dermatology/classification/binary/` |
| Dermatology Inflammatory vs Non-inflammatory Assessment | Easy | "Based on dermatological features, is this condition inflammatory or non-inflammatory?" | Inflammatory/Non-inflammatory | `domain-specific_dermatology_classification_binary_easy_2` | `domain-specific/dermatology/classification/binary/` |
| Dermatology Pigmented vs Non-pigmented Lesion Assessment | Easy | "Based on dermatological features, is this a pigmented or non-pigmented lesion?" | Pigmented/Non-pigmented | `domain-specific_dermatology_classification_binary_easy_3` | `domain-specific/dermatology/classification/binary/` |

### Multiclass Classification (4 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Dermatology Skin Cancer Classification | Easy | "Based on dermatological features, what type of skin cancer is most likely?" | Multiple skin cancer types | `domain-specific_dermatology_classification_multiclass_easy_1` | `domain-specific/dermatology/classification/multiclass/` |
| Dermatology Dermoscopic Pattern Recognition | Easy | "What dermoscopic pattern is predominantly visible?" | Multiple dermoscopic patterns | `domain-specific_dermatology_classification_multiclass_easy_2` | `domain-specific/dermatology/classification/multiclass/` |
| Dermatology Condition Category Assessment | Easy | "What category of dermatological condition is shown?" | Multiple condition categories | `domain-specific_dermatology_classification_multiclass_easy_3` | `domain-specific/dermatology/classification/multiclass/` |
| Dermatology Anatomical Location-Based Diagnosis | Easy | "Given the anatomical location and features, what is the most likely diagnosis?" | Multiple location-specific diagnoses | `domain-specific_dermatology_classification_multiclass_easy_4` | `domain-specific/dermatology/classification/multiclass/` |

### Ordinal Classification (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Dermatology Fitzpatrick Skin Type Assessment | Easy | "What Fitzpatrick skin type is shown in this image?" | Type I-VI (ordered) | `domain-specific_dermatology_classification_ordinal_easy_1` | `domain-specific/dermatology/classification/ordinal/` |

## Ophthalmology Domain (8 templates)

### Binary Classification (3 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Ophthalmology Optic Disc vs Cup Differentiation | Easy | "Is the highlighted region the optic disc or optic cup?" | Optic disc/Optic cup | `domain-specific_ophthalmology_classification_binary_easy_1` | `domain-specific/ophthalmology/classification/binary/` |
| Ophthalmology Pupil Response Assessment | Easy | "Does this pupil show normal reactive response?" | Normal/Abnormal response | `domain-specific_ophthalmology_classification_binary_easy_2` | `domain-specific/ophthalmology/classification/binary/` |
| Ophthalmology Anterior vs Posterior Segment Identification | Easy | "Does this image show anterior or posterior segment anatomy?" | Anterior/Posterior segment | `domain-specific_ophthalmology_classification_binary_easy_3` | `domain-specific/ophthalmology/classification/binary/` |

### Multiclass Classification (4 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Ophthalmology Anatomical Structure Identification | Easy | "What primary anatomical structure is shown in this fundus image?" | Multiple retinal structures | `domain-specific_ophthalmology_classification_multiclass_easy_1` | `domain-specific/ophthalmology/classification/multiclass/` |
| Ophthalmology OCT Retinal Pathology Analysis | Easy | "What retinal pathology is identified in this OCT image?" | Multiple retinal pathologies | `domain-specific_ophthalmology_classification_multiclass_easy_2` | `domain-specific/ophthalmology/classification/multiclass/` |
| Ophthalmology Optic Disc Location Assessment | Easy | "What is the spatial location of the optic disc?" | Multiple spatial locations | `domain-specific_ophthalmology_classification_multiclass_easy_3` | `domain-specific/ophthalmology/classification/multiclass/` |
| Ophthalmology Comparative Fundus Analysis | Easy | "What comparative pathology assessment applies to retinal quadrants?" | Multiple comparative assessments | `domain-specific_ophthalmology_classification_multiclass_easy_4` | `domain-specific/ophthalmology/classification/multiclass/` |

### Ordinal Classification (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Ophthalmology Diabetic Retinopathy Grading | Easy | "What diabetic retinopathy severity grade is shown?" | Severity grades (ordered) | `domain-specific_ophthalmology_classification_ordinal_easy_1` | `domain-specific/ophthalmology/classification/ordinal/` |

## Pathology Domain (8 templates)

### Binary Classification (3 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Pathology Malignant vs Benign Tissue Classification | Easy | "Based on histopathological features, is this tissue malignant or benign?" | Malignant/Benign | `domain-specific_pathology_classification_binary_easy_1` | `domain-specific/pathology/classification/binary/` |
| Pathology Tumor vs Normal Tissue Differentiation | Easy | "Based on histopathological features, is this tumor or normal tissue?" | Tumor/Normal tissue | `domain-specific_pathology_classification_binary_easy_2` | `domain-specific/pathology/classification/binary/` |
| Pathology High-Grade vs Low-Grade Neoplasm Assessment | Easy | "Based on histopathological features, is this high-grade or low-grade?" | High-grade/Low-grade | `domain-specific_pathology_classification_binary_easy_3` | `domain-specific/pathology/classification/binary/` |

### Multiclass Classification (3 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Pathology Cancer Type Classification | Easy | "What specific cancer type is identified in this histopathological image?" | Multiple cancer types | `domain-specific_pathology_classification_multiclass_easy_1` | `domain-specific/pathology/classification/multiclass/` |
| Pathology Tissue Type Identification | Easy | "What fundamental tissue type is shown?" | Multiple tissue types | `domain-specific_pathology_classification_multiclass_easy_2` | `domain-specific/pathology/classification/multiclass/` |
| Pathology Inflammatory Pattern Classification | Easy | "What inflammatory pattern is recognized?" | Multiple inflammatory patterns | `domain-specific_pathology_classification_multiclass_easy_3` | `domain-specific/pathology/classification/multiclass/` |

### Counting (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Pathology Mitotic Figure Counting Assessment | Easy | "What is the mitotic figure density evaluation?" | Multiple density categories | `domain-specific_pathology_counting_direct_easy_1` | `domain-specific/pathology/counting/direct/` |

### Segmentation (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Pathology Nuclear Segmentation Quality Assessment | Easy | "What best describes the nuclear segmentation characteristics in this histopathological image?" | Multiple segmentation quality options | `domain-specific_pathology_segmentation_instance_easy_1` | `domain-specific/pathology/segmentation/instance/` |

## Surgery Domain (8 templates)

### Binary Classification (2 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Surgery Critical View of Safety Achievement | Easy | "Has the critical view of safety been achieved?" | Critical view achieved/Not achieved | `surgery_classification_binary_easy_1` | `domain-specific/surgery/classification/binary/` |
| Surgery Tissue Plane Assessment | Easy | "Is the tissue plane adequately developed?" | Adequate/Inadequate | `surgery_classification_binary_easy_2` | `domain-specific/surgery/classification/binary/` |

### Multiclass Classification (4 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Surgery Surgical Phase Recognition | Easy | "What surgical phase is currently shown in this surgical video frame?" | Multiple surgical phases | `surgery_classification_multiclass_easy_1` | `domain-specific/surgery/classification/multiclass/` |
| Surgery Anatomical Structure Identification | Easy | "What anatomical structure is primarily visible?" | Multiple surgical structures | `surgery_classification_multiclass_easy_2` | `domain-specific/surgery/classification/multiclass/` |
| Surgery Tool Identification | Easy | "What surgical tool is being used?" | Multiple surgical tools | `surgery_classification_multiclass_easy_3` | `domain-specific/surgery/classification/multiclass/` |
| Surgery Complication Assessment | Easy | "What type of complication is evident?" | Multiple complication types | `surgery_classification_multiclass_easy_4` | `domain-specific/surgery/classification/multiclass/` |

### Ordinal Classification (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Surgery Technical Skill Assessment | Easy | "What technical skill level is demonstrated?" | Skill levels (ordered) | `surgery_classification_ordinal_easy_1` | `domain-specific/surgery/classification/ordinal/` |

### Landmarks (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Surgery Multiple Anatomical Landmarks | Easy | "How many surgical landmarks are identified?" | Numerical count | `surgery_landmarks_multiple_easy_1` | `domain-specific/surgery/anatomical-landmarks-keypoints/multiple/` |

## Radiology Domain (3 templates)

### Binary Classification (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Radiology Abnormality Detection | Easy | "Is there an abnormality present in this radiological image?" | Abnormal/Normal | `radiology_classification_binary_easy_1` | `domain-specific/radiology/classification/binary/` |

### Multilabel Classification (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Radiology Multiple Finding Detection | Easy | "Which radiological findings are present?" | Multiple simultaneous findings | `radiology_classification_multilabel_easy_1` | `domain-specific/radiology/classification/multilabel/` |

### Vision-Language (1 template)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Radiology Short Report Generation | Easy | "Which report best describes this radiological image?" | Multiple report options | `radiology_vision-language_describe_short_easy_1` | `domain-specific/radiology/vision-language/describe/short/` |

## Other-Medical Domain (8 templates)

### Binary Classification (2 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Other-Medical Abnormality Detection | Easy | "Is there an abnormality present in this medical image?" | Abnormal/Normal | `other-medical_classification_binary_easy_1` | `domain-specific/other-medical/classification/binary/` |
| Other-Medical Treatment Response Assessment | Easy | "Does this image show positive treatment response?" | Positive/Negative response | `other-medical_classification_binary_easy_2` | `domain-specific/other-medical/classification/binary/` |

### Multiclass Classification (4 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Other-Medical Condition Classification | Easy | "What medical condition is most likely shown?" | Multiple medical conditions | `other-medical_classification_multiclass_easy_1` | `domain-specific/other-medical/classification/multiclass/` |
| Other-Medical Anatomical Region Classification | Easy | "What anatomical region is primarily shown?" | Multiple anatomical regions | `other-medical_classification_multiclass_easy_2` | `domain-specific/other-medical/classification/multiclass/` |
| Other-Medical Finding Type Classification | Easy | "What type of medical finding is demonstrated?" | Multiple finding types | `other-medical_classification_multiclass_easy_3` | `domain-specific/other-medical/classification/multiclass/` |
| Other-Medical Severity Assessment | Easy | "What severity level is most appropriate?" | Multiple severity levels | `other-medical_classification_multiclass_easy_4` | `domain-specific/other-medical/classification/multiclass/` |

### Vision-Language (2 templates)

| Template Name | Difficulty | Question Pattern | Answer Choices | Template ID | File Location |
|---------------|------------|------------------|----------------|-------------|---------------|
| Other-Medical Short Description | Easy | "Which description best fits this medical image?" | Multiple description options | `other-medical_vision-language_describe_short_easy_1` | `domain-specific/other-medical/vision-language/describe/short/` |
| Other-Medical Open-Ended Q&A | Easy | "What is the answer to this medical question about the image?" | Multiple answer options | `other-medical_vision-language_ask-answer_open-ended_easy_1` | `domain-specific/other-medical/vision-language/ask-and-answer/open-ended/` |

---

## Template Statistics Summary

### By Domain Type
- **Domain-Agnostic**: 30 templates (41%)
- **Domain-Specific**: 43 templates (59%)

### By Task Type
- **Classification**: 57 templates (78%)
  - Binary: 29 templates
  - Multiclass: 20 templates  
  - Multilabel: 4 templates
  - Ordinal: 4 templates
- **Detection**: 3 templates (4%)
- **Segmentation**: 7 templates (10%)
- **Landmarks**: 3 templates (4%)
- **Vision-Language**: 6 templates (8%)
- **Counting**: 1 template (1%)

### By Difficulty
- **Easy**: 66 templates (90%)
- **Medium**: 5 templates (7%)
- **Hard**: 2 templates (3%)

### By Medical Domain (Domain-Specific)
- **Dermatology**: 8 templates (19%)
- **Ophthalmology**: 8 templates (19%)
- **Pathology**: 7 templates (17%)
- **Surgery**: 8 templates (19%)
- **Radiology**: 3 templates (7%)
- **Other-Medical**: 8 templates (19%)

---

## Key Features and Standards

### MCVQA Compliance
All templates ensure:
- **Single Correct Answer**: Each question has exactly one correct answer
- **Multiple Choice Format**: Discrete answer options provided
- **No Free Text**: No open-ended text generation
- **Deterministic Answers**: Objectively verifiable responses

### Template Structure Compliance
All templates follow the standardized 6-section format:
1. **Template Overview** (ID, Task Type, Difficulty, Question Pattern, Medical Domain, Domain-knowledge summary)
2. **Template Description** (Purpose, clinical context, use cases)
3. **Question Generation Pattern** (Question format, answer format, variables, image presentation, answer construction)
4. **Dataset Requirements** (Task types, label structures, compatible datasets)
5. **Template Usage Rules** (Implementation guidelines, label mapping, conversion process, schema alignment)
6. **Examples** (Exactly 2 concrete examples with dataset references)

### Naming Convention Compliance
All templates follow the standardized naming pattern:
- **Format**: `{domain}_{task}_{subtype}_{difficulty}_{number}.md`
- **Template IDs**: Match filename structure
- **Consistent Organization**: Hierarchical directory structure

---

## Usage Guidelines

### Template Selection
1. **Identify Task Type**: Classification, Detection, Segmentation, etc.
2. **Determine Domain**: Domain-agnostic for general use, domain-specific for specialized medical fields
3. **Select Difficulty**: Easy for basic tasks, Medium/Hard for complex reasoning
4. **Check Compatibility**: Verify dataset requirements match your data structure

### Implementation Process
1. **Read Template**: Review all 6 sections thoroughly
2. **Verify Dataset Compatibility**: Check dataset requirements section
3. **Extract Variables**: Identify and populate template variables
4. **Generate Questions**: Follow question generation pattern exactly
5. **Validate MCVQA**: Ensure single correct answer and multiple choice format
6. **Test Examples**: Use provided examples as validation references

### Quality Assurance
- **Medical Accuracy**: Verify clinical terminology and diagnostic criteria
- **Schema Compliance**: Align with unified datum schema v1.0
- **Consistency**: Maintain template structure and formatting standards
- **Documentation**: Include provenance tracking and rule IDs

---

*This summary is automatically maintained and reflects the current state of all templates in the repository. For specific implementation details, refer to individual template files and the general template guidelines.*