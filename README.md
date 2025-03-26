# Code-Related Metrics as Indicators of Sustainability

## Overview
Identify the pattern of cyclomatic and cognitive complexity using project elements, such size, version control practice, code duplication, and number of contributors in ~200 projects. This is a course project for ECS 260 in UC Davis.

## Experiments
All experiments are performed in the `src` directory.

## LLM Usage Documentation
We utilized LLMs to assist in identifying relevant research papers and to generate portions of the code used in our experiments.

## Git-Sizer - Analyzing for Code Duplication
- gitsizer_data.csv - Full data ran with gitsizer
- repo_size.csv - Data on size of repositories
- getgitsizer.py - Running git-sizer on repositories

## PMD-CPD - Analyzing for Code Duplication
- filter_repos.csv - Cleaned data for 200+ repositories
- code_duplication_results.csv - Full code duplication data for filter_repos.csv
- merged_dataset.csv - Combined data of filter_repos.csv and code_duplication_results.csv
- langGetter.py - Crawling programming language from filter_repos.csv and appending it back to the CSV file
- pmdReader.py - Cloning each repository and run PMD-CPD on them. Output report at each cloned repository
- duplicationReader.py - Gathering reports and generate code_duplication_results.csv
- duplicationMerger.py - Creating merged_dataset.csv
