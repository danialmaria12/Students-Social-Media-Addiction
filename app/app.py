import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# App title and description
st.set_page_config(page_title="Tips Dataset Dashboard", layout="wide")
st.title("🍽️ Tips Dataset Visual Dashboard")
st.markdown("This app uses the **Seaborn `tips` dataset** to explore relationships between total bill, tip, gender, and time of day.")

# Load dataset
df = sns.load_dataset("tips")
st.subheader("👀 Dataset Preview")
st.dataframe(df.head())

# Plot 1 - Histogram of total bill
st.subheader("📊 Distribution of Total Bill")
fig1, ax1 = plt.subplots()
sns.histplot(data=df, x='total_bill', bins=20, kde=True, ax=ax1)
ax1.set_title("Distribution of Total Bill")
ax1.set_xlabel("Total Bill ($)")
ax1.set_ylabel("Number of Customers")
st.pyplot(fig1)

# Plot 2 - Boxplot of tips by gender
st.subheader("🧍‍♀️ Tip Amount by Gender")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='sex', y='tip', palette='pastel', ax=ax2)
ax2.set_title("Tip Amount by Gender")
ax2.set_xlabel("Gender")
ax2.set_ylabel("Tip Amount ($)")
st.pyplot(fig2)

# Plot 3 - Scatterplot of tip vs total bill, colored by time
st.subheader("🕒 Tip vs Total Bill (Lunch vs Dinner)")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x='total_bill', y='tip', hue='time', style='time', ax=ax3)
ax3.set_title("Tip vs Total Bill (Lunch vs Dinner)")
ax3.set_xlabel("Total Bill ($)")
ax3.set_ylabel("Tip ($)")
st.pyplot(fig3)

# Footer
st.markdown("Created with ❤️ using Streamlit and Seaborn")
