 test = False
filename = "test.txt" if test else "input.txt"

with open(filename, "r") as input:
    lines = input.read().strip().split("\n")
    data = [line[line.index("|") + 2:].split(" ") for line in lines]

def partA():
    correct = [2, 4, 3, 7]

    answer = 0
    for output in data:
        for digit in output:
            if len(digit) in correct:
                answer += 1
    print(answer)

digits = {}

def similar(a, b):
    sum = 0
    for x in a:
        if x in b:
            sum += 1
    return sum

def calc_wiring(source):
    for x in source:
        if len(x) == 2:
            digits[1] = x
        elif len(x) == 4:
            digits[4] = x
        elif len (x) == 3:
            digits[7] = x
        elif len (x) == 7:
            digits[8] = x

    for x in source:
        if len(x) == 5:
            # 5, 3, 2
            if similar(x, digits[1]) == 2:
                digits[3] = x
            elif similar(x, digits[4]) == 2:
                digits[2] = x
            else:
                digits[5] = x
        if len(x) == 6:
            # 9 6 0 
            if similar(x, digits[4]) == 4:
                digits[9] = x
            elif similar(x, digits[1]) == 2:
                digits[0] = x
            else:
                digits[6] = x

def partB():
    answer = 0
    for line in lines:
        value = ''
        digit_data, wiring = line.split('| ')
        digit_data = digit_data.split(' ')
        wiring = wiring.split(' ')
        calc_wiring(digit_data)
        for digit in wiring:
            for output in digits:
                if sorted(digit) == sorted(digits[output]):
                    value += str(output)  
        answer = answer + int(value)
    print(answer)

partA() # 530 
partB() # 1051087