# General Template Guidelines

## Overview

This document serves as the **single authoritative source** for all template creation requirements in the MBU Dataset Standardization project. All templates must follow these guidelines to ensure consistency, quality, and clinical relevance across the entire repository.

## Template Purpose

Templates convert medical datasets into MCVQA (Multiple Choice Visual Question Answering) format. Each template defines:
- **Question patterns** for generating medical questions from dataset labels
- **Answer formats** that comply with MCVQA requirements  
- **Schema mappings** to the unified datum schema v1.0
- **Implementation guidelines** for proper usage

---

## Required Template Structure

### Mandatory 6-Section Format

**ALL templates MUST follow this standardized structure** (in exact order):

#### 1. Template Overview
- **Template ID**: Unique identifier following naming convention
- **Task Type**: one of the task types in our task taxonomy leaf nodes. (see docs/mbu_medical_vision_taxonomy_table.md)
- **Difficulty**: Easy, Medium, or Hard
- **Question Pattern**: Brief summary of the question format
- **Medical Domain**: Medical domain that the template is applicable
- **Domain-knowledge summary**: A summary of the domain-knowledge that is required to use the template. This should be a description of the topics that are relevant to the template (mostly for the domain-specific templates). A small paragraph is enough describing the medical problem and main concepts. 

#### 2. Template Description  
- Template purpose and approach
- Clinical context and use cases. This should be a description of the template's purpose and how it is used in a medical setting.
- Target scenarios and medical workflows

#### 3. Question Generation Pattern
- **Question Format**: Exact template with variables marked as `{variable}`
- **Answer Format**: Specific answer options and structure compatible with MCVQA format
- **Template Variables**: Definition of all variables used and how each variable is utilized in question construction and answer generation (e.g., how `{finding}` maps to specific answer choices, how `{modality}` is incorporated into the question text)
- **Image Presentation**: How the image is displayed to users (raw image, with overlays, highlights, bounding boxes, segmentation masks, landmark markers, etc.) and how visual modifications are derived from original annotations
- **Answer Construction**: Complete process for deriving ALL answer choices from original dataset annotations, including correct answer selection and distractor generation logic

#### 4. Dataset Requirements
- Supported task types and data structures
- Required label formats and metadata
- Dataset characteristics that work with this template
- Datasets from our metadata file that are compatible with this template. (see data/dataset_metadata/dataset_metadata.csv and about_dataset_metadata folder)


#### 5. Examples
- **Exactly 2 concrete examples** with real dataset references
- Each example must include:
  - Original dataset context and annotation format
  - Image presentation method (how visual modifications are applied)
  - Generated question and ALL answer choices (correct + distractors)
  - Complete conversion process explanation (from original data to final MCVQA)
  - Clinical rationale for answer choices

---

## Naming Conventions

### Template Files
**Format**: `{domain}_{task}_{subtype}_{difficulty}_{number}.md`

**Components**:
- **Domain**: `domain-agnostic` OR `domain-specific`
- **Task**: `classification`, `detection`, `segmentation`, `landmarks`, `counting`, `vision-language`
- **Subtype**: `binary`, `multiclass`, `multilabel`, `ordinal`, `semantic`, `instance`, etc.
- **Difficulty**: `easy`, `medium`, `hard`
- **Number**: Sequential number (1, 2, 3, etc.)

**Examples**:
- `domain-agnostic_classification_binary_easy_1.md`
- `domain-agnostic_vision-language_describe_short_easy_1.md`
- `domain-specific_radiology_classification_multiclass_medium_1.md`

### Template IDs (within files)
**Format**: `{domain}_{task}_{subtype}_{difficulty}_{number}`
- Must match the filename (without .md extension)
- Used in `rule_id` field within templates

---

## Directory Organization

