# Akash Kandpal
# My Domain => http://harrypotter.tech/
# from fractions import gcd
import math
# from itertools import permutations
# import statistics

def readInts():
    return list(map(int, raw_input().strip().split()))
def readInt():
    return int(raw_input())
def readIntsindex0():
    return list(map(lambda x: int(x) - 1, input().split()))
def readStrs():
    return raw_input().split()
def readStr():
    return raw_input()
def numlistTostr(list1):
    return ''.join(list1)
def strlistTostr(list1):
    return ''.join(str(e) for e in list1)
def strTolist(str):
    return str.split()
def strlistTointlist(str):
    return map(int, str)
def slicenum(number,x):
    return int(str(number)[:x])
def precise(num):
    return "{0:.10f}".format(num)
def rsorted(a):
    return sorted(a,reverse=True)
def binar(x):
    return '{0:031b}'.format(x)
def findpermute(word):
    perms = [''.join(p) for p in permutations(word)]
    return set(perms)
def findsubsets(S,m):
    return set(itertools.combinations(S, m))
def sort1(yy,index):
    return yy.sort(key = lambda x:x[index])
def reversepair(yy):
    return yy[::-1]

MOD = 10 ** 9 + 7

for __ in range(readInt()):
    n = readInt()
    a = readInts()
    b = readInts()
    a= sorted(a)
    b= sorted(b)
    suma = sum(a)-a[n-1]
    sumb = sum(b)-b[n-1]
    # print suma,sumb
    if(suma>sumb):
        print "Bob"
    elif(suma<sumb):
        print "Alice"
    else:
        print "Draw"



'''
Input:

3
5
3 1 3 3 4
1 6 2 5 3
5
1 6 2 5 3
3 1 3 3 4
3
4 1 3
2 2 7

Output:

Alice
Bob
Draw
'''
