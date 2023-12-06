import socket

HOST = "192.168.0.76"
PORT = 51234

with socket.socket() as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world!")
    data = s.recv(1024)

print(f"Received {data}")
