class Page:

    def __init__(self, page, children, colour, parent = None):
        self.page = page
        self.children = children
        self.colour = colour
        self.parent = parent

book = []

def validchild(node):
    for i in node.children:
        if book[i].colour == 0:
            return True
    return False

def notfinished():
    for child in book[1:]:
        if child.colour == 0 and validchild(child):
            return child
    return False
    
def main():

    n, m = map(int, input().split())
    book_dict = {}
    [book_dict.update({x:[]}) for x in range(n+1)]
    for dummy in range(m):
        x, y = map(int, input().split())
        if y not in book_dict[x]:
            book_dict[x].append(y)

    [book.append(Page(x, book_dict[x], 0)) for x in book_dict]
    stack = [book[1]]
    book[1].colour = 1
    lastparent = None

    while stack:
        z = stack.pop(-1)
        z.parent = lastparent
        z.colour = 1
        for i in z.children:
            if book[i].colour == 1:
                return 'DEJA VU'
            elif book[i].colour == 0:
                stack.append(book[i])
        lastparent = z
        while not z.children or not validchild(z): #or 0 not in z.children:
            z.colour = 2
            if z.parent:
                z = z.parent
            if not z.parent and not validchild(z):
                z.colour = 2
                x = notfinished()
                if not x:
                    return 'OK'
                else:
                    z = x
                    stack = [x]
                    lastparent = None
    return 'OK'

print(main())