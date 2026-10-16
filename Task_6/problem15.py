## 15.Set .difference() Operation
## https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n_eng = int(input())
eng_set = set(map(int, input().split()))
n_fre = int(input())
fre_set = set(map(int, input().split()))

print(len(eng_set.difference(fre_set)))