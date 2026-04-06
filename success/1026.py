import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
A.sort(reverse=True)
B.sort()
for num1,num2 in zip(A,B) :
    total += num1*num2

print(total)