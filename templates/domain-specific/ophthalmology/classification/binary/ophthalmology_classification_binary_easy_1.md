# Ophthalmology Optic Disc vs Cup Differentiation Template

## Template Overview

**Template ID**: `domain-specific_ophthalmology_classification_binary_easy_1`  
**Task Type**: Binary Classification  
**Difficulty**: Easy  
**Question Pattern**: Optic disc versus optic cup anatomical differentiation  
**Medical Domain**: Ophthalmology (fundus imaging and optic nerve assessment)  
**Domain-knowledge summary**: Requires specialized knowledge of optic nerve anatomy and fundus examination techniques. Understanding of optic disc morphology, optic cup characteristics, cup-to-disc ratio assessment, neuroretinal rim evaluation, and anatomical landmarks in fundus photography. Knowledge of ophthalmological terminology for optic nerve structures, glaucomatous changes, and fundus imaging interpretation for optic disc assessment.

## Template Description

This template converts binary classification datasets into MCVQA format by asking direct questions about anatomical structures in fundus images, specifically distinguishing between the optic disc and optic cup. This differentiation is crucial for glaucoma assessment, as the cup-to-disc ratio is a key diagnostic parameter.

The template is designed for ophthalmology datasets where regions of interest are labeled as either optic disc or optic cup, testing the model's ability to understand fundamental anatomical structures critical for glaucoma evaluation.

## Question Generation Pattern

### Question Format
```
"Is the highlighted region the optic disc or optic cup in this fundus image?"
```

### Answer Format
Binary choice with anatomical options:
- A. Optic disc
- B. Optic cup

### Template Variables
- `{structure}`: The anatomical structure (optic disc or optic cup). Used in question construction to specify optic nerve anatomy and in answer generation to determine anatomical structure classification based on fundus examination criteria.
- `{modality}`: Always "fundus" for this template. Incorporated into question assessment providing imaging context.
- `{region_description}`: Description of the highlighted or central region. Used to provide clinical context and determine anatomical structure classification in answer rationale.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or anatomical annotations. Ophthalmological fundus images are displayed as raw images to allow comprehensive assessment of optic nerve anatomy including disc margins, cup boundaries, neuroretinal rim characteristics, and vascular patterns. No highlighting, disc outlining, or cup marking is added to maintain authentic clinical evaluation conditions for optic disc versus cup differentiation.

### Answer Construction
**Correct Answer Generation**:
- Extract the anatomical structure label from the original dataset (optic_disc, optic_cup)
- Map specific anatomical labels to standardized optic nerve structure categories
- Use fundus examination assessment from dataset annotations focusing on disc vs cup differentiation
- Validate binary choice format ensuring single correct anatomical structure identification
- Verify answer accuracy against established ophthalmological anatomy criteria and fundus examination guidelines

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Binary anatomical structure labels distinguishing optic disc from optic cup
- **Image Types**: High-quality fundus photographs with clearly visible optic nerve anatomy
- **Assessment Requirements**: Sufficient image resolution and clarity for anatomical structure differentiation and cup-to-disc assessment
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include glaucoma assessment databases, optic nerve morphology studies, cup-to-disc ratio measurement datasets, fundus photography atlases, and optic nerve head analysis collections with expert ophthalmologist validation

## Template Usage Rules

- **Implementation guidelines**: Use exact ophthalmological terminology from dataset annotations focusing on optic nerve anatomy and fundus examination criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format for anatomical structure identification:
  - Optic disc labels mapped to "Optic disc" category
  - Optic cup labels mapped to "Optic cup" category
  - Maintain anatomical accuracy in disc vs cup differentiation
  - Always use dataset ground truth labels as definitive anatomical classification
- **Conversion Process**: Extract anatomical structure label from original dataset, identify optic nerve features and morphological characteristics from metadata, generate questions using ophthalmological examination terminology, present raw fundus images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of anatomical structure terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with anatomical structure categories, and includes provenance tracking with original labels and rule_id "domain-specific_ophthalmology_classification_binary_easy_1"

## Examples

### Example 1: Optic Disc Anatomical Identification
**Original Dataset Context and Annotation Format**: Glaucoma assessment database with anatomical structure labels in CSV format (image_id, structure_type, clinical_assessment) where structures include "optic_disc", "optic_cup" for fundus examination training  
**Image Presentation Method**: Raw fundus photograph displayed without modifications, anatomical annotations, or structure highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "Is the highlighted region the optic disc or optic cup in this fundus image?"
- **Answer Choices**: ["Optic disc", "Optic cup"]
- **Correct Answer**: "Optic disc"  
**Complete Conversion Process Explanation**: 
1. Extract anatomical structure label "optic_disc" from dataset CSV indicating fundus anatomy classification
2. Identify optic nerve features and morphological characteristics from clinical assessment metadata
3. Generate question using ophthalmological examination terminology for anatomical structure identification
4. Map optic disc label to "Optic disc" answer choice maintaining anatomical accuracy
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Optic disc identification case requiring recognition of complete neural tissue area including neuroretinal rim for glaucoma assessment - tests fundamental anatomical structure differentiation for optic nerve anatomy based on established criteria for ophthalmological examination and fundus photography interpretation

### Example 2: Optic Cup Anatomical Assessment  
**Original Dataset Context and Annotation Format**: Optic nerve morphology study with expert ophthalmologist annotations where "optic_cup" classification indicates central excavation within disc, stored in annotation file with structure names and clinical significance  
**Image Presentation Method**: Raw fundus photograph displayed without modifications, overlays, or cup boundary annotations  
**Generated Question and ALL Answer Choices**:
- **Question**: "Is the highlighted region the optic disc or optic cup in this fundus image?"
- **Answer Choices**: ["Optic disc", "Optic cup"] 
- **Correct Answer**: "Optic cup"  
**Complete Conversion Process Explanation**:
1. Extract structure label "optic_cup" from dataset annotation indicating central excavation classification
2. Map optic cup to anatomical structure category based on fundus examination criteria
3. Generate question using standardized ophthalmological terminology for cup identification
4. Convert cup classification to "Optic cup" answer choice maintaining clinical accuracy
5. Verify binary choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Optic cup identification demonstrating central depression within optic disc critical for cup-to-disc ratio assessment - tests ability to differentiate anatomical structures for accurate glaucoma evaluation according to ophthalmological examination principles

