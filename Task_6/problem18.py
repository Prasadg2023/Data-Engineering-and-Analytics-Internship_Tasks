## 18.Set Mutations
## https://www.hackerrank.com/challenges/py-set-mutations/problem

num_elements = int(input())
A = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    op, length = input().split()
    other_set = set(map(int, input().split()))
    
    if op == "update":
        A.update(other_set)
    elif op == "intersection_update":
        A.intersection_update(other_set)
    elif op == "difference_update":
        A.difference_update(other_set)
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

print(sum(A))