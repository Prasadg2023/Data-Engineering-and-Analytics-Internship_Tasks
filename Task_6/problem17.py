## 17.Check Strict Superset
## https://www.hackerrank.com/challenges/py-check-strict-superset/problem

def solve():
    A = set(input().split())
    n = int(input())
    
    is_strict_superset = True
    for _ in range(n):
        other_set = set(input().split())
        if not A.issuperset(other_set) or not (A > other_set):
            is_strict_superset = False
            
    print(is_strict_superset)

if __name__ == '__main__':
    solve()