import socket
import random

players = []
connlist = []
lives = 8
 
def sendtoplayers(word):
    for player in connlist:
        player.send(word.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 65432))
    for player in range(2):
        s.listen()
        conn, addr = s.accept()
        connlist.append(conn)
    ind = random.randint(0, 1)
    indtwo = ind -1
    connlist[ind].send(b'1') 
    connlist[indtwo].send(b'0')
    word = connlist[ind].recv(1024).decode()
    guesslist = ['-'*len(word)]
    sendtoplayers(', '.join(guesslist))
    
    game = True
    while lives != 0 and game:
        sendtoplayers('1')
        letter = connlist[indtwo].recv(1024).decode()
        if letter in word:
            for l, i in enumerate(word):
                if l == letter:
                    guesslist[i] = letter
            if '-' not in guesslist:
                game = False
            sendtoplayers('Correct guess! \n' + ', '.join(guesslist))
        else:
            lives -= 1
            sendtoplayers('Incorrect guess \n' + ', '.join(guesslist))
    sendtoplayers('0')
    
    if lives == 0:
        connlist[ind].send('You win'.encode())
        connlist[indtwo].send('You lose'.encode())
    else:
        connlist[ind].send('You lose'.encode())
        connlist[indtwo].send('You win'.encode())
