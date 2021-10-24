def rcp(left,right):
    if card[left] == 1 and card[right] == 2 or (card[left] == 2 and card[right] == 3) or (card[left] == 3 and card[right] == 1):
        return right
    else:
        return left

def dfs(s,e):
    if s == e:
        return s
    mid = (s+e)//2
    left = dfs(s,mid)
    right = dfs(mid+1,e)
    ret = rcp(left,right)
    return ret

T = int(input())
for tc in range(1,T+1):
    N =int(input())
    card = [0] + list(map(int,input().split())) #인덱스번호맞춰주려고 0더함
    ret = dfs(1,N)
    print(f'#{tc} {ret}')
