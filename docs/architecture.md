# MBU Dataset Standardization Architecture

## The Big Picture

This repository converts biomedical datasets into a standardized MCVQA (Medical Computer Vision Question Answering) format. Think of it as a **data translation pipeline**:

```
Raw Medical Dataset → Standardized JSONL Output
(Different formats)     (Unified format for all)
```

### What Problem Are We Solving?

Medical datasets come in many different formats:
- Chest X-rays with CSV labels
- Skin lesions organized in folders  
- Radiology reports in JSON
- Pathology slides with XML annotations

We need **one unified format** to train and evaluate medical AI models across all these datasets.

### Our Solution

A **3-step pipeline** that works for any medical dataset:

1. **Load** → Convert raw dataset to our internal format
2. **Template** → Generate questions/answers from the data  
3. **Output** → Write standardized JSONL for ML training

## Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Raw Dataset   │ → │   Our Pipeline   │ → │ Standardized   │
│                 │    │                  │    │ JSONL Output   │
│ • Images        │    │ 1. Loader        │    │ • Same schema  │
│ • Labels (CSV)  │    │ 2. Template      │    │ • Medical Q&A  │
│ • Metadata      │    │ 3. Converter     │    │ • ML-ready     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Design Principles

1. **One Dataset = One Loader**: Each dataset gets its own loading logic
2. **Templates Generate Questions**: Reusable question patterns across datasets
3. **Pydantic for Reliability**: Automatic validation and JSON serialization
4. **No Magic**: Explicit dictionaries instead of complex registration systems
5. **Minimal Dependencies**: Add complexity only when needed

## Repository Structure

```
src/
├── mbu_dataset_standardization/
│   ├── __init__.py                 # Package initialization
│   ├── loaders.py                  # Dataset loading implementations
│   ├── templates.py                # Question generation templates
│   ├── convert.py                  # Main conversion orchestrator
│   ├── datum.py                    # Datum schema and validation
│   └── utils.py                    # Helper functions and utilities
docs/
├── architecture.md                 # This file - architecture documentation
templates/                          # Template documentation (domain-first organization)
├── domain-agnostic/               # Templates that work across all medical domains
│   ├── classification/
│   │   ├── binary/
│   │   ├── multiclass/
│   │   └── multilabel/
│   ├── detection/
│   └── segmentation/
└── domain-specific/               # Templates requiring domain expertise
    ├── radiology/
    │   ├── classification/
    │   ├── detection/
    │   └── segmentation/
    ├── dermatology/
    ├── pathology/
    ├── ophthalmology/
    └── surgery/
```

## Core Components

### 1. Data Loading (`src/mbu_dataset_standardization/loaders.py`)

**Purpose**: Handle dataset-specific parsing and normalization.

Contains loader classes for each dataset:
- `BaseLoader`: Abstract base class defining the loader interface
- `ChestXray14Loader`: Loads Chest X-ray 14 dataset
- `DermNetLoader`: Loads DermNet dataset  
- Additional dataset loaders as needed

**Key Methods**:
```python
def load_raw_data(self, data_dir: str) -> Iterator[RawDataPoint]:
    """Load images, labels, metadata from dataset directory"""

def get_metadata(self) -> Dict:
    """Return dataset-level metadata (name, license, institution, etc.)"""
```

### 2. Template System (`src/mbu_dataset_standardization/templates.py`)

**Purpose**: Generate questions and answers from standardized data.

Templates are organized by domain first, then by task type and difficulty:

**Domain-Agnostic Templates** (work across all medical domains):
- `AgnosticBinaryTemplate1`: General binary classification (easy)
- `AgnosticBinaryTemplate2`: General binary classification (medium)  
- `AgnosticBinaryTemplate3`: General binary classification (hard)
- `AgnosticMulticlassTemplate1`: General multi-class classification (easy)

**Domain-Specific Templates** (require medical domain expertise):
- `RadiologyBinaryTemplate1`: Radiology-specific binary classification
- `DermatologyBinaryTemplate1`: Dermatology-specific binary classification
- `PathologyBinaryTemplate1`: Pathology-specific binary classification
- Additional domain-specific templates as needed

**Template Naming Convention**: `{domain}_{task}_{subtype}_{difficulty}.md`
- Examples: `agnostic_classification_binary_1.md`, `radiology_classification_binary_1.md`

**Key Methods**:
```python
def is_compatible(self, annotations: StandardizedAnnotations) -> bool:
    """Check if template is compatible with dataset labels"""

def generate_qa(self, raw_data: RawDataPoint, dataset_meta: Dict) -> QuestionAnswer:
    """Generate ONE Q&A pair from raw data point"""

def fill_datum_sections(self, raw_data: RawDataPoint, dataset_meta: Dict) -> Dict:
    """Fill the non-QA sections of datum (header, imaging, etc.)"""
```

