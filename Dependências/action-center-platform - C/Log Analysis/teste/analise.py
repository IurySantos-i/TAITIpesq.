import os

import re

def remove_blanks_and_numbers(string):
  words = string.split()
  cleaned = [word for word in words if not word.isdigit()]
  return "".join(cleaned)

log_dir = r"D:\Taiti Pesquisa\Dependências\action-center-platform - C\Log Analysis\teste"
for filename in os.listdir(log_dir):

  if filename.endswith('.log'):
    commits = 0
    files = []
    files_in_commit_total = []
    files_multi_commit = 0
    files_in_commit = 0
    with open(os.path.join(log_dir, filename)) as f:
      log = f.read()


      for line in log.split('\n'):

        if line.startswith('--'):
          commits += 1
          files_in_commit_total.append(files_in_commit)
          files_in_commit = 0
          continue


        if remove_blanks_and_numbers(line) in files:
          files_multi_commit += 1
          files.remove(remove_blanks_and_numbers(line))
          files.remove('')
        else:
          files.append(remove_blanks_and_numbers(line))

        files_in_commit =+ 1
        continue




        # Track unique files


    print(filename)
    print(f"Average files per commit: {sum(files_in_commit_total)/commits }")
    print(f"Total commits: {commits}")
    print(f"Files in multiple commits: {files_multi_commit}")
    print(" ")
