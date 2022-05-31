def to_bin(val):
    return ''.join([format(x, '08b') for x in list(map(int, val.split('.')))]) if '.' in val else val

def to_dec(val):
    return '.'.join(map(str, [int(val[i:i+8], 2) for i in range(0, 32, 8)])) if '.' not in val else val

def main():
    address, mask = input().split()
    address = format(int(to_bin(address), 2) & int('0b'+ to_bin(mask), 2), '32b')
    print(to_dec(address))
    x = to_bin(mask).count('0')
    print(2**x -2)
    print(to_dec(address[0:-1] + '1'))
    print(to_dec(address[0:32 - x] + '1'*(x-1) + '0'))
    print(to_dec(address[0:32 - x] + '1'*x))

main()