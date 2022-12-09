from itertools import tee

with open("input.in", 'r') as fh:
    input = map(lambda s: (str.split(s)[0], int(
        str.split(s)[1])), fh.read().splitlines())


class RopeBridge():
    DIRS = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }

    def __init__(self, instr, knot_amount):
        self.knot_amount = knot_amount
        self.knots = [(0, 0) for _ in range(knot_amount)]
        self.visited = {(0, 0)}
        self.instr = instr

    def process(self):
        try:
            direction, distance = next(self.instr)
            direction = self.DIRS[direction]
            for _ in range(distance):
                self.knots[0] = tuple_sum(self.knots[0], direction)
                self.visited.add(self.update_knot_positions())
        except StopIteration:
            print("Rope Bridge fully processed!")
            return 0
        return 1

    def update_knot_positions(self):
        for i in range(1, self.knot_amount):
            self.update_knot_position(i)
        return self.knots[-1]

    def update_knot_position(self, knot):
        h = self.knots[knot - 1]
        t = self.knots[knot]
        if abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2:
            return t
        dx = h[0] - t[0]
        dy = h[1] - t[1]
        if abs(dx) == 2:
            update_vector = (int(dx / 2), int(dy / 2) if abs(dy) == 2 else dy)
        else:
            update_vector = (int(dx / 2) if abs(dx) == 2 else dx, int(dy / 2))
        self.knots[knot] = tuple_sum(t, update_vector)
        return self.knots[knot]

    def tail_visits(self):
        while self.process():
            pass
        return len(self.visited)


def tuple_sum(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


i1, i2 = tee(input)

print(f"question 1: {RopeBridge(i1, 2).tail_visits()}")  # 1175
print(f"question 2: {RopeBridge(i2, 10).tail_visits()}")  # 3217
