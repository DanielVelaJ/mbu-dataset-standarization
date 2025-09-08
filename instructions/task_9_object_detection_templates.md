# Task 9: Object Detection Templates

Similarly to how we did in task 2 for binary classification, task 4 for multi-class classification, task 5 for multi-label classification, task 6 for semantic segmentation, and task 7 for instance segmentation, we will now create templates for object detection. Please read the context files and the instructions files and help me define the templates.

These should be the domain-agnostic templates that work across all medical domains. Remember object detection localizes and classifies objects using bounding boxes - this differs from classification (image-level labels) and segmentation (pixel-level masks) as we're working at the object level with rectangular spatial localization.

## What is Object Detection?

**Definition**: Detect and localize objects in the image with rectangular bounding boxes and assign a class to each detected object.

**Key Characteristics**:
- **Input**: One 2D medical image
- **Output**: List of bounding boxes + object class per box
- **Task Focus**: Object localization and classification at bounding box level
- **vs Classification**: Object-level localization instead of image-level labeling
- **vs Segmentation**: Rectangular boxes instead of pixel-accurate masks
- **vs Landmarks**: Class-labeled regions instead of point coordinates

## Object Detection Subtypes

From our medical vision taxonomy, there are **3 object detection subtypes**:

### 1. **Lesion Detection with Bounding Boxes**
- **Purpose**: Detect and localize pathological findings/lesions
- **Output**: Bounding boxes + lesion class per box
- **Examples**: CXR nodule detection, dermatology lesion detection, brain tumor detection
- **Dataset Count**: **53 datasets** in our metadata (largest subtype)

### 2. **Anatomy Detection with Bounding Boxes** 
- **Purpose**: Detect and localize anatomical structures
- **Output**: Bounding boxes + anatomical class per box  
- **Examples**: Fundus optic disc detection, organ detection in CT, bone detection in X-rays
- **Dataset Count**: **9 datasets** in our metadata

### 3. **Device Detection with Bounding Boxes**
- **Purpose**: Detect and localize medical devices/hardware
- **Output**: Bounding boxes + device class per box
- **Examples**: CXR pacemaker detection, ETT tube detection, surgical instrument detection  
- **Dataset Count**: **4 datasets** in our metadata

**Technical Note**: All subtypes share the same underlying structure (bounding box + class label) but differ in:
- **Object types** being detected (pathology vs anatomy vs devices)
- **Class vocabularies** (lesion names vs organ names vs device names)  
- **Clinical contexts** (diagnosis vs structure identification vs procedure support)

## MCVQA Conversion Challenge

Converting object detection datasets to MCVQA format requires asking questions about:
- **Object Presence**: "Are there any [lesions/organs/devices] visible in this image?"
- **Object Classification**: "What type of [lesion/organ/device] is highlighted in the bounding box?"
- **Object Localization**: "Where is the [specific object] located in this image?"
- **Object Counting**: "How many [objects] are detected in this image?"
- **Object Properties**: "What is the [property] of the highlighted [object]?"

### Highlighting Strategy
Object detection templates can leverage **bounding box highlighting** where specific detected objects are visually highlighted (using boxes from original annotations) to enable:
- **Object-specific questions** about individual detections
- **Spatial reasoning** about object locations and relationships
- **Property assessment** of particular detected objects
- **Quality validation** of detection accuracy

This highlighting approach uses existing bounding box annotations from the dataset - no new annotations needed.

## Template Requirements

### Naming Convention
Follow the established pattern: `{domain}_{task}_{subtype}_{difficulty}_{number}.md`

**Examples**:
- `domain-agnostic_detection_object_easy_1.md`
- `domain-agnostic_detection_object_easy_2.md`  
- `domain-agnostic_detection_object_easy_3.md`

### Directory Structure
Save templates in: `templates/domain-agnostic/detection/object/`

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

Create **3 easy-difficulty templates** initially that can work with the most basic information needed for object detection datasets:

### Template Ideas:

1. **Lesion Detection Template** (`domain-agnostic_detection_object_easy_1.md`)
   - **Focus**: Pathological findings and lesions
   - **Question Pattern**: "What type of lesion is highlighted in the bounding box?"
   - **Answer Type**: "single_label" 
   - **Clinical Context**: Disease diagnosis and pathology identification
   - **Primary Datasets**: 53 lesion detection datasets

