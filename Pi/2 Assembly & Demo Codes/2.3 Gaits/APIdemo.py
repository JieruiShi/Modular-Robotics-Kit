import SpiderG
import time

#forward backward turnleft turnright StandUp StayLow Lean-L Lean-R  Lean-F Lean-H

SpiderG.move_init()
time.sleep(1)
SpiderG.walk('Lean-L')
time.sleep(1)
SpiderG.walk('Lean-R')
time.sleep(1)
SpiderG.walk('Lean-F')
time.sleep(1)
SpiderG.walk('Lean-H')
time.sleep(1)
SpiderG.walk('StandUp')
time.sleep(1)
SpiderG.walk('StayLow')
time.sleep(1)
SpiderG.walk('forward')
time.sleep(1)
SpiderG.walk('backward')
time.sleep(1)
SpiderG.walk('turnleft')
time.sleep(1)
SpiderG.walk('turnright')
time.sleep(1)
SpiderG.servoStop()