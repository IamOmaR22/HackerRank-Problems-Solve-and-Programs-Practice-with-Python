# Enter your code here. Read input from STDIN. Print output to STDOUT
  
import re
T = int(input())
for i in range(0, T):
    regex_raw = input()
    try:
        regex = re.compile(regex_raw)
    except re.error:
        print(False)
    else:
        print(True)
