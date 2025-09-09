# Long Clinical Report Generation Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Leaf Node**: `Long clinical report generation — paragraph style`  
**Parent Category**: Vision–Language → Describe  
**Repository Path**: `templates/domain-agnostic/vision-language/describe/long/`

## 📁 Template Inventory

### **Current Status: ✅ COMPLETE (Task 10 Implementation)**

| Template ID | Difficulty | Purpose | Question Pattern | Status |
|-------------|------------|---------|------------------|---------|
| `domain-agnostic_vision-language_describe_long_easy_1.md` | Easy | Comprehensive Clinical Report Selection | "Which clinical report best describes the findings in this {modality} image?" | ✅ **Implemented** |

### **How This Template Works**:
- **Input**: Medical image requiring comprehensive clinical report selection
- **Question**: MCVQA format asking to select best comprehensive report from multiple choice options
- **Answer**: Single correct detailed clinical report selected from 4 comprehensive options
- **Output Examples**: 
  - A. "Chest CT demonstrates bilateral lower lobe consolidation with air bronchograms, consistent with pneumonia. There is associated pleural effusion on the right side. No evidence of pulmonary embolism or pneumothorax. Heart size is normal. Recommend antibiotic therapy and follow-up imaging."
  - B. Alternative comprehensive clinical report
  - C. Alternative comprehensive clinical report
  - D. Alternative comprehensive clinical report
- **Clinical Use**: Report recognition training, clinical documentation validation, comprehensive medical assessment evaluation

## 📋 Template Functionality

**Definition**: Select the most accurate comprehensive clinical report from multiple choice options.

**Medical Applications**:
- **Report Recognition**: Test ability to identify accurate comprehensive clinical reports
- **Clinical Assessment**: Evaluate understanding of structured medical documentation
- **Documentation Validation**: Verify correct clinical report formats and content
- **Medical Training**: Practice recognition of comprehensive clinical assessment patterns

**Compatible Datasets**: MIMIC chest X-ray reports and other detailed medical image-report datasets

**Technical Approach**: MCVQA format with single correct answer selection from comprehensive clinical report options
