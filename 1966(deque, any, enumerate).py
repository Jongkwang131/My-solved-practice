import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N, M = map(int, input().split())
    importants = list(map(int, input().split()))
    queue = deque([v,i] for i, v in enumerate(importants))
    
    count = 0
    while queue :
        current = queue.popleft()

        if any(current[0] < item[0] for item in queue) :
            queue.append(current)
        else :
            count += 1
            if current[1] == M :
                print(count)
                break