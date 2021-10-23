# Ugly Number는 숫자 2, 3, 5 를 사용하여 만들어 낼 수 있는 수
# Ugly Number = 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
# 만약 1 9 10 을 입력받았다면, 출력결과는 1 10 12

import heapq

ugly = [0] * 1501
min_heap = []
th = 1
heapq.heappush(min_heap,1)
p = -1

while th < 1501:
    now = heapq.heappop(min_heap)
    if p == now: continue

    ugly[th] = now
    th += 1

    heapq.heappush(min_heap,now*2)
    heapq.heappush(min_heap,now*3)
    heapq.heappush(min_heap,now*5)
    p = now

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    print('#{}'.format(tc), end=' ')
    for i in lst:
        print(ugly[i], end=' ')
    print()