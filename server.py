import socket

sock = socket.socket()
sock.bind(('', 8888))
sock.listen(1)
while True:
    client, addr = sock.accept()
    client.send('Hello world')
    client.close()
