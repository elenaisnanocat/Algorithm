T = int(input())
for tc in range(1,T+1):
    lst = list(input())

    for i in range(len(lst)):
        if lst[i] == '?':
            lst[i] = lst[-i-1]

    lst_reverse =[]

    for i in lst[::-1]:
        lst_reverse += i

    ans = 'Not exist'
    if lst == lst_reverse:
        ans = 'Exist'


    print('#{} {}'.format(tc,ans))