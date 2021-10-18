T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    cnt = [0]*101
    for i in range(len(cnt)):
        cnt[i] = lst.count(i)

    m_lst = max(cnt)
    for j in range(len(cnt)-1,-1,-1):
        if cnt[j] == m_lst:
            ans = j
            break

    print('#{} {}'.format(tc,ans))