#!/bin/python3

bn = int(input())

result = 0
maximum = 0

while bn > 0:
    if bn % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result

    else:
        result = 0

    bn //= 2

print(maximum)
