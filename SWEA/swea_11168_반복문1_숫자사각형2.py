T = int(input())
for tc in range(1,T+1):
    h,w = map(int,input().split())

    print('#{}'.format(tc))
    for i in range(1,h+1):
        cnt = i
        print(cnt, end=' ')
        for j in range(w-1):
            cnt += h
            print(cnt,end=' ')
        print()


# def fill():
# #     num = 1
# #     for j in range(W):
# #         for i in range(H):
# #             arr[i][j] = num
# #             num += 1
# #
# #
# # def printAll():
# #     for i in range(H):
# #         for j in range(W):
# #             print(arr[i][j], end=" ")
# #         print()
# #
# #
# # T = int(input())
# # for tc in range(T):
# #     H, W = map(int, input().split())
# #     arr = [[0] * W for _ in range(H)]
# #
# #     fill()
# #     print("#{}".format(tc + 1))
# #     printAll()