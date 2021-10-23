def dfs(now, cnt):
    global min_cnt
    if now > N: return
    if visited[now] <= cnt: return
    visited[now] = cnt
    if now == N:
        min_cnt = min(min_cnt, cnt)
        return
    for dist in range(1, lst[now] + 1):
        dfs(now + dist, cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    min_cnt = int(21e8)
    visited = [int(21e8) for _ in range(N + 1)]
    dfs(1, 0)
    print("#{} {}".format(tc, min_cnt - 1))