import pandas as pd
import openpyxl
from git import Repo




# Read in the tasks Excel file
tasks_file = 'tasks_diaspora.git.xlsx'
file_path = r'F:\Pesquisa TAITI\Dependências\diaspora'
tasks = pd.read_excel(tasks_file)

# Loop over the rows of the tasks file and determine the oldest and most recent commits for each row
oldest_commits = []
most_recent_commits = []
for index, row in tasks.iterrows():
    # Get the repository URL for the row
    repo_url = row['REPO_URL']

    # Get the last three commit hashes for the row
    last_commit = row['LAST']
    merge_commit = row['MERGE']
    base_commit = row['BASE']

    # Clone the repository
    repo = Repo(r'F:\Pesquisa TAITI\Repositórios necessários\diaspora.git')

    # Get the commit objects for the last three commit hashes
    last_commit_obj = repo.commit(last_commit)
    merge_commit_obj = repo.commit(merge_commit)
    base_commit_obj = repo.commit(base_commit)

    # Determine the oldest and most recent commits for the row
    commits = [last_commit_obj, merge_commit_obj, base_commit_obj]
    oldest_commit = min(commits, key=lambda x: x.committed_date)
    most_recent_commit = max(commits, key=lambda x: x.committed_date)

    # Append the oldest and most recent commits to their respective lists
    oldest_commits.append(oldest_commit.hexsha)
    most_recent_commits.append(most_recent_commit.hexsha)

    # Remove the temporary repository


# Add the oldest and most recent commit columns to the tasks DataFrame
tasks['Oldest Commit'] = oldest_commits
tasks['Most Recent Commit'] = most_recent_commits

# Write the updated tasks file to a new file

tasks.to_excel(r'F:\Pesquisa TAITI\Dependências\diaspora\formalized_tasks_diaspora.git.xlsx')


# Remove the temporary repository directory

