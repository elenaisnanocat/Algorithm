T = int(input())
for tc in range(1,T+1):
    alpha = input()

    lst = []
    for i in range(len(alpha)):
        if alpha[i] not in lst:
            lst.append(alpha[i])
        else:
            lst.remove(alpha[i])

    if lst == []:
        print('#{} {}'.format(tc,"Good"))
    else:
        lst.sort()
        print('#{} {}'.format(tc,''.join(lst)))