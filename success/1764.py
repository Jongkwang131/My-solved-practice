import sys
input = sys.stdin.readline

N,M = map(int, input().split())

nev_listened =[]
nev_seen = []
for _ in range(N) :
    nev_listened.append(input().strip())
for _ in range(M) :
    nev_seen.append(input().strip())

nev_listened_seen = list(set(nev_listened) & set(nev_seen))
nev_listened_seen.sort()
print(len(nev_listened_seen))
for name in nev_listened_seen :
    sys.stdout.write(name+"\n")