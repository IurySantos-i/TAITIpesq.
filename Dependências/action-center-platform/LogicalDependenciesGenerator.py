# Import the os and subprocess modules
import os
import subprocess

# Get the name of the folder from the command line argument
folder = r"F:\Pesquisa TAITI\Dependências\action-center-platform"

# Loop through all the files in the folder
for file in os.listdir(folder):
    # Check if the file is a log file
    if file.endswith(".log"):
        # Run the code-maat tool on the log file and save the output to a csv file
        subprocess.run(["java", "-jar", "code-maat-1.0.4-standalone.jar", "-l", os.path.join(folder, file), "-c", "git2", "-a", "coupling", " > ", os.path.join(folder, file + "dependencies.csv")])
        with open(os.path.join(folder, file + "dependencies.csv"), "w") as outfile:
    # Run the code-maat tool on the log file and redirect the output to the file
         subprocess.run(["java", "-jar", "code-maat-1.0.4-standalone.jar", "-l", os.path.join(folder, file), "-c", "git2", "-a", "coupling"], stdout=outfile)

