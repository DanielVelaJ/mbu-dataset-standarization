# Task 14: Domain-Specific Template Updates

## Objective

Update all domain-specific templates to comply with the new 5-section template guidelines established in `instructions/template_guidelines/general_template_guidelines.md`. This task focuses specifically on the 36+ domain-specific templates located in `templates/domain-specific/` subdirectories.

## Background

Domain-specific templates require specialized medical knowledge for particular medical specialties (cardiology, dermatology, neurology, etc.). Unlike domain-agnostic templates, these need detailed domain knowledge summaries that reflect the specialized expertise required for each medical field.

## Reference Materials

**Required Reading:**
- `instructions/template_guidelines/general_template_guidelines.md` - New 5-section template structure
- `templates/domain-agnostic/classification/binary/domain-agnostic_classification_binary_easy_1.md` - Example of corrected template
- `templates/domain-agnostic/classification/multiclass/agnostic_classification_multiclass_1.md` - Example of corrected multiclass template
- `data/dataset_metadata/datasets_metadata.csv` - Dataset references for validation
- `docs/mbu_medical_vision_taxonomy_table.md` - Valid task types

## Template Inventory

Domain-specific templates are organized by medical specialty:

### Cardiology
- `templates/domain-specific/cardiology/classification/binary/`
- `templates/domain-specific/cardiology/classification/multiclass/`

### Dermatology  
- `templates/domain-specific/dermatology/classification/binary/`
- `templates/domain-specific/dermatology/classification/multiclass/`

### Gastroenterology
- `templates/domain-specific/gastroenterology/classification/binary/`

### Neurology
- `templates/domain-specific/neurology/classification/binary/`
- `templates/domain-specific/neurology/classification/multiclass/`

### Oncology
- `templates/domain-specific/oncology/classification/binary/`
- `templates/domain-specific/oncology/classification/multiclass/`

### Ophthalmology
- `templates/domain-specific/ophthalmology/classification/binary/`
- `templates/domain-specific/ophthalmology/classification/multiclass/`

### Pathology
- `templates/domain-specific/pathology/classification/binary/`
- `templates/domain-specific/pathology/classification/multiclass/`
- `templates/domain-specific/pathology/segmentation/instance/`

### Pulmonology
- `templates/domain-specific/pulmonology/classification/binary/`

### Radiology
- `templates/domain-specific/radiology/classification/binary/`
- `templates/domain-specific/radiology/classification/multiclass/`

### Surgery
- `templates/domain-specific/surgery/classification/multiclass/`

## Required Changes

### 1. Template Overview Section Updates

**Template ID Naming Convention:**
- Change from: `specialty_task_subtype_number`
- Change to: `domain-specific_{specialty}_{task}_{difficulty}_{number}`

**Examples:**
- `cardiology_classification_binary_1` → `domain-specific_cardiology_classification_binary_easy_1`
- `ophthalmology_classification_multiclass_2` → `domain-specific_ophthalmology_classification_multiclass_medium_2`

**Required Fields:**
```markdown
**Template ID**: `domain-specific_{specialty}_{task}_{difficulty}_{number}`  
**Task Type**: {Binary classification|Multiclass classification|etc.}  
**Difficulty**: {Easy|Medium|Hard}  
**Question Pattern**: {Brief description}  
**Medical Domain**: {Specific specialty name}  
**Domain-knowledge summary**: {Detailed specialty-specific knowledge requirements}
```

### 2. Domain-Knowledge Summary Guidelines

Each specialty requires different domain knowledge. Examples:

**Cardiology:**
"Requires specialized knowledge of cardiac anatomy, physiology, and pathology. Understanding of ECG interpretation, cardiac imaging modalities (echocardiography, cardiac MRI, cardiac catheterization), hemodynamics, and cardiovascular disease pathophysiology. Knowledge of cardiac rhythm analysis, chamber assessment, and valvular function evaluation."

**Dermatology:**
"Requires specialized knowledge of skin anatomy, dermatological conditions, and dermoscopic pattern recognition. Understanding of lesion morphology, color variations, asymmetry assessment, and malignancy indicators. Knowledge of dermatological terminology, skin cancer types, and differential diagnosis of pigmented and non-pigmented lesions."

**Ophthalmology:**
"Requires specialized knowledge of ocular anatomy, retinal pathology, and ophthalmic imaging interpretation. Understanding of fundus photography, OCT imaging, visual field analysis, and retinal vascular patterns. Knowledge of diabetic retinopathy grading, glaucoma assessment, macular degeneration stages, and optic nerve evaluation."

