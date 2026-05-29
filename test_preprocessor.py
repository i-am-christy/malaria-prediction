from src.preprocessor import Preprocessor
from src.data_loader import DataLoader

loader = DataLoader(r"data\raw\NGPR81FL.DTA")
df = loader.load()

preprocessor = Preprocessor(df)
df_processed = preprocessor.preprocessor(df)

print(f"\nShape of the processed dataframe: {df_processed.shape}")
print("\nTarget Distribution")
print(df_processed["rdt_result"].value_counts())
print(f"\nTotal missing values: {df_processed.isnull().sum().sum()}")
print(f"\nColumns: {df_processed.columns.tolist()}")