**Template Domain Specification**:
```python
class RadiologyBinaryTemplate1(BaseTemplate):
    domain = "radiology"                    # Domain specification
    template_id = "radiology_classification_binary_1"
    supported_task_types = ["classification-binary"]
    
class AgnosticBinaryTemplate1(BaseTemplate):
    domain = "agnostic"                     # Works across all domains
    template_id = "agnostic_classification_binary_1" 
    supported_task_types = ["classification-binary"]
```

### 3. Conversion Orchestrator (`src/mbu_dataset_standardization/convert.py`)

**Purpose**: Coordinate the conversion process from raw dataset to MCVQA format.

Contains:
- `LOADERS`: Dictionary mapping dataset names to loader classes
- `TEMPLATES`: Dictionary mapping template names to template classes
- `convert_dataset()`: Main conversion function
- `validate_compatibility()`: Check template-dataset compatibility

**Main Interface**:
```python
def convert_dataset(dataset_name: str, template_name: str, 
                   data_dir: str, output_path: str) -> None:
    """Convert a dataset using specified template to MCVQA format"""
```

### 4. Data Structures (`src/mbu_dataset_standardization/datum.py`)

**Purpose**: Define and validate the standardized data schema.

Contains:
- `RawDataPoint`: Intermediate data structure from loaders
- `QuestionAnswer`: Single Q&A pair structure
- `Datum`: Complete output schema matching the unified datum schema
- Validation functions to ensure schema compliance

### 5. Utilities (`src/mbu_dataset_standardization/utils.py`)

**Purpose**: Common helper functions and utilities.

Contains:
- File I/O utilities
- Image processing helpers
- Logging configuration
- Path manipulation functions

## How It All Works Together

### Step-by-Step Data Flow

```
1. Raw Dataset          2. Loader Processes     3. Template Generates    4. Final Output
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ chest_xray_14/  │    │ StandardizedAnnotations │  │ QuestionAnswer  │    │ datum.jsonl     │
│ ├── images/     │ → │ RawDataPoint      │ → │ + Datum sections │ → │ (One line per   │
│ ├── labels.csv  │    │ (per image)      │    │ (per image)     │    │  image)         │
│ └── splits.txt  │    └─────────────────┘    └─────────────────┘    └─────────────────┘
└─────────────────┘
```

### What Each Component Does

**🔄 Loader** (`loaders.py`)
- **Input**: Raw dataset files (images, CSV, folders)
- **Does**: Parses dataset-specific format, normalizes labels
- **Output**: `RawDataPoint` objects (one per image)

**🎯 Template** (`templates.py`) 
- **Input**: `RawDataPoint` from loader
- **Does**: Generates medical questions and answers
- **Output**: `QuestionAnswer` + complete `Datum`

**📦 Converter** (`convert.py`)
- **Input**: Dataset name + template name
- **Does**: Orchestrates loader → template → output
- **Output**: JSONL file ready for ML training

### Data Scope: Dataset vs Single Image

This is important! Our models work at **different levels**:

| Model | Scope | Contains |
|-------|-------|----------|
| `StandardizedAnnotations` | **Single Image** | Labels for one image |
| `RawDataPoint` | **Single Image** | One image + labels + metadata |
| `QuestionAnswer` | **Single Image** | One Q&A about one image |
| `Datum` | **Single Image** + **Dataset Info** | Complete JSONL entry |

**Key Insight**: `Datum` contains both single-image info AND dataset-wide info that gets repeated for each image.

## Key Data Structures Explained

### 🏷️ StandardizedAnnotations - "The Universal Translator"

**Purpose**: Converts any dataset's label format into a common structure that templates can use.

```python
# Example: Chest X-ray with multiple findings
annotations = StandardizedAnnotations(
    task_type="classification-multilabel",
    target_classes=["pneumonia", "cardiomegaly", "no_finding"],
    active_classes=["pneumonia", "cardiomegaly"],  # What this image has
    is_positive=True,  # Convenience for binary tasks
    original_labels=["Pneumonia", "Cardiomegaly"],  # Preserved from dataset
    label_source="csv_pipe_separated"
)
```

**Key Point**: This is an **intermediate structure** - it doesn't appear in final output, just helps templates understand the data.

### 📦 RawDataPoint - "One Complete Data Point"

**Purpose**: Everything a template needs to generate Q&A for one image.

```python
# Example: One chest X-ray ready for template processing
raw_data = RawDataPoint(
    image_path="data/chest_xray_14/images/00001.png",
    image_id="00001",
    annotations=annotations,  # The StandardizedAnnotations from above
    metadata={"patient_age": 65, "view": "PA"},
    split="train"
)
```

