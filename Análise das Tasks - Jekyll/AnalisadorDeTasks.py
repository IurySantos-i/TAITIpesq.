import openpyxl
import git
import numpy as np

# Function to calculate commit statistics
def get_commit_stats(repo, commit):
    repo.head.reference = repo.commit(commit)
    stats = repo.git.show(commit, format="%H %ct %an %s")
    commit_info = stats.splitlines()[0].split()
    num_files = len(repo.index.diff(None))
    if num_files == 0: num_files = 1
    num_changed_files = len(repo.index.diff("HEAD"))
    percent_changes = (num_changed_files / num_files) * 100
    num_collaborators = len(set(repo.git.shortlog("-sn").splitlines()))
    num_commits = repo.commit(commit).count()
    changes_per_commit = [len(repo.index.diff(c)) for c in repo.iter_commits("HEAD")]
    changes_average = np.mean(changes_per_commit)
    changes_median = np.median(changes_per_commit)
    changes_sd = np.std(changes_per_commit)
    return commit_info + [num_files, num_changed_files, percent_changes, num_collaborators, num_commits, changes_average, changes_median, changes_sd]

# Load tasks from XLSX
tasks = []
workbook = openpyxl.load_workbook("formalized_tasks_jekyll.git.xlsx")
sheet = workbook["Sheet1"]  # Assuming tasks are in the first sheet

# Access the correct column index for "HASHES"
hashes_column_index = 6  # Replace with the actual column number

tasks = []
for row in sheet.iter_rows(min_row=2):
    # Access the correct cell index within the tuple
    hashes_cell = row[hashes_column_index - 1]  # Assuming "HASHES" is the 5th column
    text_content = str(hashes_cell.value)  # Explicitly convert to string

    text_content = text_content.replace(" ","").replace("[", "").replace("]", "")

    if text_content:
        tasks.append(text_content.split(","))
    else:
        print(f"Warning: Empty 'HASHES' value in row {row[0].row}.")  # Access row number from the first cell

print(tasks)

# Get a reference to the current repository
repo = git.Repo("/home/iury/Documents/Trabalho/Repositórios_necessários/jekyll/")

# Generate spreadsheets for each task
for task_id, task in enumerate(tasks):
    commit_data = [get_commit_stats(repo, commit) for commit in task]

    # Create CSV output
    filename = f"task_{task_id}_commit_details.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["hash", "author_date", "author_name", "subject", "#files", "#changedFiles", "percent-changes", "#collaborators", "#commits", "changes-average", "changes-median", "changes-sd"]
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        writer.writerows(commit_data)

print("Commit details spreadsheets generated successfully!")

