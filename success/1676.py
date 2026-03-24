N = int(input())

fac = 1

for i in range(N) :
    fac = fac * (i+1)

fac = str(fac)
word = fac[-1]
count = 0
i = 1
while word == '0' :
    count += 1
    i += 1
    word = fac[-1 * i]

print(count)
    