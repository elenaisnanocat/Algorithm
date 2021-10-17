T= int(input())
for tc in range(1,T+1):
    h,w = map(int,input().split())

    cnt = 0
    print('#{}'.format(tc))
    for i in range(h):
        for j in range(w):
            cnt += 1
            print(cnt,end=' ')
        print()

# T = int(input())
# for tc in range(T):
#     H, W = map(int, input().split())
#     num = 1
#
#     print("#{}".format(tc + 1))
#     for i in range(H):
#         for j in range(W):
#             print(num, end=" ")
#             num += 1
#         print()