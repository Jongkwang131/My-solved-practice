import sys
input = sys.stdin.readline


N = int(input())
count = 0
for i in range(1, N+1) :
    num = str(i)   
    if len(num) == 1 or len(num) == 2:
           count += 1
           continue
    elif len(num) > 2 :
        is_checked = True
        for j in range(1,len(num)-1) :
            if int(num[j])-int(num[j-1]) != int(num[j+1]) - int(num[j]) :
                is_checked = False
            if is_checked :
                count += 1

print(count) 