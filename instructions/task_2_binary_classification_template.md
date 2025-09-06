# Task 2: Binary Classification Templates
We will define our first binary classification template. Please read the context files and the instructions files and help me define the template.

We must think of a way in which we can turn a dataset that was annotated for binary classification into a MCVQA format. Here are some ideas that we can try: 

Eg: Q: Is {finding} present?  A: {yes/no}

We must explain how the template works and create its .md file in the templates/classification/binary directory.
We must provide 5 examples of how the original dataset example was converted into a MCVQA format using the template. 

## Progress and Decisions Made

### ✅ Template Design Completed (classification_binary_1.md)

**Template Created**: `templates/classification/binary/classification_binary_1.md`

**Key Design Decisions:**

1. **Question Pattern**: "Is {finding} present in this {modality} image?"
   - **Rationale**: Direct, clinically relevant questions that map naturally to diagnostic decision-making
   - **Variables**: `{finding}` for medical condition and `{modality}` for imaging type
   - **Simplicity**: Clear yes/no structure reduces ambiguity and interpretation errors

2. **Answer Format**: Standardized "Yes"/"No" responses
   - **Consistency**: Always "Yes" for positive cases, "No" for negative cases
   - **Mapping**: Clear rules for converting various label formats (0/1, positive/negative, etc.)

3. **Difficulty Level**: Easy
   - **Reasoning**: This is our first template, focusing on straightforward presence/absence detection
   - **Clinical Relevance**: Maps directly to common diagnostic questions

4. **Schema Compliance**: Full mapping to unified datum schema v1.0
   - **Answer Type**: "yes_no" 
   - **Task**: "Classification"
   - **Provenance Tracking**: Includes original labels and rule ID for auditing

**✅ Five Examples Provided:**
1. **Chest X-ray**: Pneumonia detection (ChestX-ray14)
2. **Fundus**: Diabetic retinopathy screening
3. **Skin Image**: Melanoma detection (ISIC)
4. **Brain MRI**: Tumor detection
5. **Chest CT**: Pulmonary nodule detection (LUNA16)

**✅ Documentation Quality:**
- Complete template specification with usage rules
- Implementation notes covering advantages and limitations
- Quality considerations for proper medical terminology
- Clear mapping to medical vision taxonomy (Binary classification leaf node)

### Design Rationale

**Why This Pattern Works:**
- **Clinical Alignment**: Mirrors real diagnostic workflows where radiologists/clinicians ask "Is X present?"
- **Cross-Domain Applicability**: Works across radiology, pathology, dermatology, ophthalmology
- **Low Cognitive Load**: Simple binary questions are easy for models to understand and humans to validate
- **Evaluation Clarity**: Clear success/failure criteria for model assessment

