################################## 4. Market shares table and chart file ##################################

### Set up ###

# Import packages
import pandas as pd
import numpy as np

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

print(df_ms)

### Save cleaned data ###
df_ms.to_csv('../data/output/clean_market_shares_table.csv', index= True)

################################### END OF SCRIPT ###################################
