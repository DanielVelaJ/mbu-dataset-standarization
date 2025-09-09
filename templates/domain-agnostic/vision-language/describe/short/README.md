# Short Medical Caption Generation Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Leaf Node**: `Short medical caption generation — one to two sentence description`  
**Parent Category**: Vision–Language → Describe  
**Repository Path**: `templates/domain-agnostic/vision-language/describe/short/`

## 📁 Template Inventory

### **Current Status: ✅ COMPLETE (Task 10 Implementation)**

| Template ID | Difficulty | Purpose | Question Pattern | Status |
|-------------|------------|---------|------------------|---------|
| `domain-agnostic_vision-language_describe_short_easy_1.md` | Easy | Short Medical Caption Selection | "Which of the following best describes this {modality} image?" | ✅ **Implemented** |
| `domain-agnostic_vision-language_describe_short_easy_2.md` | Easy | Clinical Findings Description Selection | "What are the key clinical findings visible in this {modality} image?" | ✅ **Implemented** |

### **How These Templates Work**:
- **Input**: Medical image requiring description selection
- **Question**: MCVQA format asking to select best description from multiple choice options
- **Answer**: Single correct description selected from 4-5 medically accurate options
- **Output Examples**: 
  - A. "Bilateral lower lobe pneumonia"
  - B. "Normal chest X-ray"
  - C. "Pneumothorax in left lung"
  - D. "Pleural effusion"
- **Clinical Use**: Description recognition training, caption validation, diagnostic terminology assessment

## 📋 Template Functionality

**Definition**: Select the most accurate short medical description from multiple choice options.

**Medical Applications**:
- **Description Recognition**: Test ability to identify accurate medical descriptions
- **Terminology Assessment**: Evaluate understanding of medical language and findings
- **Caption Validation**: Verify correct medical descriptions in datasets
- **Clinical Training**: Practice recognition of accurate medical terminology

**Compatible Datasets**: Medical image-caption datasets with short descriptions suitable for generating multiple choice options

**Technical Approach**: MCVQA format with single correct answer selection from medically accurate description options
