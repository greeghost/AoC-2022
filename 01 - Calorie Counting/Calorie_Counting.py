with open("input.in", 'r') as fh:
    input = list(map(lambda x: (
        list(map(lambda y: int(y),
                 x.split("\n")))),
        fh.read().strip().split("\n\n")))


def sum_of_max(input, amount):
    vals = list(map(sum, input))
    vals.sort(reverse=True)
    return sum(vals[:amount])


print(f"question 1: {sum_of_max(input, 1)}")  # 64929
print(f"question 1: {sum_of_max(input, 3)}")  # 193697
