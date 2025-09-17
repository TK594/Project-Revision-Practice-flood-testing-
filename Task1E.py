# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # prints a set of rivers with a monitoring station
    list_of_rivers = rivers_by_station_number(stations, 9)
    print("9 rivers with the most mornitoring stations:{}".format(list_of_rivers))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()