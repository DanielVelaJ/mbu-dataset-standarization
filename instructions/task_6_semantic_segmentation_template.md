# Task 6: Semantic Segmentation Templates

Similarly to how we did in task 2 for binary classification, task 4 for multi-class classification, and task 5 for multi-label classification, we will now create templates for semantic segmentation. Please read the context files and the instructions files and help me define the templates.

These should be the domain-agnostic templates that work across all medical domains. Remember semantic segmentation assigns a class to each pixel with no instance separation - this differs fundamentally from image-level classification as we're now working at the pixel level.

## What is Semantic Segmentation?

**Definition**: Classify each pixel into a class; instances of the same class are not separated.

**Key Characteristics**:
- **Input**: One 2D medical image
- **Output**: Pixel-wise mask (single mask file or multi-class encoding)  
- **Task Focus**: Region identification and delineation at pixel level
- **vs Classification**: Pixel-level labeling instead of image-level labeling
- **vs Instance Segmentation**: No separation between different instances of the same class

## MCVQA Conversion Challenge

Converting semantic segmentation datasets to MCVQA format requires asking questions about:
- **Regions**: "What anatomical structure is highlighted in the segmented region?"
- **Presence**: "Is [structure/pathology] segmented in this image?"
- **Coverage**: "What percentage of the image shows [tissue type]?"
- **Boundaries**: "Does the segmentation accurately outline the [organ/lesion]?"

## Template Requirements

### Naming Convention
Follow the established pattern: `{domain}_{task}_{subtype}_{difficulty}_{number}.md`

**Examples**:
- `domain-agnostic_segmentation_semantic_easy_1.md`
- `domain-agnostic_segmentation_semantic_medium_1.md`
- `domain-agnostic_segmentation_semantic_hard_1.md`

### Directory Structure
Save templates in: `templates/domain-agnostic/segmentation/semantic/`

### Template Structure Requirements
**All template files MUST follow the standardized 8-section structure:**

1. **Template Overview** - ID, task type, difficulty, pattern summary
2. **Template Description** - Detailed explanation of purpose and approach  
3. **Question Generation Pattern** - Question format, answer format, template variables
4. **Mapping to Datum Schema** - Complete JSON schema mapping example
5. **Dataset Requirements** - What types of datasets this template supports
6. **Template Usage Rules** - Implementation guidelines and requirements
7. **Examples** - Minimum 5 concrete examples with real dataset references
8. **Implementation Notes** - Advantages, limitations, quality considerations

## Starting Templates (Easy Difficulty)

Create **3 easy-difficulty templates** initially that can work with the most basic information needed for semantic segmentation datasets:

### Template Ideas:
1. **Region Identification**: "What anatomical structure is shown in the highlighted region?"
2. **Segmentation Verification**: "Is the [structure] correctly segmented in this image?"  
3. **Regional Assessment**: "What type of tissue is identified in the segmented area?"

## Dataset Compatibility

Templates must work with semantic segmentation datasets that have:
- **Medical images** (any modality: CT, MRI, X-ray, microscopy, etc.)
- **Pixel-level annotations** (masks, labeled regions)
- **Class labels** for segmented regions
- **Clear anatomical/pathological targets**

**Example Compatible Datasets**:
- Retinal vessel segmentation (fundus images)
- Liver segmentation (abdominal CT)
- Skin lesion segmentation (dermoscopy)
- Brain tumor segmentation (MRI)
- Cell nuclei segmentation (histopathology)

## Schema Considerations

For semantic segmentation in MCVQA format:
- **Answer Type**: Typically "single_label" or "yes_no" depending on question style
- **Task**: "Segmentation" 
- **Geometry**: Include bbox/polygon information when available
- **Segmentation-Specific Fields**: Utilize geometry section of datum schema

## Key Differences from Classification Templates

1. **Spatial Context**: Questions reference spatial regions, not whole images
2. **Geometry Integration**: May include bounding boxes or polygon references
3. **Regional Focus**: Emphasis on anatomical structures and tissue types
4. **Pixel-Level Reasoning**: Questions about segmentation quality and accuracy

## Success Criteria

- ✅ **3 easy-difficulty templates** created following 8-section structure
- ✅ **Schema compliance** with unified datum schema v1.0  
- ✅ **Medical accuracy** using correct anatomical/pathological terminology
- ✅ **Cross-domain applicability** working across medical specialties
- ✅ **5 examples per template** spanning different medical domains
- ✅ **Clear documentation** of segmentation-specific considerations

Let's start with the easy difficulty templates first and ensure they can work with the most basic information that is needed for semantic segmentation datasets.

## Progress Tracking

