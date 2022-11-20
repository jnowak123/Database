def clock(hour, minute):
    minute = 360 / 60 *minute
    if hour > 12:
        hour -= 12
    hour = 360 / 12 *hour
    hour += minute / 12
    print(abs(hour - minute))


clock(15, 45)