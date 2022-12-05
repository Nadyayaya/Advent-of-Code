#advent of code day 3 part 2
import string

dix = dict(zip(list(string.ascii_letters), list(range(1,53)))) #dictionary with letters (upper and lower) to their numerical values
bigList = []
same = []
sum1 = []

file = open("adventofcode1.txt", "r").read().split("\n")

bigList = list(file[i:i+3] for i in range(0,len(file), 3))



for first, second, third in bigList:
    same.append((set(first) & set(second) & set(third)).pop()) #cheated for this line lol

same = str(same) #from set to str so that i can compare to dictionary keys

for letter in same:
    for key in dix.keys():
        if letter == key:
            sum1.append(int(dix.get(key)))

print(sum(sum1)) #ans
