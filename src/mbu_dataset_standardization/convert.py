"""
Main Conversion Orchestrator for MBU Dataset Standardization

This module contains the main conversion logic that coordinates the entire
pipeline from raw datasets to MCVQA format output.

Key components:
- Loader and template registries (manual dictionaries)
- Main conversion function that orchestrates the pipeline
- Compatibility validation between loaders and templates
- Output generation and validation

Usage:
    from mbu_dataset_standardization.convert import convert_dataset
    
    convert_dataset(
        dataset_name="example_dataset",
        template_name="binary_1",
        data_dir="data/example_dataset/",
        output_path="output/example_dataset_binary_1.jsonl"
    )
"""

from typing import Dict, Type

from mbu_dataset_standardization.loaders import BaseLoader
from mbu_dataset_standardization.templates import BaseTemplate
from mbu_dataset_standardization.datum import Datum


# Manual registries for loaders and templates
# TODO: Populate these once concrete implementations are created
LOADERS: Dict[str, Type[BaseLoader]] = {
    # "example_dataset": ExampleLoader,
}

TEMPLATES: Dict[str, Type[BaseTemplate]] = {
    # Domain-first naming convention:
    # "agnostic_classification_binary_1": AgnosticBinaryTemplate1,
    # "agnostic_classification_binary_2": AgnosticBinaryTemplate2,
    # "radiology_classification_binary_1": RadiologyBinaryTemplate1,
    # "dermatology_classification_binary_1": DermatologyBinaryTemplate1,
}


def convert_dataset(dataset_name: str, template_name: str, 
                   data_dir: str, output_path: str) -> None:
    """
    Convert a dataset using specified template to MCVQA format.
    
    This is the main entry point for the conversion pipeline. It coordinates
    the entire process from loading raw data to writing standardized output.
    
    Args:
        dataset_name: Name of the dataset (must be in LOADERS registry)
        template_name: Name of the template (must be in TEMPLATES registry)
        data_dir: Path to the dataset directory
        output_path: Path where JSONL output should be written
        
    Raises:
        ValueError: If dataset_name or template_name not found in registries
        ValueError: If template is not compatible with dataset
        FileNotFoundError: If data_dir doesn't exist or is invalid
    """
    # TODO: Implement conversion logic
    raise NotImplementedError("convert_dataset function not yet implemented")


def validate_compatibility(loader: BaseLoader, template: BaseTemplate) -> bool:
    """
    Check if a template is compatible with a dataset loader.
    
    Args:
        loader: Dataset loader instance
        template: Template instance
        
    Returns:
        bool: True if compatible, False otherwise
    """
    # TODO: Implement compatibility validation
    raise NotImplementedError("validate_compatibility function not yet implemented")


def list_available_datasets() -> list[str]:
    """
    List all available dataset loaders.
    
    Returns:
        List of dataset names that can be used with convert_dataset()
    """
    return list(LOADERS.keys())


def list_available_templates() -> list[str]:
    """
    List all available templates.
    
    Returns:
        List of template names that can be used with convert_dataset()
    """
    return list(TEMPLATES.keys())


def get_dataset_info(dataset_name: str) -> Dict:
    """
    Get metadata information about a dataset.
    
    Args:
        dataset_name: Name of the dataset
        
    Returns:
        Dict containing dataset metadata
        
    Raises:
        ValueError: If dataset_name not found
    """
    # TODO: Implement dataset info retrieval
    raise NotImplementedError("get_dataset_info function not yet implemented")


def get_template_info(template_name: str) -> Dict:
    """
    Get information about a template.
    
    Args:
        template_name: Name of the template
        
    Returns:
        Dict containing template metadata (task_type, difficulty, etc.)
        
    Raises:
        ValueError: If template_name not found
    """
    # TODO: Implement template info retrieval
    raise NotImplementedError("get_template_info function not yet implemented")
