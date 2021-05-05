def main():
    n, m = map(int, input().split())
    presses = map(int, input().split())
    buttons = [0 for i in range(n+1)]
    maxnum, lastmaxnum = 0, 0
    for i in presses:
        if i == n +1:
            lastmaxnum = maxnum
        else:
            if buttons[i] < lastmaxnum:
                buttons[i] = lastmaxnum
            buttons[i] += 1
            if buttons[i] > maxnum:
                maxnum = buttons[i]
    for i in range(n+1):
        if buttons[i] < lastmaxnum:
            buttons[i] = lastmaxnum
    return buttons[1:n+1]

print(*main())
