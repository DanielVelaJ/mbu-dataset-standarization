# Task 11.3: Radiology Domain-Specific Templates

## Task Requirements
Read the task 11 general guidelines. 
Then please suggest to me the templates that you would create and the reasoning behind them. Remember to mention what leaf node from our taxonomy you would be using for each template.

Focus on radiology-specific clinical workflows, terminology, and diagnostic scenarios involving medical imaging modalities such as X-ray, CT, MRI, ultrasound, and nuclear medicine. Consider interpretation patterns, anatomical localization, and radiological findings.

## Progress and Decisions Made

### ✅ **Phase 1: Context Analysis and Dataset Review (Completed)**

**Actions Taken:**
- Analyzed all context files and general guidelines for domain-specific template requirements [[memory:8462374]]
- Reviewed 518 radiology datasets from our metadata collection (largest domain)
- Studied radiology-specific clinical workflows and imaging interpretation patterns
- Examined the MBU medical vision taxonomy for appropriate leaf nodes

**Key Findings:**
- **518 radiology datasets** available - the largest domain in our collection
- **Primary task distribution**: Multiclass classification (118), Semantic segmentation (112), Binary classification (94), Lesion detection (28), Vision-Language (70)
- **Common modalities**: Chest X-ray, CT, MRI, ultrasound, mammography
- **Clinical applications**: Disease detection, anatomical segmentation, report generation, abnormality localization
- **Quality indicators**: 57.4% medical professional annotation rate, 25.9% external validation

### ✅ **Phase 2: Template Strategy Development (Completed)**

**Design Decisions:**
1. **MCVQA Compatibility**: All templates must work for Multiple Choice Visual Question Answering format
2. **Radiological Terminology**: Use established radiological terms (BIRADS, Hounsfield units, anatomical orientations)
3. **Modality-Specific Focus**: Address unique characteristics of different imaging modalities
4. **Clinical Relevance**: Reflect real radiological interpretation workflows and reporting standards
5. **Multi-Modality Coverage**: Support X-ray, CT, MRI, ultrasound across different body systems

### ✅ **Phase 3: Template Suggestions and Reasoning (Completed)**

**8 Templates Proposed** across multiple taxonomy leaf nodes:

#### **Binary Classification Templates (3)**

**1. Pneumonia Detection in Chest X-rays**
- **Taxonomy Node**: `classification/binary/`
- **Pattern**: "Does this chest X-ray show evidence of pneumonia?"
- **Answer Options**: Pneumonia present, No pneumonia
- **Clinical Value**: Critical for emergency department triage and antibiotic decision-making
- **Available Datasets**: 94+ binary classification datasets, many focused on chest pathology
- **Radiology-Specific Features**: Leverages classic radiological signs (consolidation, air bronchograms, pleural effusion)

**2. Fracture Detection Assessment**
- **Taxonomy Node**: `classification/binary/`
- **Pattern**: "Is there evidence of a fracture in this radiographic image?"
- **Answer Options**: Fracture present, No fracture
- **Clinical Value**: Essential for orthopedic and emergency medicine decision-making
- **Available Datasets**: Multiple skeletal/orthopedic datasets with fracture annotations
- **Radiology-Specific Features**: Tests understanding of cortical disruption, alignment, and bone anatomy

**3. Intracranial Hemorrhage Detection**
- **Taxonomy Node**: `classification/binary/`
- **Pattern**: "Does this CT scan show evidence of intracranial hemorrhage?"
- **Answer Options**: Hemorrhage present, No hemorrhage
- **Clinical Value**: Critical for stroke management and neurosurgical intervention decisions
- **Available Datasets**: Brain CT datasets with hemorrhage annotations
- **Radiology-Specific Features**: Recognizes hyperdense areas, mass effect, and hemorrhage patterns

#### **Multiclass Classification Templates (3)**

**4. Chest X-ray View Classification**
- **Taxonomy Node**: `classification/multiclass/`
- **Pattern**: "What radiographic view is shown in this chest X-ray?"
- **Answer Options**: Posteroanterior (PA), Anteroposterior (AP), Lateral, Decubitus, Lordotic
- **Clinical Value**: Essential for proper image interpretation and comparison with prior studies
- **Available Datasets**: 118+ multiclass datasets with view annotations
- **Radiology-Specific Features**: Tests understanding of radiographic positioning and anatomical appearance differences

