from argparse import ArgumentParser

from dronekit import connect

parser = ArgumentParser('Launch drone, move from A to B, then rotate')
parser.add_argument(
    '--drone_ip', type=str, required=True,
    help='Drone IP to connect manipulate with'
)


def main(drone_ip):
    drone = __connect_to_drone(drone_ip)
    print(drone.mode.name)


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
