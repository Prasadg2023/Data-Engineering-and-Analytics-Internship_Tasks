## 12. Set .discard(), .remove() & .pop()
## https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    eval_line = input().split()
    command = eval_line[0]
    
    if command == "pop":
        if s:
            s.pop()
    elif command == "remove":
        val = int(eval_line[1])
        if val in s:
            s.remove(val)
    elif command == "discard":
        s.discard(int(eval_line[1]))

print(sum(s))