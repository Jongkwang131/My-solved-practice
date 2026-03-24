import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort()
person_time = 0
total_time = 0

for time in P :
    person_time += time
    total_time += person_time

print(total_time)