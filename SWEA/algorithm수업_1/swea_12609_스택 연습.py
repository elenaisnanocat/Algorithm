T = int(input())
for tc in range(1,T+1):
    N = int(input())
    stack = []
    print(f'#{tc}')
    for i in range(N):
        temp = input().rstrip().split()
        if temp[0] == 'i':
            stack.append(temp[1])
        elif temp[0] == 'c':
            print(len(stack))
        elif temp[0] == 'o':
            if not stack:
                print('empty')
            else:
                print(stack[-1])
                stack.pop()
