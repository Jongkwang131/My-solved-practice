##N = int(input())
##nums = []
##for i in range(N) :
##    nums.append(int(input()))

##nums.sort()
##for num in nums :
##    print(num)

import sys

# 1. 빠른 입력 설정
# input() 대신 sys.stdin.readline을 사용하면 속도가 비약적으로 빨라집니다.
input = sys.stdin.readline

N = int(input())
nums = []

# 2. 리스트에 담기
for _ in range(N):
    nums.append(int(input()))

# 3. 정렬 (람다 없이 기본 정렬이 가장 빠릅니다)
nums.sort()

# 4. 빠른 출력
# 리스트 전체를 하나의 문자열로 합쳐서 한 번에 출력하는 것이 효율적입니다.
sys.stdout.write('\n'.join(map(str, nums)) + '\n')