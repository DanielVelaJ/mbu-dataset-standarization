"""
Data Structures for MBU Dataset Standardization

This module defines the core data structures used throughout the conversion pipeline:
- StandardizedLabels: Unified label interface that all loaders produce
- RawDataPoint: Intermediate structure from loaders to templates
- QuestionAnswer: Individual Q&A pairs within datum
- Datum: Complete output structure matching unified schema

Uses Pydantic for robust validation, automatic JSON serialization, and schema compliance.
The standardized label interface ensures templates can work reliably across
different dataset formats and task types.
"""

from typing import List, Optional, Dict, Any, Union
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


class StandardizedLabels(BaseModel):
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
    
    Contains one data point (image + labels + metadata) in standardized format
    that templates can reliably process.
    """
    image_path: str
    image_id: str
    labels: StandardizedLabels
    metadata: Dict[str, Any] = Field(default_factory=dict)
    split: str


class QuestionAnswer(BaseModel):
    """
    Individual Q&A pair structure matching the datum schema.
    
    This represents one question-answer pair that will be included
    in the final datum's questions_and_answers array.
    """
    qa_id: str
    task: str
    question: str
    answer: Union[str, int, List[str]]
    answer_type: str
    
    # Optional fields
    options: Optional[List[str]] = None
    difficulty: str = "easy"
    uncertainty: str = "certain"
    answer_confidence: Optional[float] = None
    rationale: Optional[str] = None
    provenance: Optional[Dict[str, Any]] = None


class Datum(BaseModel):
    """
    Complete output structure matching the unified datum schema.
    
    This is the final JSON object that gets written to the JSONL output file.
    All sections must be populated according to the schema in instructions/datum_schema.md
    """
    # Required sections
    header: Dict[str, Any]
    dataset: Dict[str, Any]
    quality: Dict[str, Any]
    imaging: Dict[str, Any]
    geometry: Dict[str, Any]
    questions_and_answers: List[QuestionAnswer] = Field(alias="questions-and-answers")
    
    # Optional/customizable sections
    domain_specific: Optional[Dict[str, Any]] = Field(None, alias="domain-specific")
    version: str = "v1.0"
    
    model_config = {"populate_by_name": True}  # Allow both field names and aliases
