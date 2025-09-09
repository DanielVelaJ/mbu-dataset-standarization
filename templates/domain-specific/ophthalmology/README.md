# Ophthalmology Domain-Specific Templates

This directory contains domain-specific templates for ophthalmology, designed to evaluate vision-language models on clinical tasks specific to eye care and retinal imaging. These templates complement the domain-agnostic templates by incorporating ophthalmology-specific terminology, anatomical knowledge, and clinical workflows.

## 📁 Directory Structure

```
ophthalmology/
├── classification/
│   ├── binary/
│   │   ├── ophthalmology_classification_binary_easy_1.md    # Optic disc vs cup differentiation
│   │   ├── ophthalmology_classification_binary_easy_2.md    # Pupil response assessment
│   │   └── ophthalmology_classification_binary_easy_3.md    # Anterior vs posterior segment
│   ├── multiclass/
│   │   ├── ophthalmology_classification_multiclass_easy_1.md # Anatomical structure identification
│   │   ├── ophthalmology_classification_multiclass_easy_2.md # OCT retinal pathology analysis
│   │   ├── ophthalmology_classification_multiclass_easy_3.md # Optic disc location assessment
│   │   └── ophthalmology_classification_multiclass_easy_4.md # Comparative fundus analysis
│   └── ordinal/
│       └── ophthalmology_classification_ordinal_easy_1.md   # Diabetic retinopathy grading
└── README.md
```

## 🎯 Template Overview

### Binary Classification Templates (3 templates)

1. **Optic Disc vs Cup Differentiation** - Tests understanding of critical anatomical structures for glaucoma assessment
2. **Pupil Response Assessment** - Evaluates neurological and functional aspects of pupillary responses
3. **Anterior vs Posterior Segment Identification** - Assesses basic ocular anatomy and imaging modality understanding

### Multiclass Classification Templates (4 templates)

1. **Anatomical Structure Identification** - Tests recognition of primary retinal landmarks in fundus images
2. **OCT Retinal Pathology Analysis** - Evaluates disease recognition in cross-sectional retinal imaging
3. **Optic Disc Location Assessment** - Tests spatial reasoning and anatomical orientation skills
4. **Comparative Fundus Analysis** - Assesses regional pathology comparison and severity assessment

### Ordinal Classification Templates (1 template)

1. **Diabetic Retinopathy Grading** - Tests understanding of ordered disease severity progression using standard clinical grading systems

## 🏥 Clinical Relevance

### Ophthalmology-Specific Features

- **Clinical Terminology**: Uses established ophthalmological terminology (NPDR, PDR, cup-to-disc ratio)
- **Anatomical Specificity**: Focuses on eye-specific anatomical structures (optic disc, macula, retinal vessels)
- **Disease-Specific Knowledge**: Incorporates pathologies unique to ophthalmology (diabetic retinopathy, glaucoma, macular degeneration)
- **Imaging Modalities**: Covers fundus photography, OCT, and anterior segment imaging
- **Functional Assessment**: Includes neurological aspects (pupillary responses) beyond structural abnormalities

### Real-World Applications

- **Diabetic Retinopathy Screening**: Automated grading for diabetes care programs
- **Glaucoma Assessment**: Optic nerve evaluation for early detection
- **Macular Disease Diagnosis**: OCT-based pathology identification
- **Telemedicine**: Remote ophthalmology consultations and screening
- **Medical Education**: Training tools for ophthalmology residents and students

## 📊 Dataset Compatibility

### Supported Dataset Types

| Template Category | Compatible Datasets | Example Datasets |
|-------------------|-------------------|------------------|
| **Diabetic Retinopathy** | DR grading datasets | EyePACS, APTOS 2019, DDR, Messidor |
| **Glaucoma Assessment** | Disc/cup segmentation | REFUGE, ORIGA, G1020, RIM-ONE |
| **OCT Analysis** | Retinal pathology OCT | Duke OCT, Srinivasan2014, OCT500 |
| **Fundus Analysis** | Multi-pathology fundus | Mixed ophthalmology collections |
| **Anterior Segment** | Pupil/iris imaging | Pupil position datasets |

