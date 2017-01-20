import socket

HOST = 'localhost'
PORT = 50008

connection_pool = dict()


#def listen():
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print 'Listening on {}:{}'.format(HOST, PORT)
while True:
    conn, addr = s.accept()
    print 'Connected by', addr
    print addr
    while conn:
        data = conn.recv(1024)
        if addr not in connection_pool.keys():
            connection_pool[addr] = data
            print connection_pool
        elif data is not None:
            print data
            conn.sendall(data)
conn.close()

