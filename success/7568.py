N = int(input())

profile = []
rank = []

for i in range(N) :
    weight, height = map(int, input().split())
    profile.append([weight,height])

for i in range(N) :
    win = 0
    for j in range(N) :
        # 몸무게 비교
        if profile[i][0] < profile[j][0] and profile[i][1] < profile[j][1] :
            win += 1
    rank.append(win+1)
for i in rank :
    print(i, end = ' ')
