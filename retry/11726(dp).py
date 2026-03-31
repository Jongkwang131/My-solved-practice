import sys
input = sys.stdin.readline
from math import pow

n = int(input())
"""
if n == 1:
    answer = 1
#2x2 사각형씩 나눠서 생각, 2개의 경우의 수씩 있으니까 다 곱하면 되지 않을까?
elif n%2 == 0 :
    answer = pow(2,int(n//2))
elif n%2 == 1 :
    answer = pow(2,int(n//2)) * (n//2+1)
"""
#=> 위 경우에 |=| 같은 경우를 놓치는 문제점이 발생

dp = [0] * (n + 1)

# 2. 초기값 설정
dp[1] = 1
if n >= 2:
    dp[2] = 2

# 3. 점화식 적용: dp[i] = dp[i-1] + dp[i-2]
for i in range(3, n + 1):
    # 더할 때마다 10007로 나눠서 숫자의 크기를 조절함
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])