**Pathology:**
"Requires specialized knowledge of histopathological analysis, tissue morphology, and microscopic pattern recognition. Understanding of cellular architecture, staining techniques, tumor grading systems, and histological markers. Knowledge of tissue preparation artifacts, morphological variations, and pathological diagnostic criteria."

### 3. Question Generation Pattern Section

**Add these subsections:**

#### Image Presentation
- Describe how images are visually presented (raw vs. with annotations)
- Specify any special presentation requirements for the specialty
- Note any modality-specific considerations

#### Answer Construction  
- Explain how correct answers are derived from original dataset annotations
- Detail the logic for generating distractors specific to the medical domain
- Include specialty-specific answer construction rules

### 4. Dataset Requirements Section

**Update to include:**
- Reference to `datasets_metadata.csv` for compatible datasets
- Specialty-specific dataset requirements
- Domain-specific validation criteria

### 5. Template Usage Rules Section

**Replace old sections with:**
- **Implementation guidelines**: Specialty-specific implementation notes
- **Label mapping rules**: How to convert original annotations for this domain
- **Conversion Process**: Step-by-step process including domain-specific considerations  
- **Schema Alignment**: Reference to unified datum schema v1.0 with correct rule_id

### 6. Examples Section

**Reduce to exactly 2 examples with enhanced format:**

```markdown
### Example 1: [Specific Case]
**Original Dataset Context and Annotation Format**: [Dataset details with annotation format]  
**Image Presentation Method**: [How image is displayed]  
**Generated Question and ALL Answer Choices**: 
- **Question**: "[Full question text]"
- **Answer Choices**: [Complete list]
- **Correct Answer**: "[Exact answer]"  
**Complete Conversion Process Explanation**: 
[5-step numbered process]
**Clinical Rationale**: [Detailed medical reasoning with specialty-specific context]
```

## Sections to Remove

- "Mapping to Datum Schema" (integrated into Template Usage Rules)
- "Implementation Notes" 
- Any examples beyond the first 2
- Any outdated sections not in the 5-section structure

## Validation Checklist

For each template:

### Structure Compliance
- [ ] Template follows exact 5-section structure
- [ ] Template ID follows new naming convention  
- [ ] Medical Domain specifies correct specialty
- [ ] Domain-knowledge summary is detailed and specialty-specific
- [ ] Image Presentation subsection added
- [ ] Answer Construction subsection added
- [ ] Examples reduced to exactly 2 with enhanced format

### Content Accuracy
- [ ] Task Type matches taxonomy in `docs/mbu_medical_vision_taxonomy_table.md`
- [ ] Referenced datasets exist in `datasets_metadata.csv`
- [ ] Medical terminology is accurate for the specialty
- [ ] Domain knowledge summary reflects actual expertise requirements
- [ ] Examples use realistic clinical scenarios for the specialty

### Technical Compliance
- [ ] Schema alignment references correct rule_id
- [ ] MCVQA compliance maintained
- [ ] All outdated sections removed

## Delivery Process

1. **Start with one specialty** (recommend cardiology or dermatology)
2. **Update all templates in that specialty** before moving to next
3. **Create a tracking document** listing all completed templates
4. **Test one template thoroughly** before batch processing others
5. **Document any specialty-specific issues** encountered

## Quality Assurance

- Cross-reference domain knowledge summaries with medical literature
- Ensure clinical terminology is current and accurate
- Validate that examples reflect real clinical scenarios
- Check that difficulty levels are appropriate for the domain expertise required

## Example Complete Template

See `templates/domain-agnostic/classification/binary/domain-agnostic_classification_binary_easy_1.md` for the exact format and structure to follow, but replace the "Domain-agnostic" content with specialty-specific information.

## Questions/Issues

If you encounter any ambiguities or domain-specific questions:
1. Document the issue with specific template reference
2. Check medical literature for standard terminology
3. Consider consulting domain experts for complex clinical details
4. Flag any inconsistencies in original template content

---

## 📋 **WORK DIVISION PLAN - TASK 14**

### ✅ **COMPLETED BY AI ASSISTANT (6/43 templates)**

