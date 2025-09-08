# Task 7: Instance Segmentation Templates

Similarly to how we did in task 2 for binary classification, task 4 for multi-class classification, task 5 for multi-label classification, and task 6 for semantic segmentation, we will now create templates for instance segmentation. Please read the context files and the instructions files and help me define the templates.

These should be the domain-agnostic templates that work across all medical domains. Remember instance segmentation assigns a class to each pixel AND separates different instances of the same class - this differs from semantic segmentation where instances of the same class are not distinguished.

## What is Instance Segmentation?

**Definition**: Classify each pixel into a class AND separately identify each individual instance of the same class.

**Key Characteristics**:
- **Input**: One 2D medical image
- **Output**: Multiple masks, one for each individual instance (separate mask files or multi-instance encoding)
- **Task Focus**: Individual object identification and precise delineation at pixel level
- **vs Classification**: Pixel-level labeling instead of image-level labeling
- **vs Semantic Segmentation**: Separates different instances of the same class (e.g., multiple cells, multiple organs, multiple lesions)
- **vs Object Detection**: Provides precise pixel boundaries instead of just bounding boxes

**Medical Examples**:
- **Multiple cell nuclei** in histopathology (each nucleus gets separate mask)
- **Multiple lesions** in dermatology (each lesion segmented individually)
- **Multiple organs** in abdominal CT (separate left/right kidneys, liver lobes)
- **Multiple nodules** in chest CT (each pulmonary nodule segmented separately)
- **Multiple vessels** in retinal imaging (each vessel branch as separate instance)

## MCVQA Conversion Challenge

Converting instance segmentation datasets to MCVQA format requires asking questions about:
- **Instance Counting**: "How many [objects] are segmented in this image?"
- **Instance Classification**: "What type of [object] is the highlighted instance?"
- **Instance Properties**: "What is the [property] of the highlighted segmented [object]?"
- **Spatial Relationships**: "Which segmented [object] is closest to [landmark]?"
- **Comparative Analysis**: "Which segmented [object] shows signs of [condition]?"

### Highlighting Strategy
Instance segmentation templates can leverage the **highlighting capability** where specific instances are visually highlighted (using masks from the original dataset) to enable:
- **Instance-specific questions** about individual objects
- **Comparative analysis** between different instances  
- **Property assessment** of particular instances
- **Complex reasoning** about relationships between instances

This highlighting approach uses the existing instance masks from the dataset - no new annotations needed.

## Template Requirements

### Naming Convention
Follow the established pattern: `{domain}_{task}_{subtype}_{difficulty}_{number}.md`

**Examples**:
- `domain-agnostic_segmentation_instance_easy_1.md`
- `domain-agnostic_segmentation_instance_medium_1.md`
- `domain-agnostic_segmentation_instance_hard_1.md`

### Directory Structure
Save templates in: `templates/domain-agnostic/segmentation/instance/`

### Template Structure Requirements
**All template files MUST follow the standardized 8-section structure:**

1. **Template Overview** - ID, task type, difficulty, pattern summary
2. **Template Description** - Detailed explanation of purpose and approach
3. **Question Generation Pattern** - Question format, answer format, template variables
4. **Mapping to Datum Schema** - Complete JSON schema mapping example
5. **Dataset Requirements** - What types of datasets this template supports
6. **Template Usage Rules** - Implementation guidelines and requirements
7. **Examples** - Minimum 5 concrete examples with real dataset references
8. **Implementation Notes** - Advantages, limitations, quality considerations

## Starting Templates (Easy Difficulty)

Create **3 easy-difficulty templates** initially that can work with the most basic information needed for instance segmentation datasets:

### Template Ideas:
1. **Instance Counting**: "How many [objects] are segmented in this image?"
2. **Instance Identification**: "What type of [object] is shown in the highlighted segmented instance?"
3. **Instance Property Assessment**: "What is the [property] of the highlighted segmented [object] in this image?"

### Advanced Template Ideas (Future):
- **Spatial Relationships**: "Which segmented [object] is closest to [landmark]?"
- **Comparative Analysis**: "Which segmented [object] shows the most [characteristic]?"
- **Instance Validation**: "Are all visible [objects] correctly segmented in this image?"

## Dataset Compatibility

Templates must work with instance segmentation datasets that have:
- **Medical images** (any modality: CT, MRI, X-ray, microscopy, etc.)
- **Instance-level annotations** (separate masks for each object instance)
- **Class labels** for segmented instances
- **Clear instance boundaries** distinguishing individual objects

**Example Compatible Datasets**:
- Cell nuclei segmentation (histopathology) - each nucleus as separate instance
- Multi-organ segmentation (abdominal CT) - each organ as separate instance
- Multiple lesion segmentation (dermatology) - each lesion as separate instance
- Pulmonary nodule segmentation (chest CT) - each nodule as separate instance
- Retinal vessel segmentation (fundus) - each vessel branch as separate instance

## Schema Considerations

For instance segmentation in MCVQA format:

### Task Specification
- **Template Header**: `"Task Type": "Instance Segmentation"` (distinguishes from semantic segmentation)
- **JSON Schema**: `"task": "Segmentation"` (same as semantic segmentation - both are segmentation tasks)

### Answer Types
- **"number"** for counting questions ("How many cells are segmented?")
- **"single_label"** for classification questions ("What type of cell is the highlighted instance?")
- **"yes_no"** for validation questions ("Is the highlighted instance correctly segmented?")

### Instance Highlighting Strategy
Templates can reference specific instances in two ways:

