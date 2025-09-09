# Ophthalmology Pupil Response Assessment Template

## Template Overview

**Template ID**: `domain-specific_ophthalmology_classification_binary_easy_2`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Question Pattern**: Pupillary response normality assessment  
**Medical Domain**: Ophthalmology (anterior segment imaging and pupillary assessment)  
**Domain-knowledge summary**: Requires specialized knowledge of pupillary anatomy and neurological assessment. Understanding of pupillary light reflex pathways, normal vs abnormal pupil responses, pupil size evaluation, consensual light reflex, relative afferent pupillary defect (RAPD), and neurological examination techniques. Knowledge of ophthalmological terminology for pupillary disorders, anterior segment anatomy, and clinical assessment of pupillary function.

## Template Description

This template converts binary classification datasets into MCVQA format by asking questions about pupillary responses in anterior segment images. It focuses on determining whether the pupil shows normal or abnormal reactive responses, which is crucial for neurological and ophthalmological assessment.

The template is designed for ophthalmology datasets where anterior segment images are labeled based on pupillary response characteristics, testing the model's ability to assess functional aspects of the visual system beyond structural abnormalities.

## Question Generation Pattern

### Question Format
```
"Does this pupil show normal reactive response in this anterior segment image?"
```

### Answer Format
Binary choice with response assessment:
- A. Normal pupillary response
- B. Abnormal pupillary response

### Template Variables
- `{response_type}`: Normal or abnormal pupillary response. Used in question construction to specify pupillary assessment and in answer generation to determine response classification based on neurological examination criteria.
- `{pupil_characteristics}`: Description of pupil appearance and reactivity. Incorporated into question assessment and used to guide answer construction based on pupillary morphological features.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or pupillary annotations. Anterior segment images are displayed as raw images to allow comprehensive assessment of pupillary anatomy including pupil size, shape, reactivity, and light reflex characteristics. No highlighting, pupil outlining, or response marking is added to maintain authentic clinical evaluation conditions for pupillary response assessment.

### Answer Construction
**Correct Answer Generation**:
- Extract the pupillary response assessment from the original dataset (normal_response, abnormal_response)
- Map specific response labels to standardized pupillary assessment categories
- Use neurological examination assessment from dataset annotations focusing on pupillary function evaluation
- Validate binary choice format ensuring single correct response classification
- Verify answer accuracy against established neurological examination criteria and pupillary assessment guidelines

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Does this pupil show normal reactive response in this anterior segment image?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Normal pupillary response",
    "Abnormal pupillary response"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Pupillary response assessment for neurological evaluation",
  "provenance": {
    "original_label": "normal",
    "rule_id": "ophthalmology_classification_binary_easy_2",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary pupillary response labels distinguishing normal from abnormal responses
- **Image Types**: Anterior segment photographs with clear pupillary anatomy and functional assessment capability
- **Assessment Requirements**: Sufficient image quality for evaluation of pupillary reactivity and neurological function
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include pupil position detection datasets, anterior segment analysis datasets, neurological pupil assessment datasets, eye tracking and pupillometry datasets, and clinical pupil examination databases with expert neurological validation

## Template Usage Rules

- **Implementation guidelines**: Use exact neurological and ophthalmological terminology from dataset annotations focusing on pupillary function assessment and anterior segment examination criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format for pupillary response classification:
  - Normal response labels mapped to "Normal pupillary response" category
  - Abnormal response labels mapped to "Abnormal pupillary response" category
  - Maintain functional accuracy in normal vs abnormal differentiation
  - Always use dataset ground truth labels as definitive response classification
- **Conversion Process**: Extract pupillary response assessment from original dataset, identify functional characteristics and neurological features from metadata, generate questions using neurological examination terminology, present raw anterior segment images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of pupillary response terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with pupillary response categories, and includes provenance tracking with original labels and rule_id "domain-specific_ophthalmology_classification_binary_easy_2"

## Examples

### Example 1: Normal Pupillary Response Assessment
**Original Dataset Context and Annotation Format**: Neurological assessment database with pupillary function labels in CSV format (image_id, response_type, clinical_assessment) where responses include "normal_response", "abnormal_response" for anterior segment examination training  
**Image Presentation Method**: Raw anterior segment photograph displayed without modifications, pupillary annotations, or response highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Does this pupil show normal reactive response in this anterior segment image?"
- **Answer Choices**: ["Normal pupillary response", "Abnormal pupillary response"]
- **Correct Answer**: "Normal pupillary response"  
**Complete Conversion Process Explanation**: 
1. Extract pupillary response label "normal_response" from dataset CSV indicating functional neurological assessment
2. Identify pupillary characteristics and functional features from clinical assessment metadata
3. Generate question using neurological examination terminology for response evaluation
4. Map normal response label to "Normal pupillary response" answer choice maintaining functional accuracy
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Normal pupillary response case requiring assessment of round, reactive pupil with appropriate light reflex - tests functional neurological evaluation for pupillary examination based on established criteria for anterior segment assessment and pupillary function determination

### Example 2: Abnormal Pupillary Response Assessment  
**Original Dataset Context and Annotation Format**: Clinical pupil examination database with expert neurological annotations where "abnormal_response" classification indicates impaired pupillary function, stored in annotation file with response types and clinical significance  
**Image Presentation Method**: Raw anterior segment photograph displayed without modifications, overlays, or pupillary response highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Does this pupil show normal reactive response in this anterior segment image?"
- **Answer Choices**: ["Normal pupillary response", "Abnormal pupillary response"] 
- **Correct Answer**: "Abnormal pupillary response"  
**Complete Conversion Process Explanation**:
1. Extract response label "abnormal_response" from dataset annotation indicating impaired pupillary function
2. Map abnormal response to functional assessment category based on neurological examination criteria
3. Generate question using standardized neurological terminology for pupillary evaluation
4. Convert abnormal classification to "Abnormal pupillary response" answer choice maintaining clinical accuracy
5. Verify binary choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Abnormal pupillary response assessment demonstrating fixed, dilated, or irregularly shaped pupil indicating neurological impairment - tests ability to identify pupillary dysfunction for accurate neurological evaluation according to clinical examination principles

