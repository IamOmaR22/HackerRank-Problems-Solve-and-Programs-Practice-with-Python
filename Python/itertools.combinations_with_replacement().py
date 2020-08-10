# Solution - 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
S,k = input().split()
for i in combinations_with_replacement(sorted(S),int(k)):
 print ("".join(i))
 



# Solution - 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

lis = input().split(' ')

for i in combinations_with_replacement(sorted(lis[0]), int(lis[1])):
    print (''.join(i))