**5. Brain MRI Sequence Identification**
- **Taxonomy Node**: `classification/multiclass/`
- **Pattern**: "What MRI sequence is most likely shown in this brain image?"
- **Answer Options**: T1-weighted, T2-weighted, FLAIR, DWI, T1 post-contrast
- **Clinical Value**: Critical for proper image interpretation and lesion characterization
- **Available Datasets**: MRI datasets with sequence information
- **Radiology-Specific Features**: Leverages tissue contrast characteristics specific to different sequences

**6. Abdominal CT Phase Classification**
- **Taxonomy Node**: `classification/multiclass/`
- **Pattern**: "What contrast phase is shown in this abdominal CT?"
- **Answer Options**: Non-contrast, Arterial phase, Portal venous phase, Delayed phase, Equilibrium phase
- **Clinical Value**: Essential for lesion characterization and vascular assessment
- **Available Datasets**: Abdominal CT datasets with phase annotations
- **Radiology-Specific Features**: Tests understanding of contrast kinetics and enhancement patterns

#### **Multilabel Classification Template (1)**

**7. Chest X-ray Multiple Findings Assessment**
- **Taxonomy Node**: `classification/multilabel/`
- **Pattern**: "Which of the following findings are present in this chest X-ray? (Select all that apply)"
- **Answer Options**: Atelectasis, Cardiomegaly, Effusion, Infiltrate, Mass, Nodule, Pneumonia, Pneumothorax, Consolidation, Edema, Emphysema, Fibrosis, Pleural_Thickening, Hernia
- **Clinical Value**: Reflects real-world scenario where multiple pathologies can coexist
- **Available Datasets**: 23+ multilabel classification datasets, particularly strong for chest imaging
- **Radiology-Specific Features**: Uses standardized radiological terminology from datasets like CheXpert

#### **Vision-Language Template (1)**

**8. Radiological Finding Description**
- **Taxonomy Node**: `vision-language/describe/short/`
- **Pattern**: "Provide a concise radiological description of the primary finding in this image."
- **Answer Type**: Short medical caption generation
- **Clinical Value**: Tests ability to generate structured radiology reports and describe findings
- **Available Datasets**: 24+ short caption generation datasets plus 12 long report datasets
- **Radiology-Specific Features**: Uses standard radiological reporting terminology and structured format

## Key Design Rationale

### **Radiological Relevance Priority**
Each template addresses core radiological workflows:
- **Emergency imaging**: Pneumonia and hemorrhage detection for acute care decisions
- **Trauma assessment**: Fracture detection for orthopedic management
- **Technical proficiency**: View and sequence identification for proper interpretation
- **Multi-finding analysis**: Reflects complex real-world imaging scenarios
- **Report generation**: Tests structured radiological communication skills

### **Radiology-Specific Features**
- **Modality expertise** (X-ray positioning, CT phases, MRI sequences)
- **Anatomical precision** (specific radiological anatomy and orientations)
- **Pathological knowledge** (disease patterns, enhancement characteristics)
- **Technical understanding** (contrast phases, imaging parameters)
- **Clinical integration** (emergency vs elective, intervention triggers)

### **Dataset Availability Alignment**
Templates leverage the extensive radiology dataset collection:
- **Strong classification support**: 305 classification datasets (118 multiclass + 94 binary + 23 multilabel + 70 other)
- **Segmentation potential**: 112 semantic segmentation datasets for anatomical structure tasks
- **Vision-language strength**: 70 vision-language datasets for report generation and QA
- **Quality assurance**: 57.4% medical professional annotation provides clinical accuracy
- **External validation**: 25.9% datasets have external validation, highest among domains

### **Clinical Workflow Integration**
Templates reflect actual radiological practice:
- **Interpretation workflow**: View identification precedes diagnostic interpretation
- **Emergency protocols**: Critical findings (hemorrhage, pneumonia) require immediate recognition
- **Reporting standards**: Description template mirrors structured reporting requirements
- **Multi-pathology awareness**: Multilabel classification reflects complex cases

### **Cross-Modality Coverage**
Templates span major radiological modalities:
- **X-ray**: Chest imaging, fracture detection, view classification
- **CT**: Hemorrhage detection, contrast phase identification
- **MRI**: Sequence identification and tissue characterization
- **Multi-modal**: Generic finding description applicable across modalities

This template collection provides comprehensive coverage of essential radiological skills while maintaining MCVQA compatibility and leveraging the largest dataset collection in our metadata.
