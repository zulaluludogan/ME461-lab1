import board
import digitalio
import time
import pwmio
from adafruit_debouncer import Debouncer


leds = []


def define_leds(leds):
    if len(leds) == 0:
        leds.append(digitalio.DigitalInOut(board.GP2))
        leds.append(digitalio.DigitalInOut(board.GP3))
        leds.append(digitalio.DigitalInOut(board.GP4))
        leds.append(digitalio.DigitalInOut(board.GP5))
        leds.append(digitalio.DigitalInOut(board.GP6))
        leds.append(digitalio.DigitalInOut(board.GP7))
        leds.append(digitalio.DigitalInOut(board.GP8))
        leds.append(digitalio.DigitalInOut(board.GP9))

        for led in leds:
            led.direction = digitalio.Direction.OUTPUT

    return leds


def ByteDisplay(val=0):
    global leds
    leds = define_leds(leds)

    for led in leds:
        led.value = False

    for i in range(7, -1, -1):
        print(i)
        if val // (2 ** i) != 0:
            val -= 2 ** i
            leds[i].value = True


def Volta(N=1, speed=0.1):
    
    global leds
    leds = define_leds(leds)

    while N != 0:
        for led in leds:
            led.value = True
            time.sleep(speed)
            led.value = False
        for i in range(1, len(leds)):
            leds[len(leds) - i].value = True
            time.sleep(speed)
            leds[len(leds) - i].value = False
        N = N - 1

pwms = []

def define_pwms(pwms):
    if len(pwms) == 0:
        pwms.append(pwmio.PWMOut(board.GP2))
        pwms.append(pwmio.PWMOut(board.GP3))
        pwms.append(pwmio.PWMOut(board.GP4))
        pwms.append(pwmio.PWMOut(board.GP5))
        pwms.append(pwmio.PWMOut(board.GP6))
        pwms.append(pwmio.PWMOut(board.GP7))
        pwms.append(pwmio.PWMOut(board.GP8))
        pwms.append(pwmio.PWMOut(board.GP9))
    return pwms

def Snake(L=3, speed=0.5):
    global pwms
    pwms = define_pwms(pwms)
    
    brigthness = []
    
    for b in range(65535,150,-int(60000/(L-1))):
        brigthness.append(b)
    
    for i in range(len(pwms)+L):
        for l in range(L):
            if i-l>=0 and i-l<=len(pwms)-1:
                pwms[i-l].duty_cycle = brigthness[l]
        time.sleep(speed)
        
        for l in range(L,1,-1):
            if i-l>=0 and i-l<=len(pwms)-1:
                pwms[i-l].duty_cycle = 0
    
    for i in range(len(pwms)+L):
        for l in range(L):
            if i-l>=0 and i-l<=len(pwms)-1:
                pwms[(len(pwms)-1)-(i-l)].duty_cycle = brigthness[l]
        time.sleep(speed)
        
        for l in range(L,1,-1):
            if i-l>=0 and i-l<=len(pwms)-1:
                pwms[len(pwms)-1-(i-l)].duty_cycle = 0

def button_counter():
    global leds
    leds = define_leds(leds)
    
    button = digitalio.DigitalInOut(board.GP22)
    button.switch_to_input(pull=digitalio.Pull.DOWN)
    
    switch = Debouncer(button, interval=0.05)
    while True:
        if switch.value:
            print('not pressed')
        else:
            print('pressed')
    

