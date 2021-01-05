import os

class Main:
    def __init__(self, path):
        self.path = path
        self.decode()

    def get_key(self, text):
        dic = {}
        key = ''
        i = -1
        while True:
            i += 1
            if key[-1] == '1':
                key = key[:-1]
                key[-1] = '1'
                
            if text[i] = '0':
                key = key + '0'
            else:
                dic[i+1:i+9] = key
                key[-1] = '1'
                i += 8

    def decode(self):
        filename, dummy_file_extension = os.path.splitext(self.path)
        with open(self.path, 'r+') as file, open(filename + '.txt', 'a+') as output:
            text = file.read()
            text = ''.join(format(ord(text[i]), '08b') for i in range(len(text)))

            output.write(text)

Main('me.bin')
