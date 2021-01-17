# Solution - 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())): 
    a = int(input()); A = set(input().split()); 
    b = int(input()); B = set(input().split());
    print (A <= B)




# Solution - 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for _ in range(T):
    a = input()
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(A.issubset(B))
