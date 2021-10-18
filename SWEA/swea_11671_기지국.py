dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                #거리 2칸
                for r in range(2):
                    #방향
                    for c in range(4):
                        nx = i + dx[c]*r
                        ny = j + dy[c]*r
                        if 0<= nx <N and 0<=ny<N:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'

            if arr[i][j] == 'B':
                for r in range(3):
                    # 방향
                    for c in range(4):
                        nx = i + dx[c] * r
                        ny = j + dy[c] * r
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'

            if arr[i][j] == 'C':
                for r in range(4):
                    # 방향
                    for c in range(4):
                        nx = i + dx[c] * r
                        ny = j + dy[c] * r
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print('#{} {}'.format(tc,cnt))