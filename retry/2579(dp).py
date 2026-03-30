import sys
input = sys.stdin.readline

N = int(input())
stairs_scores = []
for _ in range(N) :
    stairs_scores.append(int(input()))

"""
#마지막 계단에서부터 시작
current_stair = N-1
current_score = stairs_scores[current_stair]
count = 1
while current_stair != 0 :
#두단계 내려간 계단과 한 단계 내려간 계단 점수를 비교, count가 2면 한단계를 더 내려갈 수 없기 때문에 무조건 두 계단 내려감
    if current_stair < 2 or (count != 2 and stairs_scores[current_stair-1] > stairs_scores[current_stair-2]) :
        current_score += stairs_scores[current_stair-1]
        current_stair -= 1
        #연속된 계단을 내려감을 표시
        count += 1
    else :
        current_score += stairs_scores[current_stair-2]
        current_stair -= 2
        #연속 계단이 초기화 됨
        count = 1
    print(current_score)
"""

dp = [0] * N
dp[0] = stairs_scores[0]
if N > 1 :
    dp[1] = stairs_scores[0] + stairs_scores[1]
if N > 2 :
    dp[2] = max(stairs_scores[0] + stairs_scores[2], stairs_scores[1]+stairs_scores[2])

for i in range(3,N) :
    dp[i] = max(dp[i-3] + stairs_scores[i-1]+stairs_scores[i], dp[i-2]+stairs_scores[i])

print(dp[N-1])