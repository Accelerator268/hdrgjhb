import socket
from string import ascii_lowercase, digits
from itertools import product
from datetime import date


chars = ascii_lowercase + digits
passwords = (opt for i in range(1, 5) for opt in product(chars, repeat = i))

ip, port = '127.0.0.1', 8000
my_socket = socket.socket()
my_socket.connect((ip, port))

while True:
    password = ''.join(next(passwords))
    my_socket.send(password.encode())
    response = my_socket.recv(1024).decode()
    if response == 'You connected to PyWorkShop!!':
        print(password)
        break
data = str(date.today()).split('-')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month = months[int(data[1])-1]
with open('data.txt', 'w', encoding='utf-8') as file:
  file.write('{month} {day}, {year} - {ip}:{port} - {password}'.format(month = month, day = data[-1], year = data[0], ip = ip, port = port, password = password))