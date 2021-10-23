import heapq

def dijkstra():
    while minheap:
        time,x,y = heapq.heappop(minheap)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if time + arr[nx][ny] < dist[nx][ny]:
                    dist[nx][ny] = time + arr[nx][ny]
                    heapq.heappush(minheap, (dist[nx][ny],nx,ny))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    dist = [[int(21e8)] * N for i in range(N)]
    dist[0][0] = 0  # 시작점
    minheap = []
    heapq.heappush(minheap, (0, 0, 0))

    dijkstra()

    print(f'#{tc} {dist[-1][-1]}')