def main():
    n, k = map(int, input().split())
    houses = list(map(int, input().split()))
    freq = {}
    count = 0
    for i in range(n):
        if i - k -1 >= 0:
            freq[houses[i-k-1]] -= 1
        if houses[i] not in freq:
            freq[houses[i]] = 0
        count += freq[houses[i]]
        freq[houses[i]] += 1
    return count

print(main())