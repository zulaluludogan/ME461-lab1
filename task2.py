import board
import digitalio

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

def ByteDisplay(val = 0):
    global leds
    leds = define_leds(leds)

    for i in range(7,-1,-1):
        print(i)   
        if val//(2**i)!=0:
            val -= 2**i
            leds[i].value = True