## 1.Set .symmetric_difference() Operation
## https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n_eng = int(input())
eng_set = set(map(int, input().split()))
n_fre = int(input())
fre_set = set(map(int, input().split()))

print(len(eng_set.symmetric_difference(fre_set)))