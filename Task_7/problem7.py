## 7.Alphabet Rangoli
## https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string


def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    
    # Generate the top half and the middle line
    for i in range(size):
        sub_alpha = alphabet[i:size]
        row = "-".join(list(sub_alpha)[::-1] + list(sub_alpha)[1:])
        lines.append(row.center(4 * size - 3, '-'))
        
    # Combine the reversed top lines (excluding the middle line) with the full list of lines
    full_rangoli = lines[::-1][1:] + lines
    print('\n'.join(full_rangoli))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)