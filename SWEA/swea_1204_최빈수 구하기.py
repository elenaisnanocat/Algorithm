T = int(input())
for tc in range(1,T+1):
    N = int(input())
    score = list(map(int,input().split()))

    cnt = [0]*101

    for i in range(len(score)):
        cnt[score[i]] += 1

    m_cnt = max(cnt)
    for j in range(len(cnt)-1,-1,-1):
        if cnt[j] == m_cnt:
            ans = j
            break

    print('#{} {}'.format(tc,ans))