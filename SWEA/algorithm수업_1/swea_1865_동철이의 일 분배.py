def dfs(i,cnt):
    global result
    if cnt <= result:
        return
    if i == N:
        result = max(result,cnt)
        return
    for j in range(N):
        if visited[j] == 1: continue
        visited[j] = 1
        dfs(i+1, cnt * (arr[i][j]/100))
        visited[j] = 0
    return


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    visited = [0]*N
    result = 0
    dfs(0,1)
    print('#{} {:.6f}'.format(tc,result*100))