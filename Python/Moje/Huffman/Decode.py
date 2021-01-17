import os

class Main:
    def __init__(self, path):
        self.path = path
        self.decode()
    
    class Node:
        def __init__(self, char=None, left=None, right=None):
            self.left = left
            self.right = right
            self.char = char

    def create_tree(self, text, i, carry):
        if text[i] == '1':
            node = self.Node(char = chr(int(text[i+1:i+9], 2)))
        else:
            left = create_tree(text, i+1)
            i = i+1 if tex[i+1] == '0' else i+9
            right = create_tree(text, i+1)
            node = self.Node(left = left, right = right)
            i = i+1 if tex[i+1] == '0' else i+9
        return node, i

    def remove_padding():
        pass

    def create_key():
        pass        
            

    def decode(self):
        filename, dummy_file_extension = os.path.splitext(self.path)
        with open(self.path, 'r+') as file, open(filename + '.txt', 'a+') as output:
            text = file.read()
            text = ''.join(format(ord(text[i]), '08b') for i in range(len(text)))

            tree, i = self.create_tree(text, 0, False)
            output.write(text)
            

Main('me.bin')
