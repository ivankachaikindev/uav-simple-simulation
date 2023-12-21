import time

from dronekit import VehicleMode

from global_constants import UPDATE_RATE


def arm_and_take_off(drone, target_altitude):
    __wait_for_armable(drone)
    __set_mode_to_guided_and_arm(drone)
    __wait_for_armed(drone)
    __take_off_to_target_altitude(drone, target_altitude)


def __wait_for_armable(drone):
    while not drone.is_armable:
        time.sleep(UPDATE_RATE)


def __set_mode_to_guided_and_arm(drone):
    drone.mode = VehicleMode('GUIDED')
    drone.armed = True


def __wait_for_armed(drone):
    while not drone.armed:
        time.sleep(UPDATE_RATE)


def __take_off_to_target_altitude(drone, target_altitude):
    drone.simple_takeoff(target_altitude)
    while True:
        if __drone_reached_target_altitude(drone, target_altitude):
            break
        time.sleep(UPDATE_RATE)


def __drone_reached_target_altitude(drone, target_altitude):
    return drone.location.global_relative_frame.alt >= target_altitude * 0.95
