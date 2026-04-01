import sys
from math import sqrt
input = sys.stdin.readline
    
"""
n = int(input())
dp = [0] * (n+1)    
for i in range(1, n+1) :
    dp[i] = i

for i in range(1,n+1) :
    j = 1
    while j * j <= i :
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1
        j+=1
    
print(dp[n])
"""

import sys

def solve():
    n = int(sys.stdin.readline())
    
    # 1. 답이 1인 경우 (n 자체가 제곱수)
    if int(n**0.5)**2 == n:
        print(1)
        return

    # 제곱수들을 미리 리스트에 담아둡니다. (시간 단축 핵심)
    squares = [i*i for i in range(1, int(n**0.5) + 1)]

    # 2. 답이 2인 경우 (n - i^2 이 제곱수인가?)
    for s in squares:
        if int((n - s)**0.5)**2 == (n - s):
            print(2)
            return

    # 3. 답이 3인 경우 (n - i^2 - j^2 이 제곱수인가?)
    # Python 3 환경에서는 이 루프가 가장 고비입니다.
    for i in squares:
        for j in squares:
            if i + j > n:
                break
            remainder = n - i - j
            if int(remainder**0.5)**2 == remainder:
                print(3)
                return

    # 4. 위에서 안 걸러졌다면 라그랑주 정리에 의해 답은 무조건 4
    print(4)

solve()