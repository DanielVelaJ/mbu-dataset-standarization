# Domain-Agnostic Multiclass Classification Templates

This directory contains domain-agnostic templates for converting multiclass classification datasets into MCVQA format. These templates work across all medical specialties and require only basic dataset information: multiclass labels, condition/anatomy names, and imaging modality.

## Template Collection

### Easy Difficulty Templates

1. **agnostic_classification_multiclass_1.md** - Basic Condition Identification
   - **Pattern**: "What medical condition is shown in this {modality} image?"
   - **Use Case**: Multi-class disease/condition classification
   - **Example**: Pneumonia vs Pleural effusion vs Pneumothorax vs Normal

2. **agnostic_classification_multiclass_2.md** - Disease Stage/Severity Grading  
   - **Pattern**: "What {assessment_type} is shown in this {modality} image?"
   - **Use Case**: Ordinal grading systems (stages, severity levels)
   - **Example**: Diabetic retinopathy grades 0-4, BIRADS categories 1-5

3. **agnostic_classification_multiclass_3.md** - Anatomical Region Identification
   - **Pattern**: "What anatomical {structure_type} is primarily shown in this {modality} image?"
   - **Use Case**: Anatomical region/organ/body part classification
   - **Example**: Chest vs Abdomen vs Pelvis vs Skull

## Key Features

- **Domain-Agnostic**: Work across radiology, pathology, dermatology, ophthalmology, and other medical specialties
- **Easy Difficulty**: Designed for straightforward classification with minimal dataset requirements
- **Schema Compliant**: Full alignment with unified datum schema v1.0
- **Clinical Relevance**: Questions mirror real medical diagnostic scenarios
- **Medical Accuracy**: All examples use correct medical terminology and established clinical standards

## Template Requirements

All templates require datasets with:
- **3+ mutually exclusive classes**: Multi-class structure with single correct answer
- **Clear medical labels**: Condition names, grades, or anatomical terms
- **Medical images**: Any imaging modality (X-ray, CT, MRI, photos, etc.)
- **Single ground truth**: Each image has exactly one correct classification

## Template Structure

Each template follows the standardized 8-section format:
1. Template Overview
2. Template Description  
3. Question Generation Pattern
4. Mapping to Datum Schema
5. Dataset Requirements
6. Template Usage Rules
7. Examples (5 concrete examples)
8. Implementation Notes

## Usage Guidelines

- Choose template based on dataset label type:
  - **Condition names** → agnostic_classification_multiclass_1 (Basic Condition Identification)
  - **Ordered stages/grades** → agnostic_classification_multiclass_2 (Disease Stage/Severity Grading)  
  - **Anatomical regions** → agnostic_classification_multiclass_3 (Anatomical Region Identification)
- Randomize option order to prevent position bias
- Use established medical terminology when possible
- Limit options to 3-8 choices for readability
- Include complete scale/class set from original dataset

## Clinical Applications

These templates enable evaluation of:
- **Differential Diagnosis**: Distinguishing between multiple medical conditions
- **Disease Staging**: Assessing progression and severity on clinical scales
- **Anatomical Recognition**: Basic medical image interpretation skills
- **Cross-Domain Knowledge**: Medical expertise across different specialties

## Future Extensions

Additional multiclass templates may include:
- Imaging view identification (AP, PA, lateral, etc.)
- Medical device classification
- Treatment response assessment
- Demographic/patient characteristic classification
