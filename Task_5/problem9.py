## 9.Word Order
## https://www.hackerrank.com/challenges/word-order/problem

n = int(input())

words = []

for _ in range(n):
    word = input().strip()
    words.append(word)

frequency = {}

for word in words:
    frequency[word] = frequency.get(word,0)+1

print(len(frequency))
print(*frequency.values())