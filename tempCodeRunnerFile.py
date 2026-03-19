while True :
    string = input()
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
그냥 카운트만 가지고는 안됨
( 이 나옴 -> 다음 (, ), [ 만 올 수 있다. 
() / (( )) / ([ )] / [()] / ()() 

(를 small +1 / )를 small -1이라고 하면?
A rope may form )( a trail in a maze. 이 상태에서 기본값이 0인데 -1이 먼저 돼서 small 이 -1이 됨 -> stop!
"""