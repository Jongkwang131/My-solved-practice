N = int(input())
profile = []
for i in range(N) :
    age, name = input().split()
    age = int(age)
    profile.append([age,name])

profile.sort(key = lambda x : x[0])

for i in range(N) :
    print(profile[i][0],profile[i][1])
