import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configure the page
st.set_page_config(page_title="Students' Social Media Addiction", layout="wide")

# App title and intro
st.title("📱 Students' Social Media Addiction Dashboard")
st.markdown("""
This interactive dashboard displays data collected from students about their 
social media usage, sleep habits, and self-rated addiction scores.
""")

# Load the dataset
df = pd.read_csv("Students Social Media Addiction.csv")

# Data preview
st.subheader("👀 Dataset Preview")
st.dataframe(df.head())

# Plot 1 – Histogram: Avg Daily Usage Hours
st.subheader("📊 Daily Social Media Usage (Hours)")
fig1, ax1 = plt.subplots()
sns.histplot(data=df, x='Avg_Daily_Usage_Hours', bins=10, kde=True, ax=ax1)
ax1.set_title("Distribution of Daily Social Media Usage")
ax1.set_xlabel("Usage Hours")
ax1.set_ylabel("Number of Students")
st.pyplot(fig1)

# Plot 2 – Boxplot: Addiction Score by Gender
st.subheader("🧠 Addiction Score by Gender")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='Gender', y='Addicted_Score', palette='coolwarm', ax=ax2)
ax2.set_title("Addiction Score by Gender")
ax2.set_xlabel("Gender")
ax2.set_ylabel("Addiction Score")
st.pyplot(fig2)

# Plot 3 – Lineplot: Sleep vs Addiction Score
st.subheader("💤 Sleep Hours vs Addiction Score")
fig3, ax3 = plt.subplots()
sns.lineplot(data=df, x='Sleep_Hours_Per_Night', y='Addicted_Score', ax=ax3)
ax3.set_title("Sleep Hours vs. Addiction Score")
ax3.set_xlabel("Sleep Hours")
ax3.set_ylabel("Addiction Score")
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("🚀 Created with ❤️ by Maria & Team – Reichman University 2025")
