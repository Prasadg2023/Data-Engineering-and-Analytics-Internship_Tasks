## 14.Anagram
## https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def anagram(s):
    # If the length of the string is odd, it cannot be split into two equal halves
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    # Count frequencies of characters in the first half
    from collections import Counter
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Calculate the number of changes needed
    changes = 0
    for char in count1:
        if count1[char] > count2[char]:
            changes += count1[char] - count2[char]
            
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
