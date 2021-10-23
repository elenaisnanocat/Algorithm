# 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램
# 마지막 연결지점 번호 N과 도로의 개수 E
# E개의 줄에 걸쳐 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w

import heapq

def dijkstra():
    minheap = []
    heapq.heappush(minheap, (0,0))
    dist = [int(21e8) for _ in range(N+1)]
    dist[0] = 0

    while minheap:
        cost, now = heapq.heappop(minheap)
        if dist[now] < cost: continue

        for w, next in adj[now]:
            if cost + w < dist[next]:
                dist[next] = cost + w
                heapq.heappush(minheap, (cost + w,next))
    return dist

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        adj[s].append((w,e))

    dist = dijkstra()

    print('#{} {}'.format(tc,dist[-1]))