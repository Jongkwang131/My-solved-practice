"""
n = int(input())

def MenOfPassion(n) :
    sum = 0
    count = 0
    for i in range(1,n-2+1) : 
        for j in range(i+1, n-1+1) :
            for k in range(j + 1, n+1) :
                sum = sum + i * j * k
                count += 1
    return count

print(MenOfPassion(7))
print(3)
"""
import sys
input = sys.stdin.readline

n = int(input())

# 3중 for문의 수행 횟수는 nC3 조합 공식과 같습니다.
# (n * n-1 * n-2) / (3 * 2 * 1)
# n이 1이나 2일 경우 음수가 나오지 않도록 처리하거나, 
# 문제 조건(1 <= n)에 따라 자연스럽게 0이 나오도록 구성합니다.

if n < 3:
    print(0)
    print(3)
else:
    # 정수 나눗셈(//)을 사용하여 큰 수 연산 시 오차를 방지합니다.
    count = (n * (n - 1) * (n - 2)) // 6
    print(count)
    print(3)