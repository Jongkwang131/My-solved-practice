"""
"""

import sys

input = sys.stdin.readline
n = int(input())
stack = []
count = 1
ans = []
possible = True


for _ in range(n) :
    num = int(input())
    
    while count <= num :
        stack.append(count)
        ans.append("+")
        count += 1

    if stack[-1] == num :
        stack.pop()
        ans.append("-")
    else :
        possible = False
        break

if not possible :
    print("NO")
else :
    sys.stdout.write("\n".join(ans))
