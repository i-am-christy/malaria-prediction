from src.data_loader import DataLoader

loader = DataLoader(r"data\raw\NGPR81FL.DTA")
df = loader.load()

print(df.head())
print(df.dtypes)


#explore rdt result
print("Exploring the rdt_result field")
print(df["rdt_result"].value_counts(dropna=False))

#explore net_type
print("Exploring the net_type field")
print(df["net_type"].value_counts(dropna=False))

#check for missing values
print("Checking for missing values")
print(df.isnull().sum())