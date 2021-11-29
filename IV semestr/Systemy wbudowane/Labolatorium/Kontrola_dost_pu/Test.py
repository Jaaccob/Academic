import socket

socket_client = socket.socket()

socket_client.bind(('192.168.0.177', 5000))
socket_client.listen(0)
socket_client.connect()
while True:
    client, addr = socket_client.accept()
    temp = str(client)
    print(temp)