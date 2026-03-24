import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N) :
    command = list(input().split())
    if command[0] == "push" :
        stack.append(command[1])
    elif command[0] == "pop" :
        if not stack : 
            sys.stdout.write("-1\n")
        else :
            sys.stdout.write(str(stack.pop(0))+"\n")
    elif command[0] == "size" :
        sys.stdout.write(str(len(stack))+"\n")
    elif command[0] == "empty" :
        if not stack :
            sys.stdout.write("1\n")
        else :
            sys.stdout.write("0\n")
    elif command[0] == "front" :
        if not stack : 
            sys.stdout.write("-1\n")
        else :
            sys.stdout.write(stack[0]+'\n')
    elif command[0] == "back" :
        if not stack : 
            sys.stdout.write("-1\n")
        else :
            sys.stdout.write(stack[-1]+'\n')