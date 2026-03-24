import sys

input = sys.stdin.readline

N,M = map(int, input().split())
board = [input().strip() for i in range(N)]

min_repaint = float('inf') #최솟값 비교를 위한 비교대상으로 무한대 값으로 초기화

for i in range(N-7) :
    for j in range(M-7) :
        draw_white = 0
        draw_black = 0

        for x in range(i,i+8) :
            for y in range(j,j+8) :
                if (x+y) % 2 == 0 :
                    if board[x][y] != 'W':
                        draw_white += 1
                    if board[x][y] != 'B':
                        draw_black += 1
                else:
                    if board[x][y] != 'B':
                        draw_white += 1
                    if board[x][y] != 'W':
                        draw_black += 1
        
        # 4. 두 패턴 중 더 적게 칠하는 값을 선택하고, 전체 최솟값과 비교
        min_repaint = min(min_repaint, draw_white, draw_black)

# 5. 결과 출력
print(min_repaint) 