### ✅ Task 6 Completed Successfully 

**Three Semantic Segmentation Templates Created** in `templates/domain-agnostic/segmentation/semantic/`:

#### **Template 1: Region Identification** (`domain-agnostic_segmentation_semantic_easy_1.md`)
- **Pattern**: "What anatomical structure is highlighted in the segmented region of this {modality} image?"
- **Use Case**: Basic anatomical structure identification in segmented regions
- **Clinical Relevance**: Tests fundamental anatomical recognition at pixel level
- **Answer Type**: Single label (structure name)
- **Examples**: Liver (CT), optic disc (fundus), skin lesion (dermoscopy), left ventricle (MRI), cell nuclei (microscopy)

#### **Template 2: Segmentation Verification** (`domain-agnostic_segmentation_semantic_easy_2.md`)  
- **Pattern**: "Is the {structure} correctly segmented in this {modality} image?"
- **Use Case**: Quality assessment and validation of segmentation accuracy
- **Clinical Relevance**: Mirrors real-world segmentation quality control workflows
- **Answer Type**: Yes/No verification
- **Examples**: Liver segmentation (CT), left ventricle (MRI), retinal vessels (fundus), skin lesion boundary (dermoscopy), prostate (MRI)

#### **Template 3: Regional Assessment** (`domain-agnostic_segmentation_semantic_easy_3.md`)
- **Pattern**: "What type of {assessment_category} is identified in the segmented region of this {modality} image?"
- **Use Case**: Tissue type and pathology classification in segmented areas
- **Clinical Relevance**: Essential for tissue characterization and pathology identification
- **Answer Type**: Single label (tissue/pathology type)
- **Examples**: Gray matter (MRI), myocardium (cardiac MRI), tumor (CT), ductal carcinoma (histopathology), inner nuclear layer (OCT)

### **Key Design Decisions:**

1. **Pixel-Level Focus**: All templates specifically address segmented regions rather than whole images
2. **Easy Difficulty**: Designed for straightforward pixel-level recognition accessible to basic models
3. **Medical Accuracy**: All examples use correct medical terminology and established clinical standards
4. **Cross-Domain Applicability**: Templates work across radiology, pathology, ophthalmology, dermatology, and cardiology
5. **Schema Compliance**: Perfect alignment with unified datum schema v1.0 using appropriate answer types

### **Template Structure Compliance:**
- ✅ **8-Section Format**: All templates follow standardized structure (Overview, Description, Pattern, Schema, Requirements, Rules, Examples, Notes)
- ✅ **5 Examples Each**: All templates include comprehensive examples across different medical domains
- ✅ **Medical Terminology**: Correct anatomical and pathological terminology throughout
- ✅ **Schema Integration**: Proper use of "Segmentation" task type and geometry fields

### **Segmentation-Specific Innovations:**

1. **Spatial Context Integration**: Questions reference specific segmented regions, not whole images
2. **Geometry Schema Utilization**: Templates leverage the geometry section for polygon/mask information
3. **Quality Assessment Focus**: Template 2 specifically addresses segmentation validation needs
4. **Tissue Classification Emphasis**: Template 3 enables detailed tissue/pathology identification

### **Clinical Applications Enabled:**
- **Anatomical Recognition**: Comprehensive assessment of structure identification capabilities
- **Quality Control**: Systematic evaluation of segmentation accuracy and validation
- **Tissue Characterization**: Detailed analysis of tissue type and pathology recognition
- **Multi-Modal Assessment**: Cross-modality evaluation (CT, MRI, microscopy, etc.)

### **Documentation Created:**
- ✅ **README.md**: Comprehensive guide for semantic segmentation template collection
- ✅ **Usage Guidelines**: Clear template selection and implementation best practices
- ✅ **Domain Applications**: Specific use cases across medical specialties
- ✅ **Schema Integration**: Detailed mapping to datum schema requirements

### **Strategic Value Achieved:**
- **Foundation for Segmentation Evaluation**: Enables systematic assessment of pixel-level medical AI capabilities
- **Clinical Quality Control**: Templates support real-world segmentation validation workflows
- **Cross-Domain Framework**: Universal applicability across medical imaging specialties
- **Educational Framework**: Systematic approach to teaching pixel-level medical image analysis

### **Key Differentiators from Classification Templates:**
1. **Spatial Precision**: Pixel-level vs. image-level reasoning
2. **Geometry Integration**: Use of segmentation masks and polygon information
3. **Regional Focus**: Emphasis on anatomical structures and localized tissue types
4. **Quality Assessment**: Specific templates for segmentation accuracy evaluation

Document progress, decisions, and any questions/answers in this file as we develop the templates. 