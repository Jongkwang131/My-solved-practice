import sys
input = sys.stdin.readline


N = int(input())
W = []
for _ in range(N) :
    W.append(int(input()))

W.sort()
max = W[-1]
for i in range(N) :
    if W[i] * (N-i) > max :
        max = W[i]*(N-i)

print(max)