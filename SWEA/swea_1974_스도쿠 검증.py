def f():

    #행
    for i in range(9):
        r_cnt = [0]*10
        for j in range(9):
            r_cnt[arr[i][j]] += 1
            if r_cnt[arr[i][j]] > 1:
                return 0

    #열
    for i in range(9):
        c_cnt = [0]*10
        for j in range(9):
            c_cnt[arr[j][i]] += 1
            if c_cnt[arr[j][i]] > 1:
                return 0

    for i in range(0,9,3):
        for j in range(0,9,3):
            s_cnt = [0]*10
            for r in range(3):
                for c in range(3):
                    s_cnt[arr[i+r][j+c]] += 1
                    if s_cnt[arr[i+r][j+c]] > 1:
                        return 0

    return 1



T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    ans = f()
    print('#{} {}'.format(tc,ans))