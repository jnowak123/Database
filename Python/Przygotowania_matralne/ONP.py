zad = '32+5*'


def to_ONP(zad):
    stack = []
    zad = list(zad)

    for x in zad:
        if x.isnumeric():
            stack.append(x)
        else:
            a = int(stack.pop(-1))
            b = int(stack.pop(-1))
            match x:
                case "+":
                    stack.append(a+b)
                case "-":
                    stack.append(a-b)
                case "*":
                    stack.append(a*b)
                case "/":
                    stack.append(a/b)
    return stack[-1]


