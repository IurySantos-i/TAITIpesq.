import os

import re

def remove_blanks_and_numbers(string):
  words = string.split()
  cleaned = [word for word in words if not word.isdigit()]
  return "".join(cleaned)

log_dir = r"D:\Taiti Pesquisa\Dependências\action-center-platform - C\Log Analysis"
for filename in os.listdir(log_dir):

  if filename.endswith('.log'):
    commits = 0
    files = []
    files_in_commit_total = []
    files_multi_commit = 0
    files_in_commit = 0
    already_verified = []
    with open(os.path.join(log_dir, filename)) as f:
      log = f.read()


      for line in log.split('\n'):

        if line.startswith('--'):
          commits += 1
          files_in_commit_total.append(files_in_commit)
          files_in_commit = 0
          continue


        if remove_blanks_and_numbers(line) in files and not already_verified:
          files_multi_commit += 1
          files.remove(remove_blanks_and_numbers(line))
          if '' in files: files.remove('')
          already_verified.append(remove_blanks_and_numbers(line))
        else:

          if remove_blanks_and_numbers(line) not in already_verified:
            files.append(remove_blanks_and_numbers(line))
            if '' in files: files.remove('')

        files_in_commit =+ 1
        continue




        


    print(filename)

    print(f"Average files per commit: {sum(files_in_commit_total)/commits }")
    print(f"Total commits: {commits}")
    print(f"Files in multiple commits: {files_multi_commit}")
    print(already_verified)
    print(" ")
