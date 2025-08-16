import pandas as pd

YEARS = [2012, 2013, 2014, 2015]
START_ITEM = 'Country'

md_df = pd.read_excel(
    r"C:\Users\adamm\OneDrive\Documents\VSC\Projects\ECDC AMR Surveillance\source_data\Acinetobacter, Tables 3-21 to 3-25.xlsx",
    sheet_name="Table 3.21",
    header=None,
    skipfooter=3,
    skiprows=3
)

metadata = md_df.at[0, 0]

col_names = md_df.iloc[0,:]
col_names = [col_name.strip() for col_name in col_names]
new_names = [START_ITEM]
for year in YEARS:
    for name in col_names[1:4]:
        if name != 'Country':
            new_names.append(f"{name}_{year}")





df = pd.read_excel(
    r"C:\Users\adamm\OneDrive\Documents\VSC\Projects\ECDC AMR Surveillance\source_data\Acinetobacter, Tables 3-21 to 3-25.xlsx",
    sheet_name="Table 3.21",
    skipfooter=3,
    skiprows=3
)

df.columns = new_names

# df = df.melt(
#     id_vars='Country',
#     var_name='MetricYear',
#     value_name='Value'
# )

# df[['Metric', 'Year']] = df['MetricYear'].str.split('_', expand=True)
# df = df.drop(columns='MetricYear')

df
