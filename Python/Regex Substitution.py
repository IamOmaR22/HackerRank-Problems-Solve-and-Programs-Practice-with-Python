# Solution - 1:

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))






# Solution - 2:

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

def change(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

for _ in range(int(input())):
    print (re.sub(r"(?<= )(\|\||&&)(?= )", change, input()))



    
