import pathlib

mapping ={
    "zero":'0',
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9'
}

def main():
    out = 0
    print(pathlib.Path(__file__).parent/'input.txt')
    with open(pathlib.Path(__file__).parent/'input.txt') as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            letters = list(line)
            num = ""
            for letter in letters:
                if letter.isnumeric():
                    num += letter
                    break
            for letter in reversed(letters):
                if letter.isnumeric():
                    num += letter
                    break
            out += int(num)
    return out

def main_B():
    out = 0
    with open(pathlib.Path(__file__).parent/'input.txt') as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            left_val = get_num(line)
            right_val = get_num(line[::-1],reverse = True)
            print(left_val+right_val)
            out += int(left_val+right_val)
    return out

def get_num(line,reverse=False):
    occurance = {}
    for key,val in mapping.items():
        if reverse:
            index = line.find(key[::-1])
        else:
            index = line.find(key)
        if index != -1:
            occurance[index] = val 
    letters = list(line)
    index,letter = get_int_num(letters)
    if index is not None:
        occurance[index] = letter
    return min(occurance.items(),key= lambda x:x[0])[1]

def get_int_num(letters):
    for index,letter in enumerate(letters):
        if letter.isnumeric():
            return index,letter
    return None,None
        
if __name__ == "__main__":
    print(main_B())