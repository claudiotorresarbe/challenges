#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    qtd = len(arr)
    pos = sum([1 if x > 0 else 0 for x in arr])
    neg = sum([1 if x < 0 else 0 for x in arr])
    zer = sum([1 if x == 0 else 0 for x in arr])
    print(pos/qtd)
    print(neg/qtd)
    print(zer/qtd)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
