# Are those who pollute also those who contribute (to biodiversity conservation)?

This code can be used to descriptively and graphically analyze data on CO2 emissions and several indicators for biodiversity conservation. I used CO2 emissions per capita as indicator for climate change.
As indicator for biodiversity I used share of forest areas in % of total land area, as well as share of terrestrial and marine protected areas in % of total land area. 
Additionally, I include data on GDP per capita. The code will produce descriptive statistics, boxplots, violin plots, regression plots, as well as scatterplots for specific relations in the data. 
The two datasets in long format can be used to display the average of worldwide average CO2 emissions from 1990-2020 and the average forest area worldwide from 1991-2020.

## Data sources

The data for the different indicators were downloaded from the World Bank Open Data (https://data.worldbank.org/) and subsequently preprocessed in a combined dataset. 
The data on CO2 emissions are from Climate Watch Historical GHG Emissions (1990-2020) are provided by the World Resources Institute
and are available online (https://www.climatewatchdata.org/ghg-emissions).
The data on the share of terrestrial and marine protected areas are provided by the World Database on Protected Areas (WDPA). The WDPA, managed by the UN Environment World Conservation Monitoring Centre (UNEP-WCMC)
in collaboration with various stakeholders, provides comprehensive data on these areas, accessible through the Protected Planet website (https://www.protectedplanet.net)
The data on the share of forest areas are gathered from the Food and Agriculture Organization of the United Nations (UN).

## How to load the dataset
Start
```shell
python main.py
```

