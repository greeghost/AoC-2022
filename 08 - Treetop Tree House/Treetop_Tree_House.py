with open("test_input.in", 'r') as fh:
    input = fh.read().splitlines()

height = len(input)
width = len(input[0])


def visible(input, x, y):
    vtop, vrig, vlef, vbot = True, True, True, True
    h = input[y][x]
    for ix in range(x):
        if input[y][ix] >= h:
            vlef = False
            break
    for ix in range(x + 1, width):
        if input[y][ix] >= h:
            vrig = False
            break
    for iy in range(y):
        if input[iy][x] >= h:
            vtop = False
            break
    for iy in range(y + 1, height):
        if input[iy][x] >= h:
            vbot = False
            break
    return vlef or vrig or vtop or vbot


def scenic_score(input, x, y):
    stop, srig, slef, sbot = 0, 0, 0, 0
    h = input[y][x]

    i = x - 1
    while i >= 0:
        slef += 1
        if input[y][i] >= h:
            break
        i -= 1

    i = x + 1
    while i < width:
        srig += 1
        if input[y][i] >= h:
            break
        i += 1

    i = y - 1
    while i >= 0:
        stop += 1
        if input[i][x] >= h:
            break
        i -= 1

    i = y + 1
    while i < height:
        sbot += 1
        if input[i][x] >= h:
            break
        i += 1

    return stop * srig * slef * sbot


def q1(input):
    count = 0
    for x in range(height):
        for y in range(width):
            count += visible(input, x, y)
    return count


def q2(input):
    smax = 0
    for x in range(height):
        for y in range(width):
            smax = max(smax, scenic_score(input, x, y))
    return smax


print(f"question 1: {q1(input)}")  # 1684
print(f"question 2: {q2(input)}")  # 486540
