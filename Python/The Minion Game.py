def minion_game(string):
    # your code goes here
    VOWELS = "aeiou" # y not considered a vowel
    KEVIN_vowels = 0
    STUART_consonants = 0
    n = len(string)
    for i in range(n): # O(n)
        letter = string[i].lower() # ensuring lowercase comparisons
        letters_remaining = n - i
        if letter in VOWELS: # O(5)
            KEVIN_vowels += letters_remaining
        else:
            STUART_consonants += letters_remaining

    if STUART_consonants == KEVIN_vowels:
        print("Draw")
    elif STUART_consonants > KEVIN_vowels:
        print("Stuart", STUART_consonants)
    else:
        print("Kevin", KEVIN_vowels)
    # TOTAL TIME COMPLEXITY = O(n)

if __name__ == '__main__':
    s = input()
    minion_game(s)
