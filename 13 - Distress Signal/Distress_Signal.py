from functools import cmp_to_key

with open("test_input.in", 'r') as fh:
    input = list(map(lambda x: x.splitlines(), fh.read().split("\n\n")))


class Comparator():
    def __init__(self, input):
        self.couples = input
        self.right_orders = []
        self.index = 0

    def get_vals(self):
        if self.index >= len(self.couples):
            return False
        val1, val2 = self.couples[self.index]
        val1, val2 = eval(val1), eval(val2)
        return val1, val2

    def compare(self):
        if self.index >= len(self.couples):
            return False
        val1, val2 = self.get_vals()
        self.index += 1

        val = Comparator.comparison(val1, val2)

        if val == 1:
            self.right_orders.append(self.index)
        return True

    @classmethod
    def comparison(cls, val1, val2):

        # one of val1, val2 empty
        if len(val1) == 0 and len(val2) != 0:
            return 1
        if len(val2) == 0 and len(val1) != 0:
            return -1
        if len(val1) == 0 and len(val2) == 0:
            return 0
        v1, v2 = val1[0], val2[0]

        # int - int
        if isinstance(v1, int) and isinstance(v2, int):
            if v1 < v2:
                return 1
            if v2 < v1:
                return -1
            if v1 == v2:
                return Comparator.comparison(val1[1:], val2[1:])

        # list - list
        if isinstance(v1, list) and isinstance(v2, list):
            res = Comparator.comparison(v1, v2)
            if res == 0:
                return Comparator.comparison(val1[1:], val2[1:])
            else:
                return res

        # int - list
        if isinstance(v1, int) and isinstance(v2, list):
            res = Comparator.comparison([v1], v2)
            if res == 0:
                return Comparator.comparison(val1[1:], val2[1:])
            else:
                return res

        # list - int
        if isinstance(v1, list) and isinstance(v2, int):
            res = Comparator.comparison(v1, [v2])
            if res == 0:
                return Comparator.comparison(val1[1:], val2[1:])
            else:
                return res

    def q1(self):
        while self.compare():
            pass
        return sum(self.right_orders)

    def q2(self):
        li = [[[2]], [[6]]]
        while (t := self.get_vals()):
            li.append(t[0])
            li.append(t[1])
            self.index += 1
        tmp = sorted(li, key=cmp_to_key(Comparator.comparison), reverse=True)

        i1, i2 = tmp.index([[2]]), tmp.index([[6]])
        return (i1 + 1) * (i2 + 1)


comp1 = Comparator(input)
comp2 = Comparator(input)

print(f"question 1: {comp1.q1()}")  # 5852
print(f"question 2: {comp2.q2()}")  # 24190
