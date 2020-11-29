# Enter your code here. Read input from STDIN. Print output to STDOUT

from __future__ import print_function
from itertools import groupby

args = input().strip()

for key, group in groupby(args):
    print((len(list(group)), int(key)), end=" ")
