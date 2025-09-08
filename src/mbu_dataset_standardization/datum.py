"""
Data Structures for MBU Dataset Standardization

This module defines the core data structures used throughout the conversion pipeline:
- StandardizedAnnotations: Unified annotation interface that all loaders produce
- RawDataPoint: Intermediate structure from loaders to templates
- QuestionAnswer: Individual Q&A pairs within datum
- Datum: Complete output structure matching unified schema

Uses Pydantic for robust validation, automatic JSON serialization, and schema compliance.
The standardized label interface ensures templates can work reliably across
different dataset formats and task types.
"""

from typing import List, Optional, Dict, Any, Union, Literal
from pydantic import BaseModel, Field


# Task type constants for consistency
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


class DatumHeader(BaseModel):
    """Header section of the datum schema with required fields."""
    image_id: str
    image_name: str
    domain: Literal["Ophthalmology", "Radiology", "Dermatology", "Pathology", "Surgery", "Other-Medical"]
    subdomain: Optional[str] = None
    category: Optional[str] = None  # label_name for classification


class DatumDataset(BaseModel):
    """Dataset section with metadata about the source dataset."""
    name: str
    dataset_id: str
    tasks: List[Literal["Classification", "Segmentation", "Detection", "Landmarks", "Describe", "Ask&Answer", "Counting", "Grounding", "Retrieval"]]
    split: Literal["train", "val", "test", "other"]
    institution: Optional[str] = None
    license: Optional[str] = None
    path: str


class DatumQuality(BaseModel):
    """Quality control information."""
    expert_involved: Literal["yes", "no", "unknown"]
    qc_passed: Literal["yes", "no", "unknown"]
    notes: Optional[str] = None


class DatumImaging(BaseModel):
    """Imaging modality and acquisition details."""
    modality: Literal["CXR", "CT", "MRI", "US", "Fundus", "OCT", "WSI", "Photo", "Endoscopy", "Echo", "Other"]
    submodality: Optional[str] = None
    frames: int = 1
    view: Optional[str] = None
    body_part: Optional[Literal["head", "neck", "chest", "abdomen", "pelvis", "upper_limb", "lower_limb", "skin", "oral", "dental", "cardiac", "fetal", "other"]] = None
    eye_part: Optional[str] = None


class DatumGeometry(BaseModel):
    """Geometric annotations (bounding boxes, polygons, etc.)."""
    bbox: Optional[List[List[float]]] = None  # [[x1, y1, x2, y2], ...]
    polygons: Optional[List[List[List[float]]]] = None  # [[[x, y], ...], ...]
    image_size: Optional[List[int]] = None  # [W, H]


class DatumProvenance(BaseModel):
    """Provenance tracking for question-answer pairs."""
    original_label: Optional[str] = None
    rule_id: Optional[str] = None
    annotation_id: Optional[str] = None
    created_by: Literal["human", "program"] = "program"


class SpatialReference(BaseModel):
    """
    Spatial reference linking a question to specific regions in the image.
    
    This enables questions like "What does the highlighted region show?" 
    where specific regions (masks, bboxes, polygons) are referenced.
    """
    reference_type: Literal["bbox", "polygon", "mask", "point", "multiple_regions"]
    
    # Geometric coordinates (relative [0,1] coordinates)
    bbox: Optional[List[float]] = None  # [x1, y1, x2, y2] for single bbox
    polygon: Optional[List[List[float]]] = None  # [[x, y], ...] for single polygon
    point: Optional[List[float]] = None  # [x, y] for single point
    
    # For multiple regions (e.g., instance segmentation with multiple instances)
    multiple_bboxes: Optional[List[List[float]]] = None  # [[x1, y1, x2, y2], ...]
    multiple_polygons: Optional[List[List[List[float]]]] = None  # [[[x, y], ...], ...]
    
    # Reference to original annotation
    annotation_id: Optional[str] = None  # ID of the original annotation being referenced
    instance_ids: Optional[List[str]] = None  # For multiple instances (instance segmentation)
    
    # Description of highlighting method
    highlighting_method: Literal["overlay", "outline", "fill", "arrow", "none"] = "overlay"
    
    # Optional visual properties for highlighting
    highlight_color: Optional[str] = None  # e.g., "red", "#FF0000"
    highlight_opacity: Optional[float] = None  # 0.0 to 1.0


class StandardizedAnnotations(BaseModel):
    """
    Unified label interface that all dataset loaders must produce.
    
    This structure works across binary, multi-class, and multi-label tasks,
    providing both convenience fields and provenance tracking.
    """
    # Task identification
    task_type: str
    
    # Core classification labels
    target_classes: List[str]
    active_classes: List[str]
    
    # Task-specific convenience fields
    is_positive: Optional[bool] = None
    primary_class: Optional[str] = None
    class_probabilities: Optional[Dict[str, float]] = None
    
    # Provenance and metadata
    original_labels: Any = None
    label_source: str = "unknown"
    confidence: Optional[str] = None
    annotator_info: Optional[Dict] = None


class RawDataPoint(BaseModel):
    """
    Intermediate data structure produced by loaders.
    
    Contains one data point (image + annotations + metadata) in standardized format
    that templates can reliably process.
    """
    image_path: str
    image_id: str
    annotations: StandardizedAnnotations
    metadata: Dict[str, Any] = Field(default_factory=dict)
    split: str


class QuestionAnswer(BaseModel):
    """
    Individual Q&A pair structure matching the datum schema.
    
    This represents one question-answer pair that will be included
    in the final datum's questions_and_answers array.
    """
    qa_id: str
    task: Literal["Classification", "Segmentation", "Detection", "Landmarks", "Describe", "Ask&Answer", "Counting", "Grounding", "Retrieval"]
    question: str
    answer: Union[str, int, List[str]]
    answer_type: Literal["yes_no", "single_label", "multi_label", "ordinal", "number", "span", "bbox", "options"]
    
    # Optional fields
    options: Optional[List[str]] = None
    difficulty: Literal["easy", "medium", "hard"] = "easy"
    uncertainty: Literal["certain", "uncertain", "unknown"] = "certain"
    answer_confidence: Optional[float] = None
    rationale: Optional[str] = None
    provenance: Optional[DatumProvenance] = None
    
    # NEW: Spatial reference for region-specific questions
    spatial_reference: Optional[SpatialReference] = None


class Datum(BaseModel):
    """
    Complete output structure matching the unified datum schema.
    
    This is the final JSON object that gets written to the JSONL output file.
    All sections must be populated according to the schema in instructions/datum_schema.md
    """
    # Required sections with structured validation
    header: DatumHeader
    dataset: DatumDataset
    quality: DatumQuality
    imaging: DatumImaging
    geometry: DatumGeometry
    questions_and_answers: List[QuestionAnswer] = Field(alias="questions-and-answers")
    
    # Optional/customizable sections
    domain_specific: Optional[Dict[str, Any]] = Field(None, alias="domain-specific")
    version: str = "v1.0"
    
    model_config = {"populate_by_name": True}  # Allow both field names and aliases
