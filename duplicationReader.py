
import os
import pandas as pd

# Directory where duplication results are stored
SOURCE_DIR = "./cloned_repos"  # Change if needed

# List to store structured data
results = []

# Walk through all files in the directory
for root, _, files in os.walk(SOURCE_DIR):
    for file in files:
        if file == "duplication_results.csv":  # Only process PMD-CPD outputs
            file_path = os.path.join(root, file)

            try:
                # First, check if the file is completely empty
                if os.path.getsize(file_path) == 0:
                    print(f"Skipping empty file: {file_path}")
                    continue

                # Read only the first few lines to determine structure
                with open(file_path, "r") as f:
                    first_lines = f.readlines()

                # Skip files that contain only a header row but no data
                if len(first_lines) <= 1:
                    print(f"Skipping {file_path}: Only contains a header row (no data).")
                    continue

                # Read the CSV using the correct separator (",")
                df = pd.read_csv(file_path, sep=",", header=0, usecols=[0, 1, 2])

                # Rename columns for clarity
                df.columns = ["lines", "tokens", "occurrences"]

                # Ensure valid data exists
                if df.empty:
                    print(f"Skipping empty results file: {file_path}")
                    continue

                # Add repo name
                repo_name = os.path.basename(root)
                df["repo_name"] = repo_name

                results.append(df)
                print(f"✅ Loaded duplication results from: {file_path}")

            except Exception as e:
                print(f"⚠️ Skipping {file_path} due to error: {e}")

# Combine all results and save to a final CSV
if results:
    final_df = pd.concat(results, ignore_index=True)
    output_path = "code_duplication_results.csv"
    final_df.to_csv(output_path, index=False)
    print(f"✅ Saved final duplication summary to {output_path}")
else:
    print("⚠️ No valid duplication results found.")

