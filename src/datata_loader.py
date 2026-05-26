import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    SELECTED_COLUMNS = ["v101", "sregion", "v025", "v190", "v106", "v113", "v127", "v128",
                    "v136", "v137", "b4", "b8", "h71", "ml0", "ml1"]
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_data(self):
        try:
            if self.file_path.exists():
                data = pd.read_stata(self.file_path, columns=self.SELECTED_COLUMNS)
                return data
            else:
                raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            raise
