def dfs(x,y):
    if x >= N or y>= N :return int(21e8)
    if x == N-1 and y == N-1:
        return MAP[x][y]
    a = dfs(x,y+1)
    b = dfs(x+1,y)
    return min(a,b) + MAP[x][y]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]

    ret = dfs(0,0)
    print(f'#{tc} {ret}')