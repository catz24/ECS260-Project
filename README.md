# Code-Related Metrics as Indicators of Sustainability

## Overview
Identify the pattern of cyclomatic and cognitive complexity using project elements, such size, version control practice, code duplication, and number of contributors in ~200 projects. This is a course project for ECS 260 in UC Davis.

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

## Contributors
- Zaishuo Xia & Mobina Noori - Collected and processed data for 200+ repositories with 500+ commits and 50+ contributors
- Zili Wang - Wrote the progress report; investigated the tools usage and debugging
- Yanfeng Ma - Plotted the rough template of report and completed introduction of progress report
- Xinyuan Jiang - Collected the data related to project size, commits, trees and blobs with Git-Sizer
- Chris Ruan - Ran PMD-CPD on dataset; Organized GitHub
