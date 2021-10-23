#  첫 줄에 제품 수 N이 주어지고, 이후 제품당 한 줄 씩 N개의 줄에 걸쳐 공장별 생산비용 Vij
# 전체 제품의 최소 생산 비용을 계산하는 프로그램

def dfs(level,sum):  # 행, 현재 타임 합
    global min_sum
    if min_sum < sum :
        return

    if level == N:
        min_sum = min(min_sum,sum)
        return

    for i in range(N):
        if used[i] == 1: continue # 공장이 이전에 사용됨
        used[i] = 1 # 이후의 재귀호출 선택금지
        dfs(level + 1, sum + MAP[level][i])
        used[i] = 0 #원상복구
    return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]

    used = [0]*N
    min_sum = int(21e8)
    dfs(0,0)
    print('#{} {}'.format(tc,min_sum))