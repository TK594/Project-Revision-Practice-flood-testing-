# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # prints a set of rivers with a monitoring station
    list_of_inconsistent = sorted(inconsistent_typical_range_stations(stations))
    print("Inconsistent data: {}".format(list_of_inconsistent))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()