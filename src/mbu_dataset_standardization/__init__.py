"""
MBU Dataset Standardization Package

A pipeline for converting biomedical datasets into MCVQA (Medical Computer Vision Question Answering) format
using standardized templates and a unified datum schema.

This package provides:
- Dataset loaders for various biomedical datasets
- Question generation templates for different task types
- Standardized data structures and validation
- Conversion orchestration tools

Usage:
    from mbu_dataset_standardization.convert import convert_dataset
    
    convert_dataset(
        dataset_name="chest_xray_14",
        template_name="binary_1", 
        data_dir="data/chest_xray_14/",
        output_path="output/chest_xray_14_binary_1.jsonl"
    )
"""

__version__ = "0.1.0"
__author__ = "MBU Project Team"

# Core imports for public API
from mbu_dataset_standardization.datum import Datum, QuestionAnswer, StandardizedLabels, RawDataPoint
from mbu_dataset_standardization.convert import convert_dataset

__all__ = [
    "Datum",
    "QuestionAnswer", 
    "StandardizedLabels",
    "RawDataPoint",
    "convert_dataset",
]
