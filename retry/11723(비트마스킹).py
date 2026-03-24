import sys
input = sys.stdin.readline

M = int(input())

#비트마스킹
"""
1.<<(비트 왼쪽 시프트) : 스위치 위치 정하기
ex)
1 << x 는 숫자 1(...0001)을 왼쪽으로 x칸 밀라는 의미
1 << 1 : 00010 (십진수 2)
1 << 3 : 01000 (십진수 8)
=> x번 숫자를 건드릴 준비가 됐다, 라는 마스크를 만드는 과정!

2.|= (비트 OR 대입) : 스위치 켜기
| 연산은 두 비트 중 하나라도 1이면 1이 됩니다. 
S |= (1 << x)는 집합 S의 x번째 자리를 무조건 1로 만듭니다.
ex)
S (00101) | Mask (01000) = 01101
이미 켜져 있어도 1, 꺼져 있어도 1이 된다.

3. &= (비트 AND 대입) : 상태 확인 및 끄기
& 연산은 두 비트가 모두 1이어야만 1이 됩니다.

*확인 (check x): S & (1 << x)
x번 자리가 1이면 결과는 1 << x (0이 아님)가 나옵니다. (스택에 x가 있는 상태)
x번 자리가 0이면 결과는 0이 나옵니다. (스택에 x가 없는 상태)

*삭제 (remove x): S &= ~(1 << x)
~는 비트를 반전시킵니다. 
1 << 3이 01000이라면 ~(1 << 3)은 10111입니다.
이걸 & 연산하면 다른 곳은 그대로 유지되지만, 3번 자리만 확실하게 0으로 바뀝니다.

4. ^= (비트 XOR 대입) : "스위치 반전 (토글)"
^ 연산은 두 비트가 다르면 1, 같으면 0이 됩니다. (없으면 키고, 있으면 꺼라)
S ^= (1 << x)는 x번째 자리를 뒤집습니다.
원래 1이었다면? 
1^1 = 0(꺼짐)
원래 0이었다면? 
0^1 = 1(켜짐)
"""

#이진수 00000000000000000000(21자리), 21자리로 만드는 이유는 all에서 연산을 쉽게 하기 위함
#20까지의 스위치가 다 꺼진 상태로 초기화
s = 0 

for _ in range(M) :
    command_arr = input().split()
    main_command = command_arr[0]
    if len(command_arr) == 2 :
        x = int(command_arr[1])

    if main_command == "all" :
        #1부터 20까지 모든 비트를 1로 켜라
        s = (1 << 21) -1
    elif main_command == "empty" :
        #모두 스위치가 꺼진 상태로 초기화
        s = 0    
    elif main_command == "add" :
        #x번째 비트를 마스킹 후 or연산 수행(있으나 마나 무조건 스위치 켜기)
        #x번째 비트를 1로 켜라
        s |= (1 << x)
    elif main_command == "remove" :
        #x번째 비트를 마스킹 후 and연산 수행(있으면 스위치 켜기)
        #~연산을 통해 스위치 전환 (원래 애들은 그대로 유지, x만 꺼짐)
        #x번쨰 비트를 0으로 꺼라
        s &= ~(1 << x)
    elif main_command == "check" :
        # x번쨰 비트를 마스킹 하고 and 연산 수행한 값이 1(True)이면
        # x가 있으면
        if s & (1 << x) :
            print(1)
        # x가 없으면 
        else :
            print(0)
    elif main_command == "toggle" :
        # x번쨰 비트를 마스킹 하고 
        # x번째 비트가 켜져있으면 끄고, 꺼져있으면 킨다.
        s ^= (1 << x)


# 일반 조건문 반복문을 활용한 방법
"""
stack = []

for _ in range(M) :
    command_arr = input().split()
    main_command = command_arr[0]
    if len(command_arr) == 2 :
        command_num = command_arr[1]
    
    if main_command == "add" :
        stack.append(command_num)
    elif main_command == "remove" :
        if command_num in stack :
            stack.remove(command_num)
    elif main_command == "check" :
        if command_num in stack :
            sys.stdout.write(str(1)+"\n")
        else :
            sys.stdout.write(str(0)+"\n")
    elif main_command == "toggle" :
        if command_num in stack :
            stack.remove(command_num) 
        else :
            stack.append(command_num) 
    elif main_command == "all" :
        stack = []
        for i in range(1, 21) : stack.append(i)
    elif main_command == "empty" :
        stack = []
"""     

    