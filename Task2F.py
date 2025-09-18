# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_level_with_fit

def run():

    # Build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)

    # 5 stations with highest relative water level
    stations_with_level = []
    
    for station in stations:
        if station.relative_water_level() is not None:
            stations_with_level.append([station, station.relative_water_level()])
    
    stations_5_highest = [station[0] for station in sorted_by_key(stations_with_level, 1, True)[:5]]
    
    
    # Plotting the water level data for the 5 stations with highest relative water level inclkuding a polynomial fit
    for station in stations_5_highest:
        dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=10)) 
        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
