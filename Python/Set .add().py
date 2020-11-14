# Solution - 1:

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

countries = set()

for i in range(N):
    countries.add(input())

print(len(countries))



# Solution - 2:

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
s = set(input() for i in range(N))
    
print (len(s))
