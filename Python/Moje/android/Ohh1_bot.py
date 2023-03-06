from time import sleep, time
import copy
from PIL import Image
import numpy
from ppadb.client import Client

columns = (150, 400, 650, 900)
fourmode = (345, 1150)
rows = (850, 1100, 1350, 1600) # for an 1080x2400 phone and for 4x4 mode


def getDevice():
    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()

    if len(devices) == 0:
        print('no devices attached')
        quit()

    return devices[0]

def createBoard(device):

    image = device.screencap()
    with open('screen.png', 'wb') as f:
        f.write(image)

    image = Image.open('screen.png')
    image = numpy.array(image, dtype=numpy.uint8)

    colours = {42: 0, 255: 1, 0: 2} #gray, yellow, blue

    board = []
    for h in rows:
        board.append([colours[image[h, w, 0]] for w in columns])

    return board

def solveBoard(board):
    for x in range(5):

        for row in range(len(board)):
            for column in range(len(board[0]) -2):

                if board[row][column] != 0 and board[row][column] == board[row][column +2] and board[row][column +1] == 0:
                    if board[row][column] == 1:
                        board[row][column +1] = 2
                    else:
                        board[row][column +1] = 1

                if board[row][column] != 0 and board[row][column] == board[row][column +1] and board[row][column +2] == 0:
                    if board[row][column] == 1:
                        board[row][column +2] = 2
                    else:
                        board[row][column +2] = 1

            if board[row].count(0) == 2:
                empty = []
                for column in range(len(board)):
                    if board[row][column] == 0:
                        empty.append(column)

                x = copy.deepcopy(board)
                
                x[row][empty[0]] = 1
                x[row][empty[1]] = 2
                if x[row] in board:
                    board[row][empty[0]] = 2
                    board[row][empty[1]] = 1
                else:
                    x[row][empty[0]] = 2
                    x[row][empty[1]] = 1
                    if x[row] in board:
                        board[row][empty[0]] = 1
                        board[row][empty[1]] = 2

            if board[row].count(1) == len(board[0]) /2:
                for column in range(len(board[0])):
                    if board[row][column] == 0:
                        board[row][column] = 2

            if board[row].count(2) == len(board[0]) /2:
                for column in range(len(board[0])):
                    if board[row][column] == 0:
                        board[row][column] = 1
        
        for row in range(len(board) -2):
            for column in range(len(board[0])):

                if board[row][column] != 0 and board[row][column] == board[row +2][column] and board[row +1][column] == 0:
                    if board[row][column] == 1:
                        board[row +1][column] = 2
                    else:
                        board[row +1][column] = 1

                if board[row][column] != 0 and board[row][column] == board[row +1][column] and board[row +2][column] == 0:
                    if board[row][column] == 1:
                        board[row +2][column] = 2
                    else:
                        board[row +2][column] = 1

        for column in range(len(board)):
            count = [0, 0, 0]
            for row in range(len(board)):
                count[board[row][column]] += 1

            if count[1] == len(board) /2:
                for row in range(len(board)):
                    if board[row][column] == 0:
                        board[row][column] = 2

            elif count[2] == len(board) /2:
                for row in range(len(board)):
                    if board[row][column] == 0:
                        board[row][column] = 1

def inputSolution(board, device, ogboard):
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 1 and ogboard[row][column] == 0:
                tap(columns[column], rows[row], device)
            elif board[row][column] == 2 and ogboard[row][column] == 0:
                tap(columns[column], rows[row], device)
                tap(columns[column], rows[row], device)

def tap(column, row, device):
    device.shell(f'input tap {column} {row}')

def main():

    for x in range(1000):
        device = getDevice()
        tap(fourmode[0], fourmode[1], device)
        sleep(0.4)
        board = createBoard(device)
        ogboard = copy.deepcopy(board)
        solveBoard(board)
        inputSolution(board, device, ogboard)
        sleep(4)
    

main()

