def change(x):
    if str.islower(x):
        return str.upper(x)
    else:
        return str.lower(x)
def swap_case(s):
    return ('').join(map(change,s))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
