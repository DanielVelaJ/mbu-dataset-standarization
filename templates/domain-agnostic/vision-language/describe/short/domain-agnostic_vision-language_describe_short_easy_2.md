# Vision-Language Description Template 2: Clinical Findings Description Selection

## Template Overview

**Template ID**: `vision_language_describe_short_2`  
**Task Type**: Vision-Language Description (Clinical Findings)  
**Difficulty**: Easy  
**Question Pattern**: Clinical findings identification from multiple choice descriptions  

## Template Description

This template converts vision-language description datasets into MCVQA format by asking users to identify the key clinical findings from multiple choice description options. It focuses specifically on pathological findings and abnormalities, making it ideal for diagnostic training and clinical assessment scenarios.

The template emphasizes recognition of specific medical findings and pathological changes, supporting clinical workflows that require identification of disease-specific features and abnormalities.

## Question Generation Pattern

### Question Format
```
"What are the key clinical findings visible in this {modality} image?"
```

### Answer Format
Multiple choice options with clinical findings descriptions:
- A. {Correct clinical findings from dataset}
- B. {Alternative pathological finding 1}
- C. {Alternative pathological finding 2}
- D. {Normal/no significant findings}
- E. {Alternative pathological finding 3} (optional)

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest CT", "abdominal ultrasound", "brain MRI", "mammography")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Describe",
  "question": "What are the key clinical findings visible in this {modality} image?",
  "answer": "{selected_option_letter}",
  "answer_type": "single_label",
  "options": [
    "A. {correct_clinical_findings}",
    "B. {alternative_finding_1}", 
    "C. {alternative_finding_2}",
    "D. {normal_findings_option}",
    "E. {alternative_finding_3}"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Clinical findings identification based on pathological assessment",
  "provenance": {
    "original_findings": "{original_dataset_findings}",
    "rule_id": "vision_language_describe_short_2",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Vision-language description with clinical findings reports
- **Findings Content**: Specific pathological findings and abnormalities
- **Medical Accuracy**: Clinically accurate findings descriptions using proper terminology
- **Pathology Focus**: Emphasis on disease-specific features and diagnostic indicators

## Template Usage Rules

1. **Findings Accuracy**: Use clinically accurate findings descriptions from the dataset
2. **Pathology Specificity**: Focus on specific abnormalities rather than general impressions
3. **Terminology Precision**: Use exact medical terminology for findings and locations
4. **Distractor Relevance**: Generate alternative findings that are medically plausible for the modality
5. **Normal Option**: Include a normal/no significant findings option when appropriate

## Examples

### Example 1: Chest CT Pulmonary Findings
**Original Dataset**: Chest CT Findings Database  
**Original Findings**: "Large mass in right upper lobe with spiculated margins"  
**Generated Q&A**:
- **Question**: "What are the key clinical findings visible in this chest CT image?"
- **Options**:
  - A. Large mass in right upper lobe with spiculated margins
  - B. Multiple bilateral pulmonary nodules
  - C. Pneumothorax with pleural effusion
  - D. Normal lung parenchyma and pleura
- **Answer**: "A"
- **Rationale**: "Solid pulmonary mass with irregular spiculated borders suggestive of malignancy"

### Example 2: Brain MRI Neurological Findings
**Original Dataset**: Brain MRI Pathology Reports  
**Original Findings**: "Acute infarct in left middle cerebral artery territory"  
**Generated Q&A**:
- **Question**: "What are the key clinical findings visible in this brain MRI image?"
- **Options**:
  - A. Multiple sclerosis plaques in white matter
  - B. Acute infarct in left middle cerebral artery territory
  - C. Hemorrhagic contusion with mass effect
  - D. Normal brain parenchyma without abnormalities
- **Answer**: "B"
- **Rationale**: "Restricted diffusion consistent with acute ischemic stroke in MCA distribution"

### Example 3: Abdominal Ultrasound Hepatic Findings
**Original Dataset**: Liver Ultrasound Assessment Database  
**Original Findings**: "Hepatomegaly with increased echogenicity suggesting steatosis"  
**Generated Q&A**:
- **Question**: "What are the key clinical findings visible in this abdominal ultrasound image?"
- **Options**:
  - A. Normal liver size and echogenicity
  - B. Hepatomegaly with increased echogenicity suggesting steatosis
  - C. Multiple hypoechoic lesions throughout liver
  - D. Gallbladder wall thickening with stones
- **Answer**: "B"
- **Rationale**: "Enlarged liver with hyperechoic appearance consistent with fatty infiltration"

### Example 4: Mammography Breast Findings
**Original Dataset**: Mammography Screening Reports  
**Original Findings**: "Clustered microcalcifications in upper outer quadrant"  
**Generated Q&A**:
- **Question**: "What are the key clinical findings visible in this mammography image?"
- **Options**:
  - A. Well-circumscribed mass with benign features
  - B. Architectural distortion with skin thickening
  - C. Clustered microcalcifications in upper outer quadrant
  - D. Normal breast tissue without abnormalities
- **Answer**: "C"
- **Rationale**: "Suspicious clustered microcalcifications requiring further evaluation"

### Example 5: Knee MRI Orthopedic Findings
**Original Dataset**: Knee MRI Injury Assessment  
**Original Findings**: "Complete ACL tear with bone marrow edema"  
**Generated Q&A**:
- **Question**: "What are the key clinical findings visible in this knee MRI image?"
- **Options**:
  - A. Meniscal tear with joint effusion
  - B. Complete ACL tear with bone marrow edema
  - C. Patellar tendon rupture
  - D. Normal knee anatomy without injury
- **Answer**: "B"
- **Rationale**: "Discontinuity of anterior cruciate ligament with associated bone bruising"

## Implementation Notes

### Advantages
- **Diagnostic Focus**: Emphasizes pathological findings essential for clinical diagnosis
- **Specific Assessment**: Tests recognition of detailed clinical abnormalities
- **Medical Precision**: Requires understanding of specific medical terminology and anatomy
- **Clinical Workflow**: Mirrors real diagnostic reporting and findings documentation

### Limitations
- **Complexity Variation**: Clinical findings can vary significantly in complexity and subtlety
- **Terminology Dependency**: Requires precise medical terminology for accurate assessment
- **Context Sensitivity**: Some findings may require clinical context for accurate interpretation

### Quality Considerations
- Ensure all findings descriptions use accurate medical terminology
- Verify that clinical findings accurately reflect the pathological changes shown
- Confirm that alternative findings options are medically plausible but clearly incorrect
- Validate that findings terminology is consistent with radiological and clinical standards
- Check that complexity level is appropriate for "easy" difficulty classification
