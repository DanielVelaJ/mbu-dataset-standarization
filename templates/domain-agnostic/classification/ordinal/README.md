# Domain-Agnostic Ordinal Grading Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Leaf Node**: `Ordinal grading — ordered severity or stage levels for a disease`  
**Parent Category**: Vision → Image-Level Classification  
**Repository Path**: `templates/domain-agnostic/classification/ordinal/`

## 📁 Template Inventory

### **Current Status: ✅ COMPLETE (Task 10 Implementation)**
This directory contains **3 ordinal grading templates** successfully implementing the highest priority missing template category.

### **Implemented Templates**:
| Template ID | Difficulty | Purpose | Question Pattern | Status |
|-------------|------------|---------|------------------|---------|
| `domain-agnostic_classification_ordinal_easy_1.md` | Easy | Basic Severity Assessment | "What {severity_type} is shown in this {modality} image?" | ✅ **Implemented** |
| `domain-agnostic_classification_ordinal_easy_2.md` | Easy | Stage Progression Assessment | "Which stage of {condition} is demonstrated in this {modality} image?" | ✅ **Implemented** |
| `domain-agnostic_classification_ordinal_easy_3.md` | Easy | Comparative Severity Assessment | "What level of {condition_severity} is shown in this {modality} image?" | ✅ **Implemented** |

## 📋 How These Templates Work

This directory contains domain-agnostic templates for converting ordinal grading datasets into MCVQA format. These templates work across all medical specialties for ordered severity or stage levels where order matters for interpretation.

## What is Ordinal Grading?

**Definition**: Assign one label from an ordered set where order matters for interpretation (Stage 1 < Stage 2 < Stage 3).

**Key Characteristics**:
- **Input**: One 2D medical image
- **Output**: One label from an ordered set (e.g., 0<1<2<3)
- **vs Multiclass**: Order matters - Stage 2 is inherently "between" Stage 1 and Stage 3
- **Clinical Focus**: Severity assessment with meaningful progression

## Medical Examples
- **Diabetic retinopathy grading**: Grade 0 (no DR) → Grade 4 (proliferative DR)
- **BI-RADS mammography**: Category 1 (normal) → Category 5 (highly suspicious)
- **Disease staging**: Stage I → Stage IV cancer progression
- **Liver fibrosis**: F0 (no fibrosis) → F4 (cirrhosis)

## Template Collection

### Templates (✅ Successfully Implemented)
This category was identified as one of the **highest priority missing template categories** and has been successfully implemented with 3 comprehensive templates.

**Implemented Templates**:
1. **Basic Severity Assessment** - "What {severity_type} is shown in this {modality} image?"
2. **Stage Progression Assessment** - "Which stage of {condition} is demonstrated in this {modality} image?"
3. **Comparative Severity Assessment** - "What level of {condition_severity} is shown in this {modality} image?"

## Dataset Requirements

Templates work with datasets that have:
- **Medical images** with **ordered severity/stage labels**
- **Established grading systems** (BI-RADS, diabetic retinopathy grades, etc.)
- **Clear progression** between levels (3-8 ordered categories)
- **Clinical staging systems** with meaningful order relationships

## Key Features

- **Order Preservation**: Questions respect the ordered nature of labels
- **Clinical Staging**: Use established medical grading systems
- **Cross-Domain**: Work across radiology, pathology, dermatology, ophthalmology
- **Schema Compliant**: Full alignment with unified datum schema v1.0

## Schema Integration

- **Task**: "Classification"
- **Answer Type**: "single_label" with ordered options
- **Special Consideration**: Order relationships preserved in evaluation
- **Difficulty**: Easy to Medium (based on grading complexity)

## Compatible Datasets

**High-Priority Datasets** (4 available):
- **EyePACS**: Diabetic retinopathy grading (0-4)
- **Fundus-MMBench**: Ophthalmologic severity assessment
- **BI-RADS datasets**: Mammography grading (1-5)
- **Disease staging datasets**: Various cancer staging systems

## Implementation Notes

**Advantages**:
- Maps directly to clinical severity assessment workflows
- Enables evaluation of model understanding of disease progression
- Critical for medical AI systems requiring severity-aware predictions

**Clinical Applications**:
- Disease severity assessment
- Treatment planning support
- Prognosis evaluation
- Clinical decision making

## Implementation Complete

This directory was part of **Task 10: Priority Missing Templates** and has been **successfully completed**. Ordinal grading templates were created as the highest priority missing category due to:
- 4 available datasets with ordinal structure
- Critical clinical importance for severity assessment  
- Clear medical grading systems available for reference

**Task 10 Results**: 3 comprehensive ordinal grading templates implemented with 100% MCVQA compliance.
