import socket

sock = socket.socket()
sock.connect(('localhost', 8888))
data = sock.recv(1024)
tm = sock.recv(1024)
sock.close()
print tm
