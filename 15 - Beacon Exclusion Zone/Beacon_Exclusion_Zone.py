import re
from math import ceil

with open("test_input.in", 'r') as fh:
    input = fh.read().splitlines()
    pattern = r'Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)'
    input = [list(map(int, re.match(pattern, lin).groups())) for lin in input]


class SubterraneanTunnel():
    @classmethod
    def dist(cls, p1, p2):
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

    def __init__(self, input):
        self.sensors = []
        self.beacons = []
        self.dists = []
        self.sensor_amount = 0
        for (x1, y1, x2, y2) in input:
            self.sensors.append((x1, y1))
            self.beacons.append((x2, y2))
            self.dists.append(SubterraneanTunnel.dist(
                self.sensors[-1], self.beacons[-1]))
            self.sensor_amount += 1

    def no_beacon_on_row(self, y, q2=False, q2args=None):
        intervals = []
        beacons_on_y = set()
        for i in range(self.sensor_amount):
            xs, ys = self.sensors[i]
            delta = self.dists[i] - abs(ys - y)
            if delta < 0:
                continue
            intervals.append((xs - delta, xs + delta))
            if self.beacons[i][1] == y:
                beacons_on_y.add(self.beacons[i])
        uni = SubterraneanTunnel.interval_union(intervals)
        res = 0 if q2 else -len(beacons_on_y)
        for (x, y) in uni:
            if q2:
                xmin, xmax = q2args[0], q2args[1]
                res += min(y, xmax) - max(x, xmin) + 1
            else:
                res += y - x + 1
        return res

    @classmethod
    def interval_union(cls, intervals):
        inter = sorted(intervals, key=lambda x: x[0])
        uni = []
        if len(inter) <= 1:
            return inter
        while len(inter) != 1:
            x = inter[0]
            while True:
                try:
                    y = inter[1]
                except IndexError:
                    break
                if y[0] <= x[1] + 1:
                    x = (x[0], max(x[1], y[1]))
                    inter.pop(1)
                else:
                    uni.append(x)
                    inter.pop(0)
                    break
        uni.append(x)
        return uni

    def q2(self, xmin, xmax):
        for y in range(xmin, xmax + 1):
            if y % ceil(xmax / 100) == 0:
                print(y/xmax)
            nbr = self.no_beacon_on_row(y, q2=True, q2args=(xmin, xmax))
            if nbr != (xmax - xmin + 1):
                break

        intervals = []
        beacons_on_y = set()
        for i in range(self.sensor_amount):
            xs, ys = self.sensors[i]
            delta = self.dists[i] - abs(ys - y)
            if delta < 0:
                continue
            intervals.append((xs - delta, xs + delta))
            if self.beacons[i][1] == y:
                beacons_on_y.add(self.beacons[i])
        uni = SubterraneanTunnel.interval_union(intervals)
        if uni[0][0] == 1:
            x = 0
        elif uni[-1][1] == xmax - 1:
            x = xmax
        else:
            x = uni[0][1] + 1

        return xmax * x + y


st = SubterraneanTunnel(input)

print(f"question 1: {st.no_beacon_on_row(10)}")  # 5299855
print(f"question 2: {st.q2(0, 20)}")  # 13615843289729