### Folder Structure
```
templates/
├── domain-agnostic/
│   ├── classification/
│   │   ├── binary/
│   │   ├── multiclass/
│   │   ├── multilabel/
│   │   └── ordinal/
│   ├── object-and-lesion-detection/
│   │   ├── lesion/
│   │   ├── anatomy/
│   │   └── device/
│   ├── segmentation/
│   │   ├── semantic/
│   │   └── instance/
│   ├── anatomical-landmarks-keypoints/
│   │   ├── single/
│   │   └── multiple/
│   ├── counting/
│   │   ├── direct/
│   │   └── density/
│   └── vision-language/
│       ├── describe/
│       ├── ask-and-answer/
│       ├── ground-and-locate/
│       └── align-and-retrieve/
└── domain-specific/
    ├── radiology/
    ├── dermatology/
    ├── pathology/
    ├── ophthalmology/
    ├── surgery/
    └── other-medical/
```

### README Requirements
- **Every folder** must have a README.md file
- Explains templates in the folder and provides usage context
- Includes example question formulas and answer choices
- Avoids boilerplate terms like "technical excellence" or "thoroughly tested"

---

## MCVQA Format Requirements

### Critical MCVQA Compliance Rules

1. **Single Correct Answer**: Each question must have exactly ONE correct answer
2. **Multiple Choice Format**: Questions must provide discrete answer options
3. **No Free Text**: Answers cannot be open-ended text generation
4. **No Multi-Label**: Cannot have multiple simultaneously correct answers
5. **Deterministic Answers**: Answers must be objectively verifiable

### Answer Types (Schema Compliance)
- **`yes_no`**: Binary yes/no questions
- **`single_label`**: Multiple choice with one correct option
- **`coordinates`**: For landmark detection (x,y coordinates)
- **`bbox`**: For object detection (bounding box coordinates)
- **`mask`**: For segmentation tasks

### Answer Format Examples
```json
// Binary Classification
"answer": "Yes",
"answer_type": "yes_no",
"options": ["Yes", "No"]

// Multi-class Classification  
"answer": "Pneumonia",
"answer_type": "single_label", 
"options": ["Pneumonia", "Pleural effusion", "Pneumothorax", "Normal"]

// Landmark Detection
"answer": {"x": 150, "y": 200},
"answer_type": "coordinates"
```

---

## Quality Standards

### Medical Accuracy Requirements
- **Correct Terminology**: All medical terms must be clinically accurate
- **Clinical Relevance**: Questions must reflect real diagnostic scenarios  
- **Domain Expertise**: Templates requiring medical knowledge must be validated
- **Anatomical Accuracy**: Anatomical references must be precise

### Schema Compliance
- **Perfect Alignment**: Must match unified datum schema v1.0 exactly
- **Required Fields**: All mandatory schema fields must be populated
- **Field Validation**: Use proper data types and value constraints
- **Provenance Tracking**: Include original labels and rule IDs for auditing

### Documentation Quality
- **Comprehensive Coverage**: Each section must be complete and actionable
- **Clear Examples**: Examples must be concrete with real dataset references
- **Implementation Ready**: Templates must be usable immediately
- **Maintenance Friendly**: Self-contained documentation without cross-references

---

## Domain Specifications

### Domain-Agnostic Templates
- **Applicability**: Work across ALL medical domains (radiology, pathology, dermatology, etc.)
- **Minimal Requirements**: Require only basic information (image + label + modality)
- **Broad Utility**: Should apply to 80%+ of datasets in their category
- **Generic Language**: Use general medical terminology

### Domain-Specific Templates  
- **Specialization**: Require domain expertise (radiology, dermatology, surgery, etc.)
- **Expert Knowledge**: Use domain-specific terminology and concepts
- **Clinical Context**: Reflect specialized diagnostic workflows
- **Advanced Features**: May include domain-specific reasoning or knowledge

---

## Difficulty Levels

### Easy Templates
- **Characteristics**: Straightforward questions with minimal clinical reasoning
- **Examples**: Presence/absence detection, basic normal/abnormal classification
- **Requirements**: Basic visual recognition capabilities
- **Target**: Entry-level medical AI evaluation

### Medium Templates  
- **Characteristics**: Moderate clinical reasoning or multiple choice complexity
- **Examples**: Differential diagnosis, severity grading, likelihood assessment
- **Requirements**: Intermediate medical knowledge and reasoning
- **Target**: Clinical-level AI evaluation

