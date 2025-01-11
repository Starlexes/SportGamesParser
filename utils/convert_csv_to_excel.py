import pandas as pd

# Конвертация csv в excel
def convert_csv_to_excel(folder_name):

    df = pd.read_csv(f'data/{folder_name}/data.csv', delimiter=',')


    df.to_excel(f'data/{folder_name}/data.xlsx', index=False)