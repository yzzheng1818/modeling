import os
from pathlib import Path

proj_dir = Path(__file__).parent.parent

# =========================================================================#
#                         DATA FILE NAMES                                  #
# =========================================================================#

RAW_DF_FILE = ".parquet"
CLEANED_DF_FILE = ".parquet"

# =========================================================================#
#                            DATA FOLDERS                                 #
# =========================================================================#

DATA_DIR = proj_dir / 'data'

RAW_DATA_DIR = DATA_DIR / "10_raw"
CLEANED_DATA_DIR =  DATA_DIR /"20_cleaned"

MODEL_DIR = proj_dir / 'models'
