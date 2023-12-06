import socket

HOST = "192.168.0.76"
PORT = 51234

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        is_connected = True
        while is_connected:
            data = conn.recv(1024)
            if not data:
                is_connected = False
            conn.sendall(data)
