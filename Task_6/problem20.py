## 20.Validating the Phone Number
## https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
import sys

def validate_phone_numbers():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    pattern = re.compile(r"^[789]\d{9}$")
    
    for i in range(1, n + 1):
        if i < len(input_data):
            number = input_data[i].strip()
            if pattern.match(number):
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    validate_phone_numbers()
