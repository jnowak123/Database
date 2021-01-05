def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a%b)

def main():
    num1 = int(input())
    miarki = list(map(int, input().split()))
    num2 = int(input())
    skladniki = list(map(int, input().split()))

    g = nwd(miarki[0], miarki[1])

    for v in range(2, num1):
        g = nwd(g, miarki[v])

    for v in range(num2):
        if skladniki[v] % g != 0:
            return 'PALUSZKI'
    return 'CIASTO'

print(main())

