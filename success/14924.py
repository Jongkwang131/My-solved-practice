import sys
input = sys.stdin.readline

vars = list(map(int, input().split()))
s = vars[0]
t = vars[1]
d = vars[2]

print(int((d/(s*2))*t))