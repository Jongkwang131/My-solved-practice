import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = []
c_M = []
for _ in range(N) :
    S.append(input())
for _ in range(M) :
    c_M.append(input())

count = 0
for str in c_M :
    if str in S :
        count += 1


print(count)