import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    SELECTED_COLUMNS = ["hv024", "shregion", "hv025", "hv270",
                         "hv201", "hv213", "hv214", "hv215", 
                         "hv009", "hv014", "hv206", "hv104", 
                         "hv105", "hml12",  "hml35"]
    
    COLUMN_RENAME = {
        "hv024": "state",
        "shregion": "geopolitical_zone",
        "hv025": "residence_type",
        "hv270": "wealth_index", 
        "hv201": "water_source", 
        "hv213": "floor_material",
        "hv214": "wall_material",
        "hv215": "roof_material",
        "hv009": "household_size",
        "hv014": "children_under5",
        "hv206": "has_electricity",
        "hv104": "sex",
        "hv105": "age",
        "hml12": "net_type",
        "hml35": "rdt_result"
    }

    #initializes the class and validatest the file path
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
    
    #loads the data from the specified file path and handles errors
    def load_data(self):
        try:
            data = pd.read_stata(self.file_path, columns=self.SELECTED_COLUMNS, convert_categoricals=False)
            return data
        except (pd.errors.ParserError, OSError, ValueError) as e:
            print(f"An error occurred while loading the data: {e}")
            raise
    
    #renames the df columns for readbility
    def rename_columns(self, df):
        df = df.rename(columns=self.COLUMN_RENAME)
        return df
    
    #ochestrator, clean entry point for the rest of the pipeline
    def load(self):
        data = self.load_data()
        print(f"Data has been loaded successfully with shape {data.shape}")
        data = self.rename_columns(data)
        print(f"Columns have been renamed successfully")
        return data