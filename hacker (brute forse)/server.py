import socket

app = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
app.bind(('127.0.0.1', 8000))
app.listen(5)


while True:
    (client, (ip, port)) = app.accept()
    print('client connected', ip, port)

    while True:
        data = client.recv(1024)
        if not data:
            break
        if data.decode() == 'abcd':
            client.send('You connected to PyWorkShop!!'.encode())
        else:
            client.send('WRONG'.encode())
    client.close()