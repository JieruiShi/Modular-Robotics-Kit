import RPIservo
import time

sc = RPIservo.ServoCtrl()
sc.start()

while True:
    sc.singleServo(0,1,1)
    time.sleep(1)
    sc.stopWiggle()
    
    sc.singleServo(0,-1,1)
    time.sleep(1)
    sc.stopWiggle()