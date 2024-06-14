import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_CO2 = pd.read_csv('CO2emissions_long.csv', parse_dates=['year'])
data_CO2.set_index('year', inplace=True)

plt.figure(figsize=(12, 6))
sns.lineplot(x=data_CO2.index, y='CO2emissionspercapita', data=data_CO2)
plt.xlabel('Years')
plt.ylabel('CO2 Emissions in Metric Tons per Capita')
plt.show()

data_forest = pd.read_csv('Forestarea_long.csv', parse_dates=['year'])
data_forest.set_index('year', inplace=True)

plt.figure(figsize=(12, 6))
sns.lineplot(x=data_forest.index, y='forestareaoflandarea', data=data_forest)
plt.xlabel('Years')
plt.ylabel('Forest Areas in % of Total Land Area')
plt.show()