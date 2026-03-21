C = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
for i in range(3):
    if B[i] > C[i] :
        total += B[i]-C[i]

print(total)