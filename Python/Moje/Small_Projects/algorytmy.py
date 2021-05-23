import time
import random
import matplotlib.pyplot as plt

def babelkowe(returnlist, n):
    for i in range(n):
        for j in range(n -i -1):
            if returnlist[j] < returnlist[j+1]:
                returnlist[j], returnlist[j+1] = returnlist[j+1], returnlist[j]
    return returnlist

def kopcowanie(returnlist, n):

    def heapify(returnlist, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and returnlist[l] > returnlist[largest]:
            largest = l;
        if r < n and returnlist[r] > returnlist[largest]:
            largest = r;
        if largest != i:
            returnlist[i], returnlist[largest] = returnlist[largest], returnlist[i];
            heapify(returnlist, n, largest);

    def extract_largest(heap):
        returnlist.append(heap[0])
        heap[0] = heap.pop()
        heapify(heap, len(heap), 0)

    for i in range(n // 2 -1, -1, -1):
        heapify(returnlist, n, i)
    heap = returnlist.copy()
    returnlist = []
    while len(heap) > 1:
        extract_largest(heap)
    returnlist.append(heap[0])

    return returnlist

def zliczanie(mylist, n, maxval):
    returnlist = [0 for x in range(n)]
    count = [0 for x in range(maxval +1)]
    for i in mylist:
        count[i] += 1
    for i in range(1, maxval +1):
        count[i] += count[i -1]
    for i in mylist:
        returnlist[count[i] -1] = i
        count[i] -= 1
    return returnlist

def run(mylist, n):
    if n < 10001:
        start = time.time()
        babelkowe(mylist.copy(), n)
        a = time.time() - start
    else:
        a = None
    start = time.time()
    kopcowanie(mylist.copy(), n)
    b = time.time() - start 
    start = time.time()
    zliczanie(mylist.copy(), n, n)
    c = time.time() - start 
    return a, b, c

def main():
    bubble_sort = []
    heap_sort = []
    counting_sort = []
    sizes = [10, 100, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
    for n in sizes:
        arr = [random.randint(0, n) for x in range(n)]
        a, b, c  = run(arr, n)
        if n < 10001:
            bubble_sort.append(a)
        heap_sort.append(b)
        counting_sort.append(c)

    plt.plot(sizes[0:6], bubble_sort)
    plt.plot(sizes, heap_sort)
    plt.plot(sizes, counting_sort)
    plt.ylabel("Speed (s)")
    plt.xlabel("Num of variables")
    plt.title("Execution speed of different sorting algorithms relative to the amount of variables to sort")
    plt.show()

    plt.plot(sizes[0:6], bubble_sort)
    plt.ylabel("Speed (s)")
    plt.xlabel("Num of variables")
    plt.title("Execution speed of bubble sort relative to the amount of variables to sort")
    plt.show()

main()
    