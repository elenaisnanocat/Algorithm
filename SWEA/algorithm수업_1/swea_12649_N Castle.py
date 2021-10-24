dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x):
    global result
    if x == N:
        result += 1
        return
    for y in range(N):
        if not used[y]:
            i = 1
            for i in range(N):
                for d in range(4):
                    nx =  x + dx[d] * i
                    ny = y + dy[d] * i
                    if nx < 0 or ny < 0 or N >= nx or N >= ny : continue
                    if arr[nx][ny] == 1:
                        break
                else:
                    continue
                break
            else:
                used[y] = 1
                arr[x][y] = 1
                dfs(x+1)
                used[y] = 0
                arr[x][y] = 0

for tc in range(1,10+1):
    N = int(input())

    used = [0]*N
    arr = [[0]*N for _ in range(N)]

    result = 0
    dfs(0)
    print('#{} {}'.format(tc,result))