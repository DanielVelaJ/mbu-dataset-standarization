# Binary Classification Templates
Here we store all of the binary classification templates that we have created for converting binary classification datasets into MCVQA format.

## Summary

This directory contains **9 binary classification templates** designed to test different aspects of medical visual reasoning, from basic detection to advanced clinical decision-making. All templates work with minimal information (binary label + condition + modality) and are universally applicable to binary classification datasets.

## Template Overview

### **Easy Difficulty Templates**

#### **Template 1: Simple Presence Detection** 
- **Pattern**: "Is {finding} present in this {modality} image?"
- **Answer**: "Yes" / "No"
- **Use Case**: Direct diagnostic questions, basic presence/absence detection
- **How it works**: Straightforward binary question about condition presence

#### **Template 3: Normal vs Abnormal Assessment**
- **Pattern**: "Is this {modality} image normal or abnormal?"  
- **Answer**: "Normal" / "Abnormal"
- **Use Case**: Screening scenarios, general health assessment
- **How it works**: Binary classification between healthy and pathological states

### **Easy-Medium Difficulty Templates**

#### **Template 6: Clear Evidence Assessment**
- **Pattern**: "Is there clear evidence of {condition} in this {modality} image?"
- **Answer**: "Yes, clear evidence" / "No clear evidence"
- **Use Case**: Evidence-based diagnosis, diagnostic confidence testing
- **How it works**: Tests strength of diagnostic evidence rather than just presence

#### **Template 7: Detection Capability Assessment**
- **Pattern**: "Can {condition} be detected in this {modality} image?"
- **Answer**: "Yes, detectable" / "No, not detectable"
- **Use Case**: Computer vision capability testing, pattern recognition validation
- **How it works**: Focuses on pure visual detection ability

### **Medium Difficulty Templates**

#### **Template 2: Multiple Choice with Distractors**
- **Pattern**: "What condition is shown in this {modality} image?"
- **Answer**: A/B/C/D (target condition + 3 related distractors, or 3 distractors + "None of the above")
- **Use Case**: Differential diagnosis testing, reduces guessing
- **How it works**: Multiple choice with anatomically related medical distractors

#### **Template 4: Likelihood Assessment**
- **Pattern**: "What is the likelihood of {condition} in this {modality} image?"
- **Answer**: "Very unlikely" / "Unlikely" / "Likely" / "Very likely"
- **Use Case**: Probabilistic reasoning, diagnostic confidence in clinical terms
- **How it works**: Tests graduated probability assessment using descriptive categories

#### **Template 5: Exclusionary Assessment**
- **Pattern**: "Can {condition} be ruled out based on this {modality} image?"
- **Answer**: "Yes, can be ruled out" / "No, cannot be ruled out"
- **Use Case**: **Critical safety testing** - catches dangerous false negatives
- **How it works**: Inverted logic testing negative predictive reasoning (positive cases = "cannot be ruled out")

### **Hard Difficulty Templates**

#### **Template 8: Definition-Based Assessment**
- **Pattern**: "Which definition best describes what is shown in this {modality} image?"
- **Answer**: A/B/C/D (correct medical definition + 3 definition distractors, or 3 definitions + "None apply")
- **Use Case**: Tests medical knowledge beyond visual recognition
- **How it works**: Multiple choice using precise medical definitions to test conceptual understanding

#### **Template 9: Multi-Doctor Clinical Assessment** ⚠️ *Partial Implementation*
- **Pattern**: "Three doctors examined this image: [assessments]. Which doctor missed a finding that is definitely present?"
- **Answer**: "Doctor A" / "Doctor B" / "Doctor C" 
- **Use Case**: Complex clinical reasoning, meta-cognitive assessment
- **How it works**: Presents competing clinical opinions; tests evaluation of diagnostic accuracy
- **Status**: Positive cases complete, negative cases need refinement

## Template Selection Guide

### **By Clinical Function:**
- **Basic Detection**: Templates 1, 7 (presence, detection capability)
- **Screening**: Templates 3, 6 (normal/abnormal, clear evidence)  
- **Advanced Reasoning**: Templates 2, 4, 5 (multiple choice, likelihood, exclusion)
- **Knowledge Testing**: Template 8 (definitions)
- **Meta-Cognition**: Template 9 (clinical reasoning evaluation)

### **By Difficulty Progression:**
- **Start Simple**: Templates 1, 3 for basic binary reasoning
- **Add Complexity**: Templates 6, 7 for evidence and detection focus
- **Increase Challenge**: Templates 2, 4, 5 for differential diagnosis and probability
- **Test Expertise**: Templates 8, 9 for advanced medical knowledge and reasoning

### **By Safety Focus:**
- **False Negative Prevention**: Template 5 (exclusionary - critical for missing dangerous conditions)
- **General Safety**: Templates 1, 3, 6 (basic detection and screening)
- **Comprehensive Assessment**: Templates 2, 8, 9 (complex reasoning scenarios)

## Implementation Status
- ✅ **8 templates fully complete** and ready for deployment
- ⚠️ **1 template partially complete** (Template 9 - positive cases only)
- 📝 **Future work**: Template 9 negative case structure refinement

## Usage Notes
- All templates require only: **binary label + condition name + modality**
- All templates follow the standardized 8-section documentation structure
- All templates map perfectly to the unified datum schema v1.0
- Templates are self-contained with no cross-references for easy maintenance