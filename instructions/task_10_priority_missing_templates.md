# Task 10: Priority Missing Templates - Ordinal Grading, Vision-Language Describe, and Landmark Detection

## 🎯 **TASK PURPOSE**

**Primary Objective**: Create **7-9 actual, working MCVQA template files** for the three highest priority missing categories in our medical vision taxonomy coverage.

**Critical Requirements**:
- **DELIVERABLE**: Physical `.md` template files, not just documentation or planning
- **FORMAT**: Multiple Choice Visual Question Answering (MCVQA) with exactly one correct answer
- **VALIDATION**: Each template must be tested and verified for MCVQA compatibility
- **SCOPE**: Domain-agnostic templates that work across all medical specialties

**What Constitutes Completion**:
- ✅ **7-9 template files** physically created in correct directories
- ✅ **All templates** follow 8-section standardized structure  
- ✅ **100% MCVQA compliance** - no free text, no multilabel, no multiple correct answers
- ✅ **Medical accuracy** verified with correct terminology
- ✅ **Schema alignment** with unified datum schema v1.0

**What Does NOT Constitute Completion**:
- ❌ Documentation that claims templates exist but no actual files
- ❌ Templates that violate MCVQA format (free text, multiple correct answers)
- ❌ Planning documents without implementation
- ❌ Templates that don't align with available datasets

## 🚨 **CRITICAL: IMPLEMENTATION VS. DOCUMENTATION**

**Based on Task 11 validation findings, this task requires ACTUAL IMPLEMENTATION, not just planning:**

**Task 11 Issues Found:**
- ✅ **Documentation claimed "✅ Completed"** 
- ❌ **Zero actual template files existed**
- ❌ **Empty directories despite completion claims**
- ❌ **24 missing templates** despite "completed" status

**Task 10 Requirements:**
- ✅ **Must create actual `.md` template files**
- ✅ **Must place files in correct directories**  
- ✅ **Must verify file existence before claiming completion**
- ✅ **Documentation must match actual implementation**

**Implementation First, Documentation Second**: Create the actual template files FIRST, then update documentation to reflect reality.

---

Similarly to how we did in task 2 for binary classification, task 4 for multiclass classification, task 5 for multilabel classification, task 6 for semantic segmentation, task 7 for instance segmentation, and task 9 for object detection, we will now create **MCVQA (Multiple Choice Visual Question Answering) templates** for the three highest priority missing template categories. Please read the context files and the instructions files and help me define the templates.

These should be the domain-agnostic MCVQA templates that work across all medical domains. This task covers three distinct categories that represent the most critical gaps in our template coverage:

1. **Ordinal Grading** (Classification subcategory)
2. **Vision-Language Describe** (New major category)
3. **Landmark Detection** (New major category)

## What are these Missing Categories?

### 1. Ordinal Grading (Classification Subcategory)

**Definition**: Assign one label from an ordered set where order matters for interpretation (Stage 1 < Stage 2 < Stage 3).

**Key Characteristics**:
- **Input**: One 2D medical image
- **Output**: One label from an ordered set (e.g., 0<1<2<3)
- **Task Focus**: Severity/stage assessment with meaningful progression
- **vs Multiclass**: Order matters - Stage 2 is inherently "between" Stage 1 and Stage 3
- **vs Binary**: More than two ordered levels

**Medical Examples**:
- **Diabetic retinopathy grading**: Grade 0 (no DR) → Grade 4 (proliferative DR)
- **BI-RADS mammography**: Category 1 (normal) → Category 5 (highly suspicious)
- **Disease staging**: Stage I → Stage IV cancer progression
- **Liver fibrosis**: F0 (no fibrosis) → F4 (cirrhosis)

**Available Datasets**: 4 datasets identified (EyePACS, Fundus-MMBench, etc.)

### 2. Vision-Language Describe (New Major Category)

**Definition**: Generate textual descriptions from medical images, ranging from short captions to full clinical reports.

**Key Characteristics**:
- **Input**: One 2D medical image
- **Output**: Text string (short caption or long report)
- **Task Focus**: Image-to-text generation with medical accuracy
- **vs Classification**: Generates free text rather than selecting from predefined labels
- **vs Detection/Segmentation**: Describes rather than localizes

