with open("test_input.in", 'r') as fh:
    input = list(map(lambda x: (x[0], x[2]), fh.read().split("\n")[:-1]))


def score_by_move(a, b):
    rps1 = {"A": 0, "B": 1, "C": 2}
    rps2 = {"X": 0, "Y": 1, "Z": 2}
    s1, s2 = rps1[a], rps2[b]
    if s1 == s2:  # Tie
        return s2 + 4
    elif (s1 + 1) % 3 == s2:  # Victory
        return s2 + 7
    return s2 + 1  # Defeat


def score_by_result(a, b):
    rps1 = {"A": 1, "B": 2, "C": 3}
    rps2 = {"X": 0, "Y": 1, "Z": 2}
    s1, s2 = rps1[a], rps2[b]
    return 3 * s2 + ((s1 + s2 - 2) % 3) + 1


def value(strategy, decrypt):
    total = 0
    for (a, b) in strategy:
        total += decrypt(a, b)
    return total


print(f"question 1: {value(input, score_by_move)}")  # 10624
print(f"question 2: {value(input, score_by_result)}")  # 14060
