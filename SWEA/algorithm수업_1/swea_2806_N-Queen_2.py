def func(level):
    global result
    if level == N:
        result += 1
        return
    for i in range(N):
        if visited[i] != 0:
            continue
        if used_hap[level+i] != 0:
            continue
        if used_gap[level-i] != 0:
            continue
        visited[i] = 1
        used_hap[level + i] = 1
        used_gap[level - i] = 1
        func(level+1)
        used_hap[level+i] = 0
        used_gap[level-i] = 0
        visited[i] = 0
    return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    MAP = [[0]*N for _ in range(N)]
    visited = [0]*N
    used_hap = [0] * (2*N)
    used_gap = [0] * (2*N)
    result = 0
    func(0)
    print('#{} {}'.format(tc,result))
