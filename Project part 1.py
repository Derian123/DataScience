#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:54:56 2017

@author: derianescobar
"""

import folium
import pandas as pd
import matplotlib.pyplot as plt

bronx = 0
manhattan = 0
queens = 0
brooklyn = 0
island = 0
population = [1455720, 1643734, 2333054, 2629150, 476015]
count = []
pRate = []
crimeRates = []

tRate = [0.0036648531310966397, 0.5060764089566804, 0.0025443045896065843, 0.01790464598824715, 0.002493618898564121]

data = {}

reader = pd.read_csv('NYPD17.csv')
for index, row in reader.iterrows():
    date = str(row["RPT_DT"])
    borough = str(row["BORO_NM"])
    #    lat = str(row["Latitude"])
    #    lon = str(row["Longitude"])
    s = date.split("/")
    month = s[0]
    #    if(Latitude == 'nan' or Longitude == 'nan'):
    #        continue
    if (month == '01'):
        print(month, borough)
        if (borough == 'BRONX'):
            bronx = bronx + 1
        if (borough == "MANHATTAN"):
            manhattan = manhattan + 1
        if (borough == "QUEENS"):
            queens = queens + 1
        if (borough == "BROOKLYN"):
            brooklyn = brooklyn + 1
        if (borough == "STATEN ISLAND"):
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
    pRate.append(rate)
    info = {"Borough": borough, "Crime Rate": rate}
    crimeRates.append(info)

dataFrame = pd.DataFrame.from_dict(crimeRates)

dataFrame.to_csv("data.csv")

plt.scatter(pRate, tRate)
plt.xlabel("Taxi Rate")
plt.ylabel("Crime Rate")
plt.title("Correlation between taxi rate and Crime rate by borough")
plt.show()

print(pRate)