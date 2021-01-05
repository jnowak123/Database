import os

class Main:
    def __init__(self, path):
        self.path = path
        self.priority_queue = []
        self.key = {}
        self.tree = ''
        self.encode()

    class Node:
        def __init__(self, val, char=None, left=None, right=None):
            self.left = left
            self.right = right
            self.val = val
            self.char = char

    def create_dict(self, string):
        dic = {}
        for char in string:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
        dic = list(map(list, sorted(dic.items(), key= lambda x: x[1], reverse=True)))
        for char in dic:
                self.priority_queue.append(self.Node(char[1], char=char[0]))

    def create_tree(self):
        while len(self.priority_queue) > 1:
            nodel = self.priority_queue[-1]
            noder = self.priority_queue[-2]
            self.priority_queue.append(self.Node(nodel.val + noder.val, left=nodel, right=noder))
            self.priority_queue.pop(-2)
            if len(self.priority_queue) > 1:
                self.priority_queue.pop(-2)
            self.priority_queue = sorted(self.priority_queue, key=lambda x: x.val, reverse=True)

    def create_key(self, node, keypath):
        if node.char:
            self.key[node.char] = keypath
            self.tree = self.tree + '1'+ format(ord(node.char), 'b')
        else:
            self.tree = self.tree + '0'
            self.create_key(node.left, keypath + '1')
            self.create_key(node.right, keypath + '0')

    def padding(self, text):
        num = '1' if text[-1] == 0 else '0'
        if len(text) %8 != 0:
            text = text + (8 - len(text) % 8)*num
        else:
            text = text + num*8
        return text

    def create_compressed_text(self, text):
        compressed_text = ''
        for char in text:
            compressed_text = compressed_text + self.key[char]
        return compressed_text

    def encode(self):
        filename, dummy_file_extension = os.path.splitext(self.path)
        output_path = filename + '.bin'

        with open(self.path, 'r') as file, open(output_path, 'a+b') as output:
            text = file.read().strip()
            output.truncate(0)

            self.create_dict(text)
            self.create_tree()   
            self.create_key(self.priority_queue[0], '')
            text = self.padding(self.tree + self.create_compressed_text(text))
            output.write(int(text, 2).to_bytes(len(text) // 8, byteorder='big'))            
            

Main('me.txt')