2. **Anatomy Detection Template** (`domain-agnostic_detection_object_easy_2.md`)
   - **Focus**: Anatomical structures and organs  
   - **Question Pattern**: "What anatomical structure is highlighted in the bounding box?"
   - **Answer Type**: "single_label"
   - **Clinical Context**: Structure identification and anatomical assessment  
   - **Primary Datasets**: 9 anatomy detection datasets

3. **Device Detection Template** (`domain-agnostic_detection_object_easy_3.md`)
   - **Focus**: Medical devices and hardware
   - **Question Pattern**: "What medical device is highlighted in the bounding box?"
   - **Answer Type**: "single_label"
   - **Clinical Context**: Procedure support and device monitoring
   - **Primary Datasets**: 4 device detection datasets

### Advanced Template Ideas (Future):
- **Multi-object Detection**: "How many [objects] are detected in this image?"
- **Spatial Relationships**: "Which detected [object] is closest to [landmark]?"
- **Detection Validation**: "Is the highlighted bounding box correctly placed around the [object]?"

## Dataset Compatibility

Templates must work with object detection datasets that have:
- **Medical images** (any modality: CT, MRI, X-ray, microscopy, photography, etc.)
- **Bounding box annotations** (rectangular object localizations)
- **Class labels** for detected objects
- **COCO-format or similar** structured annotations

**Example Compatible Datasets from Our Analysis**:
- **Lesion Detection**: Dataset for Automating Dental Condition Detection (Quality: 85), LIDC-IDRI (Quality: 85)
- **Anatomy Detection**: LeukemiaAttri (Quality: 75), Blood Cell Detection (Quality: 65)
- **Device Detection**: 4D-OR (Quality: 72), HOSPI-Tools Dataset (Quality: 70)

**Dataset Statistics**:
- **Total Object Detection Datasets**: 66 datasets
- **Domain Distribution**: Radiology (32), Pathology (13), Surgery (8), Other-Medical (7), Ophthalmology (4), Dermatology (2)
- **Quality Assessment**: Mean quality score 61.3, with 4 high-quality datasets (≥80)

## Schema Considerations

For object detection in MCVQA format:

### Task Specification
- **Template Header**: `"Task Type": "Object Detection"` (distinguishes from other vision tasks)
- **JSON Schema**: `"task": "Detection"` (maps to detection category in datum schema)

### Answer Types
- **"single_label"** for object classification questions ("What type of lesion is highlighted?")
- **"number"** for counting questions ("How many lesions are detected?")
- **"yes_no"** for presence questions ("Are there any devices visible?")

### Spatial Reference Strategy
Object detection templates use **bounding box highlighting**:

#### Example: Object Classification with Highlighting
```json
{
  "qa_id": "1",
  "task": "Detection", 
  "question": "What type of lesion is highlighted in the bounding box?",
  "answer": "Pulmonary nodule",
  "answer_type": "single_label",
  "spatial_reference": {
    "reference_type": "bbox",
    "bbox": [0.2, 0.3, 0.4, 0.5],
    "annotation_id": "lesion_detection_001",
    "highlighting_method": "outline",
    "highlight_color": "yellow", 
    "highlight_opacity": 1.0
  },
  "provenance": {
    "rule_id": "domain-agnostic_detection_object_easy_1",
    "annotation_id": "lesion_detection_001",
    "created_by": "program"
  }
}
```

### Schema Field Usage
- **spatial_reference**: Contains bounding box coordinates and highlighting specifications
- **geometry**: Contains original dataset geometric information (for reference)
- **provenance**: Contains annotation_id linking back to original detection annotations

## Key Differences from Other Templates

### vs Classification Templates:
1. **Spatial Localization**: Questions reference specific spatial regions, not whole images
2. **Object-Level Reasoning**: Focus on individual detected objects rather than image-level properties
3. **Bounding Box Integration**: Visual highlighting using rectangular regions
4. **Multi-Object Scenarios**: Can handle multiple objects of same/different classes

