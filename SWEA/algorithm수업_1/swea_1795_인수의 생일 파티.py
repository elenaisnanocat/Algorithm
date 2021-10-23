# 인수가 사는 마을에는 N개의 집, 인수의 집은 X번 집
# 각 사람들은 자신의 집에서 X번 집으로 오고 가기 위해 최단 시간으로 이동
# X번 집으로 오고 가는데 드는 시간 중에서 가장 오래 걸리는 집은 어느 정도 걸리는지?

#첫 번째 줄에는 세 정수 N,M,X ,다음 M개의 각 줄에는 세 정수 x, y, c
#x번 집에서 y번 집으로 가는 데 시간이 c가 걸리는 단 방향 도로 (st,ed,c)

import heapq

def dijkstra(dist,adj):
    minheap = []
    heapq.heappush(minheap, (0, X))

    while minheap:
        cost, now = heapq.heappop(minheap)
        if dist[now] < cost: continue

        for w , next in adj[now]:
            if cost + w < dist[next]:
                dist[next] = cost + w # 더 작은값으로 갱신
                heapq.heappush(minheap, (cost+w,next))


T = int(input())
for tc in range(1,T+1):
    N,M,X = map(int,input().split())

    adj = [[] for _ in range(N+1)]
    adj_2 = [[] for _ in range(N+1)]
    for i in range(M):
        st,ed,c = map(int,input().split())
        adj[st].append((c,ed))
        adj_2[ed].append((c,st))

    result = 0

    dist = [int(21e8) for _ in range(N+1)]
    dist[X] = 0
    dijkstra(dist,adj) #시작부터 끝 최단거리(?)

    dist_2 = [int(21e8) for _ in range(N+1)]
    dist_2[X] = 0
    dijkstra(dist_2,adj_2) #끝부터 시작점까지 최단거리(?)

    for i in range(1,N+1):
        result = max(result, dist[i]+dist_2[i]) #각 경우(?) 중 가장 오래걸리는 시간

    print('#{} {}'.format(tc,result))