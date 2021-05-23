import heapq
import math

def main():

    n, t = map(int, input().strip().split())
    czasy = list(map(int, input().strip().split()))
    result = False
    lsale = math.ceil(sum(czasy) / t)
    
    def czydziala(lsale):
        sale = [0 for dummy in range(lsale)]
        for x in czasy:
            z = heapq.heappop(sale)
            heapq.heappush(sale, z + x)
            if sale[0] > t:
                return False
        return True

    l, p = lsale, n

    while l != p:
        sr = p+l // 2
        if czydziala(sr):
            p = sr
        else:
            l = sr +1
        print(l, p)

    print(l)

main()

        



