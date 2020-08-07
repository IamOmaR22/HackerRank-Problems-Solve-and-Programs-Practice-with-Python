# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

X = int(input())
sizes = collections.Counter(map(int, input().split()))
N = int(input())

money = 0

for i in range(N):
    (size, price) = map(int, input().split())

    if sizes[size] > 0:
        sizes[size] -= 1
        money += price

print (money)
