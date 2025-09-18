# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels

def run():
    # Build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)

    # Stations with highest relative water level
    stations_with_level = []
    
    for station in stations:
        if station.relative_water_level() is not None:
            stations_with_level.append((station, station.relative_water_level()))
            
    # Stations with highest relative water level by town
    stations_highest_by_town = {}
    for station in stations_with_level:
        town = station[0].town
        if town not in stations_highest_by_town:
            stations_highest_by_town[town] = station[1]
        elif station[1] > stations_highest_by_town[town]:
            stations_highest_by_town[town] = station[1]
    
    stations_highest_by_town_sorted = dict(sorted(stations_highest_by_town.items(), key=lambda item: item[1], reverse=True))
    list_of_towns = list(stations_highest_by_town_sorted.items())
    
   
    # Sorting results(Severe: higher than 0.8, High: 0.5-0.8, Moderate: 0.3-0.5, Low: lower than 0.3)
    severe = []
    high = []       
    moderate = []
    low = []
    for town in list_of_towns:
        if town[1] >= 0.8:
            severe.append((town[0], town[1]))
        elif town[1] >= 0.5:
            high.append((town[0], town[1]))
        elif town[1] >= 0.3:
            moderate.append((town[0], town[1]))
        else:
            low.append((town[0], town[1]))
    
    print("Severe:")
    print(severe, "\n")
    print("High:")
    print(high, "\n")
    print("Moderate:")
    print(moderate, "\n")
    print("Low:")
    print(low)

if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()