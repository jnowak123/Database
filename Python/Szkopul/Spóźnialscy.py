import math

amount_of_people = int(input())
biggest_distance = -1

for i in range(amount_of_people):
    person = input().split()
    distance = math.hypot(abs(int(person[1])), abs(int(person[2])))
    if distance > biggest_distance or distance == biggest_distance and max(data[0], person[0]) == person[0]:
        biggest_distance = distance
        data = person

print(data[0], math.floor(distance/5)*60)