### ❓ QuestionAnswer - "One Q&A Pair"

**Purpose**: A single question and answer generated from one image.

```python
# Example: Generated by a binary template
qa = QuestionAnswer(
    qa_id="1",
    task="Classification",
    question="Is there evidence of pneumonia in this chest X-ray?",
    answer="Yes",
    answer_type="yes_no",
    difficulty="easy",
    rationale="Based on radiological findings"
)
```

### 📄 Datum - "Final JSONL Output"

**Purpose**: The complete entry for one image in the final JSONL file.

```python
# Example: Complete output for one image
datum = Datum(
    # Single-image specific info
    header={
        "image_id": "00001",
        "domain": "Radiology", 
        "category": "pneumonia"
    },
    questions_and_answers=[qa],  # The Q&A from above
    
    # Dataset-wide info (repeated for each image)
    dataset={
        "name": "NIH Chest X-ray 14",
        "institution": "National Institutes of Health",
        "license": "CC0"
    },
    imaging={"modality": "CXR", "body_part": "chest"},
    # ... other sections
)
```

**Key Point**: Each `Datum` becomes one line in the final JSONL output file.

## Pydantic for Data Validation

All data structures use **Pydantic models** instead of dataclasses for several key benefits:

### **Automatic JSON Serialization**
```python
# Built-in JSON serialization
datum_json = datum.model_dump_json(by_alias=True, exclude_none=True)

# Automatic field aliasing ("questions_and_answers" → "questions-and-answers")
datum_dict = datum.model_dump(by_alias=True)
```

### **Robust Type Validation**
- Automatic validation on object creation
- Clear error messages when data doesn't match expected types
- Critical for ensuring data quality across 500+ datasets

### **Schema Compliance**
- Field aliases ensure output matches exact schema format
- No custom JSON serialization code needed
- Built-in handling of optional fields and defaults

This provides better reliability and maintainability compared to manual validation with dataclasses.

## Complete Example: Converting One Image

Let's walk through converting a single chest X-ray to show how everything connects:

### 1. Raw Dataset Input
```
chest_xray_14/
├── images/00001.png
└── Data_Entry_2017.csv
    # CSV contains: "00001.png,Pneumonia|Cardiomegaly,..."
```

### 2. Loader Processes Raw Data
```python
# ChestXray14Loader.load_raw_data()
raw_labels = "Pneumonia|Cardiomegaly"  # From CSV

# Loader creates StandardizedAnnotations
annotations = StandardizedAnnotations(
    task_type="classification-multilabel",
    target_classes=["pneumonia", "cardiomegaly", "no_finding", ...],
    active_classes=["pneumonia", "cardiomegaly"],
    original_labels=["Pneumonia", "Cardiomegaly"]
)

# Loader creates RawDataPoint  
raw_data = RawDataPoint(
    image_path="chest_xray_14/images/00001.png",
    image_id="00001", 
    labels=labels,
    split="train"
)
```

### 3. Template Generates Q&A
```python
# BinaryTemplate1.generate_qa()
def generate_qa(raw_data):
    # Template reads standardized labels
    has_pneumonia = "pneumonia" in raw_data.annotations.active_classes
    
    return QuestionAnswer(
        qa_id="1",
        question="Is there evidence of pneumonia in this chest X-ray?",
        answer="Yes" if has_pneumonia else "No",
        answer_type="yes_no"
    )
```

### 4. Final JSONL Output
```json
{
  "header": {"image_id": "00001", "domain": "Radiology", "category": "pneumonia"},
  "dataset": {"name": "NIH Chest X-ray 14", "license": "CC0"},
  "imaging": {"modality": "CXR", "body_part": "chest"},
  "questions-and-answers": [
    {
      "qa_id": "1",
      "question": "Is there evidence of pneumonia in this chest X-ray?", 
      "answer": "Yes",
      "answer_type": "yes_no"
    }
  ]
}
```

**Key Insight**: `StandardizedAnnotations` is the bridge that lets any template work with any dataset!

## Standardized Label Interface

### Task Type Classification

The `task_type` field provides quick identification of the classification approach:

```python
TASK_TYPES = {
    "classification-binary": "Binary classification (yes/no, present/absent)",
    "classification-multiclass": "Multi-class classification (one of many)",
    "classification-multilabel": "Multi-label classification (multiple can be true)",
    "detection-bbox": "Object detection with bounding boxes",
    "segmentation-semantic": "Semantic segmentation",
    "segmentation-instance": "Instance segmentation",
    "regression-continuous": "Continuous value regression",
    "regression-ordinal": "Ordinal regression (ordered categories)"
}
```

### Template-Label Compatibility

