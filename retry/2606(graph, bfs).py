import sys
from collections import deque
input = sys.stdin.readline
"""
computer_num = int(input())
linked_coumputer_num = int(input())
linked_coumputers = []
virused_computers = [1]
for i in range(linked_coumputer_num) :
    new_linked_computer = list(map(int, input().split()))
    linked_coumputers.append(new_linked_computer)
    if new_linked_computer[0] in virused_computers :
        virused_computers.append(new_linked_computer[1])
    elif new_linked_computer[1] in virused_computers :
        virused_computers.append(new_linked_computer[0])

print(len(set(virused_computers))-1)
"""

n = int(input()) #컴퓨터 수
m = int(input()) #연결 쌍 수

#그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    u,v = map(int, input().split())
    #양방향 연결
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

def bfs(start) :
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue :
        current = queue.popleft()

        for neighbor in graph[current] :
            if not visited[neighbor] :
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

print(bfs(1))
