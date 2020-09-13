# Solution - 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

m, d, y = map(int, input().strip().split())

print (calendar.day_name[calendar.weekday(y, m, d)].upper())





# Solution - 2

import calendar

day = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}

m,d,y = map(int, input().split())
print (day[calendar.weekday(y,m,d)])
