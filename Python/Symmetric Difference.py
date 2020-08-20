# Enter your code here. Read input from STDIN. Print output to STDOUT
numbers1 = int(input())
set1 = set(map(int, input().split()))
numbers2 = int(input())
set2 = set(map(int, input().split()))
set3 = (set1.difference(set2)).union(set2.difference(set1))
for i in sorted(list(set3)):
    print (i)
