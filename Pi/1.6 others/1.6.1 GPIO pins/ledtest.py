import gpiozero
import time

led = gpiozero.LED(17)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)