### vs Segmentation Templates:
1. **Rectangular vs Pixel Boundaries**: Bounding boxes instead of precise masks
2. **Object-Centric**: Focus on object identification rather than region delineation
3. **Faster Annotation**: Boxes are quicker to annotate than pixel-accurate masks
4. **Different Clinical Workflow**: Detection workflows vs segmentation workflows

### vs Instance Segmentation Templates:
1. **Box vs Mask Precision**: Rectangular approximation vs pixel-accurate boundaries
2. **Efficiency Trade-off**: Faster annotation/inference but less spatial precision
3. **Clinical Applications**: Different use cases (screening vs surgical planning)

## Success Criteria

- ✅ **3 easy-difficulty templates** created following 8-section structure
- ✅ **Schema compliance** with unified datum schema v1.0
- ✅ **Medical accuracy** using correct anatomical/pathological terminology  
- ✅ **Cross-domain applicability** working across medical specialties
- ✅ **5 examples per template** spanning different medical domains
- ✅ **Clear documentation** of object detection-specific considerations
- ✅ **Bounding box highlighting** integration with spatial reference system

## Implementation Strategy

### Phase 1: Easy Templates (Current Task)
Focus on fundamental object detection capabilities:
- Basic lesion classification in bounding boxes
- Simple anatomy identification in boxes
- Elementary device detection in boxes

### Phase 2: Medium Templates (Future)
Add counting and spatial reasoning:
- Multi-object counting and enumeration
- Spatial relationship analysis between objects
- Comparative object assessment

### Phase 3: Hard Templates (Future) 
Complex reasoning and validation:
- Object detection quality assessment
- Multi-criteria object evaluation
- Advanced spatial and clinical reasoning

## Quality Considerations

### Medical Accuracy
- Use correct medical terminology for lesions, anatomy, and devices
- Ensure questions reflect real clinical workflows and diagnostic processes
- Validate examples with appropriate medical domain expertise

### Technical Precision
- **Bounding Box Reference**: Questions must clearly specify which detected object is being referenced
- **Highlighting Clarity**: Object-specific questions must clearly indicate which detection is highlighted
- **Class Vocabulary**: Object classification must use clinically meaningful and standardized terminology
- **Spatial Accuracy**: Bounding box coordinates must correspond to actual object locations

### Cross-Domain Applicability
- Templates should work across radiology, pathology, surgery, dermatology, ophthalmology
- Avoid domain-specific terminology that limits applicability
- Ensure questions scale appropriately across different imaging modalities and object scales

Let's start with the easy difficulty templates first and ensure they can work with the most basic information that is needed for object detection datasets.

## Progress Tracking

### Current Status
- **Task 9 Instructions**: ✅ **Complete** - Comprehensive guidelines established

### Next Steps
1. **Create Template 1**: Lesion detection template (`domain-agnostic_detection_object_easy_1.md`)
   - Focus on pathological findings and lesions
   - 53 compatible datasets identified
2. **Create Template 2**: Anatomy detection template (`domain-agnostic_detection_object_easy_2.md`)  
   - Focus on anatomical structures and organs
   - 9 compatible datasets identified
3. **Create Template 3**: Device detection template (`domain-agnostic_detection_object_easy_3.md`)
   - Focus on medical devices and hardware
   - 4 compatible datasets identified
4. **Create README**: Overview document for object detection template collection
5. **Test Templates**: Validate with compatible object detection datasets

### Design Decisions Made
✅ **Template Count**: 3 separate templates (one per subtype) following established pattern
✅ **Technical Pattern**: All share bounding box + class structure but different semantic contexts  
✅ **Dataset Coverage**: 66 total datasets mapped to appropriate templates
✅ **Schema Integration**: Full alignment with datum schema Detection task type
✅ **Spatial Reference**: Bounding box highlighting with coordinate specification
✅ **Clinical Focus**: Separate templates enable domain-specific question patterns

### Key Insights from Analysis
- **Lesion detection dominates** (53/66 datasets) - highest priority template
- **Quality varies widely** (mean 61.3) - need robust template design for various quality levels  
- **Domain diversity** spans 6 medical specialties - templates must be truly domain-agnostic
- **Technical uniformity** - all detection tasks share same bbox+class output format

Document progress, decisions, and any questions/answers in this file as we develop the templates.
