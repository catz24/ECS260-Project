import pandas as pd

# Load main dataset (which includes repo metadata & complexity metrics)
main_df = pd.read_csv("filter_repos.csv")

# Load code duplication results
duplication_df = pd.read_csv("code_duplication_results.csv")

# Normalize repo_name in duplication dataset (convert `xxx_yyy` → `xxx/yyy`)
duplication_df["repo_name"] = duplication_df["repo_name"].str.replace("_", "/", regex=False)

# Aggregate duplication data by repo (sum occurrences, tokens, etc.)
duplication_summary = duplication_df.groupby("repo_name").agg({
    "lines": "sum",  # Total duplicated lines in repo
    "tokens": "sum",  # Total duplicated tokens in repo
    "occurrences": "sum"  # Total occurrences of duplicated code
}).reset_index()

# Merge with the main dataset on repo_name
merged_df = main_df.merge(duplication_summary, on="repo_name", how="left")

# Fill missing duplication values with 0 (repos with no detected duplication)
merged_df.fillna({"lines": 0, "tokens": 0, "occurrences": 0}, inplace=True)

# Save the final merged dataset
merged_df.to_csv("merged_dataset.csv", index=False)
print("✅ Merged dataset saved as merged_dataset.csv")
