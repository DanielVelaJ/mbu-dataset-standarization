# Templates Summary

## Overview

This document provides a comprehensive overview of all MCVQA (Multiple Choice Visual Question Answering) templates available in the MBU Dataset Standardization project. Templates are organized hierarchically by domain (agnostic vs specific) and task type, mirroring the directory structure.

**Total Templates**: 79 templates across 6 major task categories and 6 medical specialties

---

## Quick Navigation

- [Domain-Agnostic Templates](#domain-agnostic-templates) (43 templates)
  - [Classification](#classification-28-templates) (28 templates)
  - [Object & Lesion Detection](#object--lesion-detection-3-templates) (3 templates)
  - [Segmentation](#segmentation-6-templates) (6 templates) 
  - [Anatomical Landmarks](#anatomical-landmarks--keypoints-3-templates) (3 templates)
  - [Vision-Language](#vision-language-3-templates) (3 templates)
- [Domain-Specific Templates](#domain-specific-templates) (36 templates)
  - [Dermatology](#dermatology-10-templates) (10 templates)
  - [Ophthalmology](#ophthalmology-8-templates) (8 templates)
  - [Other-Medical](#other-medical-8-templates) (8 templates)
  - [Pathology](#pathology-8-templates) (8 templates)
  - [Radiology](#radiology-3-templates) (3 templates)
  - [Surgery](#surgery-10-templates) (10 templates)

---

# Domain-Agnostic Templates

*Templates that work across all medical domains requiring only basic information (image + label + modality)*

## Classification (28 templates)

### Binary Classification (9 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Presence Detection | `classification_binary_1` | Easy | "Is {finding} present in this {modality} image?" | Yes/No | `domain-agnostic/classification/binary/domain-agnostic_classification_binary_easy_1.md` |
| Multiple Choice with Distractors | `classification_binary_2` | Medium | "What condition is shown in this {modality} image?" | A/B/C/D (with distractors) | `domain-agnostic/classification/binary/classification_binary_2.md` |
| Normal vs Abnormal | `classification_binary_3` | Easy | "Is this {modality} image normal or abnormal?" | Normal/Abnormal | `domain-agnostic/classification/binary/classification_binary_3.md` |
| Likelihood Assessment | `classification_binary_4` | Medium | "What is the likelihood of {condition} in this {modality} image?" | Very unlikely/Unlikely/Likely/Very likely | `domain-agnostic/classification/binary/classification_binary_4.md` |
| Exclusionary Assessment | `classification_binary_5` | Medium | "Can {condition} be ruled out based on this {modality} image?" | Yes, can be ruled out/No, cannot be ruled out | `domain-agnostic/classification/binary/classification_binary_5.md` |
| Clear Evidence Assessment | `classification_binary_6` | Easy-Medium | "Is there clear evidence of {condition} in this {modality} image?" | Yes, clear evidence/No clear evidence | `domain-agnostic/classification/binary/classification_binary_6.md` |
| Detection Capability | `classification_binary_7` | Easy-Medium | "Can {condition} be detected in this {modality} image?" | Yes, detectable/No, not detectable | `domain-agnostic/classification/binary/classification_binary_7.md` |
| Definition-Based Assessment | `classification_binary_8` | Hard | "Which definition best describes what is shown in this {modality} image?" | Multiple choice with definitions | `domain-agnostic/classification/binary/classification_binary_8.md` |
| Multi-Doctor Clinical Assessment | `classification_binary_9` | Hard | Complex clinical reasoning with doctor assessments | Doctor selection based on accuracy | `domain-agnostic/classification/binary/classification_binary_9.md` |

### Multiclass Classification (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Basic Condition Identification | `agnostic_classification_multiclass_1` | Easy | "What medical condition is shown in this {modality} image?" | Multiple choice conditions | `domain-agnostic/classification/multiclass/agnostic_classification_multiclass_1.md` |
| Disease Stage/Severity Grading | `agnostic_classification_multiclass_2` | Easy | "What {assessment_type} is shown in this {modality} image?" | Multiple choice grades/stages | `domain-agnostic/classification/multiclass/agnostic_classification_multiclass_2.md` |
| Anatomical Region Identification | `agnostic_classification_multiclass_3` | Easy | "What anatomical {structure_type} is primarily shown in this {modality} image?" | Multiple choice anatomical regions | `domain-agnostic/classification/multiclass/agnostic_classification_multiclass_3.md` |

### Multilabel Classification (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Multiple Findings Detection | `domain-agnostic_classification_multilabel_easy_1` | Easy | "Which of the following findings are present in this {modality} image?" | Multiple correct selections | `domain-agnostic/classification/multilabel/domain-agnostic_classification_multilabel_easy_1.md` |
| Simultaneous Conditions Assessment | `domain-agnostic_classification_multilabel_easy_2` | Easy | "Which conditions can be identified in this {modality} image?" | Multiple conditions selection | `domain-agnostic/classification/multilabel/domain-agnostic_classification_multilabel_easy_2.md` |
| Multi-System Abnormalities | `domain-agnostic_classification_multilabel_easy_3` | Easy | "What abnormalities are visible across different systems?" | Multi-system findings | `domain-agnostic/classification/multilabel/domain-agnostic_classification_multilabel_easy_3.md` |

### Ordinal Classification (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Severity Grading | `domain-agnostic_classification_ordinal_easy_1` | Easy | "What is the severity grade of {condition} in this {modality} image?" | Ordered severity levels | `domain-agnostic/classification/ordinal/domain-agnostic_classification_ordinal_easy_1.md` |
| Disease Stage Assessment | `domain-agnostic_classification_ordinal_easy_2` | Easy | "What stage of {condition} is shown in this {modality} image?" | Progressive disease stages | `domain-agnostic/classification/ordinal/domain-agnostic_classification_ordinal_easy_2.md` |
| Progressive Assessment Scale | `domain-agnostic_classification_ordinal_easy_3` | Easy | "According to the {scale_name}, what grade is this {modality} image?" | Standardized grading scales | `domain-agnostic/classification/ordinal/domain-agnostic_classification_ordinal_easy_3.md` |

## Object & Lesion Detection (3 templates)

| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Lesion Detection | `domain-agnostic_detection_object_easy_1` | Easy | "Where is the {lesion_type} located in this {modality} image?" | Bounding box regions | `domain-agnostic/object-and-lesion-detection/lesion/domain-agnostic_detection_object_easy_1.md` |
| Anatomical Structure Detection | `domain-agnostic_detection_object_easy_2` | Easy | "Where is the {anatomical_structure} located in this {modality} image?" | Anatomical bounding boxes | `domain-agnostic/object-and-lesion-detection/anatomy/domain-agnostic_detection_object_easy_2.md` |
| Medical Device Detection | `domain-agnostic_detection_object_easy_3` | Easy | "Where is the {medical_device} located in this {modality} image?" | Device bounding boxes | `domain-agnostic/object-and-lesion-detection/device/domain-agnostic_detection_object_easy_3.md` |

## Segmentation (6 templates)

### Semantic Segmentation (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Region Identification | `domain-agnostic_segmentation_semantic_easy_1` | Easy | "What anatomical structure is highlighted in the segmented region?" | Structure identification | `domain-agnostic/segmentation/semantic/domain-agnostic_segmentation_semantic_easy_1.md` |
| Tissue Type Classification | `domain-agnostic_segmentation_semantic_easy_2` | Easy | "What type of tissue is shown in the segmented area?" | Tissue type selection | `domain-agnostic/segmentation/semantic/domain-agnostic_segmentation_semantic_easy_2.md` |
| Pathology Segmentation | `domain-agnostic_segmentation_semantic_easy_3` | Easy | "What pathological condition is segmented in this region?" | Pathology identification | `domain-agnostic/segmentation/semantic/domain-agnostic_segmentation_semantic_easy_3.md` |

### Instance Segmentation (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Multiple Object Counting | `domain-agnostic_segmentation_instance_easy_1` | Easy | "How many {object_type} are segmented in this {modality} image?" | Count-based answers | `domain-agnostic/segmentation/instance/domain-agnostic_segmentation_instance_easy_1.md` |
| Individual Object Classification | `domain-agnostic_segmentation_instance_easy_2` | Easy | "What type of object is highlighted in instance {instance_id}?" | Object type per instance | `domain-agnostic/segmentation/instance/domain-agnostic_segmentation_instance_easy_2.md` |
| Instance Relationship Analysis | `domain-agnostic_segmentation_instance_easy_3` | Easy | "What is the spatial relationship between instances in this image?" | Spatial relationships | `domain-agnostic/segmentation/instance/domain-agnostic_segmentation_instance_easy_3.md` |

## Anatomical Landmarks & Keypoints (3 templates)

### Single Landmark (2 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Single Landmark Localization | `anatomical_landmarks_single_1` | Easy | "Where is the {landmark} located in this {modality} image?" | Coordinate regions | `domain-agnostic/anatomical-landmarks-keypoints/single/domain-agnostic_anatomical-landmarks-keypoints_single_easy_1.md` |
| Landmark Distance Measurement | `domain-agnostic_anatomical-landmarks-keypoints_single_easy_2` | Easy | "What is the distance between {landmark1} and {landmark2}?" | Distance measurements | `domain-agnostic/anatomical-landmarks-keypoints/single/domain-agnostic_anatomical-landmarks-keypoints_single_easy_2.md` |

### Multiple Landmarks (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Multiple Landmark Identification | `domain-agnostic_anatomical-landmarks-keypoints_multiple_easy_1` | Easy | "Which landmarks are correctly identified in this {modality} image?" | Multiple landmark verification | `domain-agnostic/anatomical-landmarks-keypoints/multiple/domain-agnostic_anatomical-landmarks-keypoints_multiple_easy_1.md` |

## Vision-Language (3 templates)

### Describe - Short (2 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Short Medical Caption Selection | `vision_language_describe_short_1` | Easy | "Which of the following best describes this {modality} image?" | Caption selection | `domain-agnostic/vision-language/describe/short/domain-agnostic_vision-language_describe_short_easy_1.md` |
| Clinical Finding Description | `domain-agnostic_vision-language_describe_short_easy_2` | Easy | "Select the most accurate clinical description for this image" | Clinical descriptions | `domain-agnostic/vision-language/describe/short/domain-agnostic_vision-language_describe_short_easy_2.md` |

### Describe - Long (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | File Location |
|----------|----|-----------|-----------------|--------------|--------------| 
| Comprehensive Medical Report | `domain-agnostic_vision-language_describe_long_easy_1` | Easy | "Which detailed report best describes this {modality} image?" | Long-form medical reports | `domain-agnostic/vision-language/describe/long/domain-agnostic_vision-language_describe_long_easy_1.md` |

---

# Domain-Specific Templates

*Templates requiring medical domain expertise and specialized knowledge*

## Dermatology (10 templates)

### Binary Classification (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Malignant vs Benign Assessment | `dermatology_classification_binary_easy_1` | Easy | "Is this lesion malignant or benign?" | Malignant/Benign | ISIC, HAM10000, Melanoma datasets | `domain-specific/dermatology/classification/binary/dermatology_classification_binary_easy_1.md` |
| Melanoma Detection | `dermatology_classification_binary_easy_2` | Easy | "Is this a melanoma?" | Yes/No | Melanoma-specific datasets | `domain-specific/dermatology/classification/binary/dermatology_classification_binary_easy_2.md` |
| Inflammatory vs Non-inflammatory | `dermatology_classification_binary_easy_3` | Easy | "Is this an inflammatory skin condition?" | Yes/No | Dermatology classification datasets | `domain-specific/dermatology/classification/binary/dermatology_classification_binary_easy_3.md` |

### Multiclass Classification (5 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Skin Lesion Type Classification | `dermatology_classification_multiclass_easy_1` | Easy | "What type of skin lesion is this?" | Multiple lesion types | HAM10000, DermNet, ISIC | `domain-specific/dermatology/classification/multiclass/dermatology_classification_multiclass_easy_1.md` |
| Skin Cancer Subtype | `dermatology_classification_multiclass_easy_2` | Easy | "What subtype of skin cancer is shown?" | Cancer subtypes | Melanoma classification datasets | `domain-specific/dermatology/classification/multiclass/dermatology_classification_multiclass_easy_2.md` |
| Dermatological Condition Classification | `dermatology_classification_multiclass_easy_3` | Easy | "What dermatological condition is present?" | Skin conditions | DermNet, dermatology atlases | `domain-specific/dermatology/classification/multiclass/dermatology_classification_multiclass_easy_3.md` |
| Pigmented Lesion Diagnosis | `dermatology_classification_multiclass_easy_4` | Easy | "What is the diagnosis for this pigmented lesion?" | Pigmented lesion types | Dermoscopy datasets | `domain-specific/dermatology/classification/multiclass/dermatology_classification_multiclass_easy_4.md` |

### Ordinal Classification (2 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Melanoma ABCDE Severity | `dermatology_classification_ordinal_easy_1` | Easy | "What ABCDE severity grade is this melanoma?" | Grade 0-4 | Melanoma grading datasets | `domain-specific/dermatology/classification/ordinal/dermatology_classification_ordinal_easy_1.md` |

## Ophthalmology (8 templates)

### Binary Classification (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Diabetic Retinopathy Detection | `ophthalmology_classification_binary_easy_1` | Easy | "Is diabetic retinopathy present?" | Yes/No | EyePACS, APTOS, IDRiD | `domain-specific/ophthalmology/classification/binary/ophthalmology_classification_binary_easy_1.md` |
| Glaucoma Detection | `ophthalmology_classification_binary_easy_2` | Easy | "Are there signs of glaucoma?" | Yes/No | Glaucoma detection datasets | `domain-specific/ophthalmology/classification/binary/ophthalmology_classification_binary_easy_2.md` |
| Age-related Macular Degeneration | `ophthalmology_classification_binary_easy_3` | Easy | "Is AMD present in this fundus image?" | Yes/No | AMD datasets | `domain-specific/ophthalmology/classification/binary/ophthalmology_classification_binary_easy_3.md` |

### Multiclass Classification (4 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Retinal Disease Classification | `ophthalmology_classification_multiclass_easy_1` | Easy | "What retinal condition is shown?" | Multiple retinal diseases | Multi-disease retinal datasets | `domain-specific/ophthalmology/classification/multiclass/ophthalmology_classification_multiclass_easy_1.md` |
| Fundus Abnormality Detection | `ophthalmology_classification_multiclass_easy_2` | Easy | "What abnormality is visible in this fundus?" | Fundus abnormalities | Comprehensive eye datasets | `domain-specific/ophthalmology/classification/multiclass/ophthalmology_classification_multiclass_easy_2.md` |
| Optic Disc Assessment | `ophthalmology_classification_multiclass_easy_3` | Easy | "What is the condition of the optic disc?" | Optic disc conditions | Glaucoma, papilledema datasets | `domain-specific/ophthalmology/classification/multiclass/ophthalmology_classification_multiclass_easy_3.md` |
| Macular Condition Classification | `ophthalmology_classification_multiclass_easy_4` | Easy | "What macular condition is present?" | Macular diseases | AMD, diabetic maculopathy datasets | `domain-specific/ophthalmology/classification/multiclass/ophthalmology_classification_multiclass_easy_4.md` |

### Ordinal Classification (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Diabetic Retinopathy Grading | `ophthalmology_classification_ordinal_easy_1` | Easy | "What grade of diabetic retinopathy is shown?" | Grade 0-4 | EyePACS, APTOS diabetic retinopathy | `domain-specific/ophthalmology/classification/ordinal/ophthalmology_classification_ordinal_easy_1.md` |

## Other-Medical (8 templates)

### Binary Classification (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| General Medical Abnormality | `other-medical_classification_binary_easy_1` | Easy | "Is there a medical abnormality in this image?" | Yes/No | Multi-domain medical datasets | `domain-specific/other-medical/classification/binary/other-medical_classification_binary_easy_1.md` |
| Chronic vs Acute Condition | `other-medical_classification_binary_easy_2` | Easy | "Is this a chronic or acute condition?" | Chronic/Acute | Temporal medical datasets | `domain-specific/other-medical/classification/binary/other-medical_classification_binary_easy_2.md` |

### Multiclass Classification (4 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Medical Specialty Classification | `other-medical_classification_multiclass_easy_1` | Easy | "Which medical specialty would handle this case?" | Medical specialties | Cross-specialty datasets | `domain-specific/other-medical/classification/multiclass/other-medical_classification_multiclass_easy_1.md` |
| Body System Classification | `other-medical_classification_multiclass_easy_2` | Easy | "Which body system is primarily affected?" | Body systems | Multi-system medical images | `domain-specific/other-medical/classification/multiclass/other-medical_classification_multiclass_easy_2.md` |
| Imaging Modality Optimization | `other-medical_classification_multiclass_easy_3` | Easy | "What imaging modality would be most appropriate?" | Imaging modalities | Multi-modal datasets | `domain-specific/other-medical/classification/multiclass/other-medical_classification_multiclass_easy_3.md` |
| Treatment Priority Assessment | `other-medical_classification_multiclass_easy_4` | Easy | "What is the treatment priority level?" | Priority levels | Triage, emergency datasets | `domain-specific/other-medical/classification/multiclass/other-medical_classification_multiclass_easy_4.md` |

### Vision-Language (2 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Medical Report Generation | `other-medical_vision-language_describe_short_easy_1` | Easy | "Select the most appropriate medical report" | Report selection | Medical report datasets | `domain-specific/other-medical/vision-language/describe/short/other-medical_vision-language_describe_short_easy_1.md` |
| Clinical Question Answering | `other-medical_vision-language_ask-answer_open-ended_easy_1` | Easy | "What is the most likely diagnosis?" | Diagnosis options | Medical VQA datasets | `domain-specific/other-medical/vision-language/ask-and-answer/open-ended/other-medical_vision-language_ask-answer_open-ended_easy_1.md` |

## Pathology (8 templates)

### Binary Classification (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Cancer vs Normal Tissue | `pathology_classification_binary_easy_1` | Easy | "Is this tissue malignant or normal?" | Malignant/Normal | Histopathology cancer datasets | `domain-specific/pathology/classification/binary/pathology_classification_binary_easy_1.md` |
| Mitosis Detection | `pathology_classification_binary_easy_2` | Easy | "Is mitotic activity present?" | Yes/No | Mitosis detection datasets | `domain-specific/pathology/classification/binary/pathology_classification_binary_easy_2.md` |
| Tissue Inflammation | `pathology_classification_binary_easy_3` | Easy | "Is there evidence of inflammation?" | Yes/No | Inflammatory pathology datasets | `domain-specific/pathology/classification/binary/pathology_classification_binary_easy_3.md` |

### Multiclass Classification (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Cancer Type Classification | `pathology_classification_multiclass_easy_1` | Easy | "What type of cancer is shown?" | Cancer types | Multi-cancer histopathology | `domain-specific/pathology/classification/multiclass/pathology_classification_multiclass_easy_1.md` |
| Tissue Type Identification | `pathology_classification_multiclass_easy_2` | Easy | "What type of tissue is this?" | Tissue types | Histopathology atlases | `domain-specific/pathology/classification/multiclass/pathology_classification_multiclass_easy_2.md` |
| Histological Grade Assessment | `pathology_classification_multiclass_easy_3` | Easy | "What histological grade is this tumor?" | Tumor grades | Cancer grading datasets | `domain-specific/pathology/classification/multiclass/pathology_classification_multiclass_easy_3.md` |

### Counting (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Cell Counting | `pathology_counting_direct_easy_1` | Easy | "How many {cell_type} are present?" | Numerical count | Cell counting datasets | `domain-specific/pathology/counting/direct/pathology_counting_direct_easy_1.md` |

### Segmentation (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Tumor Segmentation | `pathology_segmentation_instance_easy_1` | Easy | "Where are the tumor regions located?" | Segmentation masks | Pathology segmentation datasets | `domain-specific/pathology/segmentation/instance/pathology_segmentation_instance_easy_1.md` |

## Radiology (3 templates)

### Binary Classification (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Radiological Abnormality Detection | `radiology_classification_binary_easy_1` | Easy | "Is there a radiological abnormality?" | Yes/No | Chest X-ray, CT, MRI datasets | `domain-specific/radiology/classification/binary/radiology_classification_binary_easy_1.md` |

### Multilabel Classification (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Multiple Radiological Findings | `radiology_classification_multilabel_easy_1` | Easy | "Which radiological findings are present?" | Multiple findings | ChestX-ray14, MIMIC-CXR | `domain-specific/radiology/classification/multilabel/radiology_classification_multilabel_easy_1.md` |

### Vision-Language (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Radiology Report Generation | `radiology_vision-language_describe_short_easy_1` | Easy | "Select the most accurate radiology report" | Report selection | MIMIC-CXR, RadGraph | `domain-specific/radiology/vision-language/describe/short/radiology_vision-language_describe_short_easy_1.md` |

## Surgery (10 templates)

### Binary Classification (3 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Surgical Tool Detection | `surgery_classification_binary_easy_1` | Easy | "Is a surgical tool visible in this frame?" | Yes/No | Surgical video datasets | `domain-specific/surgery/classification/binary/surgery_classification_binary_easy_1.md` |
| Critical View Achievement | `surgery_classification_binary_easy_2` | Easy | "Has critical view been achieved?" | Yes/No | Laparoscopic surgery datasets | `domain-specific/surgery/classification/binary/surgery_classification_binary_easy_2.md` |

### Multiclass Classification (5 templates)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Surgical Phase Recognition | `surgery_classification_multiclass_easy_1` | Easy | "What surgical phase is currently shown?" | Surgical phases | Cholec80, EndoVis, surgical workflows | `domain-specific/surgery/classification/multiclass/surgery_classification_multiclass_easy_1.md` |
| Surgical Tool Classification | `surgery_classification_multiclass_easy_2` | Easy | "What surgical tool is being used?" | Tool types | Surgical instrument datasets | `domain-specific/surgery/classification/multiclass/surgery_classification_multiclass_easy_2.md` |
| Anatomical Structure Recognition | `surgery_classification_multiclass_easy_3` | Easy | "What anatomical structure is visible?" | Anatomical structures | Surgical anatomy datasets | `domain-specific/surgery/classification/multiclass/surgery_classification_multiclass_easy_3.md` |
| Surgical Procedure Classification | `surgery_classification_multiclass_easy_4` | Easy | "What type of surgical procedure is this?" | Procedure types | Multi-procedure surgical datasets | `domain-specific/surgery/classification/multiclass/surgery_classification_multiclass_easy_4.md` |

### Ordinal Classification (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Surgical Skill Assessment | `surgery_classification_ordinal_easy_1` | Easy | "What skill level is demonstrated?" | Skill levels (Novice/Intermediate/Expert) | Surgical training datasets | `domain-specific/surgery/classification/ordinal/surgery_classification_ordinal_easy_1.md` |

### Anatomical Landmarks (1 template)
| Template | ID | Difficulty | Question Pattern | Answer Format | Compatible Datasets | File Location |
|----------|----|-----------|-----------------|--------------|--------------------|--------------|
| Surgical Landmark Detection | `surgery_landmarks_multiple_easy_1` | Easy | "Where are the key anatomical landmarks?" | Multiple landmark coordinates | Surgical navigation datasets | `domain-specific/surgery/anatomical-landmarks-keypoints/multiple/surgery_landmarks_multiple_easy_1.md` |

---

## Template Usage Guidelines

### MCVQA Compliance
- **Single Correct Answer**: Each question has exactly one correct answer
- **Multiple Choice Format**: All questions provide discrete answer options
- **No Free Text**: No open-ended text generation allowed
- **Deterministic**: Answers must be objectively verifiable

### Compatibility Requirements
- **Domain-Agnostic**: Work with any medical dataset in their category
- **Domain-Specific**: Require specialized medical knowledge and domain expertise
- **Schema Compliance**: All templates align with unified datum schema v1.0
- **Medical Accuracy**: Validated terminology and clinical relevance

### Template Structure
All templates follow the standardized 8-section format:
1. Template Overview
2. Template Description  
3. Question Generation Pattern
4. Mapping to Datum Schema
5. Dataset Requirements
6. Template Usage Rules
7. Examples (minimum 5)
8. Implementation Notes

---

## Statistics Summary

### By Domain
- **Domain-Agnostic**: 43 templates (54%)
- **Domain-Specific**: 36 templates (46%)

### By Task Type
- **Classification**: 59 templates (75%)
  - Binary: 18 templates
  - Multiclass: 24 templates  
  - Multilabel: 4 templates
  - Ordinal: 13 templates
- **Detection**: 3 templates (4%)
- **Segmentation**: 7 templates (9%)
- **Landmarks**: 4 templates (5%)
- **Vision-Language**: 6 templates (7%)

### By Difficulty
- **Easy**: 76 templates (96%)
- **Medium**: 3 templates (4%)
- **Hard**: 2 templates (3%)

### By Medical Specialty (Domain-Specific)
- **Surgery**: 10 templates (28%)
- **Dermatology**: 10 templates (28%)
- **Ophthalmology**: 8 templates (22%)
- **Other-Medical**: 8 templates (22%)
- **Pathology**: 8 templates (22%)
- **Radiology**: 3 templates (8%)

---

*Last updated: Based on current repository state with 79 total templates across 6 task categories and 6 medical specialties*
