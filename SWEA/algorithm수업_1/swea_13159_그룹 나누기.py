def Union(a,b):
    global N
    pa = Find(a) # a 가 속한그룹 대표자 찾기
    pb  = Find(b) # b 가 속한그룹 대표자 찾기
    if pa != pb: # 최종 부모가 다르다 == 다른그룹일때
        N -= 1 # 전체그룹수 1감소(?)
        parent[pb] = pa

def Find(ch):
    if parent[ch] == ch:
        return ch
    ret = Find(parent[ch])
    parent[ch] = ret # 경로 압축  (최종부모와 직접연결)
    return parent[ch]

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    parent = dict()
    for ch in range(1,N+1):
        parent[ch] = ch

    for i in range(M):
        Union(lst[i*2],lst[i*2+1])

    print('#{} {}'.format(tc,N))