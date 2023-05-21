import pandas as pd
import git as git








df_original = pd.read_excel('tasks_990.xlsx')


split_column = 'REPO_URL'
unique_values = df_original[split_column].unique()

# Iterate through unique values and create separate Excel files
for value in unique_values:
    # Filter the original dataframe based on the current value
    df_filtered = df_original[df_original[split_column] == value]

    # Create a new Excel writer object


    # Write the filtered dataframe to a new sheet in the Excel file
    nome = "tasks_"+ value.rsplit('/',1)[1] + '.xlsx'
    print(nome)
    df_filtered.to_excel(nome,index = True)


    # Save and close the Excel writer object


    # Print success message
    print(f'Saved {value}_output_file.xlsx')


