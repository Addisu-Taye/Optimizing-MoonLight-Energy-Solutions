
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore
import os

# Load data
df = pd.read_csv("data/raw/sierraleone-bumbuna.csv", parse_dates=["Timestamp"])
print(f"Original shape: {df.shape}")

# Drop unused columns
if "Comments" in df.columns:
    df.drop(columns=["Comments"], inplace=True)

# Fill missing with median in numeric columns
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Missing values
missing = df.isna().sum()
missing_percent = (missing / len(df)) * 100
print("\nMissing value report (>5%):")
print(missing_percent[missing_percent > 5])

# Outlier detection
core_cols = ["GHI", "DNI", "DHI", "ModA", "ModB", "WS", "WSgust"]
z_scores = df[core_cols].apply(zscore)
df_clean = df[(np.abs(z_scores) <= 3).all(axis=1)]
print(f"After removing outliers: {df_clean.shape}")

# Save cleaned data
os.makedirs("data/cleaned", exist_ok=True)
df_clean.to_csv("data/cleaned/sierraleone_clean.csv", index=False)

# Create output directory for plots
os.makedirs("figures", exist_ok=True)

# Time series plot
df_clean.set_index("Timestamp")[["GHI", "DNI", "DHI", "Tamb"]].resample("D").mean().plot(figsize=(15, 5))
plt.title("Sierra Leone - Daily Solar Irradiance & Ambient Temp")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/sierraleone_timeseries.png")
plt.close()

# Cleaning impact
df_clean.groupby("Cleaning")[["ModA", "ModB"]].mean().plot(kind="bar", title="Sierra Leone - Cleaning Impact on ModA & ModB")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/sierraleone_cleaning_impact.png")
plt.close()

# Correlation heatmap
corr_cols = ["GHI", "DNI", "DHI", "TModA", "TModB"]
sns.heatmap(df_clean[corr_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Sierra Leone - Correlation Heatmap")
plt.tight_layout()
plt.savefig("figures/sierraleone_correlation.png")
plt.close()

# Scatter plots
sns.scatterplot(data=df_clean, x="WS", y="GHI")
plt.title("WS vs GHI")
plt.tight_layout()
plt.savefig("figures/sierraleone_ws_vs_ghi.png")
plt.close()

sns.scatterplot(data=df_clean, x="RH", y="Tamb")
plt.title("RH vs Tamb")
plt.tight_layout()
plt.savefig("figures/sierraleone_rh_vs_tamb.png")
plt.close()

# Histograms
df_clean[["GHI", "WS"]].hist(bins=30, figsize=(10, 4))
plt.suptitle("Sierra Leone - GHI and Wind Speed Distribution")
plt.tight_layout()
plt.savefig("figures/sierraleone_histograms.png")
plt.close()

# Bubble chart
plt.scatter(df_clean["Tamb"], df_clean["GHI"], s=df_clean["RH"], alpha=0.5, c="orange")
plt.xlabel("Ambient Temperature (°C)")
plt.ylabel("GHI (W/m²)")
plt.title("Sierra Leone - GHI vs Tamb (Bubble size = RH)")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/sierraleone_bubble_chart.png")
plt.close()
