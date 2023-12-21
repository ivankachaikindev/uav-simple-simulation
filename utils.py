import math


def get_distance_in_metres(left_position, right_position):
    diff_lat = left_position.lat - right_position.lat
    diff_lon = left_position.lon - right_position.lon
    return math.sqrt(diff_lat ** 2 + diff_lon ** 2) * 1.113195e5
