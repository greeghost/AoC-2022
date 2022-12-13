from collections import deque

with open("test_input.in", 'r') as fh:
    input = fh.read().splitlines()


class Grid():
    def __init__(self, input):
        self.height = len(input)
        self.length = len(input[0])
        self.layout = input
        self.start = self.__get_coord("S")[0]
        self.end = self.__get_coord("E")[0]

    def __get_coord(self, symbol):
        res = []
        for i in range(self.height):
            for j in range(self.length):
                if self.layout[i][j] == symbol:
                    res.append((j, i))
        return res

    def neighbours(self, coords, inv=False):
        res = []
        i, j = coords
        for (i2, j2) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if (i2 < 0) or (j2 < 0) \
                    or (i2 >= self.length) or (j2 >= self.height):
                continue  # Invalid vertex coordinates

            # replace 'S' and 'E' with 'a' and 'z'
            comp1 = self.layout[j][i]
            comp1 = [comp1, 'a', 'z'][(comp1 == 'S') + 2 * (comp1 == 'E')]
            comp2 = self.layout[j2][i2]
            comp2 = [comp2, 'a', 'z'][(comp2 == 'S') + 2 * (comp2 == 'E')]

            # Neighbours have consecutive letters in the alphabet
            c1 = comp1 if not inv else comp2
            c2 = comp2 if not inv else comp1
            if ord(c1) + 1 >= ord(c2):
                res.append((i2, j2))
        return res

    def bfs(self, s):
        queue = deque((s, ))
        seen = {s}
        parents = {}
        while queue != deque():
            (vi, vj) = queue.popleft()
            if self.layout[vj][vi] == "E":
                return parents
            for (wi, wj) in self.neighbours((vi, vj)):
                if (wi, wj) not in seen:
                    seen.add((wi, wj))
                    parents[(wi, wj)] = (vi, vj)
                    queue.append((wi, wj))

    def q1(self):
        d = self.bfs(self.start)
        path_length = 0
        node = self.end
        while node != self.start:
            node = d[node]
            path_length += 1
        return path_length

    def bfs2(self):
        queue = deque((self.end, ))
        seen = {self.end}
        parents = {}
        while queue != deque():
            (vi, vj) = queue.popleft()
            if self.layout[vj][vi] in "Sa":
                return parents, (vi, vj)
            for (wi, wj) in self.neighbours((vi, vj), inv=True):
                if (wi, wj) not in seen:
                    seen.add((wi, wj))
                    parents[(wi, wj)] = (vi, vj)
                    queue.append((wi, wj))

    def q2(self):
        d, (vi, vj) = self.bfs2()
        path_length = 0
        node = (vi, vj)
        while node != self.end:
            node = d[node]
            path_length += 1
        return path_length


g = Grid(input)

print(f"question 1: {g.q1()}")  # 456
print(f"question 2: {g.q2()}")  # 454
