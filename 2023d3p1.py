#advent of code day 3 part 1
import string

dix = dict(zip(list(string.ascii_letters), list(range(1,53)))) #dictionary with letters (upper and lower) to their numerical values
one = []
two = []
same = []
sum1 = []

file = open("adventofcode1.txt", "r").read().split("\n")

for line in file:
    one.append(tuple(list(line[:len(line)//2]))) #splits them into 2 compartments
    two.append(tuple(list(line[len(line)//2:]))) #and seperates them into individual letters
    #tupled so that i can use set()

for i, j in zip(one, two):
    same.append(set(i).intersection(j)) #list of all the ones that match BUT THEY ARE TUPLED whatever that means lol

same = str(same) #from set to str so that i can compare to dictionary keys

for letter in same:
    for key in dix.keys():
        if letter == key:
            sum1.append(int(dix.get(key)))

print(sum(sum1)) #ans
