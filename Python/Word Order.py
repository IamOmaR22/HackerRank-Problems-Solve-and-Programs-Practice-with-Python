# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1
   
print(len(words))
print(*words.values())
