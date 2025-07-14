# scripts/pandas_stats.py
import pandas as pd

# Update with your actual path
df = pd.read_csv('/Users/student/Desktop/ResearchAnalystTasks/Task_4/period_03/2024_fb_ads_president_scored_anon.csv')

print("✅ Data Loaded")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

# ===== BASIC STATS =====
print("\n--- DESCRIPTIVE STATS ---")
print(df.describe(include='all'))

# ===== UNIQUE VALUES & FREQUENCIES =====
print("\n--- UNIQUE VALUE COUNTS ---")
print(df.nunique())

print("\n--- MOST FREQUENT VALUES ---")
for col in df.select_dtypes(include='object').columns:
    print(f"{col}: {df[col].value_counts().head(1).to_dict()}")

# ===== GROUPED STATS =====
print("\n--- GROUP BY `page_id` ---")
print(df.groupby("page_id").size().head())

if "ad_id" in df.columns:
    print("\n--- GROUP BY `page_id`, `ad_id` ---")
    print(df.groupby(["page_id", "ad_id"]).size().head())