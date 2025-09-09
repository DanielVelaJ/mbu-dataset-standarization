# Multi-Label Classification Template 1: Basic Finding Detection

## Template Overview

**Template ID**: `domain-agnostic_classification_multilabel_easy_1`  
**Task Type**: Multilabel classification  
**Difficulty**: Easy  
**Question Pattern**: Multiple medical findings detection with set-based answers  
**Medical Domain**: Domain-agnostic (applicable across all medical specialties)  
**Domain-knowledge summary**: Requires understanding of medical terminology and ability to identify multiple simultaneous medical findings. Knowledge of co-occurring conditions and ability to recognize that medical images often contain multiple pathological findings simultaneously, but does not require specialized domain expertise.

## Template Description

This template converts multi-label medical datasets into MCVQA format by asking about what medical findings are present in an image. The template allows for multiple correct findings to be identified simultaneously, where any combination of findings can be true. This approach mirrors clinical image interpretation scenarios where medical professionals must identify all visible pathological findings in a single image.

The template is designed to work with datasets that have multiple binary labels per image, making it suitable for comprehensive medical image analysis across different specialties including radiology, pathology, dermatology, and ophthalmology. Unlike binary or multi-class templates, this template acknowledges that medical images often contain multiple co-occurring conditions or findings.

## Question Generation Pattern

### Question Format
`"Which of the following medical findings are present in this {modality} image?"`

### Answer Format
Set-based answer listing all present findings, with "None of the above" option for negative cases

### Template Variables
- `{modality}`: Imaging modality (e.g., "chest X-ray", "fundus", "dermoscopy", "histopathology"). Used in question text to provide clinical context about the type of medical examination.
- `{finding_list}`: List of potential medical findings from the dataset label set. Used to generate multiple choice options for findings that could be present.
- `{present_findings}`: Set of findings that are actually present in the image. Used to construct the correct answer showing all simultaneously present conditions.

### Image Presentation
Images are presented in their original form without any visual modifications, overlays, or annotations. No bounding boxes, highlighting, or segmentation masks are added. The raw medical image is shown exactly as captured, allowing for comprehensive assessment of all visible medical findings.

### Answer Construction
**Multilabel Answer Format**:
- Extract all positive labels from dataset metadata for the specific image
- Create a set-based answer listing all present findings
- Include "None of the above" option for cases where no findings are present
- Ensure all present findings are included in the correct answer
- Maintain MCVQA compliance by treating the set of findings as a single correct answer

### Example Pattern
```
Question: "Which of the following medical findings are present in this chest X-ray image?"
Options: Pneumonia, Atelectasis, Cardiomegaly, Pleural effusion, Pneumothorax, None of the above
Answer: "Pneumonia, Cardiomegaly" (if both conditions are present)
```


## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multilabel classification (Vision → Image-Level Classification → Multilabel classification)
- **Label Structure**: Multiple binary labels per image (2+ possible findings) that can be independently assigned and co-occur
- **Medical Context**: Distinct medical conditions, pathologies, or abnormalities that can be simultaneously present in single images
- **Independent Findings**: Each finding label must be independently assessable and not mutually exclusive with others
- **Datasets from metadata file**: Compatible datasets include chest X-ray datasets with multiple pulmonary findings (CheXpert, MIMIC-CXR), skin lesion datasets with multiple dermatological features, fundus datasets with multiple retinal pathologies, histopathology datasets with multiple tissue characteristics, brain imaging datasets with multiple neurological findings, and other multilabel medical classification datasets available in `datasets_metadata.csv`

## Template Usage Rules

- **Implementation guidelines**: Include all major findings that can co-occur in the imaging modality and ensure each finding can be assessed independently of others, using medically meaningful finding combinations
- **Label mapping rules**: Convert original dataset annotations to multilabel format:
  - Extract all positive binary labels from multilabel vector for each image
  - Create set-based answer listing all present findings
  - Include "None of the above" option for cases where no target findings are present
  - Ensure all present findings are included in the correct answer
- **Conversion Process**: Extract multilabel vectors from original dataset, identify all possible findings from metadata, create comprehensive finding detection question, present raw images without modifications, validate MCVQA compliance with set-based answer format, verify clinical plausibility of finding combinations
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "multi_label", task "Classification", difficulty "easy", options array with all possible findings plus "None of the above", and includes provenance tracking with original multilabel vectors and rule_id "domain-agnostic_classification_multilabel_easy_1"

### Domain Adaptation
- **Radiology**: Use modality-appropriate findings (e.g., air space opacities, masses, devices)
- **Pathology**: Include cellular and tissue-level abnormalities
- **Dermatology**: Focus on lesion characteristics and surface features
- **Ophthalmology**: Include retinal, vascular, and optical disc findings

## Examples

### Example 1: Chest X-ray Multi-Label Finding Detection
**Original Dataset Context and Annotation Format**: CheXpert-style multi-finding detection dataset with multilabel binary vectors in CSV format (image_id, pneumonia, atelectasis, cardiomegaly, pleural_effusion) where 1 = finding present, 0 = finding absent  
**Image Presentation Method**: Raw chest X-ray image displayed without modifications, overlays, or annotations  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Which of the following medical findings are present in this chest X-ray image?"
- **Answer Choices**: ["Pneumonia", "Atelectasis", "Cardiomegaly", "Pleural effusion", "None of the above"]
- **Correct Answer**: "Pneumonia, Cardiomegaly"  
**Complete Conversion Process Explanation**: 
1. Extract multilabel binary vector [1,0,1,0] from dataset CSV indicating pneumonia=1, atelectasis=0, cardiomegaly=1, pleural_effusion=0
2. Identify all possible findings from dataset metadata: pneumonia, atelectasis, cardiomegaly, pleural effusion
3. Create set-based answer from positive labels: "Pneumonia, Cardiomegaly" 
4. Generate multilabel question format with all possible findings as options plus "None of the above"
5. Validate multilabel MCVQA compliance with set-based correct answer format  
**Clinical Rationale**: Multilabel chest X-ray case with co-occurring pneumonia and cardiomegaly requiring simultaneous detection of multiple independent pathological findings - tests ability to identify multiple respiratory and cardiac conditions that commonly coexist in clinical practice

### Example 2: Dermoscopy Multi-Label Feature Detection  
**Original Dataset Context and Annotation Format**: Dermoscopy feature detection dataset with multilabel annotations where labels include asymmetry, border_irregularity, color_variation, diameter_large, pigment_network as binary indicators  
**Image Presentation Method**: Raw dermoscopy image displayed without modifications, annotations, or region highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Which of the following dermatological features are present in this dermoscopy image?"
- **Answer Choices**: ["Asymmetry", "Border irregularity", "Color variation", "Diameter >6mm", "Pigment network", "None of the above"] 
- **Correct Answer**: "Asymmetry, Color variation, Diameter >6mm"  
**Complete Conversion Process Explanation**:
1. Extract multilabel binary vector [1,0,1,1,0] from dataset indicating asymmetry=1, border_irregularity=0, color_variation=1, diameter_large=1, pigment_network=0
2. Identify all 5 dermatological features from dataset metadata as potential findings
3. Create set-based answer from positive labels: "Asymmetry, Color variation, Diameter >6mm"
4. Generate multilabel question format with all dermatological features as options
5. Verify multilabel format with set-based answer structure for MCVQA compliance  
**Clinical Rationale**: Dermoscopy case requiring simultaneous assessment of multiple ABCDE criteria features (asymmetry, border, color, diameter, evolving) - tests ability to identify multiple independent dermatological characteristics critical for melanoma risk assessment and skin lesion evaluation

