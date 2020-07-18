# Solution - 1
#!/bin/python3

import re

if __name__ == '__main__':
    N = int(input())

    pattern = r"@gmail\.com$"
    regex = re.compile(pattern)
    firstNames = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if regex.search(emailID):
            firstNames.append(firstName)

    firstNames.sort()

    for name in firstNames:
        print(name)


# Solution - 2
#!/bin/python3

import re

arr = []

n = int(input())

for i in range(n):
    data = str(input()).split(" ")
    name = data[0]
    email = data[1]

    if re.search(".+@gmail\.com$", email):
        arr.append(name)

arr.sort()

for name in arr:
    print(name)
