def dfs(now):
    for next in range(1,V+1): #노드(?)방문
        if arr[now][next] == 0: continue #now->next없다
        if visited[next] == 1: continue #이미 왔다 갔다
        visited[next] = 1
        dfs(next)


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())

    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        a,b = map(int,input().split())
        arr[a][b] = 1

    S,G = map(int,input().split())
    visited = [0]*(V+1)
    visited[S] = 1 #시작노드 재방문 x

    dfs(S)

    if visited[G] == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')