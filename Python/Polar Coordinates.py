# Solution - 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
z = input()
print (abs(complex(z)))
print (cmath.phase(complex(z)))





# Solution - 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import polar
polar = polar(complex(input()))
print (polar[0])
print (polar[1])
