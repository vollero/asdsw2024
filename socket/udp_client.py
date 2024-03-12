import socket
from sys import argv

ServerIP     = '127.0.0.1'
ServerPORT   = int(argv[1])
bufferSize   = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(str.encode('Questo è il messaggio del Client'), (ServerIP, ServerPORT))
mess, addr = UDPClientSocket.recvfrom(bufferSize) 

print('C: Messaggio da parte del server: {}'.format(mess.decode('utf-8')))
