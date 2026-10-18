## 13.Sherlock and the Valid String
## https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
from collections import Counter

def isValid(s):
    freq = Counter(s)
    counts = Counter(freq.values())
    
    # If all characters have the same frequency, it's valid
    if len(counts) == 1:
        return "YES"
    
    # If there are more than 2 distinct frequencies, it's invalid
    if len(counts) > 2:
        return "NO"
    
    # Get the two distinct frequencies and their counts
    (f1, c1), (f2, c2) = counts.items()
    
    # Case 1: One frequency appears only once and its value is 1 (we can delete it entirely)
    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return "YES"
    
    # Case 2: The difference between the two frequencies is 1 and the higher frequency occurs only once
    if (abs(f1 - f2) == 1) and ((f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1)):
        return "YES"
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
