import pandas as pd
import numpy as np

class Preprocessor:
    def __init__(self, df):
        self.df = df

    def filter_result(self, df):
        # Filter out rows where 'rdt_result' is 1
        filtered_df = df[df['rdt_result'].notna()]
        filtered_df = filtered_df[filtered_df['rdt_result'].isin([0.0, 1.0])]
        return filtered_df
    
    def create_target(self, df):
        df['rdt_result'] = df['rdt_result'].apply(lambda x: 1 if x == 1.0 else 0 )
        return df
    
    def encode_features(self, df):
        NOMINAL_COLS = ["state", "geopolitical_zone", "residence_type", "water_source",
                        "floor_material", "wall_material", "roof_material", "sex", "has_electricity"]
        df_numeric = df.drop(columns= NOMINAL_COLS + ["rdt_result"])
        df_encoded = pd.get_dummies(df[NOMINAL_COLS].astype(str), drop_first=True)
        df_final = pd.concat([df_encoded, df_numeric], axis=1)
        df_final["rdt_result"] = df["rdt_result"]
        return df_final
    
    def preprocessor(self, df):
        df = self.filter_result(df)
        df = self.create_target(df)
        df = self.encode_features(df)
        return df