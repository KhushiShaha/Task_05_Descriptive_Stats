import pandas as pd

# Load cleaned dataset
df = pd.read_csv("womens_lax_data.csv")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Debug: list all column names
print("Available columns:", df.columns.tolist())

# Compute number of games played
games_played = df['gp'].nunique()  # Use actual column name after inspecting

# Compute top scorer
top_scorer = df.groupby('player')['goals'].sum().idxmax()

print(f"Games Played: {games_played}")
print(f"Top Scorer: {top_scorer}")

# Save player stats summary
summary = df.groupby('player')[['goals', 'assists', 'turnovers']].sum()
summary.to_csv("player_summary.csv")