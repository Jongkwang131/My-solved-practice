N = int(input())

dots = []
for i in range(N) :
    x, y = map(int, input().split())
    dots.append([x,y])


dots.sort(key = lambda x : (x[0],x[1]))
for i in range(N) :
    print(dots[i][0], dots[i][1])