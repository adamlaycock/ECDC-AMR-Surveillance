import os
import re

import pandas as pd

YEARS = [2012, 2013, 2014, 2015]
START_ITEM = 'Country'
COLS = [0, 1, 2, 4, 5, 7, 8, 10, 11]
EXCLUDED_TABLES = ['Table 3.25', 'Table 3.7', ' Table 3.13', 'Table 3.20']
DIR_PATH = r'C:\Users\adamm\OneDrive\Documents\VSC\Projects\ECDC AMR Surveillance\source_data'

def extract_metadata(
    file_path: str,
    table: str
):
    md_df = pd.read_excel(
        file_path,
        sheet_name=table,
        header=None,
        skipfooter=3,
        usecols=COLS
    )
    metadata = md_df.at[0, 0]

    organism = metadata.split('.', 1)[0]
    
    pattern = r'to (.*?) \(%R\)'
    drug = re.search(pattern, metadata).group(1)

    col_names = md_df.iloc[3,:]
    col_names = [col_name.strip() for col_name in col_names]
    new_names = [START_ITEM]
    for year in YEARS:
        for name in col_names[1:3]:
            if name != 'Country':
                new_names.append(f"{name}_{year}")
    
    return (new_names, organism, drug)

def extract_data(
    file_path: str,
    table: str,
    metadata: tuple
):
    df = pd.read_excel(
        r"C:\Users\adamm\OneDrive\Documents\VSC\Projects\ECDC AMR Surveillance\source_data\Acinetobacter, Tables 3-21 to 3-25.xlsx",
        sheet_name="Table 3.21",
        skipfooter=3,
        skiprows=3,
        usecols=COLS
    )

    df.columns = metadata[0]

    df = df.melt(
        id_vars='Country',
        var_name='MetricYear',
        value_name='Value'
    )

    df['Organism'] = metadata[1]
    df['Drug'] = metadata[2]

    return df

def main():
    df_lst = []
    for file_name in os.listdir(DIR_PATH):
        file_path = os.path.join(DIR_PATH, file_name)
        xl_file = pd.ExcelFile(file_path)
        for sheet in xl_file.sheet_names:
            if sheet not in EXCLUDED_TABLES:
                metadata = extract_metadata(file_path, sheet)
                df_lst.append(extract_data(file_path, sheet, metadata))

if __name__ == '__main__':
    main()