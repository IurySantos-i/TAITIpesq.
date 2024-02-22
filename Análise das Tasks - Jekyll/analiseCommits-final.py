import pandas as pd
import openpyxl
import git
import statistics
import datetime
from datetime import datetime, timedelta

# Load the Excel file
xl = pd.ExcelFile('formalized_tasks_jekyll.git.xlsx')

# Get the sheet with the tasks
tasks_sheet = xl.parse('Sheet1')

# Initialize the GitPython repository object
repo = git.Repo('/home/iury/Documents/Trabalho/Repositórios_necessários/jekyll/')

# Loop through each task in the tasks sheet
for index, row in tasks_sheet.iterrows():
    # Get the task ID and the commits for the task
    task_id = row['TASK_ID']
    commits = row['HASHES'].replace('[', '').replace(']', '').replace(' ', '').split(',')

    # Initialize the data for the task
    data = []
    num_changed_files = []

    # Initialize the number of commits and the set of unique authors
    num_commits = 0
    unique_authors = set()

    # Loop through each commit in the task
    for commit_hash in commits:
        # Get the commit object
        commit = repo.commit(commit_hash)

        # Get the number of files in the project at the time of the commit
        num_files = len([f for f in commit.tree.traverse() if f.type == 'blob'])

        # Get the number of files changed by the commit
        num_changed = len(commit.stats.files)
        
        # Calculate the proportion of project files changed by the commit
        prop_changed_files = num_changed / num_files

        # Filter the logs for the specific task and count the number of authors and the number of commits
        unique_authors.update(set(repo.git.log('--format=%an', '--grep', commit_hash, '--pretty=', '--no-merges').split('\n')))
        
        # Calculate the total number of commits across all branches up till the date of commit
        num_commits = sum(1 for c in repo.iter_commits('--all'))

        commit_date = datetime.fromtimestamp(commit.authored_date)

        # add timedelta to datetime object
        next_day = commit.authored_datetime + timedelta(days=1)
        next_day_str = next_day.isoformat()
        num_commits = int(repo.git.execute(f"rev-list --count HEAD --before='{commit_date.isoformat()}'").strip())

        # Append the data for the commit to the task data
        data.append([commit_hash, num_files, num_changed, prop_changed_files,
                    len(unique_authors), num_commits])

        # Append the number of changed files for this commit to the list
        num_changed_files.append(num_changed)

    # Calculate the metrics for the task
    changes_average = statistics.mean(num_changed_files)
    changes_median = statistics.median(num_changed_files)
    changes_sd = statistics.stdev(num_changed_files) if len(num_changed_files) > 1 else None

    # Create a DataFrame for the task data
    task_df = pd.DataFrame(data, columns=['COMMIT_HASH', '#FILES', '#CHANGED_FILES', '%CHANGES',
                                         '#COLLABORATORS', '#COMMITS'])

    # Append the metrics to the DataFrame
    task_df = task_df._append({'COMMIT_HASH': 'METRICS', '#FILES': '', '#CHANGED_FILES': '',
                              '%CHANGES': '', '#COLLABORATORS': '', '#COMMITS': '',
                              'CHANGES_AVERAGE': changes_average,
                              'CHANGES_MEDIAN': changes_median,
                              'CHANGES_SD': changes_sd}, ignore_index=True)

    # Sort the dataframe by the 'COMMIT_HASH' column
    task_df = task_df.sort_values(by='COMMIT_HASH')

    # Save the task DataFrame to a CSV file
    task_df.to_csv(f'task_{task_id}.csv', index=False)