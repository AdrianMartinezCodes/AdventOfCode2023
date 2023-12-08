import pathlib
import re
 
 
def main_A():
    with open(pathlib.Path(__file__).parent/'input.txt') as file:
        lines = [line.rstrip() for line in file]
        times = [int(digit) for digit in re.findall(r'\d+',lines[0])]
        records = [int(digit) for digit in re.findall(r'\d+',lines[1])] 
    total = 1
    for time,record in zip(times,records):
        sub_total = 0
        for i in range(time//2 + 1):
            coef =  i*(time-i)
            if coef > record:
                sub_total += 1
        sub_total*=2
        if (time+1) % 2 != 0:
            sub_total -= 1
        total *= sub_total 
    return total

def main_B():
    with open(pathlib.Path(__file__).parent/'input.txt') as file:
        lines = [line.rstrip() for line in file]
        time = ''.join([digit for digit in re.findall(r'\d+',lines[0])])
        record = ''.join([digit for digit in re.findall(r'\d+',lines[1])])
    time = int(time)
    record = int(record)
    print(time,record)
    total = 0
    for i in range(time//2 + 1):
        coef =  i*(time-i)
        if coef > record:
            total += 1
    total*=2
    if (time+1) % 2 != 0:
        total -= 1
    return total
        
def binom():
    pass

if __name__=="__main__":
    print(main_A())
    print(main_B())