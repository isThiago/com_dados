import socket
from message import *


HOST = socket.gethostbyname(socket.gethostname())
PORT = 51234
with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Aguardando conexão…')
    conn, addr = s.accept()
    with conn:
        print(f'Conectado a ip: {addr[0]}, port: {addr[1]}.\n' \
              + 'Aguardando mensagem…')
        is_connected = True
        while is_connected:
            data = conn.recv(1024)
            if not data:
                is_connected = False
            else:
                signal = receive_signal(data)
                binary = decode_2b1q(signal)
                text = to_text(binary)
                decrypted = decrypt(text)
                print(f'Sinal digital: {signal}\n' \
                      + f'Dados digitais: {binary}\n' \
                      + f'Texto: {text}\n' \
                      + f'Descriptografada: {decrypted}')
                plot_graph(signal, 'Sinal Recebido')
    print('Conexão encerrada.')
