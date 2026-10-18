## 3.Mars Exploration
## https://www.hackerrank.com/challenges/mars-exploration/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def marsExploration(s):
    count = 0
    for i in range(len(s)):
        if i % 3 == 1:
            if s[i] != 'O':
                count += 1
        else:
            if s[i] != 'S':
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