**Template Limitations Acknowledged:**
- Cannot handle multi-class or multi-label scenarios (future templates needed)
- No spatial localization (doesn't ask about regions)
- Basic reasoning only (no complex multi-step logic)

### Next Steps
- ✅ Template 1 completed and documented
- Future: Create classification_binary_2.md (severity-based: normal vs abnormal)
- Future: Create classification_binary_3.md (comparison-based: threshold questions)
- Testing: Validate template with real datasets once loader infrastructure is ready

# Next requests from me
I would like to have another binary classification template that is more complex and offers the positive label alongside distractors that are incorrect. Eg. What does this picture depict? A: {positive label}, B: {distractor 1}, C: {distractor 2}, D: {distractor 3}. Can you help me create this template? Distractors may be for example related to other diseases or conditions that are not the one being asked about but are related to the same body part or domain problems. (these might need to be generated manually or using a language model)

I also liked the way you structured the last template  in sections. Can you please document that we need them in this way in this task as well?

## Template Structure Requirements

**All template files MUST follow this standardized structure:**

### Required Sections (in order):
1. **Template Overview** - ID, task type, difficulty, pattern summary
2. **Template Description** - Detailed explanation of purpose and approach
3. **Question Generation Pattern** - Question format, answer format, template variables
4. **Mapping to Datum Schema** - Complete JSON schema mapping example
5. **Dataset Requirements** - What types of datasets this template supports
6. **Template Usage Rules** - Implementation guidelines and requirements
7. **Examples** - Minimum 5 concrete examples with real dataset references
8. **Implementation Notes** - Advantages, limitations, quality considerations

### Quality Standards:
- **Medical Accuracy**: All examples must use correct medical terminology
- **Schema Compliance**: Perfect alignment with unified datum schema v1.0
- **Clinical Relevance**: Questions must reflect real diagnostic scenarios
- **Clear Documentation**: Each section must be comprehensive and actionable

### Additional Requirements for Complex Templates:
- **Distractor Strategy**: Detailed explanation of how distractors are generated
- **Domain-Specific Guidelines**: Rules for each medical domain (radiology, pathology, etc.)
- **Implementation Methods**: Manual vs automated approaches with quality considerations

## ✅ Template 2 Design Completed (classification_binary_2.md)

**Template Created**: `templates/classification/binary/classification_binary_2.md`

**Key Design Decisions:**

1. **Question Pattern**: "What condition is shown in this {modality} image?"
   - **Format**: Multiple choice with A, B, C, D options
   - **Increased Difficulty**: Medium level due to distractor complexity
   - **Clinical Realism**: Mimics differential diagnosis scenarios

2. **Answer Strategy**:
   - **Positive Cases**: Target condition + 3 related distractors
   - **Negative Cases**: 3 distractors + "None of the above"
   - **Distractor Selection**: Anatomically related, visually similar conditions

3. **Distractor Generation Strategy**:
   - **Clinical Plausibility**: Real medical conditions only
   - **Domain Specificity**: Same organ/body part conditions
   - **Diagnostic Challenge**: Requires medical expertise to differentiate
   - **Quality Control**: Manual curation recommended for accuracy

4. **Schema Compliance**: 
   - **Answer Type**: "single_label" 
   - **Options Array**: Full multiple choice options included
   - **Difficulty**: "medium"

**✅ Five Examples Provided:**
1. **Chest X-ray**: Pneumonia vs respiratory conditions
2. **Fundus**: Diabetic retinopathy vs ophthalmologic conditions  
3. **Skin Image**: Melanoma vs dermatologic conditions
4. **Brain MRI**: Tumor vs neurologic conditions
5. **Chest CT**: Pulmonary nodule vs thoracic conditions

**✅ Advanced Features:**
- Domain-specific distractor pools for major medical specialties
- Both manual and automated distractor generation strategies
- Quality considerations for medical accuracy and clinical relevance

### ✅ Template Structure Refinement

**Template Structure Updated**: Removed "Related Templates" section from both templates to eliminate maintenance overhead.

**Rationale**: Cross-references between templates create unnecessary maintenance burden when templates are added, removed, or reorganized. Self-contained templates are easier to maintain and update independently.

**Updated Structure** (8 required sections):
1. Template Overview
2. Template Description  
3. Question Generation Pattern
4. Mapping to Datum Schema
5. Dataset Requirements
6. Template Usage Rules
7. Examples
8. Implementation Notes

**Benefits**:
- ✅ Reduced maintenance overhead
- ✅ Self-contained template documentation
- ✅ Easier to reorganize template collections
- ✅ No broken cross-references when templates change 


# Next requests from me
Now let's discuss what other kinds of templates could be useful for binary classification --> mcvqa

## ✅ Complete Binary Classification Template Suite (Templates 3-7)

**Five Additional Templates Created** following the standardized 8-section structure:

### **Template 3: Normal vs Abnormal Assessment** - Easy
- **File**: `templates/classification/binary/classification_binary_3.md`
- **Pattern**: "Is this {modality} image normal or abnormal?"
- **Answer**: "Normal" / "Abnormal"
- **Use Case**: Screening scenarios, general abnormality detection
- **Clinical Value**: Maps directly to screening workflows and patient communication

### **Template 4: Likelihood Assessment** - Medium
- **File**: `templates/classification/binary/classification_binary_4.md`
- **Pattern**: "What is the likelihood of {condition} in this {modality} image?"
- **Answer**: "Very unlikely" / "Unlikely" / "Likely" / "Very likely"
- **Use Case**: Probabilistic reasoning, diagnostic confidence assessment
- **Clinical Value**: Mirrors how clinicians think in probabilities rather than absolutes

### **Template 5: Exclusionary Assessment** - Medium
- **File**: `templates/classification/binary/classification_binary_5.md`
- **Pattern**: "Can {condition} be ruled out based on this {modality} image?"
- **Answer**: "Yes, can be ruled out" / "No, cannot be ruled out"
- **Use Case**: **Critical safety testing** - catches dangerous false negatives
- **Clinical Value**: Tests negative predictive reasoning, high-stakes scenarios

### **Template 6: Clear Evidence Assessment** - Easy-Medium
- **File**: `templates/classification/binary/classification_binary_6.md`
- **Pattern**: "Is there clear evidence of {condition} in this {modality} image?"
- **Answer**: "Yes, clear evidence" / "No clear evidence"
- **Use Case**: Evidence-based diagnosis, diagnostic confidence
- **Clinical Value**: Emphasizes evidence quality and diagnostic certainty

### **Template 7: Detection Capability Assessment** - Easy-Medium
- **File**: `templates/classification/binary/classification_binary_7.md`
- **Pattern**: "Can {condition} be detected in this {modality} image?"
- **Answer**: "Yes, detectable" / "No, not detectable"
- **Use Case**: Computer vision capability testing, pattern recognition
- **Clinical Value**: Tests fundamental visual detection skills

## 🎯 **Complete Binary Template Suite: 7 Total Templates**

### **Template Overview by Difficulty:**
- **Easy**: Templates 1 (Presence), 3 (Normal/Abnormal)
- **Easy-Medium**: Templates 6 (Clear Evidence), 7 (Detection)
- **Medium**: Templates 2 (Multiple Choice), 4 (Likelihood), 5 (Exclusionary)

### **Template Overview by Clinical Function:**
1. **Basic Detection**: Templates 1, 7 (presence, detection capability)
2. **Screening**: Templates 3, 6 (normal/abnormal, clear evidence)
3. **Advanced Reasoning**: Templates 2, 4, 5 (multiple choice, likelihood, exclusion)

### **Universal Applicability Confirmed:**
- ✅ **Minimal Info Required**: All templates need only binary label + condition + modality
- ✅ **Schema Compliance**: Full alignment with unified datum schema v1.0
- ✅ **Medical Accuracy**: All examples use correct medical terminology
- ✅ **Clinical Relevance**: Each template maps to real diagnostic scenarios

### **Key Design Achievements:**
- **Comprehensive Coverage**: Tests presence, absence, confidence, evidence, detection
- **Safety Focus**: Template 5 specifically designed to catch dangerous false negatives
- **Difficulty Progression**: From simple yes/no to complex probabilistic reasoning
- **Clinical Realism**: Questions mirror actual medical decision-making workflows
- **Self-Contained**: No cross-references between templates for easy maintenance

### **Strategic Value:**
- **Model Evaluation**: Comprehensive assessment of binary classification capabilities
- **Clinical Safety**: Specific templates for testing high-stakes medical scenarios
- **Educational Use**: Templates teach different aspects of medical reasoning
- **Research Applications**: Enables detailed analysis of model strengths/weaknesses across reasoning types

## ✅ Advanced Binary Templates (Templates 8-9)

**Two Additional High-Difficulty Templates Created** for advanced clinical reasoning:

### **Template 8: Definition-Based Assessment** - Hard
- **File**: `templates/classification/binary/classification_binary_8.md`
- **Pattern**: "Which definition best describes what is shown in this {modality} image?"
- **Answer**: Multiple choice with medical definitions (A/B/C/D)
- **Use Case**: **Tests medical knowledge beyond visual recognition**
- **Clinical Value**: Ensures models understand what conditions actually mean, not just visual patterns
- **Implementation**: ✅ **Complete** with full positive/negative case coverage

### **Template 9: Multi-Doctor Clinical Assessment** - Hard  
- **File**: `templates/classification/binary/classification_binary_9.md`
- **Pattern**: "Three doctors examined this image: [assessments]. Which doctor missed a finding that is definitely present?"
- **Answer**: Doctor A/B/C based on who made the diagnostic error
- **Use Case**: **Tests complex clinical reasoning and meta-cognition**
- **Clinical Value**: Mirrors real clinical consultations, tests evaluation of competing opinions
- **Implementation**: ⚠️ **Partial** - Positive cases complete, negative cases need refinement

## 🎯 **Complete Binary Template Collection: 9 Templates**

### **Final Template Suite Overview:**

**Easy Difficulty (2 templates):**
1. Simple Presence Detection
3. Normal vs Abnormal Assessment

**Easy-Medium Difficulty (2 templates):**
6. Clear Evidence Assessment  
7. Detection Capability Assessment

**Medium Difficulty (3 templates):**
2. Multiple Choice with Distractors
4. Likelihood Assessment (Very unlikely → Very likely)
5. Exclusionary Assessment (Rule-out testing)

**Hard Difficulty (2 templates):**
8. Definition-Based Assessment ✅ Complete
9. Multi-Doctor Clinical Assessment ⚠️ Positive cases only

### **Advanced Template Features:**
- **Template 8**: Tests conceptual medical knowledge using precise definitions
- **Template 9**: Tests meta-cognitive clinical reasoning with physician disagreement scenarios
- **Both templates**: Require extensive domain expertise and medical validation

### **Implementation Status:**
- ✅ **8 templates fully complete** and ready for deployment
- ⚠️ **1 template partially complete** (Template 9 negative cases pending)
- 📝 **TODO tracked**: Template 9 negative case structure refinement

### **Coverage Achieved:**
- **Detection**: Visual pattern recognition (Templates 1, 7)
- **Screening**: Normal/abnormal classification (Templates 3, 6)  
- **Reasoning**: Probabilistic and evidence-based thinking (Templates 4, 5)
- **Knowledge**: Medical terminology and definitions (Template 8)
- **Meta-Cognition**: Clinical reasoning evaluation (Template 9)
- **Difficulty Range**: Easy → Hard progression for comprehensive evaluation 
