import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class FeatureSelector:
    def __init__(self, df):
        self.df = df
        self.selected_features = None

    def select(self):
        X = self.df.drop(columns=["rdt_result"])
        y = self.df["rdt_result"]
        
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(X, y)
        
        importances = pd.Series(rf.feature_importances_, index=X.columns)
        self.selected_features = importances[importances > 0.01].index.tolist()
        
        print(f"Features selected: {len(self.selected_features)} out of {len(X.columns)}")
        return self.df[self.selected_features + ["rdt_result"]]