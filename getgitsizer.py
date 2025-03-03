import subprocess
import os
import csv

# addreses of the repos
repos = [
    'address'
]

# get csv output
def parse_git_sizer_output(repo_path, output):
    data = []
    lines = output.splitlines()

    for line in lines:
        if line.startswith("|"):
            columns = [col.strip() for col in line.strip('|').split('|')]
            columns.insert(0, repo_path)
            data.append(columns)
    return data

# run git-sizer
def run(repo_path, all_data):
    try:
        os.chdir(repo_path)
        result = subprocess.run(
            ["git-sizer", "--verbose"],
            capture_output=True, text=True, check=True
        )
        parsed_data = parse_git_sizer_output(repo_path, result.stdout)
        all_data.extend(parsed_data)
        print(f"Analysis for {repo_path} completed.")

    except subprocess.CalledProcessError as e:
        print(f"Error running git-sizer on {repo_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# analyze the repos
def analyze():
    all_data = []
    for repo in repos:
        run(repo, all_data)

    # save data
    if all_data:
        csv_dir = 'csv directory'
        os.makedirs(csv_dir, exist_ok=True)  
        csv_filename = os.path.join(csv_dir, "gitsizer_data.csv")
        file_exists = os.path.isfile(csv_filename) 
        with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Repo Path", "Metric", "Value"]) 
            writer.writerows(all_data)

        print(f"All analysis results appended to {csv_filename}")

if __name__ == "__main__":
    analyze()