Templates declare their supported task types for automatic compatibility checking:

```python
class BinaryTemplate1(BaseTemplate):
    supported_task_types = ["classification-binary"]
    
    def is_compatible(self, annotations: StandardizedAnnotations) -> bool:
        return annotations.task_type in self.supported_task_types
```

### Loader Label Normalization

Each loader converts dataset-specific formats to the standardized structure:

```python
# Chest X-ray 14 (Multi-label)
annotations = StandardizedAnnotations(
    task_type="classification-multilabel",
    target_classes=["pneumonia", "cardiomegaly", "atelectasis"],
    active_classes=["pneumonia", "cardiomegaly"],
    original_labels=["Pneumonia", "Cardiomegaly"],
    label_source="csv_pipe_separated"
)

# DermNet (Multi-class)  
annotations = StandardizedAnnotations(
    task_type="classification-multiclass",
    target_classes=["acne", "melanoma", "psoriasis"],
    active_classes=["melanoma"],
    primary_class="melanoma",
    original_labels="melanoma",
    label_source="folder_name"
)
```

## For Developers: How to Use This

### Basic Usage
```python
from mbu_dataset_standardization.convert import convert_dataset

# Convert any dataset with any template (domain-first naming)
convert_dataset(
    dataset_name="chest_xray_14",           # Must be in LOADERS dict
    template_name="radiology_classification_binary_1",  # Domain-first template name
    data_dir="data/chest_xray_14/",
    output_path="output/chest_xray_14_radiology_binary_1.jsonl"
)

# Or use domain-agnostic template
convert_dataset(
    dataset_name="chest_xray_14",
    template_name="agnostic_classification_binary_1",
    data_dir="data/chest_xray_14/",
    output_path="output/chest_xray_14_agnostic_binary_1.jsonl"
)
```

### Adding a New Dataset
1. **Create loader class** inheriting from `BaseLoader`
2. **Implement three methods**:
   - `load_raw_data()` → yields `RawDataPoint` objects
   - `get_metadata()` → returns dataset info dict
   - `normalize_annotations()` → converts raw annotations to `StandardizedAnnotations`
3. **Add to registry**: `LOADERS["my_dataset"] = MyDatasetLoader`

### Adding a New Template
1. **Create template class** inheriting from `BaseTemplate`
2. **Specify domain and implement methods**:
   - Set `domain` attribute ("radiology", "dermatology", "agnostic", etc.)
   - `generate_qa()` → creates `QuestionAnswer` from `RawDataPoint`
   - `fill_datum_sections()` → creates header/dataset/quality/etc. sections
3. **Add to registry**: `TEMPLATES["radiology_classification_binary_1"] = RadiologyBinaryTemplate1`

**Example**:
```python
class RadiologyBinaryTemplate1(BaseTemplate):
    domain = "radiology"
    template_id = "radiology_classification_binary_1"
    supported_task_types = ["classification-binary"]
    
    def generate_qa(self, raw_data, dataset_meta):
        # Radiology-specific question generation
        pass
```

### Working with Pydantic Models
```python
# Create models (automatic validation)
annotations = StandardizedAnnotations(task_type="classification-binary", ...)

# Export to JSON (automatic serialization)
datum_json = datum.model_dump_json(by_alias=True, exclude_none=True)

# Load from dict (automatic validation)
datum = Datum(**data_dict)
```

### Debugging Tips
- **Check `StandardizedAnnotations`** if templates aren't working
- **Verify `task_type`** matches between loader and template
- **Use `original_labels`** to trace back to source data
- **Enable Pydantic validation** to catch data issues early

## Import Strategy

**Use absolute imports throughout:**

```python
# Good ✅
from mbu_dataset_standardization.loaders import ChestXray14Loader
from mbu_dataset_standardization.templates import BinaryTemplate1
from mbu_dataset_standardization.datum import Datum, QuestionAnswer

# Bad ❌
from .loaders import ChestXray14Loader
from ..templates import BinaryTemplate1
```

## Future Extensibility

This simple architecture can evolve as the project grows:

1. **Phase 1 (Current)**: Simple classes and manual dictionaries
2. **Phase 2**: Split into separate modules when files get large (>500 lines)
3. **Phase 3**: Add registry pattern only if we reach 50+ components
4. **Phase 4**: Plugin architecture for external contributions

## Design Decisions Made

1. **No Registries**: Too complex for current scale, using simple dictionaries
2. **No Download in Loaders**: Keep as separate preprocessing step
3. **Single Template per Conversion**: Simple 1:1 mapping
4. **Explicit Imports**: Better debugging and clarity
5. **Validation Separate**: Clear separation of concerns

This architecture balances simplicity with extensibility, making it easy to start development while supporting future growth.
