#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    f = s.replace('PM','')
    f = f.replace('AM','')
    f = f.split(':')

    pm = [x for x in range(12,24)]
    am = [x for x in range(0,12)]

    if 'PM' in s and 1 <= int(f[0]) < 12:
            hora = f[1:]
            hora.insert(0,str(pm[int(f[0])]))
            return(':'.join([x for x in hora]))

    elif 'AM' in s and 12 <= int(f[0]) <= 23:
            hora = f[1:]
            hora.insert(0,str(int(f[0])-12).zfill(2))
            return(':'.join([x for x in hora]))

    else:
            return (':'.join([x for x in f]))
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
