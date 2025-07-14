import csv
import statistics
from collections import defaultdict, Counter
from time import time

# ====== CONFIGURATION ======
CSV_FILE = '/Users/student/Desktop/ResearchAnalystTasks/Task_4/period_03/2024_fb_ads_president_scored_anon.csv'

# ====== STEP 1: LOAD DATA ======
with open(CSV_FILE, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)
    columns = reader.fieldnames

print(f"Loaded {len(data)} rows and {len(columns)} columns")

# ====== STEP 2: INITIATE STATS CONTAINERS ======
numeric_cols = []
non_numeric_cols = []
sample_row = data[0]

# Separate numeric and non-numeric
for col in columns:
    try:
        float(sample_row[col])
        numeric_cols.append(col)
    except:
        non_numeric_cols.append(col)

numeric_stats = {}
non_numeric_stats = {}

# ====== STEP 3: NUMERIC COLUMN STATS ======
for col in numeric_cols:
    try:
        values = [float(row[col]) for row in data if row[col].strip() != '']
        numeric_stats[col] = {
            'count': len(values),
            'mean': round(statistics.mean(values), 2),
            'min': min(values),
            'max': max(values),
            'stdev': round(statistics.stdev(values), 2) if len(values) > 1 else 0
        }
    except:
        pass

# ====== STEP 4: NON-NUMERIC COLUMN STATS ======
for col in non_numeric_cols:
    values = [row[col] for row in data if row[col].strip() != '']
    counter = Counter(values)
    non_numeric_stats[col] = {
        'unique_count': len(set(values)),
        'most_frequent': counter.most_common(1)[0] if counter else ('N/A', 0)
    }

# ====== STEP 5: PRINT RESULTS ======
print("\n--- NUMERIC COLUMNS STATS ---")
for k, v in numeric_stats.items():
    print(f"{k}: {v}")

print("\n--- NON-NUMERIC COLUMNS STATS ---")
for k, v in non_numeric_stats.items():
    print(f"{k}: {v}")