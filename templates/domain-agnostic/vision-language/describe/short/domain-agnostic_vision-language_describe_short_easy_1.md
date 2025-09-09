# Vision-Language Description Template 1: Short Medical Caption Selection

## Template Overview

**Template ID**: `vision_language_describe_short_1`  
**Task Type**: Vision-Language Description (Short Caption)  
**Difficulty**: Easy  
**Question Pattern**: Medical image description selection from multiple choice options  

## Template Description

This template converts vision-language description datasets into MCVQA format by asking users to select the most accurate short medical description from multiple choice options. It is designed for datasets that pair medical images with brief, clinically relevant captions or descriptions (1-2 sentences).

The template focuses on concise medical description recognition, testing the ability to identify accurate medical terminology and findings in short-form clinical language.

## Question Generation Pattern

### Question Format
```
"Which of the following best describes this {modality} image?"
```

### Answer Format
Multiple choice options with medical descriptions:
- A. {Correct medical description from dataset}
- B. {Plausible medical distractor 1}
- C. {Plausible medical distractor 2}
- D. {Plausible medical distractor 3}
- E. {Plausible medical distractor 4} (optional)

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus", "CT", "MRI", "ultrasound")

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Describe",
  "question": "Which of the following best describes this {modality} image?",
  "answer": "{selected_option_letter}",
  "answer_type": "single_label",
  "options": [
    "A. {correct_description_from_dataset}",
    "B. {plausible_distractor_1}", 
    "C. {plausible_distractor_2}",
    "D. {plausible_distractor_3}",
    "E. {plausible_distractor_4}"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Short medical description selection based on visual findings",
  "provenance": {
    "original_caption": "{original_dataset_caption}",
    "rule_id": "vision_language_describe_short_1",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Vision-language description with short medical captions
- **Caption Length**: Brief descriptions (1-2 sentences, typically 5-20 words)
- **Medical Accuracy**: Clinically accurate descriptions using proper medical terminology
- **Diverse Content**: Varied medical findings and normal cases for distractor generation

## Template Usage Rules

1. **Correct Option**: Use the exact or paraphrased caption from the dataset as the correct answer
2. **Distractor Quality**: Generate medically plausible but incorrect alternatives
3. **Medical Terminology**: Maintain clinical accuracy in all options
4. **Length Consistency**: Keep all options similar in length and detail level
5. **Avoiding Clues**: Ensure no grammatical or stylistic clues reveal the correct answer

## Examples

### Example 1: Chest X-ray Normal Finding
**Original Dataset**: MIMIC-CXR Short Captions  
**Original Caption**: "Normal chest X-ray with clear lungs"  
**Generated Q&A**:
- **Question**: "Which of the following best describes this chest X-ray image?"
- **Options**:
  - A. Normal chest X-ray with clear lungs
  - B. Bilateral lower lobe pneumonia
  - C. Pneumothorax in the left lung
  - D. Cardiomegaly with pulmonary edema
- **Answer**: "A"
- **Rationale**: "Clear lung fields without pathological findings on chest radiograph"

### Example 2: Fundus Diabetic Retinopathy
**Original Dataset**: Diabetic Retinopathy Captions  
**Original Caption**: "Moderate diabetic retinopathy with microaneurysms"  
**Generated Q&A**:
- **Question**: "Which of the following best describes this fundus image?"
- **Options**:
  - A. Normal retinal examination
  - B. Moderate diabetic retinopathy with microaneurysms
  - C. Age-related macular degeneration
  - D. Hypertensive retinopathy changes
- **Answer**: "B"
- **Rationale**: "Characteristic diabetic retinal changes with vascular microaneurysms present"

### Example 3: Skin Lesion Assessment
**Original Dataset**: Dermatology Image Captions  
**Original Caption**: "Irregular pigmented lesion suggestive of melanoma"  
**Generated Q&A**:
- **Question**: "Which of the following best describes this skin image?"
- **Options**:
  - A. Benign seborrheic keratosis
  - B. Irregular pigmented lesion suggestive of melanoma
  - C. Common benign nevus
  - D. Basal cell carcinoma
- **Answer**: "B"
- **Rationale**: "Asymmetric pigmented lesion with irregular borders characteristic of melanoma"

### Example 4: Brain MRI Findings
**Original Dataset**: Brain MRI Caption Database  
**Original Caption**: "Multiple white matter lesions consistent with MS"  
**Generated Q&A**:
- **Question**: "Which of the following best describes this brain MRI image?"
- **Options**:
  - A. Normal brain MRI appearance
  - B. Acute stroke with infarction
  - C. Multiple white matter lesions consistent with MS
  - D. Brain tumor with mass effect
- **Answer**: "C"
- **Rationale**: "Characteristic demyelinating lesions in white matter typical of multiple sclerosis"

### Example 5: Abdominal CT Assessment
**Original Dataset**: Abdominal CT Caption Collection  
**Original Caption**: "Liver cirrhosis with ascites and splenomegaly"  
**Generated Q&A**:
- **Question**: "Which of the following best describes this abdominal CT image?"
- **Options**:
  - A. Normal abdominal CT scan
  - B. Acute appendicitis with inflammation
  - C. Liver cirrhosis with ascites and splenomegaly
  - D. Kidney stones with hydronephrosis
- **Answer**: "C"
- **Rationale**: "End-stage liver disease with portal hypertension and fluid accumulation"

## Implementation Notes

### Advantages
- **Clinical Relevance**: Tests ability to recognize accurate medical descriptions
- **Terminology Assessment**: Evaluates understanding of medical language and findings
- **Concise Evaluation**: Focuses on essential diagnostic information in brief format
- **Broad Applicability**: Works across medical specialties and imaging modalities

### Limitations
- **Caption Dependency**: Requires high-quality, accurate captions in source dataset
- **Distractor Generation**: May need LLM assistance for generating plausible medical distractors
- **Length Constraints**: Limited to short descriptions, may miss complex findings

### Quality Considerations
- Ensure all description options use appropriate medical terminology
- Verify that distractors are medically plausible but clearly incorrect
- Confirm that correct descriptions accurately reflect the medical findings
- Validate that medical terminology is consistent with clinical standards
- Check that description complexity matches the "easy" difficulty level
