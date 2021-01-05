import os

class Main:
    def __init__(self, path):
        self.path = path
        self.decode()

    def count_zeros(self, text, i):
        count = 0
        while text[i] == 0:
            count += 1
            i += 1
        return count

    def get_tree(self, key):
        pass

    def make_key(self, text):
        index = 0
        index = self.count_zeros(text, 0)
        key = '0'* index

    def convert_text(self, text):
        pass

    def decode(self):
        filename, dummy_file_extension = os.path.splitext(self.path)
        with open(self.path, 'r+') as file, open(filename + '.txt', 'a+') as output:
            text = file.read()
            text = ''.join(format(ord(text[i]), '08b') for i in range(len(text)))

            output.write(text)

Main('me.bin')
