T = int(input())

for i in range(T) :
    a, b = map(int, input().split())
    print("Case #{x}: {sum}".format(x=i+1, sum=a+b))