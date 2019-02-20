import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost',10000)

print('starting up on',server_address)

sock.bind(server_address)

sock.listen(1)


while True:
    print('waiting for a conenction')
    connection, client_address = sock.accept()

    print('conenction from',client_address)

    while True:

        data = connection.recv(32)
        if data :
            print('sending data back to the client')
            connection.sendall('--->'+data)

        else:
            print('no more data from',client_address)
            break

    connection.close()

