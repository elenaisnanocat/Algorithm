def dfs(num, sum, cnt):
    global ans
    if cnt > N:
        return
    if sum > K:
        return
    if num == 21:
        if sum == K and cnt == N:
            ans += 1
        return
    dfs(num + 1, sum + num, cnt + 1) # 부분집합에 포함
    dfs(num + 1, sum, cnt) # 부분집합에 안포함


T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split()) # N : 부분집합의 수 / K : 부분집합의 합
    ans = 0
    dfs(1, 0, 0)
    print(f"#{t} {ans}")