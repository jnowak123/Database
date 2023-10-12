def encode(fraze, shift):
    return ''.join([chr((ord(x) + shift) %128) for x in fraze])

def decode(fraze, shift):
    return ''.join([chr((ord(x) + 128 - shift) %128) for x in fraze])

print(encode('Hello world!', 4))