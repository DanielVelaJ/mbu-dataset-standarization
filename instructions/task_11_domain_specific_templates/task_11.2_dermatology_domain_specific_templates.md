# Task 11.2: Dermatology Domain-Specific Templates

## Task Requirements
Read the task 11 general guidelines. 
Then please suggest to me the templates that you would create and the reasoning behind them. Remember to mention what leaf node from our taxonomy you would be using for each template.

Focus on dermatology-specific clinical workflows, terminology, and diagnostic scenarios involving skin imaging, lesion analysis, and dermatological conditions. Consider dermoscopy images, clinical photography, and dermatopathology applications.

## Progress and Decisions Made

### ✅ **Phase 1: Context Analysis and Dataset Review (Completed)**

**Actions Taken:**
- Analyzed all context files and general guidelines for domain-specific template requirements [[memory:8462374]]
- Reviewed 135 dermatology datasets from our metadata collection
- Studied dermatology-specific clinical workflows and diagnostic patterns
- Examined the MBU medical vision taxonomy for appropriate leaf nodes

**Key Findings:**
- **135 dermatology datasets** available with strong classification focus
- **Primary task distribution**: Multiclass classification (73), Binary classification (26), Semantic segmentation (18), Vision-Language tasks (9)
- **Common conditions**: Skin cancer, melanoma, dermatitis, pigmented lesions, inflammatory conditions
- **Imaging modalities**: Dermoscopy, clinical photography, dermatopathology microscopy
- **Clinical workflows**: Lesion assessment, cancer screening, severity grading, differential diagnosis

### ✅ **Phase 2: Template Strategy Development (Completed)**

**Design Decisions:**
1. **MCVQA Compatibility**: All templates must work for Multiple Choice Visual Question Answering format
2. **Dermatological Terminology**: Use established dermatological terms (ABCDE criteria, Fitzpatrick scale, morphological descriptors)
3. **Lesion-Specific Focus**: Emphasize lesion characteristics, patterns, and diagnostic features
4. **Clinical Relevance**: Reflect real dermatological diagnostic workflows and examination procedures
5. **Multi-Modal Coverage**: Support dermoscopy, clinical photography, and histopathological imaging

### ✅ **Phase 3: Template Suggestions and Reasoning (Completed)**

**8 Templates Proposed** across multiple taxonomy leaf nodes:

#### **Binary Classification Templates (3)**

**1. Malignant vs Benign Lesion Assessment**
- **Taxonomy Node**: `classification/binary/`
- **Pattern**: "Based on the dermatological features visible, is this lesion malignant or benign?"
- **Answer Options**: Malignant, Benign
- **Clinical Value**: Core cancer screening decision fundamental to dermatological practice
- **Available Datasets**: 26+ binary classification datasets focusing on malignancy detection
- **Dermatology-Specific Features**: Leverages ABCDE criteria (Asymmetry, Border, Color, Diameter, Evolution)

**2. Inflammatory vs Non-Inflammatory Condition**
- **Taxonomy Node**: `classification/binary/`
- **Pattern**: "Does this skin condition show inflammatory characteristics?"
- **Answer Options**: Inflammatory, Non-inflammatory
- **Clinical Value**: Critical for treatment selection (anti-inflammatory vs other approaches)
- **Available Datasets**: Multiple datasets with inflammatory conditions like dermatitis, psoriasis
- **Dermatology-Specific Features**: Tests understanding of inflammatory markers (erythema, scaling, papules)

**3. Pigmented vs Non-Pigmented Lesion Classification**
- **Taxonomy Node**: `classification/binary/`
- **Pattern**: "Is this lesion primarily pigmented or non-pigmented?"
- **Answer Options**: Pigmented, Non-pigmented
- **Clinical Value**: Fundamental morphological distinction affecting diagnostic approach
- **Available Datasets**: Diverse lesion datasets with varying pigmentation patterns
- **Dermatology-Specific Features**: Tests melanin recognition and pigment pattern analysis

#### **Multiclass Classification Templates (4)**

**4. Skin Cancer Type Classification**
- **Taxonomy Node**: `classification/multiclass/`
- **Pattern**: "What type of skin cancer is most consistent with the features shown?"
- **Answer Options**: Melanoma, Basal cell carcinoma, Squamous cell carcinoma, Actinic keratosis, Not cancer
- **Clinical Value**: Specific cancer type identification for treatment planning
- **Available Datasets**: 73+ multiclass datasets with cancer classifications
- **Dermatology-Specific Features**: Uses established oncological classification systems

