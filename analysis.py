import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Analysis taking GDP into consideration
data = pd.read_csv('dataset_complete_worldbank.csv')
median_gdp = data['gdppercapitacurrentus2020'].median()
data['GDP per Capita Dummy'] = np.where(data['gdppercapitacurrentus2020'] > median_gdp, 'Above Median GDP per Capita', 'Below Median GDP per Capita')
tercile_emissions = pd.qcut(data['co2emissionspercap2020'], q=3,
                            labels=['Lowest 30% of CO2 Emissions', 'Middle 30% of CO2 Emissions', 'Highest 30% of CO2 Emissions'])
forest = data['forestareaoflandarea2020']
protected_areas = data['terrestrialandmarineprotectedare']
co2 = data['co2emissionspercap2020']
gdp_percap = data['gdppercapitacurrentus2020']
GDP_per_Capita_Dummy = data['GDP per Capita Dummy']

data = pd.DataFrame({'forest': forest, 'protected_areas': protected_areas, 'co2': co2, 'Terciles CO2 Emissions': tercile_emissions,
                     'GDP per Capita Dummy': GDP_per_Capita_Dummy, 'GDP per Capita': gdp_percap})
data_clean = data.dropna()
forest_clean = data_clean['forest']
protected_areas_clean = data_clean['protected_areas']
co2_clean = data_clean['co2']
tercile_emissions_clean = data_clean['Terciles CO2 Emissions']
gdp_percap_clean = data_clean['GDP per Capita']
GDP_per_Capita_Dummy = data_clean['GDP per Capita Dummy']

plt.figure(figsize=(10, 6))
sns.scatterplot(x=forest, y=co2, hue=GDP_per_Capita_Dummy)
plt.xlabel('Share of Terrestrial and Marine Protected Areas (of Total Land Area) in %')
plt.ylabel('CO2 Emissions per Capita in Tons')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=protected_areas, y=co2, hue=GDP_per_Capita_Dummy)
plt.xlabel('Share of Terrestrial and Marine Protected Areas (of Total Land Area) in %')
plt.ylabel('CO2 Emissions per Capita in Tons')
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(x=forest, y=gdp_percap, line_kws={'color': 'red'})
plt.xlabel('Share of Forest Area (of Total Land Area) in %')
plt.ylabel('GDP per Capita in US$')
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(x=protected_areas, y=gdp_percap, line_kws={'color': 'red'})
plt.xlabel('Share of Terrestrial and Marine Protected Areas (of Total Land Area) in %')
plt.ylabel('GDP per Capita in US$')
plt.show()

# CO2 emission groups
x = range(len(data_clean['Terciles CO2 Emissions'].unique()))
bar_width = 0.35

low_co2_forest = data_clean[data_clean['Terciles CO2 Emissions'] == 'Lowest 30% of CO2 Emissions']['forest']
mid_co2_forest = data_clean[data_clean['Terciles CO2 Emissions'] == 'Middle 30% of CO2 Emissions']['forest']
high_co2_forest = data_clean[data_clean['Terciles CO2 Emissions'] == 'Highest 30% of CO2 Emissions']['forest']

low_co2_protected = data_clean[data_clean['Terciles CO2 Emissions'] == 'Lowest 30% of CO2 Emissions']['protected_areas']
mid_co2_protected = data_clean[data_clean['Terciles CO2 Emissions'] == 'Middle 30% of CO2 Emissions']['protected_areas']
high_co2_protected = data_clean[data_clean['Terciles CO2 Emissions'] == 'Highest 30% of CO2 Emissions']['protected_areas']

plt.figure(figsize=(10, 6))

plt.bar([i - bar_width for i in x], low_co2_forest, width=bar_width, label='Low Emissions')
plt.bar([i - bar_width for i in x], mid_co2_forest, width=bar_width, bottom=low_co2_forest, label='Medium Emissions')
plt.bar([i - bar_width for i in x], high_co2_forest, width=bar_width, bottom=low_co2_forest + mid_co2_forest, label='High Emissions')

plt.bar([i + bar_width for i in x], low_co2_protected, width=bar_width, label='Low Emissions')
plt.bar([i + bar_width for i in x], mid_co2_protected, width=bar_width, bottom=low_co2_protected, label='Medium Emissions')
plt.bar([i + bar_width for i in x], high_co2_protected, width=bar_width, bottom=low_co2_protected + mid_co2_protected, label='High Emissions')

plt.xlabel('CO2 Emissions')
plt.ylabel('Values')
plt.xticks(x, data_clean['Terciles CO2 Emissions'].unique())
plt.legend()
plt.tight_layout()
plt.show()
