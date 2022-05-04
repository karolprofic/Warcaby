import socket, pickle

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

board_arr_white = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [1] # Który gracz ma ruch
]
board_arr_black = [
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

print('Nawiązywanie połączenia')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

# Komunikat powitalny
Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))

while True:
    Input = input('Podaj 1 aby zasymulować ruch białymi lub 2 dla czarnych: ')

    if(int(Input) == 1):
        # Wysłanie tablicy
        Array_pickled = pickle.dumps(board_arr_white)
        ClientSocket.send(Array_pickled)
        # Odebranie tablicy
        Response = ClientSocket.recv(1024)
        Array_pickled = pickle.loads(Response)
        print(Array_pickled)
    elif(int(Input) == 2):
        # Wysłanie tablicy
        Array_pickled = pickle.dumps(board_arr_black)
        ClientSocket.send(Array_pickled)
        # Odebranie tablicy
        Response = ClientSocket.recv(1024)
        Array_pickled = pickle.loads(Response)
        print(Array_pickled)
    else:
        print('Podałeś złe dane!')


ClientSocket.close()