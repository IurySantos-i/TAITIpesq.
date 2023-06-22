
import pandas as pd
from git import Repo

# read in the csv file
df = pd.read_excel('formalized_tasks_opengovernment.git.xlsx')

# set the path to the local git repository
repo_path = r'F:\Pesquisa TAITI\Repositórios necessários\opengovernment.git'

# loop through each row and generate the git log file
for index, row in df.iterrows():
    # get the oldest and most recent commits from the row
    oldest_commit = row['Oldest Commit']
    most_recent_commit = row['Most Recent Commit']
    task_id = row['TASK_ID']

    # generate the git log command
    git_log_command = f'git log --pretty=format:"--%h--%ad--%aN" --date=short --numstat {oldest_commit}..{most_recent_commit}'

    # set the path to the destination file
    dest_path = f"{task_id}_raw_gitlog.log"

    # create the file and write the git log output to it
    with open(dest_path, 'w',encoding='utf-8') as f:
        repo = Repo(repo_path)
        git_log = repo.git.execute(git_log_command)
        f.write(git_log)

