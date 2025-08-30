import pandas as pd
import numpy as np

df = pd.read_csv(
   r'C:\Users\adamm\OneDrive\Documents\VSC\Projects\ECDC AMR Surveillance\Atlas\source_data\ecdc_surv_atlas.csv'
)
df = df.drop(columns=['HealthTopic', 'RegionCode', 'TxtValue'])
