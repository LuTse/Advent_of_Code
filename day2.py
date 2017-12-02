import numpy as np
import itertools

data = np.loadtxt('day2.txt', dtype=int)
arr = []

def ganzer_teiler(x, y):
    if x > y:
        if x % y == 0:
            arr.append(x / y)
    else:
        if y % x == 0:
            arr.append(y / x)
    return

def riddle1():
    max_vals = np.amax(data, axis=1)
    min_vals = np.amin(data, axis=1)
    diffs = max_vals - min_vals
    diff_sum = np.sum(diffs)
    print(diff_sum)

def riddle2():
    for row in data:
        for x, y in itertools.combinations(row, 2):
            ganzer_teiler(x, y)
    print(np.sum(arr))

if __name__ == '__main__':
    riddle2()
