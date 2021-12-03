with open("input.txt", "r") as data:
    lines = data.read().split("\n")

def most_common_bit(pos):
    zero = 0
    one = 0

    for line in lines:
        if line[pos] == '0':
           zero += 1
        elif line[pos] == '1':
            one += 1
    if zero > one:
        return zero, 0
    else:
        return one, 1           

def least_common_bit(pos):
    zero = 0
    one = 0

    for line in lines:
        if line[pos] == '0':
           zero += 1
        elif line[pos] == '1':
            one += 1
  
    if zero < one:
        return zero, 0
    else:
        return one, 1           

def most_common_bit_b(data, pos):
    zero = 0
    one = 0
    data_zero = []
    data_one = []

    for line in data:
        if line[pos] == '0':
           zero += 1
           data_zero.append(line)
        elif line[pos] == '1':
            one += 1
            data_one.append(line)

    if zero > one:
        return data_zero, zero, 0
    else:
        return data_one, one, 1           


def least_common_bit_b(data, pos):
    zero = 0
    one = 0
    data_zero = []
    data_one = []

    for line in data:
        if line[pos] == '0':
           zero += 1
           data_zero.append(line)
        elif line[pos] == '1':
            one += 1
            data_one.append(line)
  
    if zero <= one :
        return data_zero, zero, 0
    else:
        return data_one, one, 1           

def partA():
    most  = ""
    least = ""

    for pos in range(len(lines[0])):
        a, b = most_common_bit(pos) 
        most += str(b)
        
        a, b = least_common_bit(pos) 
        least += str(b)

    most_dec = int(most, 2) 
    least_dec = int(least, 2) 
    print (most_dec * least_dec)

def partB():
    most  = ""
    ogr = 0
    co2 = 0
    data = lines

    for pos in range(len(lines[0])):
        data, a, b = most_common_bit_b(data, pos) 
        if(len(data) == 1):
            ogr = int(data[0], 2)

    data = lines

    for pos in range(len(lines[0])):
        data, a, b = least_common_bit_b(data, pos) 
        if(len(data) == 1):
            co2 = int(data[0], 2)

    print (ogr * co2)

partA() # 1082324
partB() # 1353024