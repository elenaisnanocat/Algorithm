def cart(lv,sum,cnt):
    global result
    if cnt == N-1:
        result = min(result, sum + arr[lv][0])
        return
    for i in range(N):
        if arr[lv][i] == 0: continue
        if visited[i] == 1: continue
        visited[i] = 1
        cart(i,sum+arr[lv][i],cnt+1)
        visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    visited[0] = 1
    result = 21e8
    cart(0,0,0)
    print(f'#{tc} {result}')