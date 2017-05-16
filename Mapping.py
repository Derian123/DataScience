#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:15:32 2017

@author: derianescobar
"""

import folium
import pandas as pd

readCrime = pd.read_csv('data.csv')
readTaxi = pd.read_csv('taxiData.csv')

#Create a map:
crimeMap = folium.Map(location=[40.75, -74.125])

crimeMap.choropleth(geo_path="NYCBoroughs.geojson",
                    data = readCrime ,
                    fill_color = "PuRd",
                    key_on = "feature.properties.borough",
                    columns = ["Borough", "Crime Rate"],
                     fill_opacity=0.5, line_opacity=0.5
                     )

crimeMap.save(outfile='Crime Map.html')
print("Done")

taxiMap = folium.Map(location=[40.75, -74.125])

taxiMap.choropleth(geo_path="NYCBoroughs.geojson",
                    data = readTaxi ,
                    fill_color = "PuRd",
                    key_on = "feature.properties.borough",
                    columns = ["Borough", "Taxi Rate"],
                     fill_opacity=0.5, line_opacity=0.5
                     )

taxiMap.save(outfile='Taxi Map.html')
print("Done")