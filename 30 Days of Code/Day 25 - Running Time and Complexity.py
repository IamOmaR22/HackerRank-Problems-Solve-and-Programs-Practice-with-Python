# Solution - 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def isPrime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False
    for i in range(2, int(sqrt_n)+1):
        if n%i == 0:
            return False
    return True


num_test_cases = int(input())
for i in range(num_test_cases):
    n = int(input())
    if isPrime(n):
        print('Prime')
    else:
        print('Not prime')


# Solution - 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

T = int(input())


def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i is 0:
            return False
    return True


for _ in range(T):
    n = int(input())
    
    if n >= 2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")
