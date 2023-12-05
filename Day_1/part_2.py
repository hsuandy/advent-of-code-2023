import re


t_key = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

d_key = "123456789"

total = []

with open("input.txt", "r") as in_file:
    for line in in_file:
        numbers = {}
        
        for d_num in d_key:
            for match in re.finditer(d_num, line):
                numbers[match.start()] = d_num

        for t_num in t_key:
            for match in re.finditer(t_num, line):
                numbers[match.start()] = t_key[t_num]

        ordered = (sorted(numbers.items()))
        total.append(int(ordered[0][1]+ordered[-1][1]))

print(sum(total))
