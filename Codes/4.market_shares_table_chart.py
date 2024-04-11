################################## 4. Market shares table and chart file ##################################

### Set up ###

# Import packages
import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt

#### Import data ####

# Read clean client, target and market size revenue excel files and combine into one file
file1 = pd.read_csv('../data/inter/clean_client_rev.csv')
file2 = pd.read_csv('../data/inter/clean_target_rev.csv')
file3 = pd.read_csv('../data/inter/clean_market_rev.csv')

files = [file1, file2, file3]
df_ms = pd.DataFrame() 
for file in files:
    df_ms = pd.concat([df_ms, file])

df_ms = df_ms.melt(id_vars=["Segment", "data"], var_name="Year")

df_ms = df_ms.pivot(index=["Segment","Year"], columns="data", values=["value"])

df_ms = df_ms['value']

df_ms = df_ms[['Market_rev', 'Client_rev', 'Target_rev']]

df_ms.insert(3, "Client_share", df_ms.Client_rev/df_ms.Market_rev, True)
df_ms.insert(4, "Target_share", df_ms.Target_rev/df_ms.Market_rev, True)
df_ms.insert(5, "Combined_share", (df_ms.Client_rev + df_ms.Target_rev)/df_ms.Market_rev, True)

print(df_ms.dtypes)

df_ms['Market_rev'] = df_ms['Market_rev'].astype('string')
df_ms['Client_rev'] = df_ms['Client_rev'].astype('string')
df_ms['Target_rev'] = df_ms['Target_rev'].astype('string')

df_ms['Market_rev'] = '£'+ df_ms['Market_rev'] +'mn'
df_ms['Client_rev'] = '£'+ df_ms['Client_rev'] +'mn'
df_ms['Target_rev'] = '£'+ df_ms['Target_rev'] +'mn'

df_ms['Client_share'] = df_ms['Client_share'].map('{:.0%}'.format)
df_ms['Target_share'] = df_ms['Target_share'].map('{:.0%}'.format)
df_ms['Combined_share'] = df_ms['Combined_share'].map('{:.0%}'.format)

# View data
print(df_ms)

### Save cleaned data ###
df_ms.to_csv('../data/output/clean_market_shares_table.csv', index= True)

#### Create chart ####

# Drop unnecessary columns
df_ms = df_ms[['Client_share', 'Target_share', 'Combined_share']]

# Convert shares from object to float
df_ms['Client_share'] = df_ms['Client_share'].map('{:.2}'.format)
df_ms['Target_share'] = df_ms['Target_share'].map('{:.2}'.format)
df_ms['Combined_share'] = df_ms['Combined_share'].map('{:.2}'.format)

print(df_ms)

df_ms['Client_share'] = df_ms['Client_share'].astype(float)
df_ms['Target_share'] = df_ms['Target_share'].astype(float)
df_ms['Combined_share'] = df_ms['Target_share'].astype(float)

print(df_ms.dtypes)

values = ['Client_share','Target_share', 'Combined_share']
df_ms = pd.pivot_table(df_ms, values=values, index=['Segment','Year'], 
   fill_value=0).reset_index(level=-1)

df_ms['Combined_share'] = 100 - df_ms['Client_share'] - df_ms['Target_share']

df_ms.rename(columns={'Combined_share': 'Other_share'},inplace=True)

df_ms.index.name = 'Segment'
df_ms.reset_index(inplace=True)

df_ms = df_ms.melt(id_vars=["Segment", "Year"], var_name="Entity")

df_ms.Entity = df_ms.Entity.str.replace("_share", "")

print(df_ms)
