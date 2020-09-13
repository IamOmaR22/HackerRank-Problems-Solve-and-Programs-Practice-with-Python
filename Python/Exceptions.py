# Solution - 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except Exception as e:
        print('Error Code: ' + str(e))




# Solution - 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):

    try:
        a,b = map(int,input().split())
        c = a // b
        print(c)

    except ZeroDivisionError as e:
        print("Error Code:", e)

    except ValueError as e:
        print("Error Code:", e)

