# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data."""

from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine

# Function which returns a list of distances of stations from a coordinate p
def stations_by_distance(stations, p):
    station_distance = []
    
    #looping through each station in the list of stations
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station.name, station.town, distance))
        
    return sorted_by_key(station_distance,2)

# Function which returns a list of stations within radius r from the centre point
def stations_within_radius(stations, centre, r):
    stations_within_r = []
    
    #looping through each station in the list of stations
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            stations_within_r.append(station.name)
            
    return sorted(stations_within_r)

#  returns a  set with the names of the rivers with a monitoring station
def rivers_with_station(stations):
    set_of_rivers = set()
    
    for station in stations:
        set_of_rivers.add(station.river)
    return set_of_rivers

#  returns a dictionary that maps river names to a list of station objects on a given river.
def stations_by_river(stations):
    dict_of_river_to_stations = {}
    
    for station in stations:
        if station.river not in dict_of_river_to_stations:
            dict_of_river_to_stations[station.river] = [station.name]
        else:
            dict_of_river_to_stations[station.river].append(station.name)
    
    return dict_of_river_to_stations

#  returns a list of rivers that determines the N rivers with the greatest number of monitoring stations
def rivers_by_station_number(stations, N):
    list_of_rivers = []
    for key, value in stations_by_river(stations).items():
        list_of_rivers.append((key, len(value)))
        
    return sorted_by_key(list_of_rivers, 1, True)[:N]
    
    
        
