nums = list(map(int,input().split()))
alpha = input()

nums.sort()

answer = []

for s in alpha :
    if s == "A" :
        answer.append(str(nums[0]))
    elif s == "B" :
        answer.append(str(nums[1]))
    elif s == "C" :
        answer.append(str(nums[2]))

print(" ".join(answer))