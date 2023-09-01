import pandas as pd

def load_and_print_dataframe(csv_file_name):
  df = pd.read_csv(csv_file_name)

  print(df)


if __name__ == "__main__":
  csv_file_name = "logical_dependencies_OK205_raw_gitlog.csv"

  load_and_print_dataframe(csv_file_name)
