from random import random, randrange
from collections import Counter
import sys 


def rollDie(numberSides):
    minimum = 1
    maximum = numberSides
    val = randrange(minimum, maximum + 1)
    return val




results = []




# set readline 
numberSides = 6
for i in range(1,1000):
    results.append(rollDie(numberSides))

c = Counter(results)
total = sum(c.values())
totalPerc = c[1]/total + c[2]/total + c[3]/total + c[4]/total + c[5]/total + c[6]/total 
print("Total sample :" + str(total))
print("One : " + str(c[1]/total))
print("Two : " + str(c[2]/total))
print("Three : " + str(c[3]/total))
print("Four : " + str(c[4]/total))
print("Five : " + str(c[5]/total))
print("Six : " + str(c[6]/total))

print(str(totalPerc))

print("completed") 

