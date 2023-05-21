import pandas as pd
import git

# Load the Excel file
excel_file = 'tasks_990.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file)

# Extract the unique repository URLs from the Excel column
repo_urls = df['REPO_URL'].unique().tolist()  # Replace 'Repository URL' with the appropriate column name in your Excel file

# Clone each repository only once
for repo_url in repo_urls:
    # Clone the repository if it hasn't been cloned already
    repo_path = f'F:/Clones de reps. Taiti/{repo_url.split("/")[-1]}'  # Replace with the local path where you want to clone the repository

    try:
        git.Repo(repo_path)  # Check if the repository already exists locally
        print(f'Repository {repo_url} already exists.')
    except git.exc.NoSuchPathError:
        git.Repo.clone_from(repo_url, repo_path)
        print(f'Repository {repo_url} cloned.')
