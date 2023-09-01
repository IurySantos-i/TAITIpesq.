# Import the csv and sys modules
import csv
import sys

# Get the name of the input csv file from the command line argument
input_file = "tasks_data_990.csv"
# Open the input csv file
with open(input_file, "r") as f:
    # Create a csv reader object
    reader = csv.reader(f)
    # Get the header row
    header = next(reader)
    # Create a variable to store the current value of the first column
    current_key = None
    # Create a variable to store the current output file
    current_file = None
    # Loop through the rest of the rows
    for row in reader:
        # Get the value of the first column
        key = row[0].replace(":", "_").replace("/", "_")
        # Check if the key is different from the current key
        if key != current_key:
            # Close the current output file if it exists
           # if current_file:
            #    current_file.close()
            # Update the current key
            current_key = key
            # Create a new output file with the key as the name
            current_file = open(key + ".csv", "w")
            # Create a csv writer object for the new file
            current_file = csv.writer(current_file)
            # Write the header row to the new file
            current_file.writerow(header)
        # Write the current row to the corresponding file
        current_file.writerow(row)
    # Close the last output file if it exists
   # if current_file:
   #     current_file.close()
