'''
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
'''

# Solution - 1
score = input("Enter Score: ")

try:
    score = float(score)
except:
    score = -1

if score >= 0.9:
    print ("A")
elif score >= 0.8:
    print ("B")
elif score >= 0.7:
    print ("C")
elif score >= 0.6:
    print ("D")
elif score < 0.6:
    print ("F")
else:
    print ("Error!")
    quit()


# Solution - 2
try:
    sc = raw_input("Enter your score between 0.0 and 1.0 ")
    score = float(sc)
except:
    if score > 1.0 or score < 0.0:
        print ("Error, the score should be in the range between 0.0 and 1.0")
    quit()
    
if score >= 0.9: 
    print ('A')
elif score >= 0.8:
    print ('B')
elif score >= 0.7:
    print ('C')
elif score < 0.6:
    print ('F')



# Solution - 3
inp = input("Choose a score between 0.0 and 1.0")
score = float(inp)
 
if score >= 0.0 and score < 0.6:
    print ('F')
 
 
elif score >= 0.6 and score < 0.7:
    print ('D')
 
elif score >= 0.7 and score < 0.8:
    print ('C')
 
elif score >= 0.8 and score < 0.9:
    print ('B')
 
elif score >= 0.9 and score <= 1.0:
    print ('A')
 
else:
    print ('Error: input not within range')