#### 1. Global Questions (No Highlighting)
```json
{
  "qa_id": "1",
  "task": "Segmentation",
  "question": "How many cell nuclei are segmented in this histopathology image?",
  "answer": "15",
  "answer_type": "number",
  "provenance": {
    "rule_id": "domain-agnostic_segmentation_instance_easy_1"
  }
}
```

#### 2. Instance-Specific Questions (With Highlighting)
```json
{
  "qa_id": "2", 
  "task": "Segmentation",
  "question": "What type of cell is shown in the highlighted segmented instance?",
  "answer": "Epithelial cell",
  "answer_type": "single_label",
  "geometry": {
    "bbox": [[0.2, 0.3, 0.4, 0.5]],
    "polygons": [[[0.2, 0.3], [0.4, 0.3], [0.4, 0.5], [0.2, 0.5]]]
  },
  "provenance": {
    "rule_id": "domain-agnostic_segmentation_instance_easy_2",
    "annotation_id": "instance_7"
  }
}
```

### Geometry Section Usage
- **For counting questions**: No geometry needed (global image question)
- **For instance-specific questions**: Include bbox/polygon of the highlighted instance
- **annotation_id**: References which specific instance from the original dataset annotations

## Key Differences from Other Templates

### vs Classification Templates:
1. **Multiple Objects**: Questions reference multiple individual objects, not whole images
2. **Instance Awareness**: Distinguishes between different instances of same class
3. **Counting Capability**: Enables quantitative assessment of object populations
4. **Spatial Context**: Questions about relative positions and relationships

### vs Semantic Segmentation Templates:
1. **Instance Separation**: Questions distinguish between individual objects of same type
2. **Quantitative Focus**: Emphasis on counting and comparative analysis
3. **Individual Properties**: Assessment of characteristics of specific instances
4. **Complex Reasoning**: More sophisticated spatial and comparative reasoning

## Success Criteria

- ✅ **3 easy-difficulty templates** created following 8-section structure
- ✅ **Schema compliance** with unified datum schema v1.0
- ✅ **Medical accuracy** using correct anatomical/pathological terminology
- ✅ **Cross-domain applicability** working across medical specialties
- ✅ **5 examples per template** spanning different medical domains
- ✅ **Clear documentation** of instance segmentation-specific considerations
- ✅ **Instance-aware questions** that leverage the multi-instance nature of the data

## Implementation Strategy

### Phase 1: Easy Templates (Current Task)
Focus on fundamental instance segmentation capabilities:
- Basic counting of segmented instances
- Simple instance classification
- Elementary property assessment

### Phase 2: Medium Templates (Future)
Add spatial and comparative reasoning:
- Spatial relationship analysis
- Comparative instance assessment
- Multi-criteria evaluation

### Phase 3: Hard Templates (Future)
Complex reasoning and validation:
- Instance segmentation quality assessment
- Multi-instance clinical reasoning
- Advanced spatial and temporal relationships

## Quality Considerations

### Medical Accuracy
- Use correct medical terminology for all anatomical structures and pathologies
- Ensure questions reflect real clinical scenarios and diagnostic workflows
- Validate examples with appropriate medical domain expertise

### Technical Precision
- **Instance Reference**: Questions must clearly specify whether they're global (whole image) or instance-specific (highlighted)
- **Highlighting Clarity**: Instance-specific questions must clearly indicate which instance is being referenced
- **Counting Edge Cases**: Handle zero instances, single instances, and large numbers appropriately
- **Property Measurability**: Property assessments must be clinically meaningful and objectively determinable
- **Geometry Accuracy**: Instance highlighting must use precise mask/polygon coordinates from original annotations

### Cross-Domain Applicability
- Templates should work across radiology, pathology, dermatology, ophthalmology
- Avoid domain-specific terminology that limits applicability
- Ensure questions scale appropriately across different imaging modalities

Let's start with the easy difficulty templates first and ensure they can work with the most basic information that is needed for instance segmentation datasets.

## Progress Tracking

### Current Status
- **Task 7 Instructions**: ✅ **Created** - Comprehensive guidelines for instance segmentation template development

### Next Steps
1. **Create Template 1**: Instance counting template (`domain-agnostic_segmentation_instance_easy_1.md`)
2. **Create Template 2**: Instance identification template (`domain-agnostic_segmentation_instance_easy_2.md`)
3. **Create Template 3**: Instance property assessment template (`domain-agnostic_segmentation_instance_easy_3.md`)
4. **Create README**: Overview document for instance segmentation template collection
5. **Test Templates**: Validate with compatible instance segmentation datasets

### Design Decisions Made
✅ **Task Specification**: Use "Instance Segmentation" in template header, "Segmentation" in JSON schema
✅ **Highlighting Strategy**: Include highlighting capability using existing dataset masks for instance-specific questions
✅ **Geometry Integration**: Use geometry section only for highlighted instance questions, include annotation_id for instance reference
✅ **Temporal Sequences**: Not included - assume only basic single-image information
✅ **Partially Visible Instances**: Not addressed - assume all instances are fully visible
✅ **Confidence Levels**: Not included - keep templates simple

### Design Decisions Still To Be Made
- Specific question patterns for each template
- Answer format specifications for different question types  
- Handling of edge cases (zero instances, overlapping instances)
- Property assessment criteria for different medical domains
- Selection criteria for which instances to highlight in instance-specific questions 

Document progress, decisions, and any questions/answers in this file as we develop the templates.
