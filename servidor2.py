import sys
import socket
import serial
import time

def cvrt(str):
    try:
        int(str)
    except:
        return 0
    return int(str)

def process_dados_cs(m):
    if cvrt(m) == 0:
        msg = "saindo do programa"
    elif cvrt(m) == 1:
        msg = "Voce pediu o menu 1"
    elif cvrt(m) == 2:
        msg = "Voce pediu o menu 2"
    elif cvrt(m) == 3:
        msg = "configuracoes"
    else:
        msg = "opcao invalida("+ m +")"
    return msg

HOST = ''
PORTA = 5000

print("conectando com o arduino")
ser = serial.Serial('COM3', 9600)
time.sleep(1)
print("conectado ao arduino na COM3")

print("Tentando criar servidor com todos as interfaces! \nUtilizando a porta:\n" + str(PORTA))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORTA))
except socket.error as msg:
    print("Erro ao criar socket. Erro de codigo:" + str(msg[0]) + " Message " + msg[1])
    sys.exit()
print("Socket criado")

s.listen(10)
print("Socket esperando conexao")
conn, addr = s.accept()
print("Conectado com: " + addr[0] + ':' + str(addr[1]) + "\n")
while 1:
    #espera mensagem vinda do c#
    menu = "Digite 1 para menu 1, 2 para menu 2, 3 para configuracoes:\n4 para ler sensores e 0 para sair\n"
    conn.send(menu.encode('UTF-8'))
    csdata = conn.recv(1024)

    #demonstra no log o que recebeu do c#
    csIn = csdata.decode('UTF-8')
    print("Cliente Enviou: " + csIn + "\n")
    msg = process_dados_cs(csIn)

    #envia resposta ao c#
    msg = msg+"\n"
    conn.send(msg.encode('UTF-8'))

    if(len(csIn)==1):
        #envia comando ao arduino
        arduinoOut = bytes(csIn,"ASCII")
        ser.write(arduinoOut)

        #demonstra no log se o arduino fez algo
        arduinoIn = ser.readline().decode("ASCII")
        print("Arduino Executou : "+arduinoIn)
    print("X---------------X\n")
s.close()
