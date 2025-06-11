from git import Repo
from datetime import datetime
import pandas as pd

# Ask the user for path to any git project
repo_path = r"C:\Users\dhars\GitCommitVisualizer\flask"

# Open the Git repo
repo = Repo(repo_path)

# Get last 1000 commits from main branch
commits = list(repo.iter_commits('main', max_count=1000))

# Store data
data = []
for commit in commits:
    data.append({
        "author": commit.author.name,
        "date": datetime.fromtimestamp(commit.committed_date),
        "files_changed": len(commit.stats.files)
    })

# Save as Excel-style data (CSV)
df = pd.DataFrame(data)
df.to_csv("commit_data.csv", index=False)

print("✅ Done! Data saved to commit_data.csv")
