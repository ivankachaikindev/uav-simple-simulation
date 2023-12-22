import time

from dronekit import mavutil

from global_constants import UPDATE_RATE


def set_yaw(drone, target_yaw):
    __send_mavlink_message_setting_yaw(drone, target_yaw)
    __wait_for_setting_yaw(drone, target_yaw)


def __send_mavlink_message_setting_yaw(drone, target_yaw):
    speed = 5
    direction = 1
    is_relative = 0
    mavlink_message = drone.message_factory.command_long_encode(
        0, 0,
        mavutil.mavlink.MAV_CMD_CONDITION_YAW,
        0,
        target_yaw,
        speed,
        direction,
        is_relative,
        0, 0, 0
    )
    drone.send_mavlink(mavlink_message)


def __wait_for_setting_yaw(drone, target_yaw):
    while True:
        if __drone_reached_target_yaw(drone, target_yaw):
            break
        time.sleep(UPDATE_RATE)


def __drone_reached_target_yaw(drone, target_yaw):
    current_yaw = drone.attitude.yaw
    diff = abs(target_yaw - current_yaw)
    return diff < 0.1
