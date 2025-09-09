# Other-Medical Cell Type Classification in Microscopy Template

## Template Overview

**Template ID**: `other-medical_classification_multiclass_easy_1`  
**Task Type**: Multiclass Classification  
**Difficulty**: Easy  
**Pattern**: Cell type identification in microscopic images  
**Domain**: Other-Medical (cellular microscopy)

## Template Description

This template converts multiclass classification datasets into MCVQA format by asking questions about cell types in microscopic images. This capability is essential for biomedical research, drug testing, and cellular analysis applications across various research contexts.

The template is designed for other-medical datasets with cellular classification, testing the model's ability to recognize and distinguish different cell types based on morphological characteristics and microscopic appearance.

## Question Generation Pattern

### Question Format
```
"What type of cell is primarily shown in this microscopic image?"
```

### Answer Format
Multiclass choice with cell type options:
- A. Neuron
- B. Hepatocyte
- C. Epithelial cell
- D. Fibroblast
- E. Immune cell
- F. Stem cell
- G. Cancer cell
- H. Red blood cell

### Template Variables
- `{cell_morphology}`: Shape, size, and structural characteristics
- `{cellular_features}`: Nucleus, cytoplasm, and organelle appearance
- `{tissue_context}`: Surrounding tissue environment and cellular arrangement
- `{staining_pattern}`: Response to specific stains and imaging techniques

### Clinical Context
- **Research Applications**: Cell identification for experimental studies and drug testing
- **Diagnostic Support**: Cellular analysis for pathological investigation
- **Therapeutic Development**: Cell-based therapy and regenerative medicine applications
- **Quality Control**: Cell culture monitoring and characterization

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What type of cell is primarily shown in this microscopic image?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Neuron",
    "Hepatocyte",
    "Epithelial cell",
    "Fibroblast",
    "Immune cell",
    "Stem cell",
    "Cancer cell",
    "Red blood cell"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Cell shows characteristic neuronal morphology with prominent cell body, dendrites, and axonal processes",
  "provenance": {
    "original_label": "neuron",
    "rule_id": "other-medical_classification_multiclass_easy_1",
    "annotation_id": "cell_type_identification",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: High-resolution microscopic images of individual or grouped cells
- **Labels**: Cell type annotations with morphological context
- **Quality**: Sufficient magnification and clarity for cellular detail assessment

### Compatible Datasets

**Available in MBU Metadata:**
- `alkzar90/cell_benchmark` - Cell segmentation dataset with cellular morphology analysis
- `Docty/Blood-Cells` - Blood cell classification with 8 cell types (monocyte, neutrophil, lymphocyte, eosinophil, etc.)

**General Categories:**
- Cell culture identification datasets
- Microscopic cell classification collections
- Biomedical research cell databases
- Cellular morphology reference sets
- Drug testing cell response archives

### Minimum Standards
- **Image Quality**: Clear visualization of cellular morphology and subcellular structures
- **Annotation Quality**: Expert validation by cell biologists or research scientists
- **Data Distribution**: Representative examples of major cell types

## Template Usage Rules

### Question Construction Rules
1. Focus on primary cell type identification based on morphological features
2. Use standard cell biology terminology
3. Consider microscopic appearance and cellular characteristics
4. Emphasize research and biomedical applications

### Answer Assignment Rules
1. Map cells with neuronal processes → "Neuron"
2. Map large cells with abundant cytoplasm in liver context → "Hepatocyte"
3. Map sheet-forming cells with tight junctions → "Epithelial cell"
4. Map spindle-shaped connective tissue cells → "Fibroblast"
5. Map round immune system cells → "Immune cell"
6. Map undifferentiated pluripotent cells → "Stem cell"
7. Map morphologically abnormal cells → "Cancer cell"
8. Map small, enucleated blood cells → "Red blood cell"

### Quality Control Guidelines
1. Ensure accurate cell type identification based on established morphological criteria
2. Verify consistency with cell biology and histology standards
3. Cross-validate with expert cell biologist assessment
4. Review for research and educational applications

## Examples

### Example 1: Primary Neuron Culture
**Image**: Microscopic view showing cell with long processes and prominent cell body  
**Question**: "What type of cell is primarily shown in this microscopic image?"  
**Answer**: A. Neuron  
**Rationale**: Cell demonstrates characteristic neuronal morphology with dendrites, axons, and prominent nucleus typical of nerve cells

### Example 2: Liver Cell Culture
**Image**: Microscopic view showing large cells with abundant cytoplasm  
**Question**: "What type of cell is primarily shown in this microscopic image?"  
**Answer**: B. Hepatocyte  
**Rationale**: Cells show large size with abundant cytoplasm and characteristic hepatocyte appearance in liver cell culture

### Example 3: Epithelial Monolayer
**Image**: Microscopic view showing tightly connected sheet of cells  
**Question**: "What type of cell is primarily shown in this microscopic image?"  
**Answer**: C. Epithelial cell  
**Rationale**: Cells form characteristic epithelial sheet with tight cell-cell junctions and polarized appearance

### Example 4: Connective Tissue Culture
**Image**: Microscopic view showing elongated, spindle-shaped cells  
**Question**: "What type of cell is primarily shown in this microscopic image?"  
**Answer**: D. Fibroblast  
**Rationale**: Cells display characteristic fibroblast morphology with elongated, spindle shape typical of connective tissue cells

### Example 5: Blood Smear
**Image**: Microscopic view showing small, round, red-colored cells  
**Question**: "What type of cell is primarily shown in this microscopic image?"  
**Answer**: H. Red blood cell  
**Rationale**: Cells show characteristic small, round, enucleated appearance typical of red blood cells in blood smear

## Implementation Notes

### Technical Considerations
- Implement cellular morphology analysis algorithms
- Consider different microscopy techniques and staining methods
- Account for varying cell culture conditions and preparation methods
- Handle different magnifications and imaging parameters

### Clinical Validation
- Align with established cell biology and histology references
- Cross-reference with cellular morphology atlases
- Validate against expert cell biologist identification
- Consider research application requirements

### Dataset-Specific Adaptations
- **Research datasets**: Focus on cell types relevant to specific research applications
- **Drug testing datasets**: Include cell response and morphological changes
- **Stem cell datasets**: Emphasize differentiation states and pluripotency markers
- **Cancer datasets**: Include normal vs transformed cell comparisons

### Quality Assurance
- Regular validation by cell biologists and microscopy experts
- Cross-reference with established cellular morphology standards
- Monitoring for accuracy across different cell culture conditions
- Updates based on advancing cell biology knowledge and imaging techniques
