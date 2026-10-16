## 1.Python If-Else
## https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n >=2 and n <= 5:
        print("Not Weird")
    else:
        print("Not Weird")
