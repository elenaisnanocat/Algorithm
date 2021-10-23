# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
# 사용할 수 있는 연산이 +1, -1, *2, -10
# 연산 최소 몇번?

from collections import deque

def bfs(n,m):
    qu = deque()
    visited = [0] *1000001
    visited[n] = 1 #재등록 방지
    qu.append((n,0)) #(숫자,level) level:연산횟수

    while qu:
        num,level = qu.popleft()
        if num == m:
            return level

        # next 노드 큐에 등록(방문예약)
        # 사용할 수 있는 연산
        if 1 <= num+1 <= 1000000 and visited[num+1] == 0:
            visited[num+1] = 1
            qu.append((num+1, level +1))
        if 1 <= num -1 <= 1000000 and visited[num - 1] == 0:
            visited[num - 1] = 1
            qu.append((num - 1, level + 1))
        if 1 <= num *2 <= 1000000 and visited[num *2] == 0:
            visited[num *2] = 1
            qu.append((num *2, level + 1))
        if 1 <= num -10 <= 1000000 and visited[num -10] == 0:
            visited[num -10] = 1
            qu.append((num -10, level + 1))
    return -1

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    ret = bfs(N,M)

    print('#{} {}'.format(tc,ret))