################################## 3. Clean market size file ##################################

### Set up ###

# Import packages
import pandas as pd
import numpy as np

### Import data ###

# Read excel dataset
df_market = pd.read_csv("../data/input/market size estimates.csv", encoding="ISO-8859-1", usecols=[0, 5, 6])
df_market.dropna(inplace=True)  #remove empty rows

# Rename column headings
df_market.rename(columns={'Market': 'Segment', '2022': 'y2022','2023': 'y2023'},inplace=True)

# Create a new column to identify the dataset for merging purposes later
df_market.insert(2, "data", ['Market_rev', 'Market_rev'], True)

# Reorder columns 
df_market = df_market[['Segment','y2023', 'y2022', 'data']]

# View cleaned dataset
print(df_market)

### Save cleaned data ###
df_market.to_csv('../data/inter/clean_market_rev.csv', index= False)

################################### END OF SCRIPT ###################################
