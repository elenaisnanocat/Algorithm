dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(i,j):
    global check
    if MAP[i][j] == 3:
        check = 1
        return

    for d in range(4):
        ny = i + dy[d]
        nx = j + dx[d]
        if ny < 0 or nx <0 or ny >=N or nx >=N: continue
        if MAP[ny][nx] == 1: continue
        if visited[ny][nx] == 1:continue
        visited[ny][nx] = 1
        dfs(ny,nx)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().rstrip())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    check = 0

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                visited[i][j] = 1
                dfs(i,j)
    print(f'#{tc} {check}')