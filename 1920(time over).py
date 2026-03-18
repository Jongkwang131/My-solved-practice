N = int(input())
Nnums = set(map(int, input().split())) 

M = int(input())
Mnums = list(map(int, input().split()))


for x in Mnums :
    if x in Nnums :
        print(1)
    else :
        print(0)