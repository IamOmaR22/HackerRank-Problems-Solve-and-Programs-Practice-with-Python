# Solution - 1
#!/bin/python3

T = int(input())

for i in range(T):
    tmp = str(input()).split()
    N = int(tmp[0])
    K = int(tmp[1])

    maximum = 0

    for j in range(1, N):
        for k in range(j + 1, N + 1):
            h = j & k
            if K > h > maximum:
                maximum = h

    print(maximum)


# Solution - 2
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    print(k-1 if ((k-1) | k) <= n else k-2)
