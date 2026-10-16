## 10.Designer Door Mat
## https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = map(int, input().split())

# Top pattern
for i in range(1, n, 2):
    pattern = (".|." * i).center(m, "-")
    print(pattern)

# Center line
print("WELCOME".center(m, "-"))

# Bottom pattern
for i in range(n - 2, 0, -2):
    pattern = (".|." * i).center(m, "-")
    print(pattern)