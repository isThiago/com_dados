import socket
from message import *


print('Conectar a…\n> ', end = '')
HOST = socket.gethostbyname(input())
PORT = 51234
with socket.socket() as s:
    s.connect((HOST, PORT))
    print(f'Conectado a ip: {HOST}, port: {PORT}.')
    print('> ', end = '')
    written = input()
    print(f'Escrita: {written}')
    encrypted = encrypt(written)
    print(f'Criptografada: {encrypted}')
    binary = to_binary(encrypted)
    print(f'Dados digitais: {binary}')
    signal = encode_2b1q(binary)
    print(f'Sinal digital: {signal}')
    s.sendall(send_signal(signal))
    plot_graph(signal, 'Sinal Enviado')
print('Conexão encerrada.')
