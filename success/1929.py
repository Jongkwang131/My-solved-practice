import sys
from math import sqrt

input = sys.stdin.readline

M,N = map(int, input().split())
for i in range(M,N+1) :
    if i == 1:
        continue

    is_true = True
    for j in range(2,int(sqrt(i))+1) :
        if i % j == 0 :
            is_true = False
            break
        
    if is_true == True :
        sys.stdout.write(str(i)+'\n')
    
    
