def lowbound(numbers, num):
    left = 0
    right = len(numbers)
    while left < right:
        mid = (left + right)//2
        if numbers[mid] >= num:
            right = mid
        else:
            left = mid +1
    return left

def main():
    people = int(input())
    numbers = list(map(int, input().split()))
    for dummy_a in range(int(input())):
        myrange = list(map(int, input().split()))
        for b in range(len(myrange)):
            if b == 0:
                returnleft = lowbound(numbers, myrange[b])
            else:
                returnright = lowbound(numbers, myrange[b] +1)
        print((returnright - returnleft)*500)   

main()