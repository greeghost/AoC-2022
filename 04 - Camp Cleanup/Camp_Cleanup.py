input = []

with open("input.in", 'r') as fh:
    for line in fh:
        [p1, p2] = line[:-1].split(",")
        [s1, s2] = p1.split("-")
        [s3, s4] = p2.split("-")
        input.append((int(s1), int(s2), int(s3), int(s4)))


def inclusion(s1, s2, s3, s4):
    if (s1 <= s3) and (s2 >= s4):
        return True
    if (s3 <= s1) and (s4 >= s2):
        return True
    return False


def overlap(s1, s2, s3, s4):
    if (s2 >= s3) and (s4 >= s1):
        return True
    if (s3 >= s2) and (s1 >= s4):
        return True
    return False


def q(input, f):
    cpt = 0
    for (s1, s2, s3, s4) in input:
        cpt += f(s1, s2, s3, s4)
    return cpt


print(f"question 1: {q(input, inclusion)}")  # 657
print(f"question 2: {q(input, overlap)}")  # 938
