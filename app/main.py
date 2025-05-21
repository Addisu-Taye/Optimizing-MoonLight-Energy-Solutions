import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Data Comparison", layout="wide")

@st.cache_data
def load_data():
    benin = pd.read_csv("data/cleaned/benin_cleaned.csv", parse_dates=["Timestamp"])
    togo = pd.read_csv("data/cleaned/togo_cleaned.csv", parse_dates=["Timestamp"])
    sierra = pd.read_csv("data/cleaned/sierraleone_cleaned.csv", parse_dates=["Timestamp"])

    benin["Country"] = "Benin"
    togo["Country"] = "Togo"
    sierra["Country"] = "Sierra Leone"
    return pd.concat([benin, togo, sierra], ignore_index=True)

df = load_data()
st.title("🌍 Multi-Country Solar Data Dashboard")

# Country filter
countries = st.multiselect("Select Countries", df["Country"].unique(), default=df["Country"].unique())

filtered_df = df[df["Country"].isin(countries)]

# Summary
st.header("📊 Summary Statistics")
st.dataframe(filtered_df.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "std", "median"]))

# Boxplot
st.header("📦 Boxplots by Country")
col = st.selectbox("Select Metric", ["GHI", "DNI", "DHI"])
fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x="Country", y=col, ax=ax)
st.pyplot(fig)

# Monthly trend
st.header("📅 Monthly GHI Trends")
filtered_df["Month"] = filtered_df["Timestamp"].dt.month
monthly = filtered_df.groupby(["Country", "Month"])["GHI"].mean().reset_index()
fig2, ax2 = plt.subplots()
sns.lineplot(data=monthly, x="Month", y="GHI", hue="Country", marker="o", ax=ax2)
st.pyplot(fig2)

# Bubble chart
st.header("🫧 Bubble Chart: GHI vs Tamb (size=RH)")
sample_df = filtered_df.sample(n=1000, random_state=42)
fig3, ax3 = plt.subplots()
ax3.scatter(sample_df["Tamb"], sample_df["GHI"], s=sample_df["RH"], alpha=0.5)
ax3.set_xlabel("Tamb")
ax3.set_ylabel("GHI")
st.pyplot(fig3)

# Correlation matrix
st.header("🔥 Correlation Heatmap")
for country in countries:
    st.subheader(f"{country} Correlation")
    corr = df[df["Country"] == country][["GHI", "DNI", "DHI", "TModA", "TModB"]].corr()
    fig4, ax4 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax4)
    st.pyplot(fig4)