**5. Dermoscopic Pattern Recognition**
- **Taxonomy Node**: `classification/multiclass/`
- **Pattern**: "What is the primary dermoscopic pattern visible in this lesion?"
- **Answer Options**: Reticular pattern, Globular pattern, Homogeneous pattern, Starburst pattern, Multicomponent pattern
- **Clinical Value**: Dermoscopy-specific pattern recognition essential for lesion evaluation
- **Available Datasets**: Dermoscopy-focused datasets with pattern annotations
- **Dermatology-Specific Features**: Leverages specialized dermoscopic terminology and visual patterns

**6. Skin Condition Category Assessment**
- **Taxonomy Node**: `classification/multiclass/`
- **Pattern**: "Which dermatological condition category best describes this presentation?"
- **Answer Options**: Eczematous dermatitis, Papulosquamous disorder, Vesiculobullous disease, Infectious condition, Neoplastic lesion
- **Clinical Value**: High-level diagnostic categorization for differential diagnosis
- **Available Datasets**: Comprehensive skin disease datasets
- **Dermatology-Specific Features**: Uses morphological classification system familiar to dermatologists

**7. Anatomical Location-Specific Diagnosis**
- **Taxonomy Node**: `classification/multiclass/`
- **Pattern**: "Given the anatomical location and features, what is the most likely diagnosis?"
- **Answer Options**: Seborrheic keratosis, Solar lentigo, Melanocytic nevus, Dermatofibroma, Sebaceous hyperplasia
- **Clinical Value**: Incorporates anatomical context into diagnostic reasoning
- **Available Datasets**: Location-annotated dermatological datasets
- **Dermatology-Specific Features**: Tests location-specific disease prevalence knowledge

#### **Ordinal Classification Template (1)**

**8. Fitzpatrick Skin Type Assessment**
- **Taxonomy Node**: `classification/ordinal/`
- **Pattern**: "What Fitzpatrick skin type is shown in this image?"
- **Answer Options**: Type I (Always burns, never tans), Type II (Usually burns, tans minimally), Type III (Sometimes burns, tans gradually), Type IV (Burns minimally, tans well), Type V (Rarely burns, tans darkly), Type VI (Never burns, deeply pigmented)
- **Clinical Value**: Critical for phototherapy dosing, laser treatment planning, and skin cancer risk assessment
- **Available Datasets**: 1 ordinal grading dataset available, can leverage other datasets with skin tone information
- **Dermatology-Specific Features**: Uses established dermatological classification system with ordered progression

## Key Design Rationale

### **Dermatological Relevance Priority**
Each template addresses real dermatological diagnostic scenarios:
- **Cancer screening** is the highest-impact application of dermatological AI
- **Pattern recognition** reflects how dermatologists actually examine lesions
- **Morphological classification** mirrors clinical diagnostic processes
- **Skin type assessment** affects treatment decisions across dermatology

### **Dermatology-Specific Features**
- **Specialized terminology** (ABCDE criteria, dermoscopic patterns, Fitzpatrick scale)
- **Lesion-focused analysis** (pigmentation, borders, symmetry, patterns)
- **Clinical context integration** (anatomical location, inflammatory markers)
- **Morphological precision** (papulosquamous, vesiculobullous, etc.)
- **Multi-modal imaging expertise** (dermoscopy, clinical photography, histopathology)

### **Dataset Availability Alignment**
Templates align with available dermatology datasets:
- **Strong classification support**: 99 classification datasets (73 multiclass + 26 binary + 1 ordinal)
- **Segmentation support**: 18 semantic segmentation datasets for lesion boundary tasks
- **Vision-language potential**: 9 vision-language datasets for descriptive tasks
- **Quality assurance**: 50% medical professional annotation rate provides clinical accuracy

### **Clinical Workflow Integration**
Templates reflect real dermatological examination procedures:
- **Screening protocols**: Malignancy assessment mirrors skin cancer screening
- **Diagnostic workflows**: Pattern recognition reflects dermoscopic examination
- **Treatment planning**: Skin type assessment affects therapeutic decisions
- **Differential diagnosis**: Morphological classification supports diagnostic reasoning

This template collection provides comprehensive coverage of core dermatological diagnostic scenarios while maintaining MCVQA compatibility and leveraging domain-specific clinical knowledge.
