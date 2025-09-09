# Vision-Language Description Template 3: Long Clinical Report Selection

## Template Overview

**Template ID**: `vision_language_describe_long_1`  
**Task Type**: Vision-Language Description (Long Report)  
**Difficulty**: Easy  
**Question Pattern**: Comprehensive clinical report selection from multiple choice options  

## Template Description

This template converts vision-language description datasets into MCVQA format by asking users to select the most accurate comprehensive clinical report from multiple choice options. It is designed for datasets that contain detailed clinical reports, radiological findings, or structured medical assessments (3-6 sentences).

The template focuses on detailed medical report recognition, testing the ability to identify comprehensive clinical assessments that include findings, impressions, and clinical correlations.

## Question Generation Pattern

### Question Format
```
"Which clinical report best describes the findings in this {modality} image?"
```

### Answer Format
Multiple choice options with comprehensive clinical reports:
- A. {Correct detailed report from dataset}
- B. {Alternative detailed clinical report 1}
- C. {Alternative detailed clinical report 2}
- D. {Alternative detailed clinical report 3}

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest CT", "brain MRI", "abdominal ultrasound", "echocardiogram")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Describe",
  "question": "Which clinical report best describes the findings in this {modality} image?",
  "answer": "{selected_option_letter}",
  "answer_type": "single_label",
  "options": [
    "A. {correct_detailed_report}",
    "B. {alternative_report_1}", 
    "C. {alternative_report_2}",
    "D. {alternative_report_3}"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Comprehensive clinical report selection based on detailed medical assessment",
  "provenance": {
    "original_report": "{original_dataset_report}",
    "rule_id": "vision_language_describe_long_1",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Vision-language description with comprehensive clinical reports
- **Report Length**: Detailed descriptions (3-6 sentences, typically 50-150 words)
- **Clinical Structure**: Reports including findings, impressions, and recommendations
- **Medical Accuracy**: Clinically accurate reports using proper medical terminology and formatting

## Template Usage Rules

1. **Report Completeness**: Use comprehensive reports that include findings and clinical assessment
2. **Medical Structure**: Maintain clinical report structure with findings, impressions, and conclusions
3. **Terminology Accuracy**: Use precise medical terminology consistent with clinical documentation
4. **Distractor Quality**: Generate alternative reports that are medically coherent but clinically incorrect
5. **Length Consistency**: Ensure all options are similar in length and detail level

## Examples

### Example 1: Chest CT Comprehensive Assessment
**Original Dataset**: MIMIC-CXR Detailed Reports  
**Original Report**: "Chest CT demonstrates bilateral lower lobe consolidation with air bronchograms, consistent with pneumonia. There is associated pleural effusion on the right side. No evidence of pulmonary embolism or pneumothorax. Heart size is normal. Recommend antibiotic therapy and follow-up imaging."  
**Generated Q&A**:
- **Question**: "Which clinical report best describes the findings in this chest CT image?"
- **Options**:
  - A. Chest CT demonstrates bilateral lower lobe consolidation with air bronchograms, consistent with pneumonia. There is associated pleural effusion on the right side. No evidence of pulmonary embolism or pneumothorax. Heart size is normal. Recommend antibiotic therapy and follow-up imaging.
  - B. Chest CT shows multiple pulmonary nodules throughout both lungs, concerning for metastatic disease. Large mediastinal lymphadenopathy is present. No pleural effusion identified. Recommend oncology consultation and staging studies.
  - C. Normal chest CT examination. Lungs are clear without consolidation, nodules, or pleural effusion. Heart and mediastinal structures appear normal. No acute cardiopulmonary abnormalities identified.
  - D. Chest CT reveals large right upper lobe mass with spiculated margins, highly suspicious for primary lung malignancy. Associated hilar lymphadenopathy noted. Recommend tissue biopsy for definitive diagnosis.
- **Answer**: "A"
- **Rationale**: "Bilateral pneumonia with effusion requiring antibiotic treatment and monitoring"

### Example 2: Brain MRI Neurological Assessment
**Original Dataset**: Brain MRI Clinical Reports Database  
**Original Report**: "Brain MRI reveals multiple T2 hyperintense lesions in periventricular white matter, consistent with demyelinating disease. Lesions show characteristic ovoid morphology and perpendicular orientation to ventricular surface. No evidence of acute infarct or hemorrhage. Findings are consistent with multiple sclerosis. Recommend neurology consultation and CSF analysis."  
**Generated Q&A**:
- **Question**: "Which clinical report best describes the findings in this brain MRI image?"
- **Options**:
  - A. Normal brain MRI examination. No evidence of infarct, hemorrhage, or mass lesion. Ventricular system is normal in size and configuration. No abnormal enhancement identified after contrast administration.
  - B. Brain MRI reveals multiple T2 hyperintense lesions in periventricular white matter, consistent with demyelinating disease. Lesions show characteristic ovoid morphology and perpendicular orientation to ventricular surface. No evidence of acute infarct or hemorrhage. Findings are consistent with multiple sclerosis. Recommend neurology consultation and CSF analysis.
  - C. Brain MRI demonstrates large left middle cerebral artery territory infarct with mass effect and midline shift. Associated hemorrhagic transformation noted. Recommend neurosurgical evaluation for decompression.
  - D. Brain MRI shows enhancing mass in right frontal lobe with surrounding vasogenic edema. Appearance suggests primary brain tumor versus metastatic disease. Recommend tissue sampling and oncology consultation.
- **Answer**: "B"
- **Rationale**: "Characteristic demyelinating lesions requiring neurological evaluation and further testing"

### Example 3: Abdominal CT Comprehensive Evaluation
**Original Dataset**: Abdominal CT Emergency Reports  
**Original Report**: "Abdominal CT demonstrates acute appendicitis with appendiceal wall thickening and periappendiceal fat stranding. Small amount of free fluid in pelvis. No evidence of perforation or abscess formation. Liver, spleen, kidneys, and pancreas appear normal. Recommend urgent surgical consultation for appendectomy."  
**Generated Q&A**:
- **Question**: "Which clinical report best describes the findings in this abdominal CT image?"
- **Options**:
  - A. Normal abdominal CT examination. All organs appear normal in size, density, and enhancement pattern. No evidence of inflammatory changes, masses, or fluid collections identified.
  - B. Abdominal CT shows large liver mass with heterogeneous enhancement, concerning for hepatocellular carcinoma. Associated portal vein thrombosis noted. Recommend liver biopsy and oncology consultation.
  - C. Abdominal CT demonstrates acute appendicitis with appendiceal wall thickening and periappendiceal fat stranding. Small amount of free fluid in pelvis. No evidence of perforation or abscess formation. Liver, spleen, kidneys, and pancreas appear normal. Recommend urgent surgical consultation for appendectomy.
  - D. Abdominal CT reveals multiple kidney stones with bilateral hydronephrosis. Largest stone measures 8mm in left ureter. Associated perinephric fat stranding suggests acute obstruction. Recommend urological evaluation and stone removal.
- **Answer**: "C"
- **Rationale**: "Acute appendicitis requiring immediate surgical intervention before complications develop"

### Example 4: Cardiac MRI Comprehensive Assessment
**Original Dataset**: Cardiac MRI Function Reports  
**Original Report**: "Cardiac MRI demonstrates severely reduced left ventricular systolic function with ejection fraction of 25%. Anterior wall akinesis consistent with prior myocardial infarction. Moderate mitral regurgitation present. Right heart chambers are normal in size and function. No evidence of pericardial disease. Recommend heart failure management and cardiology follow-up."  
**Generated Q&A**:
- **Question**: "Which clinical report best describes the findings in this cardiac MRI image?"
- **Options**:
  - A. Normal cardiac MRI examination. Left and right ventricular size and systolic function are normal. No wall motion abnormalities or valvular disease identified. Ejection fraction is 60%.
  - B. Cardiac MRI shows hypertrophic cardiomyopathy with asymmetric septal hypertrophy. Left ventricular outflow tract obstruction present. Recommend genetic counseling and family screening.
  - C. Cardiac MRI demonstrates severely reduced left ventricular systolic function with ejection fraction of 25%. Anterior wall akinesis consistent with prior myocardial infarction. Moderate mitral regurgitation present. Right heart chambers are normal in size and function. No evidence of pericardial disease. Recommend heart failure management and cardiology follow-up.
  - D. Cardiac MRI reveals large pericardial effusion with hemodynamic compromise. Evidence of cardiac tamponade with ventricular septal shift. Recommend urgent pericardiocentesis and cardiac surgery consultation.
- **Answer**: "C"
- **Rationale**: "Ischemic cardiomyopathy with severe dysfunction requiring comprehensive heart failure management"

### Example 5: Mammography Comprehensive Screening Report
**Original Dataset**: Mammography Screening Database  
**Original Report**: "Bilateral mammography demonstrates heterogeneously dense breast tissue. Clustered pleomorphic microcalcifications in left upper outer quadrant spanning 15mm, BI-RADS category 4B. No associated mass or architectural distortion. Right breast shows scattered benign-appearing calcifications. Recommend stereotactic biopsy of left breast calcifications for tissue diagnosis."  
**Generated Q&A**:
- **Question**: "Which clinical report best describes the findings in this mammography image?"
- **Options**:
  - A. Normal bilateral mammography examination. Breast tissue is predominantly fatty with no masses, calcifications, or architectural distortion. BI-RADS category 1. Recommend routine annual screening.
  - B. Bilateral mammography shows large spiculated mass in right breast with associated skin thickening and nipple retraction. Appearance highly suspicious for malignancy, BI-RADS category 5. Recommend urgent tissue biopsy.
  - C. Bilateral mammography demonstrates heterogeneously dense breast tissue. Clustered pleomorphic microcalcifications in left upper outer quadrant spanning 15mm, BI-RADS category 4B. No associated mass or architectural distortion. Right breast shows scattered benign-appearing calcifications. Recommend stereotactic biopsy of left breast calcifications for tissue diagnosis.
  - D. Bilateral mammography reveals multiple bilateral masses with benign morphology. Largest mass measures 2cm in right breast. No calcifications or architectural distortion. BI-RADS category 2. Recommend routine follow-up.
- **Answer**: "C"
- **Rationale**: "Suspicious microcalcifications requiring tissue sampling for definitive diagnosis"

## Implementation Notes

### Advantages
- **Comprehensive Assessment**: Tests understanding of complete clinical reports and structured medical documentation
- **Clinical Context**: Includes findings, impressions, and recommendations mirroring real clinical practice
- **Medical Depth**: Evaluates ability to process complex medical information and clinical reasoning
- **Professional Format**: Uses standard clinical report structure and medical terminology

### Limitations
- **Length Complexity**: Longer reports may be more challenging to process and compare
- **Clinical Knowledge**: Requires deeper medical knowledge to distinguish between detailed alternatives
- **Report Generation**: May need sophisticated LLM assistance for generating plausible alternative reports

### Quality Considerations
- Ensure all report options maintain clinical accuracy and proper medical terminology
- Verify that alternative reports are medically coherent but contain different clinical scenarios
- Confirm that report structure follows standard clinical documentation practices
- Validate that medical recommendations and conclusions are clinically appropriate
- Check that report complexity is suitable for "easy" difficulty level while maintaining clinical authenticity
