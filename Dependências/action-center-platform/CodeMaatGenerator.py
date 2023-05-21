import os
import subprocess

# specify the folder containing the raw git log files
folder_path = "F:/Pesquisa TAITI/Dependências/action-center-platform"

# loop through all files in the folder with "raw_gitlog.txt" extension
for file in os.listdir(folder_path):
    if file.endswith("_raw_gitlog.txt"):
        task_number = file.split("_")[0]

        output_file_path = os.path.join(folder_path, f"{task_number}_task_dependencies")

        # run Code Maat tool on the input file and save output to output file
        subprocess.run(f'java -jar code-maat-1.0.4-standalone.jar -l {file} -c git -a coupling > {output_file_path}')

subprocess.run(f'java -jar code-maat-1.0.4-standalone.jar -l 120_raw_gitlog.log -c git -a coupling')
