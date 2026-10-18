## 12.Making Anagrams
## https://www.hackerrank.com/challenges/making-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Calculate the absolute difference in frequencies for all lowercase letters
    diff = count1 - count2 + (count2 - count1)
    
    return sum(diff.values())
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
