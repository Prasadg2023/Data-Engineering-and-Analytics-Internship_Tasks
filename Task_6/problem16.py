## 16.Check Subset
## https://www.hackerrank.com/challenges/py-check-subset/problem

for _ in range(int(input())):
    input()
    a = set(input().split())
    input()
    b = set(input().split())
    print(a.issubset(b))