import sys
input = sys.stdin.readline

inputs = list(map(int, input().split()))
N = inputs[0]
m = inputs[1]
M = inputs[2]
T = inputs[3]
R = inputs[4]

ex_time = 0
real_time = 0
total_beat = m
possible = True
if total_beat+T > M and total_beat-R < m :
    possible = False
else :
    while ex_time != N :
        if total_beat+T <= M and total_beat+T > m :
            total_beat += T
            ex_time += 1
            real_time += 1
        else :
            if total_beat-R < m :
                total_beat = m
            else :
                total_beat -= R
            real_time += 1

if possible == True :
    print(real_time)
else :
     print(-1)
        



    
