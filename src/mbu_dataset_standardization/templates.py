"""
Question Generation Templates for MBU Dataset Standardization

This module contains template implementations that generate questions and answers
from standardized data points. Templates are organized by task type and difficulty level.

Each template is responsible for:
- Checking compatibility with dataset labels
- Generating appropriate questions for the task type
- Creating correct answers based on standardized labels
- Filling non-QA sections of the datum structure
- Providing provenance information

All templates inherit from BaseTemplate and implement the standardized interface.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

from mbu_dataset_standardization.datum import RawDataPoint, QuestionAnswer, StandardizedLabels


class BaseTemplate(ABC):
    """
    Abstract base class for all question generation templates.
    
    Defines the standard interface that all templates must implement.
    This ensures consistent template behavior across different task types.
    """
    
    # Template metadata (override in subclasses)
    template_id: str = "base_template"
    task_type: str = "classification"
    difficulty: str = "easy"  # "easy", "medium", "hard"
    supported_task_types: List[str] = []
    
    @abstractmethod
    def generate_qa(self, raw_data: RawDataPoint, dataset_meta: Dict[str, Any]) -> QuestionAnswer:
        """
        Generate a single question-answer pair from raw data.
        
        Args:
            raw_data: Standardized data point from loader
            dataset_meta: Dataset-level metadata
            
        Returns:
            QuestionAnswer: Generated Q&A pair with provenance
        """
        pass
    
    @abstractmethod
    def fill_datum_sections(self, raw_data: RawDataPoint, dataset_meta: Dict[str, Any]) -> Dict[str, Any]:
        """
        Fill the non-QA sections of the datum structure.
        
        Args:
            raw_data: Standardized data point from loader
            dataset_meta: Dataset-level metadata
            
        Returns:
            Dict containing header, dataset, quality, imaging, geometry sections
        """
        pass
    
    def is_compatible(self, labels: StandardizedLabels) -> bool:
        """
        Check if this template can handle the given labels.
        
        Args:
            labels: Standardized labels from loader
            
        Returns:
            bool: True if template is compatible
        """
        return labels.task_type in self.supported_task_types
    
    def _create_provenance(self, raw_data: RawDataPoint) -> Dict[str, Any]:
        """Helper method to create provenance information."""
        return {
            "original_label": raw_data.labels.original_labels,
            "rule_id": self.template_id,
            "annotation_id": None,
            "created_by": "program"
        }


# TODO: Add concrete template implementations here once template designs are finalized
# Templates will be organized by task type and difficulty:
# - Binary classification templates (easy, medium, hard)
# - Multi-class classification templates (easy, medium, hard)  
# - Multi-label classification templates (easy, medium, hard)
# Each template should inherit from BaseTemplate and implement all abstract methods
