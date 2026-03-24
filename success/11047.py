import sys
input = sys.stdin.readline

N,K = map(int, input().split())
vals = []


for _ in range(N) :
    vals.append(int(input().strip()))

vals.sort(reverse=True)

total = K
num = 0
total_count = 0
while total != 0 :
    if vals[num] > total :
        num += 1
    else :
        count = total // vals[num]
        total_count += count
        total -= count * vals[num]
        num += 1

print(total_count)