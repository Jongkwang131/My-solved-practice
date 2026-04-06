"""
import sys
from collections import heap
input = sys.stdin.readline

N = int(input())

dq = deque([])
for _ in range(N) :
    x = int(input())
    dq = deque(sorted(dq))
    if not dq and x == 0 :
        print(0)
    elif x != 0 :
        dq.append(x)
    elif x == 0 :
        print(dq.popleft())
"""        

import sys
import heapq # 최소 힙을 위한 모듈

input = sys.stdin.readline

N = int(input())
heap = [] # 힙으로 사용할 빈 리스트

for _ in range(N):
    x = int(input())
    
    if x != 0:
        # 힙에 숫자 추가 (자동으로 최소값이 맨 앞으로 오도록 정렬됨)
        heapq.heappush(heap, x)
    else:
        # 0이 입력되었을 때
        if not heap:
            print(0)
        else:
            # 가장 작은 값(루트 노드)을 꺼내서 출력
            print(heapq.heappop(heap))