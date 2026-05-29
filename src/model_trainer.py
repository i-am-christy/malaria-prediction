import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_validate
from imblearn.over_sampling import SMOTE
import joblib

class ModelTrainer:
    def __init__(self, df):
        self.df = df
        self.models = {
            "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
            "Decision Tree": DecisionTreeClassifier(random_state=42),
            "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
        }
        self.results = {}
        self.trained_models = {}

    def get_X_y(self):
        X = self.df.drop(columns=["rdt_result"])
        y = self.df["rdt_result"]
        return X, y

    def apply_smote(self, X, y):
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X, y)
        print(f"After SMOTE — Positive: {y_resampled.sum()}, Negative: {(y_resampled==0).sum()}")
        return X_resampled, y_resampled

    def train(self):
        X, y = self.get_X_y()
        X, y = self.apply_smote(X, y)
        cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
        
        for name, model in self.models.items():
            print(f"Training {name}...")
            scores = cross_validate(model, X, y, cv=cv,
                                    scoring=["accuracy","precision","recall","f1","roc_auc"])
            self.results[name] = {
                "accuracy":  scores["test_accuracy"].mean(),
                "precision": scores["test_precision"].mean(),
                "recall":    scores["test_recall"].mean(),
                "f1":        scores["test_f1"].mean(),
                "roc_auc":   scores["test_roc_auc"].mean()
            }
            model.fit(X, y)
            self.trained_models[name] = model
            print(f"{name} done — F1: {self.results[name]['f1']:.3f}")
        
        return self.results, self.trained_models

    def save_models(self, output_dir="models/"):
        for name, model in self.trained_models.items():
            filename = f"{output_dir}{name.replace(' ', '_')}.pkl"
            joblib.dump(model, filename)
            print(f"Saved: {filename}")