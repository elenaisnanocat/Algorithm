T = int(input())
for tc in range(1,T+1):
    lst = list(input())

    stack = []
    for i in lst:
        if '(' or '{' or '}' or ')':
            if i not in stack:
                stack.append(i)
                continue
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)



