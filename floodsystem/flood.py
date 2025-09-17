# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
 flood data."""

from floodsystem.utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, each containing a station and its relative water level,
    for all stations where the relative level is over the threshold tol. The list is sorted
    in descending order of relative level."""
    
    stations_over_tol = []
    
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > tol:
            stations_over_tol.append((station.name, station.relative_water_level()))
    
    return sorted_by_key(stations_over_tol, 1, True)