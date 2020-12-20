# Enter your code here. Read input from STDIN. Print output to STDOUT

n1=input()
s1=set(input().split(" "))
n2=input()
s2=set(input().split(" "))
s3=s1.union(s2)
print (len(s3))
