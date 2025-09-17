# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # prints a list of tuples (station name, town, distance) for the 10 closest and the 10 furthest stations from (52.2053, 0.1218)
    list_of_tuples = stations_by_distance(stations, (52.2053, 0.1218))
    print("10 closest stations to Cambridge city centre:{}".format(list_of_tuples[:10]))
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("10 furthest stations to Cambridge city centre:{}".format(list_of_tuples[-10:]))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
