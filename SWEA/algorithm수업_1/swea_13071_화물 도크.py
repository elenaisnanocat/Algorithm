# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력
# 작업 시작 시간 s와 종료 시간 e

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr.sort(key=lambda x : x[1]) # 0 1 에서 1기준으로 정렬

    cnt = 0
    ed = 0
    for i in range(N):
        if arr[i][0] >= ed:
            cnt += 1
            ed = arr[i][1]
    print(f'#{tc} {cnt}')