# Domain-Agnostic Multi-Label Classification Templates

This directory contains domain-agnostic templates for converting multi-label classification datasets into MCVQA format. These templates work across all medical specialties and require only basic dataset information: multi-label annotations, finding/structure/criteria names, and imaging modality.

## Template Collection

### Easy Difficulty Templates

1. **domain-agnostic_classification_multilabel_easy_1.md** - Basic Finding Detection
   - **Pattern**: "Which of the following medical findings are present in this {modality} image?"
   - **Use Case**: Multiple co-occurring medical conditions or pathological findings
   - **Example**: Pneumonia + Cardiomegaly + Pleural effusion detection in chest X-rays

2. **domain-agnostic_classification_multilabel_easy_2.md** - Anatomical Structure Identification  
   - **Pattern**: "Which of the following anatomical structures are visible in this {modality} image?"
   - **Use Case**: Multiple anatomical structures visible in single image
   - **Example**: Liver + Kidney + Spleen identification in abdominal CT

3. **domain-agnostic_classification_multilabel_easy_3.md** - Clinical Assessment with Multiple Criteria
   - **Pattern**: "Which of the following {assessment_type} are present in this {modality} image?"
   - **Use Case**: Multiple clinical criteria, quality assessment, or diagnostic features
   - **Example**: ABCDE criteria assessment for skin lesions, image quality criteria

## Key Features

- **Domain-Agnostic**: Work across radiology, pathology, dermatology, ophthalmology, and other medical specialties
- **Easy Difficulty**: Designed for straightforward multi-label classification with minimal dataset requirements
- **Schema Compliant**: Full alignment with unified datum schema v1.0
- **Clinical Relevance**: Questions mirror real medical diagnostic scenarios where multiple findings coexist
- **Medical Accuracy**: All examples use correct medical terminology and established clinical standards

## Multi-Label Classification Characteristics

### What Makes These Different from Binary/Multi-Class Templates:
- **Multiple Correct Answers**: Each image can have 0, 1, or multiple correct labels simultaneously
- **Independent Labels**: Each label is assessed independently (not mutually exclusive)
- **Set-Based Answers**: Answers are sets of present findings/structures/criteria
- **Comprehensive Assessment**: Evaluates ability to detect all relevant features in a single image

### Template Applications:
- **Clinical Decision Making**: Mirrors real scenarios where multiple conditions coexist
- **Comprehensive Screening**: Systematic evaluation of multiple potential findings
- **Quality Assessment**: Multi-criteria evaluation of images or clinical features
- **Educational Training**: Teaching systematic, comprehensive image analysis

## Template Requirements

All templates require datasets with:
- **Multi-label structure**: 2+ independent binary labels per image that can co-occur
- **Clear medical labels**: Finding names, anatomical structures, or assessment criteria
- **Medical images**: Any imaging modality (X-ray, CT, MRI, photos, microscopy, etc.)
- **Independent assessability**: Each label must be evaluable independently of others

## Template Structure

Each template follows the standardized 8-section format:
1. Template Overview
2. Template Description  
3. Question Generation Pattern
4. Mapping to Datum Schema
5. Dataset Requirements
6. Template Usage Rules
7. Examples (5 concrete examples)
8. Implementation Notes

## Usage Guidelines

### Template Selection:
- **Medical findings/pathologies** → domain-agnostic_classification_multilabel_easy_1 (Basic Finding Detection)
- **Anatomical structures/organs** → domain-agnostic_classification_multilabel_easy_2 (Anatomical Structure Identification)  
- **Clinical criteria/quality assessment** → domain-agnostic_classification_multilabel_easy_3 (Clinical Assessment)

### Implementation Best Practices:
- Use "None of the above" option for negative cases (no target labels present)
- Ensure label independence (each can be true/false regardless of others)
- Randomize option order to prevent position bias
- Use established medical terminology and standards
- Include complete label set from original dataset
- Consider clinical plausibility of label combinations

## Evaluation Considerations

Multi-label classification requires specialized evaluation metrics:
- **Exact Match Accuracy**: Percentage of images where predicted set exactly matches ground truth
- **Hamming Loss**: Average proportion of incorrectly predicted labels
- **F1-Score**: Harmonic mean of precision and recall (macro/micro averaged)
- **Subset Accuracy**: Fraction of samples whose labels are predicted exactly correctly
- **Individual Label Performance**: Per-label precision, recall, and F1-scores

## Clinical Applications

These templates enable evaluation of:
- **Comprehensive Diagnosis**: Ability to detect multiple co-occurring conditions
- **Systematic Assessment**: Following clinical protocols with multiple criteria
- **Quality Control**: Multi-criteria image and clinical assessment
- **Screening Efficiency**: Detecting multiple potential issues in single examination
- **Clinical Decision Support**: Supporting complex multi-factorial medical decisions

## Dataset Compatibility

### Compatible Multi-Label Medical Datasets:
- **CheXpert**: Multiple chest pathology findings
- **MIMIC-CXR**: Multiple radiological findings with detailed labels
- **ISIC**: Multiple dermatological features and characteristics
- **Retinal datasets**: Multiple fundus pathologies and anatomical features
- **Histopathology**: Multiple tissue characteristics and cellular features

### Label Format Examples:
```json
// Binary multi-hot vector format
"labels": [1, 0, 1, 1, 0]  // findings 1, 3, 4 present

// Named label set format  
"findings": ["pneumonia", "cardiomegaly", "pleural_effusion"]

// Structured criteria format
"criteria": {
  "adequate_inspiration": true,
  "proper_positioning": false,
  "good_contrast": true
}
```

## Future Extensions

Additional multi-label templates may include:
- Severity-based multi-label assessment (mild/moderate/severe for multiple conditions)
- Temporal multi-label classification (progression assessment)
- Spatial multi-label classification (region-specific findings)
- Hierarchical multi-label classification (nested medical taxonomies)
