level = 0

def silnia(num):
    global level
    level += 1
    print(" "*level + "enter")
    if num == 1:
        result = 1
    else:
        result = num * silnia(num - 1)

    print(" "*level + "exit " + str(result))
    level -= 1
    return result

print(silnia(int(10)))