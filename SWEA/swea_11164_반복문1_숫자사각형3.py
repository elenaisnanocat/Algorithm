T = int(input())
for tc in range(1,T+1):
    h,w = map(int,input().split())


    print('#{}'.format(tc))
    for i in range(h):
        if i % 2 == 0:
            cnt = i * w
            for _ in range(w):
                cnt += 1
                print(cnt,end=' ')
            print()
        else:
            cnt = (i+1)*w + 1
            for j in range(w):
                cnt -= 1
                print(cnt,end=' ')
            print()


# def fill():
#     num = 1
#     for i in range(H):
#         if i % 2 == 0:  # 짝수이면
#             for j in range(W):
#                 arr[i][j] = num
#                 num += 1
#         else:  # 홀수이면
#             for j in range(W - 1, -1, -1):
#                 arr[i][j] = num
#                 num += 1
#
#
# def printAll():
#     for i in range(H):
#         for j in range(W):
#             print(arr[i][j], end=" ")
#         print()
#
#
# T = int(input())
# for tc in range(T):
#     H, W = map(int, input().split())
#     arr = [[0] * W for _ in range(H)]
#
#     fill()
#     print("#{}".format(tc + 1))
#     printAll()