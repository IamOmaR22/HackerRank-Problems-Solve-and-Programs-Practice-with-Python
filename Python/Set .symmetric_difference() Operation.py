# Solution - 01

# Enter your code here. Read input from STDIN. Print output to STDOUT

_, en_subscribers = input(), set(map(int, input().split())) 
_, fr_subscribers = input(), set(map(int, input().split())) 
print(len(en_subscribers.symmetric_difference(fr_subscribers)))



# Solution - 02

# Enter your code here. Read input from STDIN. Print output to STDOUT

N1 = int(input())
storage1 = set(input().split())

N2 = int(input())
storage2 = set(input().split())

storage3 = storage1.symmetric_difference(storage2)
print(len(storage3))



# Solution - 03

# Enter your code here. Read input from STDIN. Print output to STDOUT

e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng ^ fre))
