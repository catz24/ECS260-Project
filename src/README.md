# Measuring Sustainability in Open-Source Software: The Impact of Code Complexity

## Setup
### Step 1: Data preparation
Extract the data for analysis and models training:
```
tar -xzvf data.tar.gz
```

The data for our experiment is consist of two files, complexity_data.csv and filter_repos_with_language.csv, which includes the metadata and code complexity of open-source software (OSS) projects.

### Step 2: Set Up a Conda Environment
Create and activate a new Conda environment:
```
conda env create -f environment.yml
conda activate complexity
```
This will install all necessary Python packages and dependecies for the project.
When you are running `main.ipynb` in Visual Stuido Code, please select `complexity` as the kernel.



