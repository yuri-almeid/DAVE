import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)

def on(pin):
    gpio.output(pin, gpio.HIGH)

def off(pin):
    gpio.output(pin, gpio.LOW)

while True:
    say = input('say: ')

    if say == '11 on':
        on(11)
    elif say == '11 off':
        off(11)
    elif say == '12 on':
        on(12)
    elif say == '12 off':
        off(12)
    elif say == 'exit':
        break
    else:
        print('error')
gpio.cleanup()
