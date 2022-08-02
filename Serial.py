import serial
import time

print("conectando ao arduino")
ser = serial.Serial('COM3', 9600)
time.sleep(1)
arduinoOUT = -1
while arduinoOUT!=0:
    arduinoOUT = bytes(input("msg do servidor:\n"),"ASCII")
    ser.write(arduinoOUT)
    arduinoIn = ser.readline().decode("ASCII")
    print ("Recebido "+str(arduinoOUT))