**Subcategories**:
- **Short medical caption generation**: 1-2 sentence descriptions
- **Long clinical report generation**: Paragraph-style structured reports

**Medical Examples**:
- **Short captions**: "Irregular pigmented lesion on arm", "Normal chest X-ray"
- **Long reports**: Full radiology reports with findings, impressions, recommendations

**Available Datasets**: 5+ datasets identified (MIMIC chest X-ray reports, brain-tumor-captions, etc.)

### 3. Landmark Detection (New Major Category)

**Definition**: Predict precise (x,y) coordinates of anatomical landmarks in medical images.

**Key Characteristics**:
- **Input**: One 2D medical image
- **Output**: (x,y) coordinates for single landmark OR list of (x,y) points for multiple landmarks
- **Task Focus**: Precise point localization for measurement and analysis
- **vs Object Detection**: Point coordinates instead of bounding boxes
- **vs Segmentation**: Point locations instead of pixel masks

**Subcategories**:
- **Single landmark detection**: One anatomical point per image
- **Multiple landmark detection**: Several anatomical points per image

**Medical Examples**:
- **Single**: Fovea center in fundus images, pupil center
- **Multiple**: Cephalometric landmarks, surgical tracking points, anatomical measurement points

**Available Datasets**: 4 datasets identified (Pupil_Position_in_the_Eye, SurgicalVideoEndoNeRFTracking, etc.)

## MCVQA Format and Option Generation

**Critical**: All templates must generate **Multiple Choice Visual Question Answering (MCVQA)** format, not free-form responses. This applies to all three categories, including Vision-Language Describe templates.

### Option Generation Strategy

**Based on Dataset Annotations Only**: We can only use information that the dataset provides in its annotations. Multiple choice options must be generated from:

1. **Ordinal Grading**: Options come directly from the ordered label set in the dataset
   - Example: ["Grade 0", "Grade 1", "Grade 2", "Grade 3", "Grade 4"] for diabetic retinopathy
   - Use exact grade/stage labels from dataset annotations

2. **Vision-Language Describe**: Options generated from text annotations in the dataset
   - **Method 1**: Use actual text descriptions from dataset as correct option + similar descriptions as distractors
   - **Method 2**: Generate options later with LLMs when necessary during template application
   - **Note**: Cannot create free-form text generation - must provide multiple choice options

3. **Landmark Detection**: Options generated from coordinate annotations
   - **Method 1**: Use coordinate ranges/regions as multiple choice options
   - **Method 2**: Generate coordinate-based options later with LLMs when necessary
   - **Format**: Provide coordinate ranges or regions rather than exact pixel coordinates

### When LLM Option Generation is Needed

For **Vision-Language Describe** and **Landmark Detection** templates:
- If dataset only provides ground truth without sufficient similar examples
- Generate plausible distractors using LLMs during template application
- Ensure generated options maintain medical accuracy and clinical relevance
- Always include the correct answer from dataset annotations

### MCVQA Requirements
- **Minimum 3 options** per question (typically 4-5 for better evaluation)
- **One correct answer** from dataset annotations
- **Plausible distractors** that require medical knowledge to distinguish
- **Clear option formatting** following established MCVQA patterns

## Template Requirements

### Naming Convention
Follow the established pattern: `{domain}_{task}_{subtype}_{difficulty}_{number}.md`

**Examples for this task**:
- `domain-agnostic_classification_ordinal_easy_1.md`
- `domain-agnostic_vision-language_describe_short_easy_1.md`  
- `domain-agnostic_anatomical-landmarks-keypoints_single_easy_1.md`

### Directory Structure
Save templates in their respective new directories:
- **Ordinal Grading**: `templates/domain-agnostic/classification/ordinal/`
- **Vision-Language Describe**: `templates/domain-agnostic/vision-language/describe/short/` and `templates/domain-agnostic/vision-language/describe/long/`
- **Landmark Detection**: `templates/domain-agnostic/anatomical-landmarks-keypoints/single/` and `templates/domain-agnostic/anatomical-landmarks-keypoints/multiple/`

### Template Structure Requirements
**All template files MUST follow the standardized 8-section structure:**

