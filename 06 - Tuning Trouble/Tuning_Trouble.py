with open("input.in", 'r') as fh:
    input = fh.readline().strip()


def diff_chars(stream, char_amount):
    for i in range(char_amount, len(stream)):
        valid = True
        for c in range(i - char_amount, i):
            for d in range(c + 1, i):
                if stream[c] == stream[d]:
                    valid = False
        if valid:
            return i


print(f"question 1: {diff_chars(input, 4)}")  # 1175
print(f"question 2: {diff_chars(input, 14)}")  # 3217
