#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = str(input()).split()
    arr.reverse()

    for i in arr:
        print(i + " ", end="")