#### Required Sections (in order):
1. **Template Overview** - ID, task type, difficulty, pattern summary
2. **Template Description** - Detailed explanation of purpose and approach
3. **Question Generation Pattern** - Question format, answer format, template variables
4. **Mapping to Datum Schema** - Complete JSON schema mapping example
5. **Dataset Requirements** - What types of datasets this template supports
6. **Template Usage Rules** - Implementation guidelines and requirements
7. **Examples** - Minimum 5 concrete examples with real dataset references
8. **Implementation Notes** - Advantages, limitations, quality considerations

#### Quality Standards:
- **Medical Accuracy**: All examples must use correct medical terminology
- **Schema Compliance**: Perfect alignment with unified datum schema v1.0
- **Clinical Relevance**: Questions must reflect real diagnostic scenarios
- **Clear Documentation**: Each section must be comprehensive and actionable

#### Special Requirements for Each Category:

**Ordinal Grading Templates:**
- **Order Preservation**: Questions must respect the ordered nature of labels
- **Clinical Staging**: Use established medical grading systems (BI-RADS, TNM, etc.)
- **Scale Awareness**: Templates should work with 3-8 ordered levels

**Vision-Language Describe Templates:**
- **Description Selection**: MCVQA questions about selecting correct descriptions from multiple choice options
- **Length Appropriateness**: Short vs long description options with appropriate medical detail
- **Medical Terminology**: All description options must use correct clinical language

**Landmark Detection Templates:**
- **Coordinate Selection**: MCVQA questions expecting selection from coordinate region/set options
- **Spatial Precision**: Emphasis on anatomically meaningful location options
- **Anatomical Accuracy**: Use correct anatomical landmark names in coordinate options

## Starting Templates (Easy Difficulty)

Create **2-3 easy-difficulty templates** for each category (total 7-9 templates):

### 1. Ordinal Grading Templates (2-3 templates)

#### Template 1: Basic Severity Assessment
- **Pattern**: "What {severity_type} is shown in this {modality} image?"
- **Use Case**: Disease staging, severity grading
- **Example**: "What diabetic retinopathy grade is shown in this fundus image?"
- **Answer Type**: "single_label" with ordered options
- **MCVQA Options**: ["Grade 0 (No DR)", "Grade 1 (Mild NPDR)", "Grade 2 (Moderate NPDR)", "Grade 3 (Severe NPDR)", "Grade 4 (Proliferative DR)"]

#### Template 2: Stage Progression Assessment  
- **Pattern**: "Which stage of {condition} is demonstrated in this {modality} image?"
- **Use Case**: Disease progression, staging systems
- **Example**: "Which stage of liver fibrosis is demonstrated in this ultrasound image?"
- **Answer Type**: "single_label" with stage progression
- **MCVQA Options**: ["F0 (No fibrosis)", "F1 (Minimal fibrosis)", "F2 (Moderate fibrosis)", "F3 (Advanced fibrosis)", "F4 (Cirrhosis)"]

### 2. Vision-Language Describe Templates (2-3 templates)

#### Template 1: Short Medical Caption Generation
- **Pattern**: "Which of the following best describes this {modality} image?"
- **Use Case**: Image captioning, quick summaries
- **Example**: "Which of the following best describes this chest X-ray image?"
- **Answer Type**: "single_label" selecting from caption options
- **MCVQA Options**: ["Bilateral lower lobe pneumonia", "Normal chest X-ray", "Pneumothorax in left lung", "Pleural effusion"] (generated from dataset captions or LLM when needed)

#### Template 2: Clinical Findings Description
- **Pattern**: "What are the key clinical findings visible in this {modality} image?"
- **Use Case**: Structured medical reporting
- **Example**: "What are the key clinical findings visible in this chest CT image?"
- **Answer Type**: "single_label" selecting from findings options
- **MCVQA Options**: ["Large mass in right upper lobe with spiculated margins", "Multiple bilateral nodules", "Normal lung parenchyma", "Ground glass opacities"] (generated from dataset annotations or LLM when needed)

### 3. Landmark Detection Templates (2-3 templates)

#### Template 1: Single Anatomical Landmark
- **Pattern**: "Where is the {landmark} located in this {modality} image?"
- **Use Case**: Single point anatomical localization
- **Example**: "Where is the fovea center located in this fundus image?"
- **Answer Type**: "single_label" selecting from coordinate regions
- **MCVQA Options**: ["Upper left quadrant (120, 150)", "Center region (256, 200)", "Lower right quadrant (380, 290)", "Temporal region (400, 180)"] (coordinate regions generated from dataset annotations or LLM when needed)