### Imaging Modalities

- **Fundus Photography**: Color retinal photography for posterior segment assessment
- **OCT (Optical Coherence Tomography)**: Cross-sectional retinal imaging
- **Anterior Segment Photography**: Slit-lamp and anterior segment imaging
- **Wide-field Imaging**: Extended peripheral retinal visualization

## 🔬 Technical Specifications

### MCVQA Compatibility

All templates are designed for Multiple Choice Visual Question Answering:
- **Answer Format**: Multiple choice with 2-5 options
- **Single Correct Answer**: Each question has exactly one correct choice
- **Clinical Distractors**: Wrong answers are plausible medical alternatives
- **Schema Compliance**: Full alignment with unified datum schema v1.0

### Difficulty Levels

- **Easy**: Fundamental anatomical recognition and basic pathology identification
- **Medium**: (Future expansion) Complex diagnostic reasoning and comparative analysis
- **Hard**: (Future expansion) Advanced clinical decision-making and multi-factor assessment

## 📈 Evaluation Metrics

### Standard Metrics
- **Accuracy**: Overall correct classification rate
- **Precision/Recall**: Per-class performance assessment
- **F1-Score**: Balanced precision-recall evaluation
- **Confusion Matrix**: Detailed error pattern analysis

### Ophthalmology-Specific Metrics
- **Clinical Accuracy**: Agreement with expert ophthalmologist assessments
- **Grading Consistency**: Ordinal classification error analysis (for DR grading)
- **Anatomical Precision**: Spatial localization accuracy
- **Cross-Modal Performance**: Consistency across different imaging modalities

## 🎓 Educational Applications

### Medical Training
- **Ophthalmology Residency**: Systematic evaluation of anatomical and pathological knowledge
- **Continuing Education**: Assessment tools for practicing ophthalmologists
- **Board Preparation**: Standardized question formats similar to certification exams

### Research Applications
- **Model Benchmarking**: Standardized evaluation of vision-language models in ophthalmology
- **Algorithm Development**: Training and testing AI systems for clinical applications
- **Clinical Validation**: Systematic assessment of automated diagnostic tools

## 🔄 Future Expansions

### Planned Template Categories
- **Vision-Language Describe**: Fundus image captioning and report generation
- **Anatomical Landmarks**: Precise coordinate-based landmark detection
- **Segmentation Analysis**: Pixel-level structure identification
- **Temporal Analysis**: Disease progression assessment across time series

### Advanced Difficulty Levels
- **Medium Templates**: Multi-step reasoning, comparative diagnosis, uncertainty assessment
- **Hard Templates**: Complex clinical scenarios, multi-modal integration, expert-level decision making

## 📋 Usage Guidelines

### Implementation Steps
1. **Dataset Selection**: Choose ophthalmology datasets matching template requirements
2. **Template Application**: Apply appropriate templates based on dataset labels and imaging modality
3. **Quality Validation**: Review generated questions for medical accuracy
4. **Expert Review**: Consider ophthalmologist validation for clinical relevance
5. **Evaluation**: Use ophthalmology-specific metrics alongside standard measures

### Best Practices
- **Clinical Accuracy**: Ensure all medical terminology and concepts are correct
- **Expert Consultation**: Involve ophthalmologists in template validation when possible
- **Dataset Quality**: Use high-quality, clinically validated datasets
- **Ethical Considerations**: Maintain patient privacy and data security
- **Continuous Improvement**: Update templates based on clinical feedback and new knowledge

## 📚 References

### Clinical Guidelines
- American Academy of Ophthalmology Clinical Guidelines
- International Council of Ophthalmology Standards
- Diabetic Retinopathy Clinical Research Network Protocols

### Dataset Standards
- Unified MBU Medical Vision Taxonomy
- Ophthalmology-specific imaging protocols
- Clinical data annotation guidelines

---

*These templates are designed to advance the evaluation of AI systems in ophthalmology while maintaining the highest standards of clinical accuracy and educational value.*
