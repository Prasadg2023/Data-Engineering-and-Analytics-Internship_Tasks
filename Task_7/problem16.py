## 16.Caesar Cipher
## https://www.hackerrank.com/challenges/caesar-cipher-1/problem


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def caesarCipher(s, k):
    # Ensure k wraps around the alphabet length (26)
    k = k % 26
    encrypted = []
    
    for char in s:
        if 'a' <= char <= 'z':
           
            shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            encrypted.append(shifted)
        elif 'A' <= char <= 'Z':
           
            shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            encrypted.append(shifted)
        else:
           
            encrypted.append(char)
            
    return "".join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
