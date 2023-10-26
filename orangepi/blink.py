import time
import board
import digitalio

print("hello blinky!")

led = digitalio.DigitalInOut(board.PA12)
led.direction = digitalio.Direction.OUTPUT
led1 = digitalio.DigitalInOut(board.PA11)
led1.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(0.5)
