def merge(A, B):
    C = []
    #tutaj uzupelnic
    return C

def mergeSort(T, l, r):
    if l < r:
        #tutaj uzupelnic
        pass
    return [T[l]]


def testMerge():
    import random
    A = []
    B = []
    tf = [True, False]
    for i in range(1000):
        if random.choice(tf):
            A.append(i)
        else:
            B.append(i)
    C = merge(A, B)
    print(A)
    print(B)
    print(C)

def testSort():
    import random
    n = 1000
    T = [i for i in range(n)]
    random.shuffle(T)
    print(T)
    print()
    Tsort = mergeSort(T, 0, n-1)
    print(T)
    print(Tsort)

if __name__ == '__main__':
    testMerge()
    #testSort()