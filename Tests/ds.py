import serial
import time

porta = serial.Serial("/dev/ttyAMA0", 9600)
while True:
    strin = 'A'
    porta.write(str(strin))
    resp = porta.read(15)
    print(resposta)
    time.sleep(1)
