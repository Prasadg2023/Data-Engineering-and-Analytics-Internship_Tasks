## 19.Company Logo
## https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")