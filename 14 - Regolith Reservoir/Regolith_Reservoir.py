import functools

with open("input.in", 'r') as fh:
    input = list(map(lambda x: (
                list(map(lambda y: (
                    list(map(int, y.split(',')))),
                    x.split(' -> ')))),
                    fh.read().splitlines()))


class CaveSystem():
    def __init__(self, input):
        self.walls = input
        self.sand = set()
        self.depth = 0
        for wall in self.walls:
            for w in wall:
                self.depth = max(self.depth, w[1])
        self.floor = self.depth + 2
        self.lastX, self.lastY = 500, 0

    @functools.cache
    def walled(self, x, y):
        if y == self.floor:
            return True
        for wall in self.walls:
            for i in range(len(wall) - 1):
                w1 = wall[i]
                w2 = wall[i + 1]
                if ((x - w1[0]) * (x - w2[0]) <= 0) and (y - w1[1]) * (y - w2[1]) <= 0:
                    return True
        return False

    def process_some_sand1(self):
        x = 500
        y = 0
        while True:
            if y >= self.depth:
                return False
            if not (self.walled(x, y + 1) or (x, y + 1) in self.sand):
                y += 1
                continue
            if not (self.walled(x - 1, y + 1) or (x - 1, y + 1) in self.sand):
                x -= 1
                y += 1
                continue
            if not (self.walled(x + 1, y + 1) or (x + 1, y + 1) in self.sand):
                x += 1
                y += 1
                continue
            self.sand.add((x, y))
            return True

    def q1(self):
        cont = 0
        while self.process_some_sand1():
            cont += 1
        return cont

    def process_some_sand2(self, xorg=500, yorg=0):
        x = xorg
        y = yorg
        while True:
            if (xorg, yorg) in self.sand:
                return False
            if not (self.walled(x, y + 1) or (x, y + 1) in self.sand):
                y += 1
                continue
            if not (self.walled(x - 1, y + 1) or (x - 1, y + 1) in self.sand):
                x -= 1
                y += 1
                continue
            if not (self.walled(x + 1, y + 1) or (x + 1, y + 1) in self.sand):
                x += 1
                y += 1
                continue
            self.sand.add((x, y))
            # print(x, y, self.floor)
            return True

    def q2(self):
        cont = 0
        while self.process_some_sand2():
            cont += 1
            if cont % 100 == 0:
                print(cont)
        return cont


print(f"question 1: {CaveSystem(input).q1()}")  # 719
print(f"question 2: {CaveSystem(input).q2()}")  # 23390
