from .data_loader import DataLoader
from .preprocessor import Preprocessor
from .feature_selector import FeatureSelector
from .model_trainer import ModelTrainer
from .evaluator import Evaluator

class MalariaPipeline:
    def __init__(self, data_path):
        self.data_path = data_path

    def run(self):
        # Layer 1 - Load
        print("\n[1/5] Loading data...")
        loader = DataLoader(self.data_path)
        df = loader.load()

        # Layer 2 - Preprocess
        print("\n[2/5] Preprocessing...")
        preprocessor = Preprocessor(df)
        df = preprocessor.preprocessor(df)
        print(f"Processed shape: {df.shape}")

        # Layer 3 - Feature Selection
        print("\n[3/5] Selecting features...")
        selector = FeatureSelector(df)
        df = selector.select()
        print(f"Selected shape: {df.shape}")

        # Layer 4 - Train
        print("\n[4/5] Training models...")
        trainer = ModelTrainer(df)
        results, trained_models = trainer.train()
        trainer.save_models()

        # Layer 5 - Evaluate
        print("\n[5/5] Evaluating...")
        evaluator = Evaluator(results, trained_models, df)
        evaluator.evaluate()

        print("\nPipeline complete.")
        return results

if __name__ == "__main__":
    pipeline = MalariaPipeline("data/raw/NGPR81FL.DTA")
    pipeline.run()