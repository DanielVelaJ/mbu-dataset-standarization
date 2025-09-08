"""
Dataset Loaders for MBU Dataset Standardization

This module contains dataset-specific loading implementations that convert
raw dataset formats into standardized RawDataPoint structures.

Each loader is responsible for:
- Parsing dataset-specific file formats (CSV, folder structure, etc.)
- Converting annotations to StandardizedAnnotations format
- Determining task type and dataset metadata
- Handling train/val/test splits

All loaders inherit from BaseLoader and implement the standardized interface.
"""

from abc import ABC, abstractmethod
from typing import Iterator, Dict, Any

from mbu_dataset_standardization.datum import RawDataPoint, StandardizedAnnotations


class BaseLoader(ABC):
    """
    Abstract base class for all dataset loaders.
    
    Defines the standard interface that all loaders must implement.
    This ensures templates can work with any dataset loader consistently.
    """
    
    @abstractmethod
    def load_raw_data(self, data_dir: str) -> Iterator[RawDataPoint]:
        """
        Load raw data points from the dataset directory.
        
        Args:
            data_dir: Path to the dataset directory
            
        Yields:
            RawDataPoint: Standardized data points ready for template processing
        """
        pass
    
    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        """
        Return dataset-level metadata for populating datum.dataset section.
        
        Returns:
            Dict containing dataset name, institution, license, etc.
        """
        pass
    
    @abstractmethod
    def normalize_annotations(self, raw_annotations: Any, **context) -> StandardizedAnnotations:
        """
        Convert dataset-specific annotations to standardized format.
        
        Args:
            raw_annotations: Annotations in dataset's native format
            **context: Additional context (image_path, metadata, etc.)
            
        Returns:
            StandardizedAnnotations: Converted annotations with task_type and standardized fields
        """
        pass
    
    def get_class_definitions(self) -> Dict[str, str]:
        """
        Return all possible classes and their descriptions.
        
        Returns:
            Dict mapping class names to human-readable descriptions
        """
        return {}
    
    def _determine_split(self, image_id: str, split_info: Dict = None) -> str:
        """
        Helper method to determine train/val/test split for an image.
        
        Args:
            image_id: Unique identifier for the image
            split_info: Optional split information (depends on dataset)
            
        Returns:
            Split name: "train", "val", "test", or "other"
        """
        return "other"  # Default fallback


# TODO: Add concrete loader implementations here once datasets are chosen
# Each loader should inherit from BaseLoader and implement all abstract methods
