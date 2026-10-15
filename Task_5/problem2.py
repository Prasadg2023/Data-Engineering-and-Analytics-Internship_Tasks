## 2.String Split and Join
## https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    string = line.replace(" ", "-")
    return string
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)