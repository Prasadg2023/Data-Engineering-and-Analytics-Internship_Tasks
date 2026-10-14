## 19.Collections.Counter()
## https://www.hackerrank.com/challenges/collections-counter/problem


from collections import Counter


if __name__ == '__main__':
    X = int(input())
    shoes = list(map(int, input().split()))
    n = int(input())
    total_earnings = 0
    shoe_counts = Counter(shoes)

    for _ in range(n):
        size, price = map(int, input().split())
        if shoe_counts[size] > 0:
            total_earnings += price
            shoe_counts[size] -= 1

    print(total_earnings)