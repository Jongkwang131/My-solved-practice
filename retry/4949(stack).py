while True :
    string = input()
    if string == "." :
        break
    
    stack = []
    is_balanced = True
    for char in string :
        if char == "(" or char == "[" :
            stack.append(char)
        
        elif char == ")" :
            if not stack or stack[-1] != "(" :
                is_balanced = False
                break
            stack.pop()
        
        elif char == "]" :
            if not stack or stack[-1] != "[" :
                is_balanced = False
                break
            stack.pop()
    if is_balanced and not stack :
        print("yes")
    else :
        print("no")


"""
    small = 0
    big = 0 
    answer = "yes"
    if string == "." :
        break
    else :    
        for i in string :
            if small < 0 or big < 0 :
                answer = "no"
                break
            elif (i == ")" and prev == "b") or (i =="]" and prev == "s") :
                answer = "no"
                break
            elif i == "(" :
                small += 1
                prev = "s"
            elif i == ")" :
                small -= 1
            elif i == "[" :
                big += 1
                prev = "b"
            elif i == "]" :
                big -= 1
    
    if small > 0 or big > 0 :
        answer = "no"
    
    print(answer)

"""