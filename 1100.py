import sys
input = sys.stdin.readline

count = 0

for i in range(8) :
    dots = list(input())
    for j in range(8) :
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1) :
            if dots[j] == "F" :
                count += 1
print(count)