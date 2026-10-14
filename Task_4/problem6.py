## Find the Runner-Up Score!
## https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = map(int, input().split())
arr1 = sorted(set(arr),reverse = True)
runner_up = arr1[1]
print(runner_up)