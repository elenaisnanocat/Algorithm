def min_sum(lv,sum):
    global minsum
    if sum > minsum:
        return
    if lv == N:
        minsum = min(minsum,sum)
        return
    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        min_sum(lv+1,sum+arr[lv][i])
        used[i] = 0
    return


T = int(input())
for tc in range(1,T+1):
    N =int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0]*N
    minsum = int(21e8)

    min_sum(0,0)
    print(f'#{tc} {minsum}')