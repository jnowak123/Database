import imp
import importlib
import random
import matplotlib.pyplot

pointsx, pointsy = [], []
x, y = 1, 1
for i in range(5000):
    if i > 100:
        r = random.randint(0,1)
        if r == 0:
            x = -0.4*x -1
            y = -0.4*y + 0.1
        else:
            x = 0.76*x - 0.4*y
            y = 0.4*x + 0.76*y
        pointsx.append(x)
        pointsy.append(y)

print(round(sum(pointsx) / len(pointsx), 2))
print(round(sum(pointsy) / len(pointsy), 2))
print(max(pointsx), min(pointsx))
print(max(pointsy), min(pointsy))

matplotlib.pyplot.plot(pointsx, pointsy, 'ro')
matplotlib.pyplot.show()