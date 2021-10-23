# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# 정점 개수 V(1≤V≤100,000), 간선 개수 E(1≤E≤200,000)
# A번 정점과 B번 정점이 가중치 C인 간선으로 연결
# 최소 스패닝 트리를 계산하는 알고리즘으로 Prim's algorithm과 Kruskal's algorithm이 있다.
# Prim's algorithm을 이용할 경우, 자료구조 힙(heap)을 이용
# Kruskal's algorithm을 이용할 경우, Disjoint Set(서로소 집합) 혹은 Union-Find 알고리즘을 이용

def Union(a,b):
    global total
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        MST[pb] = pa
        total += c
    return

def Find(a):
    if MST[a] == a:
        return a
    ret = Find(MST[a])
    MST[a] = ret
    return ret

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    MST = list(range(100001))
    total = 0
    values = [list(map(int,input().split())) for _ in range(E)]
    values.sort(key=lambda x : x[2])
    for v in values:
        a,b,c = v
        Union(a,b)

    print(f'#{tc} {total}')