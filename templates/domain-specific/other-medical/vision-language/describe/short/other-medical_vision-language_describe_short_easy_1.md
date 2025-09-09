# Other-Medical Biomedical Research Finding Description Template

## Template Overview

**Template ID**: `other-medical_vision-language_describe_short_easy_1`  
**Task Type**: Vision-language (describe)  
**Difficulty**: Easy  
**Question Pattern**: Scientific finding description selection  
**Medical Domain**: Other-Medical (biomedical research)  
**Domain-knowledge summary**: Requires general medical research knowledge for biomedical findings interpretation and scientific documentation. Must understand research methodology, scientific terminology, experimental design principles, data interpretation, and ability to generate accurate scientific descriptions of biomedical research findings across various research applications.

## Template Description

This template converts vision-language datasets into MCVQA format by asking models to select the most accurate scientific description of biomedical research findings. This capability tests the model's ability to recognize appropriate scientific terminology and research documentation conventions through multiple choice selection.

The template is designed for other-medical datasets with image-text pairs, testing the model's ability to identify scientifically accurate, concise descriptions that follow biomedical research reporting standards.

## Question Generation Pattern

### Question Format
```
"Which statement best describes the key finding or structure in this biomedical image?"
```

### Answer Format
Multiple choice with scientific description options:
- A. [First biomedical description option]
- B. [Second biomedical description option]
- C. [Third biomedical description option]
- D. [Fourth biomedical description option]
- E. No significant findings

### Template Variables
- `{research_context}`: Experimental setting and research application
- `{biological_structures}`: Cellular, molecular, or anatomical components
- `{experimental_findings}`: Observed results and scientific observations
- `{measurement_data}`: Quantitative or qualitative assessments

### Clinical Context
- **Research Documentation**: Accurate scientific description for research records
- **Scientific Communication**: Appropriate terminology for peer review and publication
- **Educational Value**: Scientific literacy and biomedical knowledge assessment
- **Quality Control**: Validation of experimental observations and interpretations

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "Which statement best describes the key finding or structure in this biomedical image?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "Fluorescently labeled neurons showing dendritic branching patterns in cultured hippocampal tissue",
    "Immunostained cardiac muscle cells with visible sarcomeric organization",
    "Phase contrast microscopy of dividing epithelial cells in monolayer culture",
    "Confocal imaging of vascular endothelial cells with junction proteins",
    "No significant findings"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Description accurately captures the fluorescent labeling, neuronal identity, and morphological features visible in the research image",
  "provenance": {
    "original_label": "neuronal_dendrites_description",
    "rule_id": "other-medical_vision-language_describe_short_easy_1",
    "annotation_id": "research_finding_description",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Biomedical research images with scientific annotations
- **Captions**: Research descriptions or scientific documentation
- **Quality**: Professional scientific language and accurate terminology

### Compatible Datasets
- Biomedical research image-caption collections
- Scientific publication figure databases
- Laboratory research documentation sets
- Experimental result imaging archives
- Educational biomedical image resources

### Minimum Standards
- **Image Quality**: Clear visualization of biomedical structures or findings
- **Caption Quality**: Scientifically accurate and professionally written descriptions
- **Research Accuracy**: Verified by qualified researchers or scientists

## Template Usage Rules

### Question Construction Rules
1. Ask for the "best" description to emphasize scientific accuracy
2. Focus on key findings or structures in the research context
3. Ensure all options use proper scientific terminology
4. Include scientifically relevant differential options

### Description Option Guidelines
1. Correct option should include accurate scientific terminology and observations
2. Distractors should be scientifically plausible but incorrect for the specific image
3. Use standard biomedical terminology and research conventions consistently
4. Include normal/negative option when appropriate

### Quality Control Guidelines
1. Verify scientific accuracy and appropriate terminology
2. Ensure descriptions are relevant to biomedical research applications
3. Check for proper experimental context and methodology references
4. Validate research interpretation and scientific reasoning

## Examples

### Example 1: Neuronal Culture Research
**Image**: Fluorescence microscopy showing labeled neurons with dendritic processes  
**Question**: "Which statement best describes the key finding or structure in this biomedical image?"  
**Options**: A. Fluorescently labeled neurons showing dendritic branching patterns in cultured hippocampal tissue | B. Immunostained cardiac muscle cells with visible sarcomeric organization | C. Phase contrast microscopy of dividing epithelial cells | D. Confocal imaging of vascular endothelial cells  
**Answer**: A  
**Rationale**: Correctly identifies fluorescent labeling, neuronal cell type, and dendritic morphology

### Example 2: Cell Division Study
**Image**: Phase contrast microscopy showing cells undergoing mitosis  
**Question**: "Which statement best describes the key finding or structure in this biomedical image?"  
**Options**: A. Apoptotic cells with membrane blebbing | B. Mitotic cells in metaphase with condensed chromosomes | C. Differentiated neurons with axonal projections | D. Senescent cells with enlarged morphology  
**Answer**: B  
**Rationale**: Accurately describes mitotic phase and chromosomal condensation visible in the image

### Example 3: Tissue Engineering Research
**Image**: Confocal microscopy of engineered tissue construct  
**Question**: "Which statement best describes the key finding or structure in this biomedical image?"  
**Options**: A. Native tissue architecture with normal organization | B. Engineered tissue construct with scaffold integration | C. Pathological tissue with inflammatory infiltrate | D. Cell culture monolayer with tight junctions  
**Answer**: B  
**Rationale**: Correctly identifies engineered tissue context and scaffold integration

### Example 4: Protein Expression Study
**Image**: Immunofluorescence showing protein localization  
**Question**: "Which statement best describes the key finding or structure in this biomedical image?"  
**Options**: A. Cytoplasmic protein aggregation in stressed cells | B. Nuclear protein localization in proliferating cells | C. Membrane protein expression in epithelial cells | D. Mitochondrial protein distribution in metabolically active cells  
**Answer**: C  
**Rationale**: Accurately describes membrane localization pattern and cell type

### Example 5: Drug Response Study
**Image**: Microscopy showing cellular response to treatment  
**Question**: "Which statement best describes the key finding or structure in this biomedical image?"  
**Options**: A. Untreated control cells with normal morphology | B. Drug-treated cells showing cytotoxic response | C. Vehicle-treated cells with minimal changes | D. Positive control cells with expected phenotype  
**Answer**: B  
**Rationale**: Correctly identifies treatment context and cellular response to drug exposure

## Implementation Notes

### Technical Considerations
- Correlate descriptions with actual biomedical research standards
- Consider different microscopy techniques and experimental approaches
- Account for varying research contexts and scientific applications
- Handle specialized biomedical terminology and methodology

### Clinical Validation
- Align with scientific research documentation standards
- Cross-reference with biomedical research publication guidelines
- Validate against expert researcher assessment
- Consider peer review and scientific communication requirements

### Dataset-Specific Adaptations
- **Research datasets**: Focus on experimental findings and scientific observations
- **Educational datasets**: Emphasize learning and knowledge assessment
- **Publication datasets**: Include high-quality scientific descriptions
- **Multi-modal datasets**: Adapt descriptions for different imaging techniques

### Quality Assurance
- Regular validation by biomedical researchers and scientists
- Cross-reference with scientific literature and research standards
- Monitoring for scientific accuracy and terminology consistency
- Updates based on evolving biomedical research practices and terminology
