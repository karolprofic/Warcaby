import socket, pickle, sys, threading, os
from _thread import *

Lock = threading.Lock()
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
BoardArray = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [2] # Który gracz ma ruch
]

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Oczekiwanie na graczy:')
ServerSocket.listen(2)

def threaded_client(connection):
    global BoardArray
    global Lock
    connection.send(str.encode('Połączenie nawiązane!'))
    while True:
        # Odebranie tablicy
        Response = connection.recv(2096)
        RecivedArray = pickle.loads(Response)
        Lock.acquire()
        if(RecivedArray[8][0] == BoardArray[8][0]):
            BoardArray = RecivedArray
            if(BoardArray[8][0] == 1):
                BoardArray[8][0] = 2
            else:
                BoardArray[8][0] = 1
            print(BoardArray)
        Lock.release()
        if not Response:
            break

        # Wysłanie tablicy
        ArrayPickled = pickle.dumps(BoardArray)
        connection.sendall(ArrayPickled)

    connection.close()


while True:
    Client, Address = ServerSocket.accept()
    print('Połączono z: ' + Address[0] + ':' + str(Address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Utworzenie wątku: ' + str(ThreadCount))
ServerSocket.close()