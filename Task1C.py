# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # prints a list of tuples stations within 10km from the Cambridge city centre, (52.2053, 0.1218)
    list_of_stations = stations_within_radius(stations, (52.2053, 0.1218), 10)
    print("stations within 10km from Cambridge city centre:{}".format(list_of_stations))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
