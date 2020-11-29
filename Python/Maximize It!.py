# Solution - 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

(K, N) = map(int, input().split())

L = list()
for i in range(K):
    l = list(map(int, input().split()))
    n = l[0]
    L.append(l[1:])
    assert len(L[i]) == n

S_max = 0
L_max = None

for l in itertools.product(*L):
    s = sum([x**2 for x in l]) % N

    if s > S_max:
        S_max = s
        L_max = l

print (S_max)


# Solution - 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import *

K, M = map(int, input().split())
N = []

for _ in range(K):
    N.append(list(map(int, input().split()))[1:])        
MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x**2, i))%M, MAX)
    
print (MAX)
