N = int(input())

for i in range(N) :
    string = input()
    stack = []
    is_balanced = True

    for char in string :
        if char == "(" :
            stack.append(char)
        
        elif char == ")" :
            if not stack or stack[-1] != "(" :
                is_balanced = False
                break
            stack.pop()

    if is_balanced and not stack :
        print("YES")
    else :
        print("NO")