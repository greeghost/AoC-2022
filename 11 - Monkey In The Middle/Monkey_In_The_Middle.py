with open("test_input.in", 'r') as fh:
    input = map(str.splitlines, fh.read().split("\n\n"))


class Item():
    def __init__(self, worry_level):
        self.worry_level = worry_level


class Monkey():
    MAGIC_OPERATION_CONSTANT = len("  Operation: new = ")

    def __init__(self, index, invt, operation, test, m_true, m_false):
        self.index = index
        self.invt = invt
        self.operation = lambda old: eval(operation)
        self.test = lambda x: not (x % test)
        self.monkey_true = m_true
        self.monkey_false = m_false
        self.activity = 0
        self.test_prod = test

    def inspect(self, q=1):
        item = self.invt.pop(0)
        item.worry_level = self.operation(item.worry_level)
        if q == 1:
            item.worry_level = int(item.worry_level / 3)
        item.worry_level = item.worry_level % self.test_prod
        self.throw(item)
        self.activity += 1

    def throw(self, item):
        if self.test(item.worry_level):
            self.monkey_true.invt.append(item)
        else:
            self.monkey_false.invt.append(item)


class MonkeyPack():
    def __init__(self):
        self.monkeys = []
        self.test_prod = 1

    def add_monkey(self, **kwargs):
        self.monkeys.append(Monkey(**kwargs))
        self.test_prod *= kwargs.get("test", 1)

    def finish_initialization(self):
        # To be called once no more monkeys will be added to the Monkey Pack
        for monkey in self.monkeys:
            monkey.monkey_true = self.monkeys[monkey.monkey_true]
            monkey.monkey_false = self.monkeys[monkey.monkey_false]
            monkey.test_prod = self.test_prod

    def do_round(self, q=1):
        for monkey in self.monkeys:
            while monkey.invt != []:
                monkey.inspect(q)

    def monkey_business(self):
        max1, max2 = 0, 0
        for m in self.monkeys:
            act = m.activity
            if act > max1:
                max1, max2 = act, max1
            elif act > max2:
                max2 = act
        return max1 * max2

    def q1(self):
        for i in range(20):
            self.do_round(1)
        return self.monkey_business()

    def q2(self):
        for i in range(10000):
            self.do_round(2)
        return self.monkey_business()


packs = [MonkeyPack(), MonkeyPack()]

for monkey in input:
    packs[0].add_monkey(index=int(monkey[0].split()[1][:-1]),
                        invt=[Item(int(tl[:] if tl[-1] != "," else tl[:-1]))
                              for tl in monkey[1].split()[2:]],
                        operation=monkey[2][Monkey.MAGIC_OPERATION_CONSTANT:],
                        test=int(monkey[3].split()[-1]),
                        m_true=int(monkey[4].split()[-1]),
                        m_false=int(monkey[5].split()[-1]))

    packs[1].add_monkey(index=int(monkey[0].split()[1][:-1]),
                        invt=[Item(int(tl[:] if tl[-1] != "," else tl[:-1]))
                              for tl in monkey[1].split()[2:]],
                        operation=monkey[2][Monkey.MAGIC_OPERATION_CONSTANT:],
                        test=int(monkey[3].split()[-1]),
                        m_true=int(monkey[4].split()[-1]),
                        m_false=int(monkey[5].split()[-1]))

packs[0].finish_initialization()
packs[1].finish_initialization()


print(f"question 1: {packs[0].q1()}")  # 1175
print(f"question 2: {packs[1].q2()}")  # 3217
