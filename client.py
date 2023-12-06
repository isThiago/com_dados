import socket
from message import *


print('Conectar a…\n> ', end = '')
HOST = socket.gethostbyname(input())
PORT = 51234
with socket.socket() as s:
    s.connect((HOST, PORT))
    print(f'Conectado a ip: {HOST}, port: {PORT}.\n> ', end = '')
    written = input()
    encrypted = encrypt(written)
    binary = to_binary(encrypted)
    signal = encode_2b1q(binary)
    s.sendall(send_signal(signal))
    print(f'Escrita: {written}\n' \
          + f'Criptografada: {encrypted}\n' \
          + f'Dados digitais: {binary}\n' \
          + f'Sinal digital: {signal}')
    plot_graph(signal, 'Sinal Enviado')
print('Conexão encerrada.')
