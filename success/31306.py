import sys
input = sys.stdin.readline

string = input()

mo = ["a","e","i","o","u"]
mo_count = 0
y_count = 0

for s in string :
    if s in mo :
        mo_count += 1
    elif s == "y" :
        y_count += 1

print(mo_count, mo_count+y_count)