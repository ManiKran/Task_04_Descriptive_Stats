# visualizations/visualizations.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/student/Desktop/ResearchAnalystTasks/Task_4/period_03/2024_fb_ads_president_scored_anon.csv')

# Histogram for numeric field
numeric_cols = df.select_dtypes(include='number').columns.tolist()
for col in numeric_cols:
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

# Bar plot for top categories
for col in df.select_dtypes(include='object').columns[:3]:
    df[col].value_counts().head(10).plot(kind='bar')
    plt.title(f'Top 10 values in {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
