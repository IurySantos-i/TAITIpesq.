import os
import subprocess

# specify the folder containing the raw git log files
folder_path = "F:/Pesquisa TAITI/Dependências/gitlabhq"

# loop through all files in the folder with "raw_gitlog.txt" extension
for file in os.listdir(folder_path):
    if file.endswith("_raw_gitlog.log"):
        task_number = file.split("_")[0]
        output_file_path = f"{task_number}_task_dependencies.csv"
        print("algo")


        with open(output_file_path, "w") as output_file: # run Code Maat tool on the input file and save output to output file
            subprocess.run(f'java -jar code-maat-1.0.4-standalone.jar -l {file} -c git2 -a coupling', stdout=output_file, shell=True)






