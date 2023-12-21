from argparse import ArgumentParser

from dronekit import connect

from take_off import arm_and_take_off

parser = ArgumentParser('Launch drone, move from A to B, then rotate')
parser.add_argument(
    '--drone_ip', type=str, required=True,
    help='Drone IP to connect manipulate with'
)

TARGET_ALTITUDE = 100.0


def main(drone_ip):
    drone = __connect_to_drone(drone_ip)
    arm_and_take_off(drone, TARGET_ALTITUDE)


def __connect_to_drone(drone_ip):
    drone = connect(
        drone_ip,
        wait_ready=True,
        timeout=60,
        heartbeat_timeout=60
    )
    return drone


if __name__ == '__main__':
    args = parser.parse_args()
    main(args.drone_ip)
