limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

good_games = []

with open("input.txt", "r") as in_file:
    for index, line in enumerate(in_file, 1):
        game = line.split(":")[1]
        hands =  [hand.split(",") for hand in game.split(";")]
        violations = 0

        for colors in hands:
            for color in colors:
                c_count = color.strip().split(" ")
                if limits[c_count[1]] < int(c_count[0]):
                    violations += 1

        if not violations:
            good_games.append(index)

print(sum(good_games))
