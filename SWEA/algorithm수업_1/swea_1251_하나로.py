#환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L2)만큼 지불
#총 환경 부담금을 최소로 지불하며, N개의 모든 섬을 연결할 수 있는 교통 시스템을 설계하시오.

# 첫번째 줄 섬의 개수 N
# 두번째 줄 각 섬들의 정수인 X좌표
# 세 번째 줄에는 각 섬들의 정수인 Y좌표
# 마지막으로, 해저터널 건설의 환경 부담 세율 실수 E

import heapq

def Union(a,b,cost):
    global N,result
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        N -= 1
        result += cost
        parent[pb] = pa

def Find(ch):
    if parent[ch] == ch:
        return ch

    ret = Find(parent[ch])
    parent[ch] = ret
    return parent[ch]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    parent = dict()
    for ch in range(N+1):
        parent[ch] = ch

    heap = []
    for a in range(N-1):
        for b in range(a+1,N):
            L = (X[b]-X[a])**2 + (Y[b]-Y[a])**2
            heapq.heappush(heap, (L,a,b))
    result = 0
    while N != 1:
        cost,a,b = heapq.heappop(heap)
        Union(a,b,cost)

    print('#{} {}'.format(tc,round(result * E)))