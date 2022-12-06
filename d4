# advent of code day 4 part 1 and 2

def cont(a, b):
    a, b = a.split('-'), b.split('-')  # gets rid of -
    ast, ae, bs, be = int(a[0]), int(a[1]), int(b[0]), int(b[1])
    if ast >= bs and ae <= be or bs >= ast and be <= ae:
        return 1
    else:
        return 0


def overlap(a, b):
    a, b = a.split('-'), b.split('-')  # gets rid of -
    aRange = range(int(a[0]), int(a[1])+1) #why is it +1????
    bRange = range(int(b[0]), int(b[1])+1)

    if set(aRange).intersection(set(bRange)):  # duplicates basically mean overlap
        return 1
    else:

        return 0


file = open('adventofcode1.txt', 'r').read().split('\n')
pairs = []
sum1 = 0
sum2 = 0
for line in file:
    pairs.append(line.split(','))  # list of list

for group in pairs:
    sum1 += cont(group[0], group[1])  # ans1
    sum2 += overlap(group[0], group[1])  # an2
# print(sum1)
print(sum2)