#### Template 2: Multiple Anatomical Landmarks
- **Pattern**: "Which set of points correctly identifies the {landmark_set} in this {modality} image?"
- **Use Case**: Multiple point anatomical localization
- **Example**: "Which set of points correctly identifies the cephalometric landmarks in this X-ray?"
- **Answer Type**: "single_label" selecting from landmark sets
- **MCVQA Options**: ["Set A: [(120,80), (200,120), (180,200)]", "Set B: [(115,85), (205,115), (175,205)]", "Set C: [(130,75), (190,125), (185,195)]", "Set D: [(125,82), (198,118), (182,198)]"] (coordinate sets generated from dataset annotations or LLM when needed)

## Dataset Compatibility

### Ordinal Grading Datasets Requirements:
- **Medical images** with **ordered severity/stage labels**
- **Established grading systems** (BI-RADS, diabetic retinopathy grades, etc.)
- **Clear progression** between levels
- **3-8 ordered categories**

### Vision-Language Describe Datasets Requirements:
- **Medical images** paired with **textual descriptions**
- **Caption/report text** (short descriptions or full clinical reports)
- **Medically accurate language** in text descriptions
- **Any imaging modality**

### Landmark Detection Datasets Requirements:
- **Medical images** with **precise point annotations**
- **Anatomical landmark coordinates** (x,y positions)
- **Clear anatomical targets** (fovea, pupil, bone landmarks, etc.)
- **Single or multiple points per image**

## Schema Considerations

### Ordinal Grading Schema Mapping:
- **Task**: "Classification"
- **Answer Type**: "single_label" 
- **Options**: Ordered list of severity levels
- **Special Field**: Consider adding "ordinal_scale" metadata

### Vision-Language Describe Schema Mapping:
- **Task**: "Describe" 
- **Answer Type**: "single_label" (selecting from description options)
- **Options**: Generated from dataset text annotations or LLM-created distractors
- **MCVQA Format**: Multiple choice selection rather than free text generation

### Landmark Detection Schema Mapping:
- **Task**: "Landmarks"
- **Answer Type**: "single_label" (selecting from coordinate options)
- **Options**: Coordinate regions or landmark sets as multiple choice
- **Spatial Reference**: Include coordinate regions/sets in MCVQA options
- **MCVQA Format**: Multiple choice selection of coordinate locations rather than direct coordinate output

## Key Differences from Existing Templates

### Ordinal vs Multiclass Classification:
1. **Order Matters**: Ordinal preserves meaningful sequence (mild < moderate < severe)
2. **Distance Concepts**: "Close" predictions are better than "far" predictions
3. **Clinical Staging**: Maps to established medical progression systems
4. **Evaluation Metrics**: May use different metrics than standard multiclass

### Vision-Language vs Classification:
1. **Description Selection**: MCVQA selection from text description options rather than standard label classification
2. **Option Generation**: Options generated from dataset text annotations or LLM-created distractors
3. **Medical Text Accuracy**: Requires medically accurate description options and terminology
4. **Evaluation**: Classification accuracy on description selection rather than text generation metrics

### Landmark vs Object Detection:
1. **Coordinate Selection**: MCVQA selection from coordinate regions/sets rather than bounding box output
2. **Spatial Precision**: Options represent precise anatomical locations as multiple choice
3. **Anatomical Knowledge**: Requires anatomically meaningful coordinate options
4. **Clinical Applications**: Different MCVQA format for measurement-based questions vs identification

## ✅ **SPECIFIC DELIVERABLES REQUIRED**

**Task 10 MUST produce the following actual files:**

### **Required Template Files (7-9 total)**
1. **Ordinal Grading**: 2-3 templates in `templates/domain-agnostic/classification/ordinal/`
   - Example names: `domain-agnostic_classification_ordinal_easy_1.md`, `domain-agnostic_classification_ordinal_easy_2.md`
   
2. **Vision-Language Describe**: 2-3 templates in `templates/domain-agnostic/vision-language/describe/`
   - Example names: `domain-agnostic_vision-language_describe_short_easy_1.md`, `domain-agnostic_vision-language_describe_long_easy_1.md`
   
