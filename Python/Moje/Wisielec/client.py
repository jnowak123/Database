import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(('127.0.0.1', 65432))
    data = s.recv(1024).decode()
    if data == '1':
        word = input('You are player 1 \nchoose a word ')
        s.send(word.encode())
    else:
        print('You are player 2 \nyou will be guessing')
    print(s.recv(1024).decode())

    
    while s.recv(1024).decode() == '1':
        if data == '0':
            s.send(input('type in your guess ').encode())
        print(s.recv(1024).decode())

    print(s.recv(1024).decode())