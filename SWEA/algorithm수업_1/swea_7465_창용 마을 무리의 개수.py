# 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면, 하나의 무리
# 몇 개의 무리가 존재하는지?
# N, M 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수
# M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호

def Union(a,b):
    global family
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        family -= 1
        parent[pb] = pa

def Find(ch):
    if parent[ch] == ch:
        return ch
    ret = Find(parent[ch])
    parent[ch] = ret
    return ret

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())

    parent = [i for i in range(N+1)]
    family = N
    for i in range(M):
        a,b =map(int,input().split())
        if Find(a) != Find(b):
            Union(a,b)

    print(f'#{tc} {family}')
