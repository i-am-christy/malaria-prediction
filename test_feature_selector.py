from src.data_loader import DataLoader
from src.preprocessor import Preprocessor
from src.feature_selector import FeatureSelector

loader = DataLoader("data/raw/NGPR81FL.DTA")
df = loader.load()
preprocessor = Preprocessor(df)
df = preprocessor.preprocessor(df)
selector = FeatureSelector(df)
df_selected = selector.select()

features = [c for c in df_selected.columns if c != "rdt_result"]
print(f"Total features: {len(features)}")
print(features)
