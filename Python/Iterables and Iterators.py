# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
L = input().split()
K = int(input())
C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)

print("{0:.3}".format(len(list(F))/len(C)))
