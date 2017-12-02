import numpy as np

with open('day1.txt') as f:
    data = f.read()

data = list(data)
data.remove('\n')
data = [int(i) for i in data]

def riddle1():
    capcha_sum = 0
    index = 0
    while index < (len(data) -1):
        if data[index] == data[index + 1]:
            capcha_sum += data[index]
        index += 1
    if data[0] == data[-1]:
        capcha_sum += data[0]
    print(capcha_sum)

def riddle2():
    capcha_sum = 0
    index = 0
    data_len = len(data)
    data1 = data[:int(data_len/2)]
    data2 = data[int(data_len/2):]
    while index < len(data1):
        if data1[index] == data2[index]:
            capcha_sum += 2*data[index]
        index += 1
    print(capcha_sum)

if __name__ == '__main__':
    riddle1()
    riddle2()
