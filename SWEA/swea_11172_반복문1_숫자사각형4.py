T = int(input())
for tc in range(1,T+1):
    n = int(input())

    print('#{}'.format(tc))
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i*j,end=' ')
        print()


#
# def fill():
#     for i in range(N):
#         num = i + 1
#         for j in range(N):
#             arr[i][j] = num
#             num += i + 1
#
#
# def printAll():
#     for i in range(N):
#         for j in range(N):
#             print(arr[i][j], end=" ")
#         print()
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     arr = [[0] * N for _ in range(N)]
#
#     fill()
#     print("#{}".format(tc + 1))
#     printAll()