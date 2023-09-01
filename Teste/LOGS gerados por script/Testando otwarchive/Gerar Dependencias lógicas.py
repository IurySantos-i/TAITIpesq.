import os
import subprocess

def process_logfile(logfile):
  output_file_name = "logical_dependencies_{}".format(logfile)
  with open(output_file_name, "w") as output_file:
    command = "java -jar code-maat-1.0.4-standalone.jar -l {} -c git2 -a coupling > {}".format(logfile, output_file_name)
    subprocess.call(command, stdout=output_file)

def main():
  for logfile in os.listdir("./"):
    if logfile.endswith(".log"):
      process_logfile(logfile)

if __name__ == "__main__":
  main()
