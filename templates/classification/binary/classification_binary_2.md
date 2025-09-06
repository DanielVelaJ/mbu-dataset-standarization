# Binary Classification Template 2: Multiple Choice with Distractors

## Template Overview

**Template ID**: `classification_binary_2`  
**Task Type**: Binary Classification  
**Difficulty**: Medium  
**Question Pattern**: Multiple choice with one correct answer and relevant medical distractors  

## Template Description

This template converts binary classification datasets into MCVQA format by presenting the positive condition alongside plausible medical distractors in a multiple choice format. It increases task difficulty by requiring the model to distinguish between the target condition and related medical conditions from the same anatomical domain or clinical context.

## Question Generation Pattern

### Question Format
```
"What condition is shown in this {modality} image?"
```

### Answer Format
- **Multiple Choice**: A, B, C, D options
- **One Correct Answer**: The positive label when true, "None of the above" when false
- **Three Distractors**: Related medical conditions from the same domain

### Template Variables
- `{modality}`: The imaging modality (e.g., "chest X-ray", "fundus", "skin", "CT", "MRI")
- `{positive_condition}`: The target medical condition from the original dataset
- `{distractor_1}`, `{distractor_2}`, `{distractor_3}`: Related medical conditions

### Option Generation Rules

#### For Positive Cases (Original Label = 1):
```
A: {positive_condition}
B: {distractor_1}
C: {distractor_2}  
D: {distractor_3}
```
**Correct Answer**: "A"

#### For Negative Cases (Original Label = 0):
```
A: {distractor_1}
B: {distractor_2}
C: {distractor_3}
D: None of the above
```
**Correct Answer**: "D"

## Mapping to Datum Schema

