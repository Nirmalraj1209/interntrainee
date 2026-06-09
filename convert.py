import pandas as pd

data = pd.read_csv("data.txt")
data.to_excel("output.xlsx", index=False)
print("Excel file created!")