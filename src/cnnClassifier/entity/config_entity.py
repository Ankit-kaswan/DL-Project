from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    unzip_dir: str
    required_files: List[str]


@dataclass
class DataTransformationConfig:
    train_dir: str
    test_dir: str
    image_size: tuple
    batch_size: int
