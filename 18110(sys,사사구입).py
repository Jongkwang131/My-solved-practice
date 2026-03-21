import sys

input = sys.stdin.readline

n = int(input())

scores = []

def my_format(num) :
    return int(num+0.5)

if n == 0 :
    sys.stdout.write('0')
else :    
    for i in range(n) :
        scores.append(int(input()))
    scores.sort()
    jersa_person = my_format(n*0.15)
    if jersa_person > 0 :
        scores = scores[jersa_person:-jersa_person]
    sys.stdout.write(str(my_format(sum(scores)/len(scores))))
