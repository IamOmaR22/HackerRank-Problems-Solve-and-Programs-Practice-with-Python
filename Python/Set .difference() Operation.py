# Enter your code here. Read input from STDIN. Print output to STDOUT

e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng - fre))
