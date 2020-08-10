# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = map(int,input().split())
B = map(int,input().split())

for item in product(A,B):
    print(item,end=' ')
