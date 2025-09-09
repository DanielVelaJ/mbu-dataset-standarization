# Task 13: Template Validation and Guidelines Compliance Review

## 🎯 **TASK PURPOSE**

**Primary Objective**: Systematically validate that ALL existing templates comply with the updated General Template Guidelines and ensure dataset references are accurate.

**Critical Requirements**:
- **SCOPE**: Validate all 79+ templates across domain-agnostic and domain-specific categories
- **COMPLIANCE**: Ensure 100% adherence to new 5-section format from `general_template_guidelines.md`
- **DATA VALIDATION**: Verify all dataset references exist in our metadata files
- **CLEANUP**: Remove outdated sections and add missing required information
- **DOCUMENTATION**: Track all changes and create summary report

---

## 📋 **VALIDATION SCOPE**

### Templates to Review

**Domain-Agnostic Templates** (~43 templates):
- `templates/domain-agnostic/classification/binary/` (9 templates)
- `templates/domain-agnostic/classification/multiclass/` (3 templates)
- `templates/domain-agnostic/classification/multilabel/` (3 templates)
- `templates/domain-agnostic/classification/ordinal/` (3 templates)
- `templates/domain-agnostic/object-and-lesion-detection/*/` (3 templates)
- `templates/domain-agnostic/segmentation/*/` (6 templates)
- `templates/domain-agnostic/anatomical-landmarks-keypoints/*/` (3 templates)
- `templates/domain-agnostic/vision-language/describe/*/` (3 templates)

**Domain-Specific Templates** (~36 templates):
- `templates/domain-specific/dermatology/` (10 templates)
- `templates/domain-specific/ophthalmology/` (8 templates)
- `templates/domain-specific/other-medical/` (8 templates)
- `templates/domain-specific/pathology/` (8 templates)
- `templates/domain-specific/radiology/` (3 templates)
- `templates/domain-specific/surgery/` (10 templates)

---

## 📚 **REQUIRED DOCUMENTATION REFERENCES**

Before starting validation, read ALL of these files:

### Primary Guidelines
- **`instructions/general_template_guidelines.md`** - Current authoritative template requirements
- **`templates/templates_summary.md`** - Overview of all existing templates

### Dataset Metadata References
- **`data/dataset_metadata/datasets_metadata.csv`** - Master dataset catalog
- **`context/about_dataset_metadata/README.md`** - Metadata file documentation
- **`context/about_dataset_metadata/unified_schema.json`** - Schema structure

### Task Taxonomy
- **`docs/mbu_medical_vision_taxonomy_table.md`** - Valid task types for templates
- **`docs/task_taxonomy_template_repository_mapping.md`** - Task-template mappings

### Historical Context
- **`instructions/task_2_binary_classification_template.md`** - Original template structure
- **`instructions/task_11.7_validation_and_review.md`** - Previous validation findings

---

## ✅ **NEW TEMPLATE REQUIREMENTS (5-Section Format)**

All templates MUST follow this exact structure:

### **Section 1: Template Overview**
- [ ] **Template ID**: Matches filename (without .md)
- [ ] **Task Type**: Valid type from taxonomy table
- [ ] **Difficulty**: Easy, Medium, or Hard
- [ ] **Question Pattern**: Brief summary
- [ ] **Medical Domain**: Applicable domain
- [ ] **Domain-knowledge summary**: Required domain expertise (especially for domain-specific)

### **Section 2: Template Description**
- [ ] Template purpose and approach
- [ ] Clinical context and use cases (medical setting description)
- [ ] Target scenarios and medical workflows

### **Section 3: Question Generation Pattern**
- [ ] **Question Format**: Template with `{variables}`
- [ ] **Answer Format**: MCVQA-compatible structure
- [ ] **Template Variables**: Definitions + usage in Q&A construction
- [ ] **Image Presentation**: Visual modifications (overlays, masks, etc.)
- [ ] **Answer Construction**: Complete process including distractors

### **Section 4: Dataset Requirements**
- [ ] Supported task types and data structures
- [ ] Required label formats and metadata
- [ ] Dataset characteristics compatibility
- [ ] **Datasets from metadata file**: Must reference actual datasets from `datasets_metadata.csv`

### **Section 5: Examples**
- [ ] **Exactly 2 concrete examples** (not more, not less)
- [ ] Each example includes:
  - Original dataset context and annotation format
  - Image presentation method
  - Generated question AND ALL answer choices
  - Complete conversion process explanation
  - Clinical rationale for choices

---

## ❌ **SECTIONS TO REMOVE (If Present)**

These sections should NO LONGER exist in templates:

- **"Mapping to Datum Schema"** (integrated into Section 3)
- **"Implementation Notes"** (removed to reduce boilerplate)
- **"Related Templates"** (creates maintenance burden)
- **"Advantages/Limitations"** (part of old Implementation Notes)
- **"Quality Considerations"** (covered in guidelines)

---

## 🔍 **VALIDATION CHECKLIST**

For EACH template, verify:

### **File Structure & Naming**
- [ ] File follows naming convention: `{domain}_{task}_{subtype}_{difficulty}_{number}.md`
- [ ] Template ID within file matches filename (without .md)
- [ ] File is in correct directory path
- [ ] No naming inconsistencies (e.g., old incorrect names)

