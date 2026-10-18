## 2.The Captain's Room
## https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
room_numbers = list(map(int, input().split()))

room_set = set(room_numbers)

captain_room = (sum(room_set) * k - sum(room_numbers)) // (k - 1)

print(captain_room)