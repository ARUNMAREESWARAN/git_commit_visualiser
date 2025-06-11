import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv(r"C:\Users\dhars\GitCommitVisualizer\commit_data.csv")
df['date'] = pd.to_datetime(df['date'])

# 📊 Commits per Author – Top 10 Only
author_counts = df['author'].value_counts().head(10)  # Top 10 authors

plt.figure(figsize=(10, 6))
bars = author_counts.plot(kind='bar', color='skyblue')

plt.title("Top 10 Authors by Number of Commits")
plt.xlabel("Author")
plt.ylabel("Number of Commits")
plt.xticks(rotation=45, ha='right')

# Add commit count labels on top of each bar
for i, v in enumerate(author_counts):
    plt.text(i, v + 2, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()
