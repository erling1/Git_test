from itertools import chain
from collections import Counter
import sys
import numpy

rucksacks = open("adventofcode3.txt","r").read()

items = rucksacks.split()


compartment1 = []
compartment2 = []


for i in items:
    compartment1.append(i[:len(i)//2])
    compartment2.append(i[len(i)//2:])


commonletters = []

for i,j in  zip(compartment1,compartment2):
    #print(i,j)
    for k in i:
        for l in j:
            if k == l:
                commonletters.append(k)

concatenated = chain(range(96, 123), range(65,91))

alphabetlist = list(map(chr, concatenated))


sorted_commonletters = sorted(commonletters)

#for elem in sorted_commonletters:
#    sorted_commonletters.count(elem)

x = Counter(sorted_commonletters)
list1 = list(x.values())

total_points = []


def points(x,y):
    for i in x:
        for j in y:
            if i==j:
                points = 0
                points += alphabetlist.index(j)
                total_points.append(points)
                result = [num*total_points.count(num) for num in set(total_points)]
    return result


totaltotal_points = points(sorted_commonletters, alphabetlist)

print(sum(totaltotal_points))
print(commonletters)


#for i in alphabetlist:
#    for j in x:
#     
#    if i == j:
#            total_points = alphabetlist.index([i] * list1[i])



