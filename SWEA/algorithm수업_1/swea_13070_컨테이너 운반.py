# N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로
# 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마
# 다음 줄에 N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    w = list(map(int,input().split()))
    t = list(map(int,input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)

    used = [0]*M
    result = 0

    for container in w: #화물의 각 무게 반복
        for ti in range(M): #트럭 적재용량
            if not used[ti] and t[ti] >= container: #아직 확인 전이고 컨테이너 무게보다 트럭에 적재할 수 있는 용량이 많을때
                used[ti] = 1
                result += container
                break

    print(f'#{tc} {result}')
