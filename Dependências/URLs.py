import pandas as pd

# Load the CSV file
df = pd.read_csv('tasks_990.csv')

# Get the unique values in the column
unique_values = df['REPO_URL'].unique()

# Convert to list and print
unique_values_list = unique_values.tolist()
print(unique_values_list)
