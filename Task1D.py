# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # prints a set of rivers with a monitoring station
    list_of_rivers = rivers_with_station(stations)
    print("{} stations. First 10 - {}".format(len(list_of_rivers), sorted(list_of_rivers)[:10]))
    
    # prints rivers for a given monitoring station
    dict_of_rivers = stations_by_river(stations)
    print("River Aire: {}".format(sorted(dict_of_rivers["River Aire"])))
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("River Cam: {}".format(sorted(dict_of_rivers["River Cam"])))
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("River Thames: {}".format(sorted(dict_of_rivers["River Thames"])))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
