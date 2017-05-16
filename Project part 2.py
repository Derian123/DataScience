#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:16:31 2017

@author: derianescobar
"""

import folium
import pandas as pd

bronx = 0
manhattan = 0
queens = 0
brooklyn = 0
island = 0
longitude = []
latitude = []
count = []
population = [1455720, 1643734, 2333054, 2629150, 476015]
crimeRates = []

tRate = []

reader = pd.read_csv('taxi.csv')
for index, row in reader.iterrows():
    lat = row["dropoff_latitude"]
    lon = row["dropoff_longitude"]
    if (lat < 40.87731 and lat > 40.80231) and (lon < -73.86898 and lon > -73.92125):
        bronx = bronx + 1
    if (lat < 40.800816 and lat > 40.71259) and (lon < -73.930435 and lon > -74.012403):
        manhattan = manhattan + 1
    if (lat < 40.780541 and lat > 40.648866) and (lon < -73.779373 and lon > -73.848038):
        queens = queens + 1
    if (lat < 40.708751 and lat > 40.608219) and (lon < -73.957901 and lon > -74.034119):
        brooklyn = brooklyn + 1
    if (lat < 40.603005 and lat > 40.507535) and (lon < 74.058151 and lon > -74.254532):
        island = island + 1

count.append(bronx)
count.append(manhattan)
count.append(queens)
count.append(brooklyn)
count.append(island)
boroughs = ["Bronx", "Manhattan", "Queens", "Brooklyn", "Staten Island"]

for i in range(0, len(count)):
    rate = count[i] / population[i]
    borough = boroughs[i]
    tRate.append(rate)
    info = {"Borough": borough, "Taxi Rate": rate}
    crimeRates.append(info)

dataFrame = pd.DataFrame.from_dict(crimeRates)

dataFrame.to_csv("taxiData.csv")

print(tRate)