**Dermatology Domain (6/9 completed):**
- ✅ `dermatology_classification_binary_easy_1.md` - **MASTER TEMPLATE**
- ✅ `dermatology_classification_binary_easy_2.md` - Inflammatory vs Non-inflammatory
- ✅ `dermatology_classification_binary_easy_3.md` - Pigmented vs Non-pigmented  
- ✅ `dermatology_classification_multiclass_easy_1.md` - Skin Cancer Classification
- ✅ `dermatology_classification_multiclass_easy_2.md` - Dermoscopic Pattern Recognition
- ✅ `dermatology_classification_multiclass_easy_3.md` - Condition Category Assessment

### 🔄 **WORK DIVISION OPTIONS**

**Option A - AI Continues Dermatology + High Priority Domains**
**AI Assistant takes:**
- 🔄 Remaining Dermatology (3 templates): 
  - `dermatology_classification_multiclass_easy_4.md`
  - `dermatology_classification_ordinal_easy_1.md`
- 🆕 Ophthalmology Domain (8 templates) - High dataset availability
- 🆕 Pathology Domain (8 templates) - High clinical impact

**Friend takes:**
- 🆕 Surgery Domain (10 templates)
- 🆕 Radiology Domain (3 templates)  
- 🆕 Other-Medical Domain (8 templates)

**Option B - Domain-Based Division**
**AI Assistant takes:**
- 🔄 Complete Dermatology Domain (3 remaining)
- 🆕 Ophthalmology Domain (8 templates)
- 🆕 Pathology Domain (8 templates)
- **Total: 19 templates**

**Friend takes:**
- 🆕 Surgery Domain (10 templates)
- 🆕 Radiology Domain (3 templates)
- 🆕 Other-Medical Domain (8 templates) 
- **Total: 21 templates**

### 📊 **CURRENT STATUS SUMMARY**

| Domain | Total Templates | Completed | Remaining | Status |
|--------|-----------------|-----------|-----------|---------|
| **Dermatology** | 9 | 6 ✅ | 3 🔄 | In Progress |
| **Ophthalmology** | 8 | 0 | 8 🆕 | Not Started |
| **Pathology** | 8 | 0 | 8 🆕 | Not Started |
| **Surgery** | 10 | 0 | 10 🆕 | Not Started |
| **Radiology** | 3 | 0 | 3 🆕 | Not Started |
| **Other-Medical** | 8 | 0 | 8 🆕 | Not Started |
| **TOTAL** | **46** | **6** | **40** | **13% Complete** |

### 🎯 **MASTER TEMPLATE PATTERN ESTABLISHED**

**✅ Proven Pattern (Copy this approach):**
1. **Template ID**: Change to `domain-specific_{specialty}_classification_{type}_easy_{number}`
2. **Template Overview**: Add "Medical Domain" and detailed "Domain-knowledge summary"
3. **Question Generation Pattern**: Add "Image Presentation" and "Answer Construction" subsections
4. **Dataset Requirements**: New consolidated format with `datasets_metadata.csv` references
5. **Template Usage Rules**: Consolidated format with schema alignment
6. **Examples**: Reduce to exactly 2 with enhanced conversion process format
7. **Remove Sections**: Delete "Mapping to Datum Schema" and "Implementation Notes"

**📁 Reference Templates:**
- **Master**: `templates/domain-specific/dermatology/classification/binary/dermatology_classification_binary_easy_1.md`
- **Examples**: Any of the 6 completed dermatology templates

### 🚀 **RECOMMENDED DIVISION**

**Recommendation: Option B (Domain-Based)**
- **Efficiency**: Each person becomes expert in fewer domains
- **Consistency**: Domain-specific knowledge remains with one person
- **Quality**: Better domain expertise per person
- **Balance**: Nearly equal workload (19 vs 21 templates)

### 📝 **COORDINATION NOTES**

**For Friend:**
1. **Read the master template first**: `dermatology_classification_binary_easy_1.md`
2. **Follow exact pattern**: Use completed dermatology templates as reference
3. **Domain-knowledge summaries**: Each domain needs specialized knowledge descriptions
4. **MCVQA compliance**: Ensure single correct answer format
5. **Progress tracking**: Update this file with completion status

**Critical Success Factors:**
- ✅ Follow 5-section format exactly
- ✅ Update Template IDs to new naming convention
- ✅ Add Image Presentation and Answer Construction subsections
- ✅ Reference datasets from `datasets_metadata.csv`
- ✅ Exactly 2 enhanced examples per template
- ✅ Remove outdated sections

---

**Priority**: High  
**Estimated Time**: 2-3 hours per specialty (depending on number of templates)  
**Dependencies**: Completion of domain-agnostic template updates
