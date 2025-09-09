# Vision-Language Describe Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Sub-Category**: `Describe`  
**Parent Category**: Vision–Language  
**Repository Path**: `templates/domain-agnostic/vision-language/describe/`

## 📁 Template Inventory

### **Current Status: ❌ MISSING (Highest Priority)**

| Subdirectory | Leaf Node | Planned Templates | Dataset Availability | Status |
|--------------|-----------|-------------------|---------------------|---------|
| `short/` | Short medical caption generation — one to two sentence description | 1-2 easy templates | 🟢 **5+ datasets** | 📝 **Highest Priority (Task 10)** |
| `long/` | Long clinical report generation — paragraph style | 1-2 easy templates | 🟢 **5+ datasets** | 📝 **Highest Priority (Task 10)** |

### **Planned Template Functionality**:

#### **Short Medical Caption Generation** (`short/`)
- **Question Pattern**: "Provide a brief medical description of this {modality} image."
- **Answer Format**: 1-2 sentence free text description
- **Example Output**: "Bilateral lower lobe pneumonia in chest X-ray" or "Irregular pigmented lesion on arm"
- **Clinical Use**: Quick image summaries, clinical documentation, case presentations

#### **Long Clinical Report Generation** (`long/`)
- **Question Pattern**: "Generate a comprehensive clinical report for this {modality} image."
- **Answer Format**: Paragraph-style structured clinical report
- **Example Output**: Multi-paragraph radiology report with findings, impressions, recommendations
- **Clinical Use**: Full clinical documentation, detailed medical reporting, comprehensive analysis

## 📋 Sub-Category Details

### 1. **Short Medical Caption Generation** (`short/`)
- **Definition**: Generate a short descriptive sentence from the image
- **Input**: Medical image
- **Output**: Short text string (1-2 sentences)
- **Recognition**: "Image-caption pairs", short captions (<3 sentences)
- **Medical Examples**: 
  - Dermoscopy: "Irregular pigmented lesion on arm"
  - Chest X-ray: "Normal chest radiograph"
  - CT scan: "Large mass in right upper lobe"

### 2. **Long Clinical Report Generation** (`long/`)
- **Definition**: Generate a long structured or unstructured clinical report
- **Input**: Medical image
- **Output**: Long text (paragraphs)
- **Recognition**: "Image-report pairs", often radiology reports
- **Medical Examples**:
  - Full radiology reports with findings, impressions, recommendations
  - Comprehensive pathology descriptions
  - Detailed clinical assessments

## Compatible Datasets

**High-Priority Datasets** (5+ available):
- **MIMIC Chest X-ray Reports**: Image-report pairs for long clinical report generation
- **brain-tumor-captions**: Short medical captions for brain imaging
- **X-ray Caption Datasets**: Various chest X-ray description datasets
- **Medical Image-Text Pairs**: Multiple caption/report generation datasets

## Schema Integration

- **Task**: "Describe"
- **Answer Type**: "span" (free text generation)
- **Text Length**: Distinguish between short captions and long reports
- **Language Model Requirements**: May require specialized medical language evaluation

## Clinical Applications

**Short Caption Generation**:
- Quick image summaries for medical records
- Case presentation preparation
- Medical education and training
- Automated image indexing and search

**Long Report Generation**:
- Comprehensive clinical documentation
- Radiology report assistance
- Detailed medical analysis
- Clinical decision support

## Implementation Notes

**Advantages**:
- Essential for automated medical documentation
- Supports clinical workflow efficiency
- Enables comprehensive medical image analysis
- Critical for medical AI communication

**Quality Considerations**:
- **Medical Accuracy**: Must use correct medical terminology
- **Clinical Relevance**: Descriptions must be medically meaningful
- **Language Quality**: Proper grammar and medical communication standards
- **Completeness**: Reports must cover relevant clinical findings

**Evaluation Challenges**:
- More complex evaluation than classification tasks
- Requires medical expert validation
- Language quality assessment needed
- Clinical utility evaluation required

## Future Development

**Easy Templates First**: Basic caption and report generation
**Advanced Templates**: Structured reporting, multi-finding descriptions, uncertainty handling
**Quality Enhancement**: Medical terminology validation, clinical relevance scoring
