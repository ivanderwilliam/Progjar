from threading import Thread
import socket
import os

TARGET_IP = "127.0.0.1"
TARGET_PORT = 9891

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((TARGET_IP, TARGET_PORT))
files=["download.png","g.png"]

def sendImage(CLIENT_IP, CLIENT_PORT):
   addr = CLIENT_IP, CLIENT_PORT
   sock.sendto("SENDING" , (addr))
   for name in files:
      sock.sendto("START {}" . format(name) , (addr))
      size = os.stat(name).st_size
      fp = open(name,'rb')
      tes = fp.read()
      count=0
      for test in tes:
         sock.sendto(test, (addr))
         count = count + 1
         print "\r Sent {} of {} " . format(count,size)
      sock.sendto("FINISH", (addr))
      fp.close()
   sock.sendto("ENDING", (addr))


while True:
   print "Connecting"
   data, addr = sock.recvfrom(1024)
   if(data=="READY"):
      thread = Thread(target=sendImage, args=(addr))
      thread.start()
