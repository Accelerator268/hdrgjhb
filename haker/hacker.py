import socket


password = input()
ip, port = '127.0.0.1', 7845


my_socket = socket.socket()
my_socket.connect((ip, port))
my_socket.send(password.encode())


response = my_socket.recv(1024).decode()
print(response)