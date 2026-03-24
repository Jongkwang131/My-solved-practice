import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site_pwd = {}

for _ in range(N) :
    siteandpwd = list(input().split())
    site_pwd[siteandpwd[0]] = siteandpwd[1]


for _ in range(M) :
    site_to_pwd = input().strip()
    sys.stdout.write(site_pwd[site_to_pwd]+"\n")
