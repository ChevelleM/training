################################## 1. Clean client revenue file ##################################

### Set up ###

# Import packages
import pandas as pd
import numpy as np

# Import data
# Read excel dataset
df_client = pd.read_csv("../data/input/client revenue.csv", encoding = "ISO-8859-1", skiprows=1, usecols=[1,2,3,4]) #skip first row and col
df_client.dropna(inplace=True) #remove empty rows

### Clean data ###

# Rename column headings 
df_client.rename(columns={'Site': 'Site', 'Service': 'Segment', '2023FY': 'y2023', '2022FY': 'y2022'}, inplace=True)

# Remove typos in the data
df_client['y2023'] = df_client['y2023'].str.replace('nf', '') #remove typo 'nf'
df_client['Segment'] = df_client['Segment'].str.replace('1', '') #remove typo '1'

# Check class types of the data 
print(df_client.dtypes)

# Change values in y2022 and y2023 columns from object to float and values in Site and Segment columns from object to string
df_client['Site'] = df_client['Site'].astype('string')
df_client['Segment'] = df_client['Segment'].astype('string')
df_client['y2023'] = df_client['y2023'].astype(str).astype(float)
df_client['y2022'] = df_client['y2022'].astype(str).astype(float)
print(df_client.dtypes)

#### Transform data ####

# Collapse revenue data into totals for each segment per year
df_client = df_client.groupby('Segment').agg(y2023=('y2023', 'sum'), y2022=('y2022', 'sum'))

# Round all numeric values to 1.d.p
df_client.y2023 = df_client.y2023.round(1)
df_client.y2022 = df_client.y2022.round(1)

# Create a new column to identify the dataset for merging purposes later
df_client.insert(2, "data", ['Client_rev', 'Client_rev'], True)

df_client.index.name = 'Segment'
df_client.reset_index(inplace=True)

# View cleaned dataset
print(df_client)

### Save cleaned data ###
df_client.to_csv('../data/inter/clean_client_rev.csv', index= False)

################################### END OF SCRIPT ###################################
