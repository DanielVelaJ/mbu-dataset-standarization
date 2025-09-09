# Dermatology Dermoscopic Pattern Recognition Template

## Template Overview

**Template ID**: `domain-specific_dermatology_classification_multiclass_easy_2`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Question Pattern**: Dermoscopic pattern identification  
**Medical Domain**: Dermatology (dermoscopy and dermatoscopic pattern analysis)  
**Domain-knowledge summary**: Requires specialized knowledge of dermoscopic patterns and dermatoscopy interpretation. Understanding of dermoscopic structures (network, globules, streaks, dots, blotches), pattern recognition principles, dermoscopic criteria for different lesion types, and correlation between dermoscopic patterns and histopathological findings. Knowledge of dermoscopic terminology, pattern classification systems, and dermatoscopic diagnostic algorithms.

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking direct questions about dermoscopic patterns in skin lesions. Dermoscopic pattern recognition is essential for lesion evaluation, as specific patterns are associated with different types of lesions and help guide clinical decision-making.

The template is designed for dermoscopy datasets where lesions exhibit distinct dermoscopic patterns, testing the model's ability to recognize and classify the specialized visual patterns visible under dermoscopic examination.

## Question Generation Pattern

### Question Format
```
"What is the primary dermoscopic pattern visible in this lesion?"
```

### Answer Format
Multiclass choice with dermoscopic pattern options:
- A. Reticular pattern
- B. Globular pattern
- C. Homogeneous pattern
- D. Starburst pattern
- E. Multicomponent pattern

### Template Variables
- `{pattern_description}`: Detailed description of the visible pattern. Used in question construction to provide clinical context and in answer generation to determine the correct dermoscopic pattern based on specialized dermoscopy criteria.
- `{lesion_type}`: Type of lesion showing the pattern. Incorporated into question assessment and used to guide answer construction based on lesion-specific dermoscopic characteristics.
- `{pattern_distribution}`: How the pattern is distributed across the lesion. Used to provide clinical context and determine pattern classification in answer rationale.

### Image Presentation
Images are presented in their original form without visual modifications, overlays, or annotations. Dermoscopic images are displayed as raw dermoscopy captures to allow comprehensive assessment of dermoscopic patterns including network structures, globular patterns, pigmentation distribution, and specialized dermoscopic features. No highlighting, pattern outlining, or dermoscopic structure marking is added to maintain authentic clinical dermoscopy evaluation conditions.

### Answer Construction
**Correct Answer Generation**:
- Extract the dermoscopic pattern from the original dataset (reticular, globular, homogeneous, starburst, multicomponent)
- Map specific pattern labels to standardized dermoscopic pattern categories
- Use dermoscopic assessment from dataset annotations focusing on pattern classification
- Validate answer accuracy against established dermoscopic pattern recognition criteria
- Ensure clinical relevance of dermoscopic terminology and pattern descriptions

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Multiclass classification (Vision → Image-Level Classification → Multiclass classification)
- **Label Structure**: Multiple dermoscopic pattern labels with specific pattern categories per image
- **Image Types**: Dermoscopic images with clear pattern visualization and sufficient magnification for pattern recognition
- **Assessment Requirements**: Sufficient image quality for evaluation of dermoscopic structures and pattern characteristics
- **Datasets from metadata file**: Compatible datasets available in `datasets_metadata.csv` include dermoscopy pattern databases, ISIC dermoscopic challenges, melanocytic lesion dermoscopy collections, educational dermoscopy atlases, and pattern-annotated dermoscopy datasets with expert dermoscopist validation

## Template Usage Rules

- **Implementation guidelines**: Use exact dermoscopic terminology from dataset annotations focusing on pattern recognition and dermoscopic assessment criteria
- **Label mapping rules**: Convert original dataset annotations to MCVQA format:
  - Pattern labels "network", "pigment network", "reticular" → "Reticular pattern"
  - Pattern labels "globules", "dots", "globular" → "Globular pattern"  
  - Pattern labels "structureless", "diffuse", "homogeneous" → "Homogeneous pattern"
  - Pattern labels "streaks", "radial", "starburst" → "Starburst pattern"
  - Pattern labels "multiple patterns", "multicomponent" → "Multicomponent pattern"
  - Always use dataset ground truth labels as definitive pattern classification
- **Conversion Process**: Extract dermoscopic pattern from original dataset, identify lesion type and pattern characteristics from metadata, generate questions using dermoscopic assessment terminology, present raw dermoscopic images without modifications, validate MCVQA compliance with single correct answer, ensure clinical relevance of dermoscopic terminology
- **Schema Alignment**: Output aligns with unified datum schema v1.0 using answer_type "single_label", task "Classification", difficulty "easy", options array with dermoscopic pattern categories, and includes provenance tracking with original labels and rule_id "domain-specific_dermatology_classification_multiclass_easy_2"

## Examples

### Example 1: Reticular Pattern Recognition
**Original Dataset Context and Annotation Format**: Dermoscopy pattern classification dataset with pattern labels in CSV format (image_id, pattern_type) where labels include "reticular", "globular", "homogeneous", "starburst", "multicomponent"  
**Image Presentation Method**: Raw dermoscopic image displayed without modifications, annotations, or pattern highlighting  
**Generated Question and ALL Answer Choices**: 
- **Question**: "What is the primary dermoscopic pattern visible in this lesion?"
- **Answer Choices**: ["Reticular pattern", "Globular pattern", "Homogeneous pattern", "Starburst pattern", "Multicomponent pattern"]
- **Correct Answer**: "Reticular pattern"  
**Complete Conversion Process Explanation**: 
1. Extract pattern label "reticular" from dataset CSV indicating network pattern classification
2. Identify lesion type and dermoscopic characteristics from dataset metadata
3. Generate question using dermoscopic assessment terminology focused on pattern identification
4. Map reticular label to "Reticular pattern" answer choice based on dermoscopic criteria
5. Validate MCVQA compliance with single correct answer format  
**Clinical Rationale**: Reticular pattern case requiring recognition of network structures including intersecting brown lines and pigment network characteristics - tests dermoscopic pattern recognition for reticular vs other pattern classification based on established criteria for dermoscopic pattern analysis and classification

### Example 2: Globular Pattern Assessment  
**Original Dataset Context and Annotation Format**: Dermoscopy education dataset with expert dermoscopist pattern annotations where "globular" classification indicates round to oval structures, stored in annotation file with image names and pattern labels  
**Image Presentation Method**: Raw dermoscopic image displayed without modifications, overlays, or structural annotations  
**Generated Question and ALL Answer Choices**:
- **Question**: "What is the primary dermoscopic pattern visible in this lesion?"
- **Answer Choices**: ["Reticular pattern", "Globular pattern", "Homogeneous pattern", "Starburst pattern", "Multicomponent pattern"] 
- **Correct Answer**: "Globular pattern"  
**Complete Conversion Process Explanation**:
1. Extract pattern label "globular" from dataset annotation indicating globular pattern classification
2. Map "globular" to globular pattern category based on dermoscopic morphology
3. Generate question using standardized dermoscopic pattern assessment terminology
4. Convert globular diagnosis to "Globular pattern" answer choice following label mapping rules
5. Verify multiclass choice format with single correct answer for MCVQA compliance  
**Clinical Rationale**: Globular pattern case demonstrating round to oval brown structures distributed throughout lesion - tests ability to distinguish globular patterns from other dermoscopic patterns based on morphological features and dermoscopic classification criteria for accurate pattern identification

