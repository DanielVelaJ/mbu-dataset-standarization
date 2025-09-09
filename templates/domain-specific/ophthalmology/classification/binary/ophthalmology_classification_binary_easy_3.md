# Ophthalmology Anterior vs Posterior Segment Identification Template

## Template Overview

**Template ID**: `domain-specific_ophthalmology_classification_binary_easy_3`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Question Pattern**: Anatomical segment identification in ocular imaging  
**Medical Domain**: Ophthalmology (anterior and posterior segment imaging)  
**Domain-knowledge summary**: Requires specialized knowledge of ocular anatomy and imaging modalities. Understanding of anterior segment structures (cornea, iris, lens, anterior chamber), posterior segment anatomy (retina, vitreous, optic nerve), different imaging techniques (slit-lamp, fundus photography, OCT), and anatomical landmarks for segment differentiation. Knowledge of ophthalmological terminology for eye anatomy, imaging interpretation, and clinical assessment of ocular structures.

## Template Description

This template converts binary classification datasets into MCVQA format by asking questions about anatomical segment identification in ophthalmic images. It focuses on distinguishing between anterior segment (cornea, iris, lens) and posterior segment (retina, vitreous, optic nerve) structures, which is fundamental for ophthalmological assessment and determines appropriate imaging modalities and treatment approaches.

The template is designed for ophthalmology datasets containing mixed anterior and posterior segment images, testing the model's ability to understand basic ocular anatomy and appropriate clinical contexts.

## Question Generation Pattern

### Question Format
```
"Does this image show anterior segment or posterior segment anatomy?"
```

### Answer Format
Binary choice with anatomical segment options:
- A. Anterior segment (cornea, iris, lens)
- B. Posterior segment (retina, vitreous, optic nerve)

### Template Variables
- `{segment}`: Anterior or posterior segment. Used in question construction to specify ocular anatomical region and in answer generation to determine segment classification based on anatomical examination criteria.
- `{modality}`: Imaging modality (fundus, slit-lamp, OCT, etc.). Incorporated into question assessment providing imaging context.
- `{anatomical_structures}`: Specific structures visible in the segment. Used to provide clinical context and determine anatomical segment classification in answer rationale.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or anatomical annotations. Ocular segment images are displayed as raw images to allow comprehensive assessment of eye anatomy including anterior structures (cornea, iris, lens) and posterior structures (retina, vitreous, optic nerve). No highlighting, segment outlining, or anatomical marking is added to maintain authentic clinical evaluation conditions for anterior versus posterior segment identification.

### Answer Construction
**Correct Answer Generation**:
- Extract the anatomical segment label from the original dataset (anterior_segment, posterior_segment)
- Map specific segment labels to standardized ocular anatomy categories
- Use anatomical examination assessment from dataset annotations focusing on segment differentiation
- Validate binary choice format ensuring single correct segment identification
- Verify answer accuracy against established ophthalmological anatomy criteria and ocular examination guidelines

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Does this image show anterior segment or posterior segment anatomy?",
  "answer": "B",
  "answer_type": "single_label",
  "options": [
    "Anterior segment (cornea, iris, lens)",
    "Posterior segment (retina, vitreous, optic nerve)"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Anatomical segment identification for appropriate clinical assessment",
  "provenance": {
    "original_label": "posterior",
    "rule_id": "ophthalmology_classification_binary_easy_3",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary anatomical segment labels distinguishing anterior from posterior segments
- **Image Types**: Various ophthalmic imaging modalities with clear anatomical segment visualization
- **Assessment Requirements**: Sufficient image quality for evaluation of ocular anatomy and segment differentiation
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include mixed ophthalmology imaging datasets, multi-modal eye imaging collections, comprehensive eye examination datasets, ophthalmic imaging training datasets, and clinical photography databases with expert anatomical validation

## Template Usage Rules

- **Implementation guidelines**: Use exact ophthalmological terminology from dataset annotations focusing on ocular anatomy and segment differentiation criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format for anatomical segment identification:
  - Anterior segment labels mapped to "Anterior segment (cornea, iris, lens)" category
  - Posterior segment labels mapped to "Posterior segment (retina, vitreous, optic nerve)" category
  - Maintain anatomical accuracy in anterior vs posterior differentiation
  - Always use dataset ground truth labels as definitive segment classification
- **Conversion Process**: Extract anatomical segment label from original dataset, identify structural characteristics and anatomical features from metadata, generate questions using ophthalmological examination terminology, present raw ocular images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of anatomical segment terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with anatomical segment categories, and includes provenance tracking with original labels and rule_id "domain-specific_ophthalmology_classification_binary_easy_3"

## Examples

### Example 1: Posterior Segment Anatomical Identification
**Original Dataset Context and Annotation Format**: Multi-modal ophthalmology dataset with anatomical segment labels in CSV format (image_id, segment_type, imaging_modality) where segments include "anterior_segment", "posterior_segment" for comprehensive eye examination training  
**Image Presentation Method**: Raw ophthalmic image displayed without modifications, anatomical annotations, or segment highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Does this image show anterior segment or posterior segment anatomy?"
- **Answer Choices**: ["Anterior segment (cornea, iris, lens)", "Posterior segment (retina, vitreous, optic nerve)"]
- **Correct Answer**: "Posterior segment (retina, vitreous, optic nerve)"  
**Complete Conversion Process Explanation**: 
1. Extract anatomical segment label "posterior_segment" from dataset CSV indicating fundus anatomy classification
2. Identify structural characteristics and anatomical features from imaging modality metadata
3. Generate question using ophthalmological examination terminology for segment identification
4. Map posterior segment label to "Posterior segment (retina, vitreous, optic nerve)" answer choice maintaining anatomical accuracy
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Posterior segment identification case requiring recognition of retinal structures, vitreous, and optic nerve anatomy for comprehensive eye examination - tests fundamental anatomical segment differentiation for ocular anatomy based on established criteria for ophthalmological examination and imaging interpretation

### Example 2: Anterior Segment Anatomical Assessment  
**Original Dataset Context and Annotation Format**: Comprehensive eye examination database with expert anatomical annotations where "anterior_segment" classification indicates front eye structures, stored in annotation file with segment names and clinical significance  
**Image Presentation Method**: Raw ophthalmic image displayed without modifications, overlays, or anatomical segment highlighting  
**Generated Question and ALL Answer Choices**:
- **Question**: "Does this image show anterior segment or posterior segment anatomy?"
- **Answer Choices**: ["Anterior segment (cornea, iris, lens)", "Posterior segment (retina, vitreous, optic nerve)"] 
- **Correct Answer**: "Anterior segment (cornea, iris, lens)"  
**Complete Conversion Process Explanation**:
1. Extract segment label "anterior_segment" from dataset annotation indicating front eye anatomy classification
2. Map anterior segment to anatomical structure category based on ophthalmological examination criteria
3. Generate question using standardized anatomical terminology for segment evaluation
4. Convert anterior classification to "Anterior segment (cornea, iris, lens)" answer choice maintaining clinical accuracy
5. Verify binary choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Anterior segment identification demonstrating cornea, iris, and lens structures visible in front eye examination - tests ability to differentiate anatomical segments for accurate ocular evaluation according to ophthalmological examination principles

- **Comprehensive Assessment**: Foundation for more advanced diagnostic evaluations
