## 17.Separate the Numbers
## https://www.hackerrank.com/challenges/separate-the-numbers/problems

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#
def separateNumbers(s):
    n = len(s)

    for i in range(1, n // 2 + 1):
        first_str = s[:i]

        if first_str[0] == '0':
            break
            
        current_num = int(first_str)
        generated = first_str
        while len(generated) < n:
            current_num += 1
            generated += str(current_num)
            
        if generated == s:
            print(f"YES {first_str}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
