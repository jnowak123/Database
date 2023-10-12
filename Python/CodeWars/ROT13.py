def rot13(message):
    alf = list('abcdefghijklmnopqrstuvwxyz')
    return [alf[(alf.index(letter) +13)%26] if letter in alf else letter for letter in message.lower()]

print(rot13("EBG13 rknzcyr."))