### Hard Templates
- **Characteristics**: Complex clinical reasoning, meta-cognition, or advanced knowledge
- **Examples**: Definition-based assessment, multi-expert evaluation, complex differential diagnosis
- **Requirements**: Advanced medical expertise and reasoning capabilities
- **Target**: Expert-level AI evaluation

---

## Implementation Guidelines

### Template Creation Process

1. **Requirements Analysis**: Identify target datasets and clinical use cases
2. **Pattern Design**: Create question pattern with appropriate variables  
3. **Schema Mapping**: Ensure full compliance with datum schema v1.0
4. **Example Generation**: Create exactly 2 concrete examples with real datasets
5. **Quality Validation**: Verify medical accuracy and clinical relevance
6. **Documentation**: Complete all 6 required sections
7. **File Creation**: Save with proper naming convention in correct directory
8. **README Update**: Update folder README to include new template

### Validation Checklist

Before considering any template complete:

- [ ] **File exists** in correct directory with proper naming
- [ ] **6 sections complete** following exact structure requirements  
- [ ] **MCVQA compliance** verified (single correct answer, multiple choice)
- [ ] **Schema alignment** confirmed within Template Usage Rules section
- [ ] **Exactly 2 examples** provided with real dataset references
- [ ] **Image presentation method** clearly specified for each example
- [ ] **Answer construction process** documented with distractor generation logic
- [ ] **Conversion process** explained from original dataset to MCVQA format
- [ ] **Medical terminology** validated for accuracy
- [ ] **Clinical relevance** confirmed for target scenarios
- [ ] **Template ID** matches filename and appears in rule_id
- [ ] **README updated** in template directory

### Common Pitfalls to Avoid

- **Cross-references**: Do not reference other templates (creates maintenance burden)
- **Boilerplate language**: Avoid generic phrases like "thoroughly tested"
- **MCVQA violations**: Multiple correct answers, free text, or ambiguous questions
- **Schema misalignment**: Incorrect field types or missing required fields
- **Medical inaccuracy**: Incorrect terminology or unrealistic clinical scenarios
- **Incomplete examples**: Examples without sufficient context or rationale
- **Vague image presentation**: Failing to specify how images are shown (raw, with overlays, highlights, etc.)
- **Missing conversion details**: Not explaining how to get from original annotations to MCVQA format
- **Unclear answer construction**: Not documenting how correct answers and distractors are generated
- **Incomplete workflow**: Missing steps in the conversion process from dataset to MCVQA 

---

## Maintenance and Updates

### Version Control
- All template changes must be tracked in task instruction files
- Document rationale for template modifications
- Maintain backward compatibility when possible

### Quality Assurance  
- Regular medical accuracy reviews
- Schema compliance validation
- Clinical relevance assessment
- Cross-domain applicability verification

### Evolution Guidelines
- Templates may be enhanced but core structure must remain stable
- New sections require update to these guidelines first
- Breaking changes require explicit task documentation

---

## Authority and Precedence

**This document (`general_template_guidelines.md`) serves as the single source of truth for all template requirements.**

**In case of conflicts**:
1. This document takes precedence over task-specific instructions
2. Task-specific instructions should be updated to align with this document
3. Any exceptions must be explicitly documented and justified

**For updates**:
- All template requirement changes must be reflected in this document first
- Task instruction files should reference this document rather than duplicate requirements
- This document should be reviewed and updated with each major template initiative

---

## References

This document consolidates requirements from:
- `instructions/task_2_binary_classification_template.md` (standardized structure)
- `instructions/general_instructions.md` (naming conventions and organization)
- `instructions/template_readme_guidelines.md` (directory documentation)
- `instructions/task_10_priority_missing_templates.md` (MCVQA compliance)
- `docs/architecture.md` (schema alignment requirements)

For implementation examples, see existing templates in:
- `templates/domain-agnostic/classification/binary/`
- `templates/domain-agnostic/classification/multiclass/`
- `templates/domain-specific/*/classification/`
