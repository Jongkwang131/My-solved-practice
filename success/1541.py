import sys
input = sys.stdin.readline

line = input().strip()

###괄호 여러개 칠 수 있다고 가정하고 다시 풀어보기
#그냥 똑같이 다 한다음에 맥스 안찾고 다 마이너스로 합쳐서 계산하면 됨



#-단위로 끊기, 각각의 합이 가장 큰것에 괄호 씌우기
if "-" in line :
    ls = line.split("-")
    changed_index = 0
    eval_ls = []
    #먼저 그냥 사전에 다 바꿔놓기?
    for i in range(len(ls)) :
        if "+" in ls[i] :
            plus_ls = ls[i].split("+")
            for j in range(len(plus_ls)):
                plus_ls[j] = int(plus_ls[j])
                plus_ls[j] = str(plus_ls[j])  
            ls[i] = "+".join(plus_ls)
            eval_ls.append(eval(ls[i]))
        else :
            eval_ls.append(int(ls[i]))
            ls[i] = int(ls[i])
    for i in range(len(eval_ls)) :
        eval_ls[i] = str(eval_ls[i])
    print(eval(str("-".join(eval_ls))))
#-가 없는 경우 바로 합산 해서 결과 출력
else :
    ls = line.split("+")
    for i in range(len(ls)):
        ls[i] = int(ls[i])
        ls[i] = str(ls[i])    
    print(eval(str("+".join(ls))))


"""
    #각 합산 구해서 최대값 도출하기
    max_num = eval_ls[0]
    changed_index = 0
    for i in range(len(ls)) :
        if eval_ls[i] > max_num :
            max_num = eval_ls[i]
            changed_index = i
    ls[changed_index] = eval_ls[changed_index]
"""  

