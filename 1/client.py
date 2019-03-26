from threading import Thread
import socket
import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 9891

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("READY", (SERVER_IP, SERVER_PORT))
counter=True

def getImage():
    while True:
        data, addr = sock.recvfrom(1024)
        if(data[0:5]=="START"):
            print data[6:]
            fp = open(data[6:],'wb+')
        elif(data=="FINISH"):
            fp.close()
        elif(data=="ENDING"):
            break
        else:
            print "Block ", len(data), data[0:10]
            fp.write(data)

while counter==True:
    data, addr = sock.recvfrom(1024)
    if(data=="SENDING"):
        getImage()
        counter = 0
