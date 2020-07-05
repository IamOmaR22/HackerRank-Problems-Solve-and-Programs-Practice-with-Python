# Solution 1

S = input().strip()
try:
    integer_value = int(S)
    print(integer_value)
except ValueError:
    print('Bad String')


    
# Solution 2

try:
    print(int(input().strip()))
except ValueError:
    print("Bad String")
