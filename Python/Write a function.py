def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    
    return leap

year = int(input())
print(is_leap(year))
