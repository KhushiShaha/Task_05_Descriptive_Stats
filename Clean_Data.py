import pandas as pd

# Load dataset
df = pd.read_csv("raw_data.csv") 

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Print column names for debug
print("Column names:", df.columns.tolist())

# Drop rows missing key data
df.dropna(subset=["player", "goals"], inplace=True)

# Convert goals to integer
df["goals"] = df["goals"].astype(int)

# Save cleaned data
df.to_csv("womens_lax_data.csv", index=False)
