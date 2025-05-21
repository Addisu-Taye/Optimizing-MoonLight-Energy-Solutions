import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configure the Streamlit app
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# Apply a consistent style
sns.set_theme(style="whitegrid")

# Load data from GitHub with caching
@st.cache_data
def load_data():
    base_url = "https://raw.githubusercontent.com/Addisu-Taye/Optimizing-MoonLight-Energy-Solutions/main/data/cleaned/"
   
    benin = pd.read_csv(base_url + "benin_cleaned.csv", parse_dates=["Timestamp"])
    togo = pd.read_csv(base_url + "togo_cleaned.csv", parse_dates=["Timestamp"])
    sierra = pd.read_csv(base_url + "sierraleone_cleaned.csv", parse_dates=["Timestamp"])

    benin["Country"] = "Benin"
    togo["Country"] = "Togo"
    sierra["Country"] = "Sierra Leone"
    
    return pd.concat([benin, togo, sierra], ignore_index=True)

# Load dataset
df = load_data()

# Title and intro
st.title("🌞 Solar Energy Monitoring Dashboard")
st.markdown("""
This dashboard provides a comparative view of solar radiation and climate parameters across **Benin**, **Togo**, and **Sierra Leone**.
Use the filters and visualizations below to explore the trends and variability of GHI, DNI, DHI, temperature, and humidity data.
""")

# Sidebar filters
st.sidebar.header("🔍 Filters")
countries = st.sidebar.multiselect("Select Country", df["Country"].unique(), default=df["Country"].unique())
metric = st.sidebar.selectbox("Metric for Boxplot", ["GHI", "DNI", "DHI"])
sample_size = st.sidebar.slider("Sample Size for Bubble Chart", min_value=100, max_value=3000, value=1000, step=100)

# Filter data
filtered_df = df[df["Country"].isin(countries)]

# Summary Section
st.subheader("📊 Summary Statistics")
summary_df = (
    filtered_df.groupby("Country")[["GHI", "DNI", "DHI"]]
    .agg(["mean", "std", "median"])
    .round(2)
)
st.dataframe(summary_df, use_container_width=True)

# Boxplot
st.subheader(f"📦 Distribution of {metric} by Country")
fig_box, ax_box = plt.subplots(figsize=(10, 4))
sns.boxplot(data=filtered_df, x="Country", y=metric, palette="Set2", ax=ax_box)
ax_box.set_title(f"{metric} Distribution", fontsize=14)
st.pyplot(fig_box)

# Monthly Trend Line
st.subheader("📅 Monthly Average GHI Trends")
filtered_df["Month"] = filtered_df["Timestamp"].dt.month
monthly_avg = filtered_df.groupby(["Country", "Month"])["GHI"].mean().reset_index()
fig_line, ax_line = plt.subplots(figsize=(10, 4))
sns.lineplot(data=monthly_avg, x="Month", y="GHI", hue="Country", marker="o", ax=ax_line)
ax_line.set_xticks(range(1, 13))
ax_line.set_title("Monthly GHI Averages", fontsize=14)
st.pyplot(fig_line)

# Bubble Chart
st.subheader("🫧 Bubble Chart: GHI vs Ambient Temp (Bubble = RH)")
sample_df = filtered_df.sample(n=min(sample_size, len(filtered_df)), random_state=42)
fig_bubble, ax_bubble = plt.subplots(figsize=(10, 5))
bubble = ax_bubble.scatter(sample_df["Tamb"], sample_df["GHI"], s=sample_df["RH"], alpha=0.5, c="tab:blue", edgecolors="w", linewidth=0.5)
ax_bubble.set_xlabel("Ambient Temperature (Tamb)")
ax_bubble.set_ylabel("Global Horizontal Irradiance (GHI)")
ax_bubble.set_title("Bubble Chart: GHI vs Tamb")
st.pyplot(fig_bubble)

# Correlation Heatmaps
st.subheader("🔥 Correlation Heatmaps")
for country in countries:
    st.markdown(f"**{country}**")
    corr = df[df["Country"] == country][["GHI", "DNI", "DHI", "TModA", "TModB"]].corr()
    fig_corr, ax_corr = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax_corr, cbar=False)
    ax_corr.set_title(f"{country} - Correlation Matrix")
    st.pyplot(fig_corr)

# Footer
st.markdown("---")
st.markdown("Developed by **Addisu Taye** | [GitHub Repo](https://github.com/Addisu-Taye/Optimizing-MoonLight-Energy-Solutions)")
