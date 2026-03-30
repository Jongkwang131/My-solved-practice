from math import sqrt, pow

test_num = 1

while True :
    nums = list(map(int, input().split()))
    a = nums[0]
    b = nums[1]
    c = nums[2]
    if a == 0 and b == 0 and c == 0 :
        break
    else :
        if c != -1 and (a>=c or b>=c) :
            print("Triangle #{}\nImpossible.".format(str(test_num))) 
        
        else :
            if a == -1 :
                find = "a"
                answer = sqrt(pow(c,2)-pow(b,2))
            elif b == -1 :
                find = "b"
                answer = sqrt(pow(c,2)-pow(a,2))
            elif c == -1 :
                find = "c"
                answer = sqrt(pow(a,2)+pow(b,2)) 
            print("Triangle #{}\n{} = {:.3f}".format(str(test_num), find, answer))
        print("")
        test_num += 1