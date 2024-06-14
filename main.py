import pandas as pd

data = pd.read_csv('dataset_complete_worldbank.csv')
pd.set_option('display.max_columns', None)
print(data)
