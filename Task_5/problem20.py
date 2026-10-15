## 20.Piling Up!
## https://www.hackerrank.com/challenges/piling-up/problem


def can_stack(blocks):
    left = 0
    right = len(blocks) - 1
    last = float('inf')

    while left <= right:
        if blocks[left] >= blocks[right]:
            current = blocks[left]
            left += 1
        else:
            current = blocks[right]
            right -= 1

        if current > last:
            return "No"

        last = current

    return "Yes"


T = int(input())

for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    print(can_stack(blocks))
