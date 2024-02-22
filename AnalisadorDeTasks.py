import csv
import git
import numpy as np

# Function to calculate commit statistics
def get_commit_stats(repo, commit):
    repo.head.reference = repo.commit(commit)
    stats = repo.git.show(commit, format="%H %ct %an %s")
    commit_info = stats.splitlines()[0].split()
    num_files = len(repo.index.diff(None))
    num_changed_files = len(repo.index.diff("HEAD"))
    percent_changes = (num_changed_files / num_files) * 100
    num_collaborators = len(set(repo.git.shortlog("-sn").splitlines()))
    num_commits = repo.git.rev_list("--count", "HEAD").splitlines()[0]
    changes_per_commit = [len(repo.index.diff(c)) for c in repo.iter_commits("HEAD")]
    changes_average = np.mean(changes_per_commit)
    changes_median = np.median(changes_per_commit)
    changes_sd = np.std(changes_per_commit)
    return commit_info + [num_files, num_changed_files, percent_changes, num_collaborators, num_commits, changes_average, changes_median, changes_sd]

# Load tasks from CSV
tasks = []
with open("tasks.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        tasks.append(row[0])  # Assuming commit hashes are in the first column

# Clone the repository
repo_url = "https://github.com/example/your-repo"  # Replace with your repository URL
repo = git.Repo.clone_from(repo_url, ".")

# Generate spreadsheets for each task
for task in tasks:
    commit_data = [get_commit_stats(repo, commit) for commit in task.split(",")]

    # Create CSV output
    filename = f"task_{task}_commit_details.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["hash", "author_date", "author_name", "subject", "#files", "#changedFiles", "%changes", "#collaborators", "#commits", "changes-average", "changes-median", "changes-sd"]
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        writer.writerows(commit_data)

print("Commit details spreadsheets generated successfully!")