3. **Landmark Detection**: 2-3 templates in `templates/domain-agnostic/anatomical-landmarks-keypoints/`
   - Example names: `domain-agnostic_anatomical-landmarks-keypoints_single_easy_1.md`, `domain-agnostic_anatomical-landmarks-keypoints_multiple_easy_1.md`

### **File Content Requirements**
Each template file MUST contain:
- ✅ Complete 8-section structure (Overview, Description, Pattern, Schema, Requirements, Rules, Examples, Notes)
- ✅ MCVQA-compatible questions (multiple choice with single correct answer)
- ✅ 5 concrete medical examples with real dataset references
- ✅ Proper schema mapping to unified datum schema v1.0
- ✅ Medical terminology accuracy

## Success Criteria

- ✅ **7-9 easy-difficulty templates** physically created following 8-section structure
- ✅ **Schema compliance** with unified datum schema v1.0
- ✅ **Medical accuracy** using correct anatomical/pathological terminology
- ✅ **Cross-domain applicability** working across medical specialties  
- ✅ **5 examples per template** spanning different medical domains
- ✅ **MCVQA format compliance** - all templates use multiple choice format
- ✅ **Clear documentation** of category-specific considerations
- ✅ **Proper folder organization** in new directory structure

## Implementation Strategy

### Phase 1: Easy Templates (Current Task)
Focus on fundamental capabilities for each category:
- **Ordinal**: Basic severity grading and stage assessment
- **Vision-Language**: Short captions and clinical findings descriptions  
- **Landmarks**: Single and multiple point localization

### Phase 2: Medium Templates (Future)
Add complexity and advanced reasoning:
- **Ordinal**: Comparative grading, progression assessment
- **Vision-Language**: Long clinical reports, structured reporting
- **Landmarks**: Spatial relationships, measurement-based questions

### Phase 3: Hard Templates (Future)
Complex reasoning and validation:
- **Ordinal**: Multi-factor grading, uncertainty assessment
- **Vision-Language**: Multi-image reports, differential descriptions
- **Landmarks**: Dynamic tracking, multi-view consistency

## Quality Considerations

### Medical Accuracy
- Use correct medical terminology for all conditions, anatomy, and procedures
- Ensure questions reflect real clinical workflows and diagnostic processes
- Validate examples with appropriate medical domain expertise
- Follow established medical grading and staging systems

### Technical Precision
- **MCVQA Format**: All templates must generate multiple choice questions, not free-form responses
- **Option Quality**: All multiple choice options must be medically accurate and plausible distractors
- **Dataset-Based Options**: Use only information available in dataset annotations for option generation
- **Ordinal Templates**: Preserve order relationships and use clinically meaningful scales in options
- **Vision-Language Templates**: Generate medically accurate description options from dataset text or LLM when needed
- **Landmark Templates**: Provide anatomically meaningful coordinate regions/sets as multiple choice options
- **Cross-Category Consistency**: Maintain MCVQA quality standards across different template types

### Cross-Domain Applicability
- Templates should work across radiology, pathology, surgery, dermatology, ophthalmology
- Avoid domain-specific terminology that limits applicability
- Ensure questions scale appropriately across different imaging modalities and clinical contexts

## Priority Order for Implementation

Based on dataset availability and clinical impact:

### 🥇 **Highest Priority** (Start here):
1. **Ordinal Grading Templates** - 4 available datasets, critical for severity assessment
2. **Vision-Language Describe Templates** - 5+ available datasets, major new capability

### 🥈 **High Priority** (Follow-up):
3. **Landmark Detection Templates** - 4 available datasets, distinct from object detection

This prioritization balances dataset availability, clinical importance, and technical feasibility to maximize impact.

## Progress Tracking

### Current Status
- **Folder Structure**: ✅ **Complete** - All new directories created
- **Task 10 Instructions**: ✅ **Complete** - Comprehensive guidelines established

### Next Steps
1. **Create Ordinal Grading Templates**: Start with basic severity assessment
2. **Create Vision-Language Describe Templates**: Begin with short caption generation  
3. **Create Landmark Detection Templates**: Focus on single point localization
4. **Create README files**: Overview documents for each new template collection
5. **Test Templates**: Validate with compatible datasets from our metadata

