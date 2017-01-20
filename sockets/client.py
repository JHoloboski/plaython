import socket

HOST = 'localhost'
PORT = 50008
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = raw_input('Enter your username: ')
s = socket.create_connection((HOST, PORT))
s.sendall(name)
while True:
    message = raw_input('')
    if message == "/exit":
        s.close()
        break
    s.sendall(message)
    data = s.recv(1024)
