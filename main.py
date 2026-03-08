from orbit import ISS
from datetime import datetime
from time import sleep
import math

RUN_TIME = 9 * 60
INTERVAL = 5


def get_position():
    satellite = ISS()
    ts = satellite.ts
    t = ts.now()

    geocentric = satellite.at(t)

    x, y, z = geocentric.position.km  # 3D position in km

    return datetime.now(), (x, y, z)


def distance_3d(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def main():
    start_time = datetime.now()
    positions = []

    while (datetime.now() - start_time).total_seconds() < RUN_TIME:
        positions.append(get_position())
        sleep(INTERVAL)

    total_distance = 0

    for i in range(1, len(positions)):
        total_distance += distance_3d(
            positions[i - 1][1],
            positions[i][1]
        )

    total_time = (positions[-1][0] - positions[0][0]).total_seconds()

    speed = total_distance / total_time  # km/s

    speed_formatted = "{:.5g}".format(speed)

    with open("result.txt", "w") as f:
        f.write(speed_formatted)


if __name__ == "__main__":
    main()