### Design Decisions Made
✅ **Three-Category Approach**: Cover ordinal grading, vision-language describe, and landmark detection
✅ **Priority Order**: Ordinal → Vision-Language → Landmarks based on impact and dataset availability
✅ **Folder Structure**: Proper organization in new directory hierarchy
✅ **Schema Integration**: Full alignment with unified datum schema v1.0
✅ **Clinical Focus**: Templates designed for real medical workflows and applications

### Key Insights from Analysis
- **Ordinal grading** fills critical gap in classification capabilities for medical severity assessment
- **Vision-Language describe** opens entirely new capability for image-to-text medical applications
- **Landmark detection** provides precise spatial localization different from object detection
- **Combined impact** significantly expands template coverage across medical vision taxonomy

Document progress, decisions, and any questions/answers in this file as we develop the templates.

---

## 🔍 **COMPLETION VALIDATION CHECKLIST**

**Before claiming Task 10 is complete, verify ALL of the following:**

### **📁 File Existence Verification**
- [ ] **Ordinal Templates**: 2-3 `.md` files physically exist in `templates/domain-agnostic/classification/ordinal/`
- [ ] **Vision-Language Templates**: 2-3 `.md` files physically exist in `templates/domain-agnostic/vision-language/describe/short/` and/or `templates/domain-agnostic/vision-language/describe/long/`
- [ ] **Landmark Templates**: 2-3 `.md` files physically exist in `templates/domain-agnostic/anatomical-landmarks-keypoints/single/` and/or `templates/domain-agnostic/anatomical-landmarks-keypoints/multiple/`
- [ ] **Total Count**: 7-9 actual template files (not documentation files)

### **🎯 MCVQA Format Compliance**
- [ ] **Question Format**: Every template asks a multiple choice question
- [ ] **Answer Options**: Every template provides 3-5 multiple choice options
- [ ] **Single Correct Answer**: Every template has exactly one correct answer (no multilabel)
- [ ] **No Free Text**: No templates ask for free text generation or open-ended responses
- [ ] **Answer Type**: All templates use `"answer_type": "single_label"` in schema mapping

### **📋 Template Structure Compliance**  
- [ ] **8-Section Structure**: Every template follows the required 8-section format
- [ ] **Medical Accuracy**: All templates use correct medical terminology
- [ ] **Domain-Agnostic**: Templates work across medical specialties, not domain-specific
- [ ] **Dataset Alignment**: Templates reference compatible datasets from our metadata

### **🔬 Content Quality Verification**
- [ ] **Ordinal Templates**: Preserve order relationships in answer options (Grade 0 < Grade 1 < Grade 2...)
- [ ] **Vision-Language Templates**: Provide medical description options, not free text generation
- [ ] **Landmark Templates**: Provide coordinate region/set options, not exact coordinate output
- [ ] **Clinical Relevance**: All examples reflect real medical scenarios and workflows

### **📚 Documentation Accuracy**
- [ ] **Progress Tracking**: This file accurately reflects actual implementation status
- [ ] **README Updates**: Relevant README files updated to reflect new templates
- [ ] **No False Claims**: No documentation claims completion without actual files

---

## ⚠️ **AVOIDING TASK 11 PITFALLS**

**Learn from Task 11 validation issues - DO NOT:**
- ❌ **Document completion without implementation** - Creates discrepancy between claims and reality
- ❌ **Create multilabel templates** - Violates MCVQA single correct answer requirement  
- ❌ **Create free text generation templates** - Not compatible with multiple choice format
- ❌ **Claim templates exist when directories are empty** - Leads to project validation failures

**DO:**
- ✅ **Create actual template files first, then document completion**
- ✅ **Test each template for MCVQA compliance before claiming completion**
- ✅ **Verify all files exist in correct directories before final validation**
- ✅ **Update documentation to match actual implementation, not planned implementation**

---

## 📊 **TASK 10 SUCCESS CRITERIA**

**This task is complete ONLY when:**
1. **7-9 physical template files exist** in the correct directories
2. **All templates are 100% MCVQA compliant** (verified by testing)
3. **All templates follow the 8-section structure** (verified by inspection)
4. **All templates are medically accurate** (verified by domain expertise)
5. **Documentation accurately reflects implementation** (no false completion claims)

**Verification Method**: Run directory listing commands and template content inspection to confirm physical existence and format compliance before claiming completion.
