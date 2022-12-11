state = []
instr = []

with open("test_input.in", 'r') as fh:
    s = True
    for line in fh:
        if s and (line != "\n"):
            state.append(line[: -1])
        elif line == "\n":
            s = False
        elif not s and (line != "\n"):
            instr.append(line[:-1])

stack_amount = int(state[-1].strip().split()[-1])
stacks = [[] for _ in range(stack_amount)]

for line in state[:-1]:
    for i in range(len(line)):
        if not line[i] in "[] ":
            stacks[int(i // 4)].append(line[i])

for i in range(len(stacks)):
    stacks[i] = stacks[i][::-1]


def CrateMover9000(stacks, instr):
    stacks_copy = [s[:] for s in stacks]

    for inst in instr:
        i = inst.split()
        a, f, t = int(i[1]), int(i[3]) - 1, int(i[5]) - 1
        for _ in range(a):
            stacks_copy[t].append(stacks_copy[f].pop())

    return "".join([stack[-1] for stack in stacks_copy])


def CrateMover9001(stacks, instr):
    stacks_copy = [s[:] for s in stacks]

    for inst in instr:
        i = inst.split()
        a, f, t = int(i[1]), int(i[3]) - 1, int(i[5]) - 1

        buff = []
        for _ in range(a):
            buff.append(stacks_copy[f].pop())
        for _ in range(a):
            stacks_copy[t].append(buff.pop())

    return "".join([stack[-1] for stack in stacks_copy])


print(f"question 1: {CrateMover9000(stacks, instr)}")  # TGWSMRBPN
print(f"question 2: {CrateMover9001(stacks, instr)}")  # TZLTLWRNF
