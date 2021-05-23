from functools import lru_cache

@lru_cache(maxsize=5)
def fib(x):
    if x <= 1:
        return 1
    return fib(x -1) + fib(x -2)

def main(y):
    for x in range(y):
        print(x, fib(x))

main(400)