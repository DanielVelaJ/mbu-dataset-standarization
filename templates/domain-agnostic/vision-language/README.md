# Domain-Agnostic Vision-Language Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Parent Group**: `Vision–Language`  
**Repository Path**: `templates/domain-agnostic/vision-language/`

## 📁 Template Inventory

### **Current Status: ❌ COMPLETELY MISSING (High Priority)**

| Sub-Category | Subdirectory | Leaf Nodes | Planned Templates | Dataset Availability | Status |
|--------------|--------------|------------|-------------------|---------------------|---------|
| **Describe** | `describe/` | Short & Long medical caption generation | 2-3 easy templates | 🟢 **5+ datasets** | 📝 **High Priority (Task 10)** |
| **Ask and Answer** | `ask-and-answer/` | Open-ended, Multiple choice, Visual reasoning QA | 3+ easy templates | 🟡 **3+ datasets** | 📝 **High Priority** |
| **Ground and Locate** | `ground-and-locate/` | Referring expression to bbox/mask, Multi phrase grounding | 3+ templates | 🟡 **1+ dataset** | 📝 **Medium Priority** |
| **Align and Retrieve** | `align-and-retrieve/` | Image-text retrieval, Text-image retrieval, Pair matching | 3+ templates | 🟡 **1+ dataset** | 📝 **Medium Priority** |

## 📋 Sub-Category Overview

### 1. **Describe** (`describe/`) - **HIGHEST PRIORITY**
- **Short Caption Generation** (`short/`): One to two sentence descriptions
- **Long Clinical Report Generation** (`long/`): Paragraph-style structured reports
- **Question Pattern**: "Provide a {brief/detailed} medical description of this image"
- **Answer Format**: Free text (span)
- **Clinical Use**: Image captioning, clinical reporting, medical documentation

### 2. **Ask and Answer** (`ask-and-answer/`) - **HIGH PRIORITY**
- **Open-ended QA** (`open-ended/`): Free text answers to medical questions
- **Multiple Choice QA** (`multiple-choice/`): Select from provided options
- **Visual Reasoning QA** (`visual-reasoning/`): Multi-step reasoning questions
- **Question Pattern**: Direct medical questions about image content
- **Answer Format**: Free text or single label selection
- **Clinical Use**: Medical education, diagnostic support, knowledge assessment

### 3. **Ground and Locate** (`ground-and-locate/`) - **MEDIUM PRIORITY**
- **Referring Expression to Bbox** (`bbox/`): Find bounding box of referred entity
- **Referring Expression to Mask** (`mask/`): Produce pixel-accurate mask of entity
- **Multi Phrase Grounding** (`multi-phrase/`): Locate multiple phrases in sentence
- **Question Pattern**: "Locate the {anatomical_structure}" or "Find the region showing {condition}"
- **Answer Format**: Bounding box coordinates or segmentation masks
- **Clinical Use**: Spatial localization, region identification, anatomy mapping

### 4. **Align and Retrieve** (`align-and-retrieve/`) - **MEDIUM PRIORITY**
- **Image to Text Retrieval** (`image-to-text/`): Find relevant text for image
- **Text to Image Retrieval** (`text-to-image/`): Find relevant images for text
- **Image and Text Pair Matching** (`pair-matching/`): Verify image-text match
- **Question Pattern**: Retrieval and matching questions
- **Answer Format**: Rankings, matches, yes/no verification
- **Clinical Use**: Medical information retrieval, case matching, documentation alignment

## Schema Integration

| Sub-Category | Schema Task Value | Answer Types | Special Considerations |
|--------------|------------------|--------------|----------------------|
| Describe | `"Describe"` | `"span"` (free text) | Text length distinction (short vs long) |
| Ask and Answer | `"Ask&Answer"` | `"span"`, `"single_label"` | Question type variations |
| Ground and Locate | `"Grounding"` | `"bbox"`, masks | Spatial reference integration |
| Align and Retrieve | `"Retrieval"` | Rankings, matches | Ranking and matching metrics |

## Dataset Compatibility

### **High Compatibility (5+ datasets)**:
- ✅ **Vision-Language Describe**: MIMIC chest X-ray reports, brain-tumor-captions, X-ray captions

### **Medium Compatibility (1-3 datasets)**:
- 🟡 **Ask & Answer**: Combined_MRI_ChestXray_QA, Fundus-MMBench
- 🟡 **Ground & Locate**: retinal_oct_analysis2
- 🟡 **Align & Retrieve**: retinal_oct_analysis2

## Clinical Applications

**Medical Education**:
- Interactive medical image analysis training
- Knowledge assessment through visual questioning
- Comprehensive medical image interpretation

**Clinical Documentation**:
- Automated medical report generation
- Image description for medical records
- Clinical finding documentation

**Diagnostic Support**:
- Visual reasoning for complex medical cases
- Multi-modal medical information integration
- Clinical decision support systems

## Implementation Priority

### **Phase 1: Describe Templates** (Task 10)
- Short medical caption generation
- Long clinical report generation
- Foundation for all vision-language capabilities

### **Phase 2: Ask and Answer Templates**
- Open-ended medical question answering
- Multiple choice medical questions
- Visual reasoning for medical education

### **Phase 3: Advanced Vision-Language**
- Grounding and localization templates
- Retrieval and matching templates
- Complex multi-modal reasoning

## Key Differences from Vision-Only Templates

1. **Text Generation**: Produces free text rather than selecting labels
2. **Open Vocabulary**: Not limited to predefined categories
3. **Language Quality**: Requires assessment of grammar, fluency, medical accuracy
4. **Evaluation Complexity**: More complex evaluation than classification accuracy
5. **Multi-Modal Integration**: Combines visual understanding with language generation

## Quality Requirements

**Medical Accuracy**: Generated text must use correct medical terminology
**Clinical Relevance**: Questions and answers must reflect real medical scenarios
**Language Quality**: Proper grammar, fluency, and medical communication standards
**Schema Compliance**: Integration with unified datum schema for vision-language tasks
