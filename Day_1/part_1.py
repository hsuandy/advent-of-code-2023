total = []

with open("input.txt", "r") as in_file:
    for line in in_file:
        digits = ''.join([d for d in line if d.isdigit()])
        total.append(int(digits[0]+digits[-1]))

print(sum(total))
