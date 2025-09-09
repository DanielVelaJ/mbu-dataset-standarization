# Other-Medical Domain-Specific Templates

This directory contains MCVQA templates for diverse medical imaging applications beyond primary specialties. These templates support cellular microscopy, biomedical research, veterinary applications, dental imaging, and specialized medical contexts.

## Template Organization

### Multiclass Classification (`classification/multiclass/`)
- **Cell Type Classification in Microscopy** - Biomedical research and cellular analysis
- **Brain Region Identification** - Neuroscience and neuroimaging applications
- **Dental Pathology Assessment** - Oral health and dental diagnosis
- **Laboratory Animal Species Identification** - Veterinary and research applications

### Binary Classification (`classification/binary/`)
- **Normal vs Abnormal Cell Morphology** - Research quality control
- **Research-Grade vs Clinical-Grade Image Quality** - Data quality assessment

### Vision-Language (`vision-language/`)
- **Biomedical Research Finding Description** - Scientific documentation (MCVQA format)
- **Experimental Result Interpretation** - Research analysis and methodology (MCVQA format)

## Example Question Generation

**Template**: `other-medical_classification_multiclass_easy_1.md`  
**Question Formula**: "What type of cell is primarily shown in this microscopic image?"  
**Answer Formula**: A. Neuron | B. Hepatocyte | C. Epithelial cell | D. Fibroblast | E. Immune cell | F. Stem cell | G. Cancer cell | H. Red blood cell  
**Input**: Microscopic image showing neuronal cell culture  
**Generated Answer**: A. Neuron

## Clinical Context

These templates bridge research and clinical applications across diverse medical sub-domains including cellular biology, neuroscience, dental medicine, veterinary care, and biomedical research methodology.
