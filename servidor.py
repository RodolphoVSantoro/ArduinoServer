import sys
import socket
from _thread import *

HOST = ''
PORTA = 5000


def Ouvir_thread(conn):
    while 1:
        data = conn.recv(1024)
        reply = data.decode('UTF-8')
        print("Cliente Enviou: " + reply)
        print("\nEnvie uma mensagem para o cliente:")
        #confirmacao = "Mensagem Recebida com sucesso!(Mensagem:" + reply + ")"
        #conn.send(confirmacao.encode('UTF-8'))
        if not data:
            break
    conn.close()
    print(msg)
    print("Envie uma mensagem para o cliente:")


def Enviar_thread(conn, msg):
    if msg != "":
        mensagem = "Servidor enviou:" + msg
        conn.send(mensagem.encode('UTF-8'))
        print("Envie uma mensagem para o cliente:")


print("Tentando criar servidor com todos as interfaces! \nUtilizando a porta:\n" + str(PORTA))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORTA))
except socket.error as msg:
    print("Erro ao criar socket. Erro de codigo:" + str(msg[0]) + " Message " + msg[1])
    sys.exit()
print("Socket criado")

s.listen(10)
print("Socket esperando conexão")
conn, addr = s.accept()
print("Conectado com: " + addr[0] + ':' + str(addr[1]) + "\n")
msg = ""
msg = input("Envie uma mensagem para o cliente:\n")
start_new_thread(Ouvir_thread, (conn,))
while msg != '0':
    msg = input()
    start_new_thread(Enviar_thread, (conn, msg,))
s.close()
