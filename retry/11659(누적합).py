import sys
input = sys.stdin.readline

N,M = map(int, input().split())
nums = list(map(int, input().split()))
"""
for _ in range(M) :
    i,j = map(int, input().split())
    total = 0

    for s in range(i-1, j) :
        total += nums[s]
    print(total)
"""
#미리 누적합을 구해놓고 i,j 가 주어졌을떄 S[j]-S[i-1]를 구하면 됨
S = [0, nums[0]]
for s in range(1,N) :
    S.append(S[s]+nums[s])

for _ in range(M) :
    i,j = map(int, input().split())
    print(S[j]-S[i-1])