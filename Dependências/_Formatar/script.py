import os
import csv

def remove_empty_first_column(file_path):
  """Removes all the rows with an empty first column from the CSV file at the specified path."""

  with open(file_path, "r") as csv_file:
    reader = csv.reader(csv_file)
    lines = []
    for row in reader:
      if len(row) > 0:
        lines.append(row)

  with open(file_path, "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(lines)

if __name__ == "__main__":
  # Get the current working directory.
  working_directory = os.getcwd()

  # Get all the files in the current working directory that end with ".csv".
  csv_files = [
      file for file in os.listdir(working_directory) if file.endswith(".csv")
  ]

  # Iterate over the CSV files.
  for csv_file in csv_files:
    file_path = os.path.join(working_directory, csv_file)
    remove_empty_first_column(file_path)
