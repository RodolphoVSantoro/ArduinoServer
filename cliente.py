import sys
import socket
from _thread import *

host = "127.0.0.1"
porta = 2000
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alvo = (host, porta)
conn.connect(alvo)


def Ouvir_thread(conn):
    while 1:
        data = conn.recv(1024)
        reply = data.decode('utf-8')
        print(reply)
        if not reply:
            break
        print("Envie uma mensagem para o servidor:")

    conn.close()
    print(msg)


print("Para sair use CRTL+X")
start_new_thread(Ouvir_thread, (conn,))
msg = ""
msg = input("Envie uma mensagem para o servidor:\n")
while msg != '\x18':
    conn.send(msg.encode('UTF-8'))
    msg = input()
conn.close()
