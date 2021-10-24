def dfs(n):
    global cnt
    if n == N:
        cnt += 1
        return
    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        dfs(n+1)
        used[i] = 0

for tc in range(1,11):
    N = int(input())
    used = [0]*N
    cnt = 0
    dfs(0)

    print(f'#{tc} {cnt}')