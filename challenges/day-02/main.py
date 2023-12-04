import pathlib

total = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

def main():
    out = 0
    with open(pathlib.Path(__file__).parent/'input.txt') as file:
        lines = [line.rstrip() for line in file]
        for index,line in enumerate(lines):
            game_pass = True
            for l in line.split(":")[1:]:
                games = l.split(";")
                for game in games:
                    for g in game.split(','):
                        colors = g.split(" ")
                        num = colors[1]
                        color = colors[2]
                        if int(num) > total[color]:
                            game_pass = False
            if game_pass:
                out += index + 1
    print(out)
    return out

def main_2():
    total = 0
    with open(pathlib.Path(__file__).parent/'input.txt') as file:
        lines = [line.rstrip() for line in file]
        for index,line in enumerate(lines):
            lowest = {}
            for l in line.split(":")[1:]:
                games = l.split(";")
                for game in games:
                    for g in game.split(','):
                        colors = g.split(" ")
                        num = int(colors[1])
                        color = colors[2]
                        if color not in lowest:
                            lowest[color] = num
                        else:
                            if num > lowest[color]:
                                lowest[color] = num
                        
            out = 1
            # print(lowest)
            for val in lowest.values():
                out *= val
            total += out
    print(total)
    return out
    

if __name__=="__main__":
    main_2()