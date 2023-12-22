import time

from dronekit import LocationGlobalRelative

from global_constants import UPDATE_RATE
from utils import get_distance_in_metres


def go_to_target_position(drone, target_position):
    target_position = LocationGlobalRelative(*target_position)
    drone.simple_goto(target_position)
    __wait_for_reaching_target_position(drone, target_position)


def __wait_for_reaching_target_position(drone, target_position):
    while True:
        if __drone_reached_target_position(drone, target_position):
            break
        time.sleep(UPDATE_RATE)


def __drone_reached_target_position(drone, target_position):
    current_position = drone.location.global_relative_frame
    distance = get_distance_in_metres(current_position, target_position)
    return distance < 0.5
