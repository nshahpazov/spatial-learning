import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


DEC_LANDS_PATH = './data/DEC_lands/DEClands.shp'
full_data = gpd.read_file(DEC_LANDS_PATH)


full_data.dtypes


type(full_data)


data = full_data.loc[:, ['CLASS', 'COUNTY', 'geometry']].copy()


data['CLASS'].value_counts()


WILD_TYPES = ['WILD FOREST', 'WILDERNESS']
wild_lands_data = data[data['CLASS'].isin(WILD_TYPES)]
wild_lands_data.head()


data['is_wilderness'] = data['CLASS'].isin(WILD_TYPES)
data.plot(column='is_wilderness', figsize=(14, 8))


wild_lands_data.plot(figsize=(14, 14), column='COUNTY');


poi_data = gpd.read_file('./data/Decptsofinterest.shp', encoding="utf-8")
road_data = gpd.read_file('./data/DEC_roadstrails/Decroadstrails.shp', encoding="utf-8")
county_data = gpd.read_file('./data/NY_county_boundaries/NY_county_boundaries.shp')


county_data.shape
# dbx file contains information about the columns (get_ipython().getoutput("IMPORTANT)")


CAMPSITE_TYPE = 'PRIMITIVE CAMPSITE'
campsites_df = poi_data[poi_data['ASSET'] == CAMPSITE_TYPE].copy()


# Define a base map with county boundaries
ax = county_data.plot(figsize=(10,10), color='none', edgecolor='gainsboro', zorder=3)

wild_lands_data.plot(color='lightgreen', ax=ax)
campsites_df.plot(color='maroon', markersize=0.5, ax=ax)
road_data.plot(color='pink', ax=ax)