### **Section Compliance**
- [ ] Exactly 5 sections in correct order
- [ ] All required subsections present in Section 3
- [ ] No outdated/removed sections present
- [ ] Section 1 has all 5 required fields
- [ ] Section 5 has exactly 2 examples (not 5+)

### **Content Quality**
- [ ] **MCVQA Compliance**: Single correct answer, multiple choice format
- [ ] **Medical Accuracy**: Correct terminology and clinical relevance
- [ ] **Image Presentation**: Clearly specified for each example
- [ ] **Answer Construction**: Complete process documented
- [ ] **Template Variables**: Usage in Q&A construction explained

### **Dataset Validation**
- [ ] **Critical**: All dataset references in Section 4 exist in `datasets_metadata.csv`
- [ ] Dataset names match exactly (case-sensitive)
- [ ] No references to non-existent or misnamed datasets
- [ ] Dataset characteristics align with template requirements

### **Cross-References**
- [ ] **Task Type** matches entries in `mbu_medical_vision_taxonomy_table.md`
- [ ] **Medical Domain** appropriate for file location
- [ ] No broken references to other templates or external sources

---

## 🔧 **VALIDATION PROCESS**

### **Phase 1: Automated Checks**
1. **File Inventory**: List all template files and verify naming conventions
2. **Section Structure**: Check that each template has exactly 5 sections
3. **Dataset References**: Extract all dataset mentions and cross-check with metadata
4. **Template ID Consistency**: Verify IDs match filenames

### **Phase 2: Content Review**
1. **Medical Accuracy**: Review terminology and clinical relevance
2. **MCVQA Compliance**: Ensure single correct answers and multiple choice format
3. **Completeness**: Verify all required subsections and information present
4. **Example Quality**: Check that examples show complete conversion process

### **Phase 3: Corrections**
1. **Remove Outdated Sections**: Delete Implementation Notes, Schema Mapping, etc.
2. **Add Missing Information**: Complete Template Overview fields, Image Presentation, etc.
3. **Fix Dataset References**: Correct any invalid dataset mentions
4. **Standardize Format**: Ensure consistent structure across all templates

---

## 📊 **DELIVERABLES**

### **1. Validation Report** (`template_validation_report.md`)
Create comprehensive report including:
- **Summary Statistics**: Templates validated, issues found, corrections made
- **Issue Categories**: Breakdown by type (structural, content, dataset, etc.)
- **Dataset Validation Results**: Missing/invalid dataset references
- **Template Compliance Matrix**: Section-by-section compliance for each template

### **2. Corrected Templates**
- All templates updated to 5-section format
- Outdated sections removed
- Missing information added
- Valid dataset references confirmed

### **3. Dataset Reference Catalog** (`dataset_template_mapping.csv`)
- Template name
- Referenced datasets
- Validation status (valid/invalid/corrected)
- Notes on corrections made

### **4. Updated README Files**
- Folder README files updated to reflect template changes
- Remove references to outdated template sections
- Add any new template functionality

---

## 🚨 **CRITICAL VALIDATION POINTS**

### **High Priority Issues**
1. **Invalid Dataset References**: Any template referencing non-existent datasets
2. **MCVQA Violations**: Templates with multiple correct answers or free text
3. **Missing Image Presentation**: Templates without visual modification specifications
4. **Structural Non-Compliance**: Templates not following 5-section format

### **Medium Priority Issues**
1. **Incomplete Examples**: Examples missing conversion process explanations
2. **Missing Template Variables Usage**: Variables not explained for Q&A construction
3. **Medical Terminology**: Inaccurate or non-standard medical terms

### **Low Priority Issues**
1. **Formatting Inconsistencies**: Minor markdown or structure variations
2. **Boilerplate Language**: Generic phrases like "thoroughly tested"

---

## 📈 **SUCCESS CRITERIA**

Task completion requires:
- [ ] **100% Template Validation**: All 79+ templates reviewed and corrected
- [ ] **Dataset Reference Accuracy**: All dataset mentions verified against metadata
- [ ] **Structure Compliance**: All templates follow 5-section format exactly
- [ ] **Quality Standards**: Medical accuracy and MCVQA compliance confirmed
- [ ] **Documentation Complete**: Validation report and mapping files created
- [ ] **No Broken References**: All internal and external references valid

---

## 🎯 **IMPLEMENTATION TIMELINE**

**Estimated Effort**: 2-3 days for systematic validation

**Day 1**: Automated checks and file inventory
**Day 2**: Content review and structural corrections  
**Day 3**: Final validation and documentation

**Parallel Processing**: Can be done by domain (agnostic vs specific) or by task type

---

## 📝 **NOTES FOR REVIEWERS**

- **Be Systematic**: Use the validation checklist for every template
- **Document Changes**: Note all modifications made for the report
- **Preserve Intent**: When updating, maintain the original template's purpose
- **Ask Questions**: If medical accuracy is uncertain, flag for expert review
- **Test Compliance**: Verify MCVQA format can be properly implemented

This validation ensures our template repository maintains high quality and consistency as we scale to more datasets and use cases.