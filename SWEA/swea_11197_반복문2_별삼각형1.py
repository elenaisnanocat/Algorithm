T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())

    if m == 1:
        print('#{}'.format(tc))
        for i in range(1,n+1):
            for j in range(1,m+1):
                print('*'*i)

    if m == 2:
        print('#{}'.format(tc))
        for i in range(n,0,-1):
                print('*'*i)

    if m == 3:
        print('#{}'.format(tc))
        for i in range(1,n+1):
            print(' '*(n-i) + '*'*(i*2-1))


#
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#
#     print("#{}".format(tc + 1))
#     if M == 1:
#         for i in range(N):
#             for j in range(i + 1):
#                 print("*", end="")
#             print()
#     elif M == 2:
#         for i in range(N):
#             for j in range(N - i):
#                 print("*", end="")
#             print()
#     elif M == 3:
#         for i in range(N):
#             for j in range(N - i - 1):
#                 print(" ", end="")
#             for j in range((i + 1) * 2 - 1):
#                 print("*", end="")
#             print()