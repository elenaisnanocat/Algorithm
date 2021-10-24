for tc in range(1,11):
    N,words = map(str,input().split())

    stack = []
    for i in words:
        if i not in stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print('#{} {}'.format(tc,''.join(stack)))