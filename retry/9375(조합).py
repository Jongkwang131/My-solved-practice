import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    n = int(input())
    clothes_dict = {}
    
    for _ in range(n) :
        cloth, cloth_kind = input().split()
        if cloth_kind in clothes_dict :
            clothes_dict[cloth_kind] += 1
        else :
            clothes_dict[cloth_kind] = 1
    total = 1
    for i in clothes_dict.values() :
            total *= i+1
    print(total-1)
