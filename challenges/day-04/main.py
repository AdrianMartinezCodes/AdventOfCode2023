import pathlib

def main():
    # print(pathlib.Path(__file__).parent/'sample.txt')
    total = 0
    with open(pathlib.Path(__file__).parent/'sample.txt') as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            input =  line.split("|")
            input[0] = input[0].split(" ")[1:]
            input[1] = input[1].split(" ")[1:]
            inset = {s for s in input[0] if s.isnumeric()}
            first_pass = True
            out = 0
            for n in input[1]:
                if n in inset and not first_pass:
                    out*= 2
                elif n in inset and first_pass:
                    first_pass = False
                    out = 1
            # print(out)
            total += out
    return total
                
                
def main():
    # print(pathlib.Path(__file__).parent/'sample.txt')
    total = 0
    with open(pathlib.Path(__file__).parent/'input.txt') as file:
        lines = [line.rstrip() for line in file]
        copies = {n+1:1 for n in range(len(lines))}
        copies[1] = 1
        for i,line in enumerate(lines):
            input =  line.split("|")
            input[0] = input[0].split(" ")[1:]
            input[1] = input[1].split(" ")[1:]
            inset = {s for s in input[0] if s.isnumeric()}
            copy = 0
            for j,n in enumerate(input[1]):
                if n in inset:
                    copy += 1
            # print("copy",copy)
            j = 1
            while copy > 0:
                to_add = i+1+j
                copies[to_add] += copies[i+1]
                copy -= 1
                j += 1
            # print(copies)
                
            # print(out)
    totals = {}
    # print(totals)
    return sum(copies.values())                
        
if __name__ == "__main__":
    print(main())