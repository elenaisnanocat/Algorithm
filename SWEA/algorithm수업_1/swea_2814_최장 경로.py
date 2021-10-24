def dfs(now, cnt):
    global N, ans
    ans = max(ans, cnt)
    for next in range(1, N + 1):
        if visited[next] == 1: continue
        if MAP[now][next] == 1:
            visited[next] = 1
            dfs(next, cnt + 1)
            visited[next] = 0

t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    MAP = [[0 for i in range(N + 1)] for j in range(N + 1)]
    visited = [0 for i in range(N + 1)]
    ans = 0
    for i in range(M):
        y, x = map(int, input().split())
        MAP[y][x] = 1
        MAP[x][y] = 1

    for y in range(1, N + 1):
        visited[y] = 1
        dfs(y, 1)
        visited[y] = 0

    print(f'#{tc} {ans}')