import socket
from sys import argv

localIP     = '127.0.0.1'
localPORT   = int(argv[1])
bufferSize  = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPORT))

print("S: UDP SERVER UP AND RUNNING!")

while True:
    mess, addr = UDPServerSocket.recvfrom(bufferSize)

    print('S: Messaggio ricevuto da {}'.format(addr))
    print('S: Messaggio: {}'.format(mess.decode('utf-8')))

    UDPServerSocket.sendto(str.encode('Grazie del messaggio!'), addr)
