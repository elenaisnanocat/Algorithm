def binary_search(s,e,target):
    flag = 0 #'left','right'이전상태
    while s <= e:
        mid = (s+e)//2
        if A[mid] == target:
            return True
        elif target < A[mid]:
            if flag == 0:
                flag = 'right'
            elif flag == 'right':
                return False
            flag = 'right'
            e = mid - 1  # s  mid target  e   right 구간선택함
        elif A[mid] < target:
            if flag == 0:
                flag = 'left'
            elif flag == 'left':
                return False
            flag = 'left'
            s = mid + 1  # s target  mid   e    left 구간선택

    return False


T = int(input())
for tc in range(1,T+1):
     N,M = map(int,input().split())
     A = list(map(int,input().split()))
     B = list(map(int,input().split()))
     A.sort()

     cnt = 0
     for i in range(len(B)):
         target = B[i]
         ret = binary_search(0,len(A)-1,target) #B[i]가 A안에 있는지 탐색
         if ret == True:
             cnt += 1
     print('#{} {}'.format(tc,cnt))