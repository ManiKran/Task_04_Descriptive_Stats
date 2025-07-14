# scripts/polars_stats.py

import polars as pl

df = pl.read_csv('/path/to/your/dataset.csv')

print("✅ Data Loaded")
print("Shape:", df.shape)
print("Columns:", df.columns)

# ===== DESCRIPTIVE STATS =====
print("\n--- DESCRIPTIVE STATS ---")
print(df.describe())

# ===== UNIQUE VALUES =====
print("\n--- UNIQUE VALUE COUNTS ---")
for col in df.columns:
    print(f"{col}: {df[col].n_unique()}")

# ===== GROUPED STATS =====
print("\n--- GROUP BY `page_id` ---")
if "page_id" in df.columns:
    print(df.groupby("page_id").count().head())

if "ad_id" in df.columns:
    print("\n--- GROUP BY `page_id`, `ad_id` ---")
    print(df.groupby(["page_id", "ad_id"]).count().head())