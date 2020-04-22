import math
import os
import random
import re
import sys

#print((10**(i)//9)*i)

# Return double of n
"""
numbers = (1, 2, 3, 4)

def addition(n):
    return n + n
result = map(addition, numbers)
print(list(result))
# zip code
n, x = map(int, input().split())

sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) )

for i in zip(*sheet):
    print( sum(i)/len(i) )


ui = input().split()
x = int(ui[0])
print(eval(input()) == int(ui[1]))


#p_x=x**3+x**2+x+1

def function(x):
    return x**3+x**2+x+1
print(function(1))

text = 'geeks for geeks'
# Splits at space
print(text.split())
"""
#ui = [10, 2, 5]
#print (ui)
#N, M = map(int, ui.split())

#N, M = map(int, input().split())
#rows = [input() for _ in range(N)]
#K = int(input())

#for row in sorted(rows, key=lambda row: int(row.split()[K])):
#    print(row)

x = (1,)
y=x
x+=(2,)
print(y)
