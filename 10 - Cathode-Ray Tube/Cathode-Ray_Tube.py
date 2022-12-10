with open("test_input.in", 'r') as fh:
    input = fh.read().splitlines()


def q1(input, start=20, interval=40):
    cycle = 0
    rax = 1
    sigstr = 0
    for instr in input:
        if instr == "noop":
            cycle += 1
            if (cycle >= start) and ((cycle - start) % interval) == 0:
                sigstr += cycle * rax
                print(cycle)
        else:
            cycle += 2
            if (cycle >= start) and ((cycle - start) % interval) in [0, 1]:
                sigstr += (cycle - (cycle % 2)) * rax
                print(cycle)
            rax += int(instr.split()[1])
    return sigstr


def q2_logic(input, interval=40):
    cycle = 0
    rax = 1
    crt = ''
    for instr in input:
        if instr == "noop":
            crt += "█" if abs((cycle % interval) - rax) <= 1 else ' '
            cycle += 1
        else:
            for _ in '  ':
                crt += "█" if abs((cycle % interval) - rax) <= 1 else ' '
                cycle += 1
            rax += int(instr.split()[1])
    return crt


def q2(input, interval=40):
    q2l = q2_logic(input, interval)
    q2l = [q2l[i:i + interval] for i in range(0, len(q2l), interval)]
    return "\n" + "\n".join(q2l)


print(f"question 1: {q1(input)}")  # 1175
print(f"question 2: {q2(input)}")  # 3217
