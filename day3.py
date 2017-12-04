import numpy as np

'''
really ugly to declare posx and posy global variables like that
should fix it
multiple for loops not winning a beauty pageant either
maybe implement repeat() instead
'''

data = np.loadtxt('day3.txt', dtype=int)
n = int(np.ceil(np.sqrt(data)))
arr = np.arange((n-2)**2 + 1, n**2 + 1)
index = (n**2 - (n-2)**2) / 4
grid = np.zeros([n, n])
posx = n // 2
posy = n // 2

def left():
    global posx
    posx = posx - 1

def right():
    global posx
    posx = posx + 1

def up():
    global posy
    posy = posy - 1

def down():
    global posy
    posy = posy + 1

def make_a_move(direction):
    direction()
    array_element = int(np.sum(grid[posx - 1:posx + 2, posy - 1:posy + 2]))
    grid[posx, posy] = array_element

def make_spiral():
    grid[posx, posy] = 1
    array_element = 1
    i = 2
    counter = 0
    while counter < 5:
        make_a_move(right)
        for _ in range(i - 1):
            make_a_move(up)
        for _ in range(i):
            make_a_move(left)
        for _ in range(i):
            make_a_move(down)
        for _ in range(i):
            make_a_move(right)
        i = i + 2
        counter = counter + 1

def riddle1():
    pos = np.where(arr == data)[0]
    step1 = (n - 1) / 2
    step2 = abs (np.divmod(pos+1, index)[1] - index / 2)
    print(step1 + step2)

def riddle2():
    make_spiral()
    greater_elements = grid[np.where(grid > data)]
    answer = np.amin(greater_elements)
    print(answer)

if __name__ == '__main__':
    riddle1()
    riddle2()
