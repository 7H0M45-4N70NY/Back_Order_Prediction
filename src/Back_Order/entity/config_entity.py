from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_path : str
    local_file_dir : Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    target : Path
    result: str
    all_schema:dict
@dataclass(frozen=True)  
class DataTransfomrationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    target_column: str
    n_estimators: float
    min_samples_split:float
    min_samples_leaf:float
    max_samples:float
    max_depth:float
    criterion:str
    ccp_alpha:float    

    