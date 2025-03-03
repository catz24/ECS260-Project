import os
import subprocess
import pandas as pd

# Load the dataset
file_path = "filter_repos.csv"  # Modify as needed
df = pd.read_csv(file_path)

# Directory to store cloned repositories
CLONE_DIR = "./cloned_repos"
os.makedirs(CLONE_DIR, exist_ok=True)

# Mapping dataset languages to PMD-CPD supported languages
LANGUAGE_MAPPING = {
    "Python": "python",
    "Java": "java",
    "JavaScript": "ecmascript",
    "TypeScript": "typescript",
    "C": "c",
    "C++": "cpp",
    "Go": "go",
    "PHP": "php",
    "Kotlin": "kotlin",
    "Swift": "swift",
    "Ruby": "ruby",
    "Rust": "rust",
    "R": "r",
    "Scala": "scala",
    "CSS": "css",
    "HTML": "html",
    "Jupyter Notebook": "python",
    "TeX": "tex",
    "SCSS": "css",
    "Shell": "bash",
    "Makefile": "bash",
    "Dockerfile": "bash",
    "JSON": None,
    "Markdown": None,
    "Procfile": None,
    "HCL": None,
    "Starlark": None,
}

# Function to clone a repository
def clone_repo(repo_name):
    repo_url = f"https://github.com/{repo_name}.git"
    repo_path = os.path.join(CLONE_DIR, repo_name.replace("/", "_"))
    
    if not os.path.exists(repo_path):  # Avoid re-cloning
        print(f"Cloning {repo_url}...")
        subprocess.run(["git", "clone", "--depth", "1", repo_url, repo_path], check=True)
    
    return repo_path

# Function to run PMD-CPD for code duplication analysis
def run_pmd_cpd(repo_path, language):
    output_file = os.path.join(repo_path, "duplication_results.csv")
    
    # Ensure language is supported
    if language not in LANGUAGE_MAPPING or LANGUAGE_MAPPING[language] is None:
        print(f"Skipping {repo_path}: Unsupported language '{language}'")
        return None

    # Construct shell command with output redirection
    cmd = f"pmd cpd --minimum-tokens 100 --dir {repo_path} --language {LANGUAGE_MAPPING[language]} --format csv > {output_file}"
    
    try:
        print(f"Running command: {cmd}")  # Debugging
        subprocess.run(cmd, shell=True, check=True)
        print(f"PMD-CPD analysis complete for {repo_path}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error running PMD-CPD for {repo_path}: {e}")
        return None

# Process each repository
results = []
for _, row in df.iterrows():
    repo_name = row["repo_name"]
    language = row["language"]

    # Skip if language is missing or unsupported
    if pd.isna(language) or language not in LANGUAGE_MAPPING or LANGUAGE_MAPPING[language] is None:
        print(f"Skipping {repo_name}: Language '{language}' not supported.")
        continue

    repo_path = clone_repo(repo_name)
    output_file = run_pmd_cpd(repo_path, language)

    # Load and process the duplication results
    if output_file and os.path.exists(output_file):
        cpd_df = pd.read_csv(output_file)
        cpd_df["repo_name"] = repo_name
        results.append(cpd_df)

# Combine results and save to CSV
if results:
    final_df = pd.concat(results, ignore_index=True)
    output_path = "code_duplication_results.csv"
    final_df.to_csv(output_path, index=False)
    print(f"Saved code duplication analysis results to {output_path}")
