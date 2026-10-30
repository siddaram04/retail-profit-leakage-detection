import pandas as pd

df = pd.read_excel("data/RAW/sample_superstore.xls")

#check profit data quality

#print("missing profit:", df['Profit'].isnull().sum())
#print("negative profit:", (df['Profit'] < 0).sum())
#print("zero profit:", (df['Profit'] == 0).sum())

print(df.duplicated().sum())
print(df.isnull().sum())