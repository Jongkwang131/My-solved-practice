vars = list(map(int, input().split()))
u_r = vars[0]
t_r = vars[1]
u_o = vars[2]
t_o = vars[3]

score = u_r*56 + t_r*24 + 14*u_o + 6*t_o
print(score)