import pandas as pd
import re

YEARS = [2012, 2013, 2014, 2015]
START_ITEM = 'Country'
COLS = [0, 1, 2, 4, 5, 7, 8, 10, 11]

md_df = pd.read_excel(
    r"C:\Users\adamm\OneDrive\Documents\VSC\Projects\ECDC AMR Surveillance\source_data\Acinetobacter, Tables 3-21 to 3-25.xlsx",
    sheet_name="Table 3.21",
    header=None,
    skipfooter=3,
    usecols=COLS
)

metadata = md_df.at[0, 0]

col_names = md_df.iloc[3,:]
col_names = [col_name.strip() for col_name in col_names]
new_names = [START_ITEM]
for year in YEARS:
    for name in col_names[1:3]:
        if name != 'Country':
            new_names.append(f"{name}_{year}")

df = pd.read_excel(
    r"C:\Users\adamm\OneDrive\Documents\VSC\Projects\ECDC AMR Surveillance\source_data\Acinetobacter, Tables 3-21 to 3-25.xlsx",
    sheet_name="Table 3.21",
    skipfooter=3,
    skiprows=3,
    usecols=COLS
)

df.columns = new_names

df = df.melt(
    id_vars='Country',
    var_name='MetricYear',
    value_name='Value'
)

df[['Metric', 'Year']] = df['MetricYear'].str.split('_', expand=True)
df = df.drop(columns='MetricYear')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

df['Organism'] = metadata.split('.', 1)[0]
pattern = r'to (.*?) \(%R\)'
print(metadata)
df['Drug'] = re.search(pattern, metadata).group(1)

df


