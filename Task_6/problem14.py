## 14. Set .intersection() Operation
## https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input())
set_english = set(map(int, input().split()))
b = int(input())
set_french = set(map(int, input().split()))

print(len(set_english.intersection(set_french)))