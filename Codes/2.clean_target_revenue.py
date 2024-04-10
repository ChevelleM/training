################################## 2. Clean target revenue file ##################################

### Set up ###

# Import packages
import pandas as pd
import numpy as np

### Import data ###

# Read excel dataset
df_target = pd.read_csv("../data/input/target revenue.csv", encoding = "ISO-8859-1")
df_target.dropna(inplace=True) #remove empty rows

#### Clean data ####

# Pivot table from wide to long
df_target = df_target.melt(id_vars = 'Segment')

#Rename columns
df_target = df_target.rename(columns={'Segment': 'Segment', 'variable': 'Year', 'value': 'Revenue'})

# Check class types of the data 
print(df_target.dtypes)

# Change values in Revenue column from object to float
df_target['Revenue'] = df_target['Revenue'].astype(str)
df_target['Revenue'] = df_target['Revenue'].replace(",","", regex = True)
df_target['Revenue'] = df_target['Revenue'].astype(float)

# Change values in Year column from object to string
df_target['Year'] = df_target['Year'].astype(str)
df_target['Year'] = df_target['Year'].str[-2:]
df_target['Year'] = 'y20'+df_target['Year']

# Check class types of the data 
print(df_target.dtypes)

# Round all Revenue values to millions and 1.d.p
df_target['Revenue'] = df_target['Revenue']/1000000
df_target.Revenue = df_target.Revenue.round(1)

### Transform data ###

# Collapse data and group by Segment and Year
df_target = df_target.groupby(['Segment','Year']).agg(Revenue=('Revenue', 'sum'))

# Pivot table from long to wide
df_target = df_target.unstack()

# Remove Revenue header
df_target = df_target['Revenue']

# Create a new column to identify the dataset for merging purposes later
df_target.insert(2, "data", ['Target_rev', 'Target_rev'], True)

# Reorder columns 
df_target = df_target[['y2023', 'y2022', 'data']]

#View cleaned dataset
print(df_target)

### Save cleaned data ###
df_target.to_csv('../data/inter/clean_target_rev.csv', index= False)

################################### END OF SCRIPT ###################################
