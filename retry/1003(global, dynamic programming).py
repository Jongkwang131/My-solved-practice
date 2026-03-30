import sys
input = sys.stdin.readline

T = int(input())

def fibonacci(n) :
    global count_zero
    global count_one
    if n == 0:
        count_zero += 1
        return 0
    elif n == 1:
        count_one += 1
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
for _ in range(T) :
    N = int(input())
    count_zero = 0
    count_one = 0
    fibonacci(N)
    print(count_zero, count_one)

def solve():
    T = int(input())
    zero = [1, 0]
    one = [0, 1]
    for i in range(2, 41):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])
    for _ in range(T):
        N = int(input())
        print(zero[N], one[N])

solve()




