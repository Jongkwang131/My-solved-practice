K = int(input())
stack = []
total = 0    

for i in range(K) :
    num = int(input())
    if num != 0 :
        stack.append(num)
    else :
        stack.pop()

for i in stack :
    total += i

print(total)