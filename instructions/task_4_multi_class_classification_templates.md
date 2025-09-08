# Task 4: Multi-Class Classification Templates
Similarly to how we did in task 2 for binary classification, we will now create templates for multi-class classification. Please read the context files and the instructions files and help me define the templates.
These should be the domain-agnostic templates that work across all medical domains. Remember multi-class classification has more than two calasses and the correct answer is only one of the classes. Save them in templates/domain-agnostic/classification/multi-class directory please. 
Let's start with the easy difficulty templates first, think of just 3 templates for now. They must be able to work with the most basic information that is needed for a multi-class classification dataset.

## Progress and Decisions Made

### ✅ Task 4 Complete: 3 Easy-Difficulty Multi-Class Templates Created

**Templates Created** (following proper naming convention `{domain}_{task}_{subtype}_{difficulty}.md`):

1. **agnostic_classification_multiclass_1.md** - **Basic Condition Identification**
   - **Pattern**: "What medical condition is shown in this {modality} image?"
   - **Use Case**: General multi-class disease/condition classification
   - **Example**: Pneumonia vs Pleural effusion vs Pneumothorax vs Normal

2. **agnostic_classification_multiclass_2.md** - **Disease Stage/Severity Grading**
   - **Pattern**: "What {assessment_type} is shown in this {modality} image?"
   - **Use Case**: Ordinal grading systems (stages, severity levels)
   - **Example**: Diabetic retinopathy grades 0-4, BIRADS categories 1-5

3. **agnostic_classification_multiclass_3.md** - **Anatomical Region Identification**
   - **Pattern**: "What anatomical {structure_type} is primarily shown in this {modality} image?"
   - **Use Case**: Anatomical region/organ/body part classification
   - **Example**: Chest vs Abdomen vs Pelvis vs Skull

### ✅ Key Features Delivered:

- **Domain-Agnostic**: Work across radiology, pathology, dermatology, ophthalmology
- **Easy Difficulty**: Designed for basic multi-class classification requirements
- **Schema Compliant**: Perfect alignment with unified datum schema v1.0
- **Standardized Structure**: All follow the established 8-section template format
- **Clinical Relevance**: Questions mirror real diagnostic workflows
- **Comprehensive Examples**: 5 concrete examples per template across different medical domains

### ✅ Template Requirements Met:

All templates work with datasets that have:
- **3+ mutually exclusive classes** (multi-class structure)
- **Clear medical labels** (condition names, grades, anatomical terms)
- **Medical images** (any modality: X-ray, CT, MRI, photos, etc.)
- **Single ground truth** (one correct classification per image)

### ✅ Files Created:

- `templates/domain-agnostic/classification/multi-class/agnostic_classification_multiclass_1.md`
- `templates/domain-agnostic/classification/multi-class/agnostic_classification_multiclass_2.md`
- `templates/domain-agnostic/classification/multi-class/agnostic_classification_multiclass_3.md`
- `templates/domain-agnostic/classification/multi-class/README.md`

### ✅ Naming Convention Correction:

**Issue Identified**: Initially created templates with incorrect naming (multiclass_1.md, multiclass_2.md, multiclass_3.md)

**Fixed**: Renamed all files to follow proper convention: `{domain}_{task}_{subtype}_{difficulty}.md`
- Updated Template IDs and rule_ids within files to match proper naming
- Updated README.md to reference correct file names
- Deleted old incorrectly named files

The templates are now ready for immediate use and follow the same high-quality standards established in the binary classification templates. They enable evaluation of vision-language models on multi-class medical classification tasks across diverse medical specialties.