with open("input.in", 'r') as fh:
    input = fh.read().splitlines()


class File(object):
    def __init__(self, name, size):
        self.name = name
        self._size = size

    def size(self):
        return self._size


class Folder(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.folder_childs = []
        self.file_childs = []
        # self.parent = parent

    def size(self):
        s1 = sum([i.size() for i in self.folder_childs])
        s2 = sum([i.size() for i in self.file_childs])
        return s1 + s2

    def q1(self, val=100000):
        res = 0
        if (size := self.size()) <= val:
            res += size
        for f in self.folder_childs:
            res += f.q1()
        return res

    def register_size(self, mem):
        mem.append((self, self.size()))
        for f in self.folder_childs:
            f.register_size(mem)

    def q2(self, tot=70000000, need=30000000):
        available = tot - self.size()
        needed = need - available
        mem = []
        self.register_size(mem)
        mem.sort(key=lambda t: t[1])
        mem = filter(lambda t: t[1] >= needed, mem)
        return next(mem)[1]


def create_filesystem(input):
    stack = []
    for instr in input:
        if instr == "$ cd ..":
            stack.pop()
            continue
        if instr[:4] == "$ cd":
            name = instr[5:]
            f = Folder(name)
            if stack != []:
                stack[-1].folder_childs.append(f)
            stack.append(f)
        elif instr[:4] == "$ ls":
            continue
        elif instr[:3] == "dir":
            continue
        else:
            [size, _name] = instr.split()
            stack[-1].file_childs.append(File(_name, int(size)))
    return stack[0]


filesystem = create_filesystem(input)

print(f"question 1: {filesystem.q1()}")  # 1175
print(f"question 2: {filesystem.q2()}")  # 3217
