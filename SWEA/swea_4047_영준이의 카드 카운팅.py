T = int(input())
for tc in range(1,T+1):
    lst = list(input())

    card = []
    ans = ""

    S = 13
    D = 13
    H = 13
    C = 13

    for i in range(0,len(lst)-2,3):
        card.append(lst[i:i+3])

    for a in range(len(card)-1):
        for b in range(a+1,len(card)):
            if card[a] == card[b]:
                ans = "ERROR"
                break
        if ans == "ERROR":
            break

    if ans == "ERROR":
        print(f'#{tc} {ans}')

    else:
        for j in range(len(card)):
            if card[j][0] == 'S':
                S -= 1
            elif card[j][0] == 'D':
                D -= 1
            elif card[j][0] == 'H':
                H -= 1
            elif card[j][0] == 'C':
                C -= 1

        print(f'#{tc} {S} {D} {H} {C}')