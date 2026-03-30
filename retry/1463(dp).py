import sys
input = sys.stdin.readline

n = int(input())
"""
count = 0
while n != 1 :
    if n % 3 == 0 and n != 3:
        div_num = int(n//3)-1 
        count += div_num
        n = n - 3*div_num
    elif n % 2 == 0 and n != 2:
        div_num = int(n//2)-1
        count += div_num
        n = n - 2*(div_num)
    else :
        count += 1
        n -= 1

print(count)
"""

dp = [0] * (n+1) #메모이제이션 : 한번 구한 최소 횟수 리스트에 저장해놓고 계속 사용
for i in range(2, n+1) :
    #1을 빼는 연산을 수행한다고 가정
    dp[i] = dp[i-1] + 1

    #2로 나누어 떨어진다면, 1을 뺸 결과와 2로 나눈 결과 중 최솟값 선택
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2]+1)
    
    #3로 나누어 떨어진다면, 위 결과와 3으로 나눈 결과중 최솟값 선택
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1)
    
print(dp[n])
