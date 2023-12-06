powers = []

with open("input.txt", "r") as in_file:
    for index, line in enumerate(in_file, 1):
        game = line.split(":")[1]
        hands =  [hand.split(",") for hand in game.split(";")]
        max_c = {
            "red": 0,
            "green": 0,
            "blue": 0
        } 

        for colors in hands:
            for color in colors:
                c_count = color.strip().split(" ")
                if max_c[c_count[1]] < int(c_count[0]):
                    max_c[c_count[1]] = int(c_count[0])
        
        powers.append(max_c["red"]*max_c["green"]*max_c["blue"])

print(sum(powers))
