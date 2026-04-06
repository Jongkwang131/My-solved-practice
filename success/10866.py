import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
queue = deque([])
for _ in range(N) :
    command = list(input().strip().split())
    if len(command) == 2:
        command_num = int(command[1])

    command = command[0]
    if command == "push_front" :
        queue.appendleft(command_num)
    if command == "push_back" :
        queue.append(command_num)
    if command == "pop_front" :
        if not queue :
            print(-1)
        else :
            print(queue.popleft())
    if command == "pop_back" :
        if not queue :
            print(-1)
        else :
            print(queue.pop())
    if command == "size" :
        print(len(queue))
    if command == "empty" :
        if not queue :
            print(1)
        else :
            print(0)
    if command == "front" :
        if not queue :
            print(-1)
        else :
            print(queue[0])
    if command == "back" :
        if not queue :
            print(-1)
        else :
            print(queue[-1])      

