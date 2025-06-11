import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Git Commit Visualizer & Analyzer")

# Load data
df = pd.read_csv("commit_data.csv")
df['date'] = pd.to_datetime(df['date'])

# Sidebar options
st.sidebar.title("Filter Options")
author_list = df['author'].unique().tolist()
selected_authors = st.sidebar.multiselect("Select Author(s)", author_list, default=author_list)

# Filter data
filtered_df = df[df['author'].isin(selected_authors)]

# --- Bar Chart: Top Commit Authors ---
st.subheader("Top Commit Authors")
top_n = st.slider("Number of top authors to show", 5, 20, 10)

top_authors = filtered_df['author'].value_counts().head(top_n)
fig1, ax1 = plt.subplots(figsize=(10, 6))
top_authors.plot(kind='bar', color='teal', ax=ax1)
ax1.set_title(f"Top {top_n} Authors by Commit Count")
ax1.set_xlabel("Author")
ax1.set_ylabel("Number of Commits")
plt.xticks(rotation=45, ha='right')
ax1.grid(True)
st.pyplot(fig1)

# --- Line Chart: Commit Trend Over Time ---
st.subheader("Commit Timeline Trend")

freq_option = st.selectbox("Select Time Frequency", ['Daily', 'Weekly', 'Monthly'])

if freq_option == 'Daily':
    grouped = filtered_df.groupby(pd.Grouper(key='date', freq='D')).size()
elif freq_option == 'Weekly':
    grouped = filtered_df.groupby(pd.Grouper(key='date', freq='W')).size()
else:
    grouped = filtered_df.groupby(pd.Grouper(key='date', freq='M')).size()

fig2, ax2 = plt.subplots(figsize=(12, 5))
grouped.plot(kind='line', marker='o', linestyle='-', color='green', ax=ax2)
ax2.set_title(f"Commits Over Time ({freq_option})")
ax2.set_xlabel("Date")
ax2.set_ylabel("Number of Commits")
ax2.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig2)

# --- Footer ---
st.markdown("---")
st.markdown("📊 Built with Streamlit by Dharshini G 💡")
