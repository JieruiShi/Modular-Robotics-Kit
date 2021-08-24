import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

while True:
    for i in range(0,100):
        pwm.set_pwm(0, 0, (200+2*i))
        time.sleep(0.05)
    for i in range(0,100):
        pwm.set_pwm(0, 0, (400-2*i))
        time.sleep(0.05)