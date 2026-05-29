import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (classification_report, confusion_matrix,
                             roc_curve, auc)
import joblib

class Evaluator:
    def __init__(self, results, trained_models, df):
        self.results = results
        self.trained_models = trained_models
        self.df = df

    def print_results(self):
        print("\n" + "="*60)
        print("  MODEL EVALUATION RESULTS")
        print("="*60)
        for name, metrics in self.results.items():
            print(f"\n{name}")
            for metric, value in metrics.items():
                print(f"  {metric:<12}: {value:.4f}")
        print("="*60)

    def plot_confusion_matrices(self):
        X = self.df.drop(columns=["rdt_result"])
        y = self.df["rdt_result"]
        
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        for ax, (name, model) in zip(axes, self.trained_models.items()):
            cm = confusion_matrix(y, model.predict(X))
            sns.heatmap(cm, annot=True, fmt="d", ax=ax, cmap="Blues")
            ax.set_title(name)
            ax.set_xlabel("Predicted")
            ax.set_ylabel("Actual")
        plt.tight_layout()
        plt.savefig("outputs/confusion_matrices.png")
        print("Saved: outputs/confusion_matrices.png")

    def plot_roc_curves(self):
        X = self.df.drop(columns=["rdt_result"])
        y = self.df["rdt_result"]
        
        plt.figure(figsize=(8, 6))
        for name, model in self.trained_models.items():
            fpr, tpr, _ = roc_curve(y, model.predict_proba(X)[:, 1])
            roc_auc = auc(fpr, tpr)
            plt.plot(fpr, tpr, label=f"{name} (AUC={roc_auc:.3f})")
        
        plt.plot([0,1], [0,1], "k--")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC Curves")
        plt.legend()
        plt.savefig("outputs/roc_curves.png")
        print("Saved: outputs/roc_curves.png")

    def evaluate(self):
        self.print_results()
        self.plot_confusion_matrices()
        self.plot_roc_curves()