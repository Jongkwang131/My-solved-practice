import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
N_cards = list(map(int, input().split()))
M = int(input())
M_cards = list(map(int, input().split()))

count_dict = Counter(N_cards)

answer = []

for num in M_cards :
    answer.append(count_dict[num])

sys.stdout.write(' '.join(map(str, answer)))