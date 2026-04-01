import sys
input = sys.stdin.readline

N = int(input().strip())

def factorial(n) :
    if n == 0 :
        return 1
    else :
        return factorial(n-1) * n

print(factorial(N))