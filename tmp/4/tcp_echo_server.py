import socket
from sys import argv

localIP     = argv[1]
localPORT   = int(argv[2])

TCPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
TCPServerSocket.bind((localIP, localPORT))

print('TCP Server UP ({},{}), waiting for connections ...'.format(localIP, localPORT))
TCPServerSocket.listen()
conn, addr = TCPServerSocket.accept()

print('Client: {}'.format(addr))
while True:
    data = conn.recv(1024)

    if not data:
        break

    print('{}: echo message: {}'.format(addr, data[:-1].decode('utf-8')))
    
    conn.sendall(data)

conn.close()
TCPServerSocket.close()
