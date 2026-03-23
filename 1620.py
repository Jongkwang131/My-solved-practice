import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 도감 생성
name_to_num_pokedex = {}
num_to_name_pokedex = {}
for i in range(1,N+1) :
    poketmon = input().strip()
    name_to_num_pokedex[poketmon] = i
    num_to_name_pokedex[i] = poketmon

for _ in range(M) :
    question = input().strip()
    if question.isdigit() :
        poket_num = int(question)
        sys.stdout.write(num_to_name_pokedex[poket_num]+"\n")
    else :
        print(name_to_num_pokedex[question])