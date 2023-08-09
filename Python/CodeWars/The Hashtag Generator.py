def generate_hashtag(s):
    s = '#'+''.join([x[0].upper() + x[1:].lower() for x in s.split()])
    return False if len(s) >  140 or len(s) == 1 else s

print(generate_hashtag('CoDeWaRs is niCe'))
