# Solution - 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

super_set=set(map(int,input().split()))
count=True
n=int(input())
for i in range(n):
    normal_set=set(map(int,input().split()))
    if len(super_set)>len(normal_set):
        if  not super_set.issuperset(normal_set):
            count=False
print(count)



# Solution - 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
for _ in range(int(input())):
    X = set(map(int, input().split()))
    if A.issuperset(X) != True or len(A) == len(X): 
        print(False)
        break 
else: print(True)
