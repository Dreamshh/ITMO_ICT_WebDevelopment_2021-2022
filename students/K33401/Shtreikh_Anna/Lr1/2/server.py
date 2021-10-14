import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 9900))
sock.listen(10)

conn, addr = sock.accept()
a = int(conn.recv(1024).decode('utf-8'))
b = int(conn.recv(1024).decode('utf-8'))
h = int(conn.recv(1024).decode('utf-8'))
s = (((a+b)/2)*h)
data = str(s)

conn.send(data.encode("utf-8"))
conn.close()
