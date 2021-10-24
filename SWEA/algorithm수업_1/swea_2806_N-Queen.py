# 퀸은 같은 행, 열, 또는 대각선 위에 있는 말을 공격할 수 있다.
# N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수?

def n_queen(x):
    global result
    if x == N:
        result += 1
        return
    for y in range(N):
        if not used[y]:
            i = 1
            for i in range(N):
                for d in range(2):
                    nx = x + dx[d] * i
                    ny = y + dy[d] * i
                    if 0 <= nx < N and 0 <= ny < N:
                        if chess[nx][ny] == 1:
                            break
                else:
                    continue
                break
            else:
                used[y] = 1
                chess[x][y] = 1
                n_queen(x+1)
                used[y] = 0
                chess[x][y] = 0

dx = [-1,-1]
dy = [-1,1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    chess = [[0]*N for _ in range(N)]
    used = [0]*N

    result = 0
    n_queen(0)
    print('#{} {}'.format(tc,result))