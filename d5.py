# advent of code day 5 part 1
import string
from collections import deque

letters = list(string.ascii_uppercase)
nLetters = 56 #n of crates
nStacks = 9 #n of columns, x
nCrates = 8 #n of rows, y
cratesMatrix= []
cratesDeque = []
instr = []
instNum = []
index = 0
indexDeque = 0
file = open('adventofcode1.txt', 'r').read().split('\n')
#getting the crates
for crates in file[0:nCrates]: #first 9 lines
    cratesMatrix.append(list(crates)) #len = 35, one crate has a length of 3
    cratesDeque.append(deque())

for line in cratesMatrix:
    index = 0
    for element in range(0, len(line), 4):
        if index == 8:
            break
        singleCrate = line[element:element+3]
        cratesDeque[index].appendleft(singleCrate) #still horicontal deque, not verticcal like what i want
        index += 1



#sort this and you're algood
x = cratesDeque[0] #whole first stack
cratesDeque[0].pop()
cratesDeque[1].appe(x)
print(cratesDeque[1])


#getting the instructions
for inst in file[nCrates+2:len(file)]: #'move n from x to y'
    instr.append(inst.split(' ')) #'move', 'n', 'from', 'x', 'to', 'y'

for x in instr:
    for i in x:
        if set(i).intersection(set(string.digits)): #just the n, x, y
            instNum.append(i)

numList = list(instNum[i:i+3] for i in range(0,len(instNum), 3)) #[[n, x, y], [n, x, y]...]

for x in numList:
    move = x[0]
    fromX = x[1]
    toX = x[2]

