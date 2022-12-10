with open("test_input.in", 'r') as fh:
    input = fh.readline().strip()


def diff_chars(stream, char_amount):
    i = char_amount
    while i < len(stream):
        valid = True
        for c in range(i - char_amount, i):
            for d in range(c + 1, i):
                if stream[c] == stream[d]:
                    valid = False
                    skip = 1 + c + char_amount - i  # skip after the first repeated character
        if valid:
            return i
        i += skip


print(f"question 1: {diff_chars(input, 4)}")  # 1175
print(f"question 2: {diff_chars(input, 14)}")  # 3217
