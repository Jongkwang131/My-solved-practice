import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque(range(1, N+1))
answer = []

while queue :
    queue.rotate(-(K-1))
    
    removed_person = queue.popleft()
    answer.append(removed_person)

answer = ", ".join(map(str, answer))
print(f"<{answer}>")

"""
12457

3 6
팝을 하면 인덱스가 이상해진다.
그럼 어떻게 해야할까?

"""
