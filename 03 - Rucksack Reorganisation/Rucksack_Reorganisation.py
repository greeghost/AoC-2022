with open("test_input.in", 'r') as fh:
    input = list(map(
        lambda s: (s[:int(len(s) / 2)], s[int(len(s) / 2):]),
        fh.read().splitlines()))


def rank(c):
    return "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(c)


def find_duplicate(s1, s2):
    for c in s1:
        if c in s2:
            return c
    raise ValueError(f"No duplicate in {s1} and {s2}")


def find_truplicate(s1, s2, s3):
    for c in s1:
        if (c in s2) and (c in s3):
            return c
    raise ValueError(f"No truplicate in {s1}, {s2} and {s3}")


def q1(rucksacks):
    s = 0
    for (s1, s2) in rucksacks:
        s += rank(find_duplicate(s1, s2))
    return s


def q2(rucksacks):
    s = 0
    for i in range(0, len(rucksacks) - 2, 3):
        s1 = rucksacks[i][0] + rucksacks[i][1]
        s2 = rucksacks[i + 1][0] + rucksacks[i + 1][1]
        s3 = rucksacks[i + 2][0] + rucksacks[i + 2][1]
        s += rank(find_truplicate(s1, s2, s3))
    return s


print(f"question 1: {q1(input)}")  # 8109
print(f"question 2: {q2(input)}")  # 2738
