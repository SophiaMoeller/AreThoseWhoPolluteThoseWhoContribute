import statistics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Distribution of CO2 emissions per capita
dataco2 = pd.read_csv('dataset_complete_worldbank.csv')
dataco2 = dataco2.dropna(subset=['co2emissionspercap2020'])
mode_co22020 = statistics.mode(dataco2['co2emissionspercap2020'])
print(mode_co22020)
median_co22020 = statistics.median(dataco2['co2emissionspercap2020'])
print(median_co22020)
mean_co22020 = statistics.mean(dataco2['co2emissionspercap2020'])
print(mean_co22020)
stdev_co22020 = statistics.stdev(dataco2['co2emissionspercap2020'])
print(stdev_co22020)
sns.boxplot(dataco2['co2emissionspercap2020'])
plt.ylabel('CO2 Emissions per Capita in Tons')
plt.show()
sns.violinplot(dataco2['co2emissionspercap2020'])
plt.ylabel('CO2 Emissions per Capita in Tons')
plt.show()

# Distribution of forest area
dataforest = pd.read_csv('dataset_complete_worldbank.csv')
dataforest = dataforest.dropna(subset=['forestareaoflandarea2020'])
mode_forest2020 = statistics.mode(dataforest['forestareaoflandarea2020'])
print(mode_forest2020)
median_forest2020 = statistics.median(dataforest['forestareaoflandarea2020'])
print(median_forest2020)
mean_forest2020 = statistics.mean(dataforest['forestareaoflandarea2020'])
print(mean_forest2020)
stdev_forest2020 = statistics.stdev(dataforest['forestareaoflandarea2020'])
print(stdev_forest2020)
sns.boxplot(dataforest['forestareaoflandarea2020'])
plt.ylabel('Share of Forest Area (of Total Land Area) in %')
plt.show()
sns.violinplot(dataforest['forestareaoflandarea2020'])
plt.ylabel('Share of Forest Area (of Total Land Area) in %')
plt.show()

# Distribution of protected areas
dataprotec = pd.read_csv('dataset_complete_worldbank.csv')
dataprotec = dataprotec.dropna(subset=['terrestrialandmarineprotectedare'])
mode_protec2020 = statistics.mode(dataprotec['terrestrialandmarineprotectedare'])
print(mode_protec2020)
median_protec2020 = statistics.median(dataprotec['terrestrialandmarineprotectedare'])
print(median_protec2020)
mean_protec2020 = statistics.mean(dataprotec['terrestrialandmarineprotectedare'])
print(mean_protec2020)
stdev_protec2020 = statistics.stdev(dataprotec['terrestrialandmarineprotectedare'])
print(stdev_protec2020)
sns.boxplot(dataprotec['terrestrialandmarineprotectedare'])
plt.ylabel('Share of Terrestrial and Marine Protected Areas (of Total Land Area) in %')
plt.show()
sns.violinplot(dataprotec['terrestrialandmarineprotectedare'])
plt.ylabel('Share of Terrestrial and Marine Protected Areas (of Total Land Area) in %')
plt.show()

# Covariance and correlation between biodiversity indicators and CO2 emissions
dataset = pd.read_csv('dataset_complete_worldbank.csv')
forest = dataset['forestareaoflandarea2020']
protected_areas = dataset['terrestrialandmarineprotectedare']
co2 = dataset['co2emissionspercap2020']

data = pd.DataFrame({'forest': forest, 'protected_areas': protected_areas, 'co2': co2})
data_clean = data.dropna()
forest_clean = data_clean['forest']
protected_areas_clean = data_clean['protected_areas']
co2_clean = data_clean['co2']

cov_matrix1 = np.cov(forest_clean, co2_clean)
cov_matrix2 = np.cov(protected_areas_clean, co2_clean)
covariance1 = cov_matrix1[0, 1]
print(covariance1)
covariance2 = cov_matrix2[0, 1]
print(covariance2)
pearson_corr1 = np.corrcoef(forest_clean, co2_clean)[0, 1]
pearson_corr2 = np.corrcoef(protected_areas_clean, co2_clean)[0, 1]
print(pearson_corr1)
print(pearson_corr2)

plt.figure(figsize=(10, 6))
sns.regplot(x=forest, y=co2, line_kws={'color': 'red'})
plt.xlabel('Share of Forest Area (of Total Land Area) in %')
plt.ylabel('CO2 Emissions per Capita in Tons')
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(x=protected_areas, y=co2, line_kws={'color': 'red'})
plt.xlabel('Share of Terrestrial and Marine Protected Areas (of Total Land Area) in %')
plt.ylabel('CO2 Emissions per Capita in Tons')
plt.show()


