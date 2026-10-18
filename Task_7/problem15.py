## 15.Game of Thrones - I
## https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import Counter

def gameOfThrones(s):
    char_counts = Counter(s)
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    if len(s) % 2 == 0:
        return "YES" if odd_count == 0 else "NO"
    else:
        return "YES" if odd_count == 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
