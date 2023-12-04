import pathlib

nums = {}

def main():
    out = 0
    with open(pathlib.Path(__file__).parent/'input.txt') as file:
        lines = [line.rstrip() for line in file]
        for i,line in enumerate(lines):
            for j,char in enumerate(line):
                if not(char.isnumeric() or char == '.'):
                    out += get_locations(i,j,lines)
    print(out)
    # print(nums)
    return out

def main_2():
    out = 0
    with open(pathlib.Path(__file__).parent/'input.txt') as file:
        lines = [line.rstrip() for line in file]
        for i,line in enumerate(lines):
            for j,char in enumerate(line):
                if char == '*':
                    out += get_locations_gear(i,j,lines)
    print(out)
    # print(nums)
    return out

def get_locations(i,j,lines):
    total = 0
    seen = set()
    for x,y in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
        if x< 0 or y <0 or x >= len(lines) or y >=len(lines[0]):
            continue
        if lines[x][y].isnumeric():
            num = int(get_num(x,y,lines))
            if num not in seen:
                seen.add(num)
                total += num
    return total

def get_locations_gear(i,j,lines):
    total = 0
    seen = set()
    for x,y in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
        if x< 0 or y <0 or x >= len(lines) or y >=len(lines[0]):
            continue
        if lines[x][y].isnumeric():
            num = (int(get_num_gear(x,y,lines)))
            if num not in seen:
                seen.add(num)
    if len(seen) == 2:
        multi = 1
        for e in seen:
            multi *= e
        return multi
    return 0

def get_num(x,y,lines):
    if x in nums:
        for out in nums[x]:
            all_nums = out[0]
            num = out[1]
            if y in all_nums:
                return num
    num = []
    num_list = set()
    line = list(lines[x])

    for index,left in enumerate(reversed(line[:y])):
        if left =='.' or not left.isnumeric():
            break
        num_list.add(index)
        num.append(left)
        num.reverse()
    for index,right in enumerate(line):
        if index < y:
            continue
        if right == '.' or not right.isnumeric():
            break
        num.append(right)
        num_list.add(index)
    num = ''.join(num)
    if x not in nums:
        nums[x] = [(num_list,int(num))]
    else:
        nums[x].append((num_list,int(num)))
    return num
    
def get_num_gear(x,y,lines):
    if x in nums:
        for out in nums[x]:
            all_nums = out[0]
            num = out[1]
            if y in all_nums:
                return num
    num = []
    num_list = set()
    line = list(lines[x])

    for index,left in enumerate(reversed(line[:y])):
        if left =='.' or not left.isnumeric():
            break
        num_list.add(index)
        num.append(left)
        num.reverse()
    for index,right in enumerate(line):
        if index < y:
            continue
        if right == '.' or not right.isnumeric():
            break
        num.append(right)
        num_list.add(index)
    num = ''.join(num)
    if x not in nums:
        nums[x] = [(num_list,int(num))]
    else:
        nums[x].append((num_list,int(num)))
    return num

if __name__=="__main__":
    # main()
    main_2()