This template generates question-answer pairs that map to the datum schema as follows:

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What condition is shown in this {modality} image?",
  "answer": "A" | "B" | "C" | "D",
  "answer_type": "single_label",
  "options": ["Option A text", "Option B text", "Option C text", "Option D text"],
  "difficulty": "medium",
  "uncertainty": "certain",
  "answer_confidence": 1.0,
  "rationale": "Multiple choice binary classification with medical distractors",
  "provenance": {
    "original_label": "{original_label_value}",
    "rule_id": "classification_binary_2",
    "created_by": "program"
  }
}
```

## Dataset Requirements

This template is suitable for datasets that have:
- **Task Type**: Binary classification (Vision → Image-Level Classification → Binary classification)
- **Label Structure**: Single binary label per image (0/1, positive/negative)
- **Domain Knowledge**: Well-defined medical conditions with known related conditions
- **Image Level**: Whole image classification

## Distractor Generation Strategy

### Principle: Clinical Plausibility
Distractors should be:
1. **Anatomically Related**: Conditions affecting the same organ/body part
2. **Visually Similar**: Conditions that might appear similar on the same imaging modality
3. **Clinically Relevant**: Real medical conditions, not nonsensical options
4. **Diagnostically Challenging**: Conditions that require expertise to differentiate

### Domain-Specific Distractor Categories

#### Chest X-ray (Respiratory/Cardiac)
- **For Pneumonia**: Pulmonary edema, Pleural effusion, Atelectasis
- **For Cardiomegaly**: Normal heart, Pericardial effusion, Pulmonary edema
- **For Pneumothorax**: Pleural effusion, Emphysema, Normal lung

#### Fundus (Ophthalmology)
- **For Diabetic Retinopathy**: Glaucoma, Age-related macular degeneration, Hypertensive retinopathy
- **For Glaucoma**: Diabetic retinopathy, Normal fundus, Papilledema

#### Skin (Dermatology)
- **For Melanoma**: Basal cell carcinoma, Seborrheic keratosis, Benign nevus
- **For Basal Cell Carcinoma**: Squamous cell carcinoma, Melanoma, Actinic keratosis

#### Brain MRI (Neurology)
- **For Brain Tumor**: Stroke, Multiple sclerosis lesion, Normal brain
- **For Stroke**: Brain tumor, Hemorrhage, Normal brain

## Template Usage Rules

1. **Condition Names**: Use precise medical terminology from established classifications
2. **Distractor Selection**: Choose conditions from the same anatomical domain
3. **Option Randomization**: Randomize the position of the correct answer (A, B, C, or D)
4. **"None of the Above"**: Always use for negative cases to maintain binary nature
5. **Consistency**: Maintain consistent difficulty level across distractors

## Examples

### Example 1: Chest X-ray Pneumonia Detection
**Original Dataset**: ChestX-ray14 Pneumonia subset  
**Original Label**: 1 (positive for pneumonia)  
**Generated Q&A**:
- **Question**: "What condition is shown in this chest X-ray image?"
- **Options**:
  - A: Pneumonia
  - B: Pulmonary edema
  - C: Pleural effusion
  - D: Atelectasis
- **Answer**: "A"
- **Rationale**: "Multiple choice question with respiratory conditions as distractors"

### Example 2: Fundus Diabetic Retinopathy Screening
**Original Dataset**: Diabetic Retinopathy Detection  
**Original Label**: 0 (no diabetic retinopathy)  
**Generated Q&A**:
- **Question**: "What condition is shown in this fundus image?"
- **Options**:
  - A: Glaucoma
  - B: Age-related macular degeneration
  - C: Hypertensive retinopathy
  - D: None of the above
- **Answer**: "D"
- **Rationale**: "Normal fundus with ophthalmologic conditions as distractors"

### Example 3: Skin Lesion Melanoma Detection
**Original Dataset**: ISIC Melanoma Classification  
**Original Label**: 1 (malignant melanoma)  
**Generated Q&A**:
- **Question**: "What condition is shown in this skin image?"
- **Options**:
  - A: Basal cell carcinoma
  - B: Melanoma
  - C: Seborrheic keratosis
  - D: Benign nevus
- **Answer**: "B"
- **Rationale**: "Melanoma identification with dermatologic conditions as distractors"

### Example 4: Brain MRI Tumor Detection
**Original Dataset**: Brain Tumor Classification  
**Original Label**: 0 (no tumor)  
**Generated Q&A**:
- **Question**: "What condition is shown in this brain MRI image?"
- **Options**:
  - A: Glioblastoma
  - B: Meningioma
  - C: Metastatic lesion
  - D: None of the above
- **Answer**: "D"
- **Rationale**: "Normal brain with neurologic tumor types as distractors"

### Example 5: Chest CT Pulmonary Nodule Detection
**Original Dataset**: LUNA16 Nodule Detection  
**Original Label**: 1 (nodule present)  
**Generated Q&A**:
- **Question**: "What condition is shown in this chest CT image?"
- **Options**:
  - A: Pulmonary nodule
  - B: Pulmonary embolism
  - C: Pneumonia
  - D: Pleural thickening
- **Answer**: "A"
- **Rationale**: "Pulmonary nodule identification with thoracic conditions as distractors"

## Implementation Notes

### Advantages
- **Increased Difficulty**: Tests model's ability to discriminate between similar conditions
- **Clinical Realism**: Mimics real diagnostic decision-making with differential diagnosis
- **Reduced Guessing**: Four options reduce random success rate to 25%
- **Educational Value**: Provides learning opportunities about related conditions

### Limitations
- **Distractor Dependency**: Requires domain knowledge to generate appropriate distractors
- **Complexity**: More complex to implement than simple yes/no questions
- **Answer Length**: Longer options may introduce text bias
- **Negative Cases**: "None of the above" option may be easier to identify

### Quality Considerations
- **Medical Accuracy**: All options must be real, properly named medical conditions
- **Difficulty Balance**: Distractors should be plausible but distinguishable
- **Domain Consistency**: All options should be from the same medical domain
- **Terminology**: Use standard medical terminology and ICD/SNOMED codes when possible

### Distractor Generation Methods

#### Manual Curation (Recommended)
- Medical expert creates condition lists for each domain
- Ensures clinical accuracy and appropriate difficulty
- Requires domain expertise but provides highest quality

#### Automated Generation (Future)
- Use medical ontologies (SNOMED-CT, ICD-11) for related conditions
- Language model generation with medical knowledge
- Requires validation by medical experts

#### Hybrid Approach
- Pre-defined condition pools for each anatomical domain
- Automated selection with manual validation
- Balances efficiency with quality control

