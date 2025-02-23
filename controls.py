import pyfirmata
from time import sleep
board = pyfirmata.Arduino('/dev/ttyACM0')

iter8 = pyfirmata.util.Iterator(board)
iter8.start()

motor = board.get_pin('d:9:s')
steer = board.get_pin('d:10:s')
motor.write(0)
steer.write(0)
def move_servo(angle,servo,delay):
    val = int(servo.read())
    diff = 0
    if val < angle:
        diff = 1
    else:
        diff = -1
    while angle != servo.read():
        val += diff
        sleep(delay)
        print("angle = "+str(val))
        servo.write(int(val))

def steerSet(angle):
    print("setting steer angle: "+str(angle))
    move_servo(angle,steer,.1)
    print("steering set: "+str(angle))
def motorSet(angle):
    print("setting motor angle: "+str(angle))
    move_servo(angle,motor,.1)
    print("motor set: "+str(angle))

count = 0
while True:
    print("count = "+str(count))
    if count % 2 == 0:
        motorSet(180,.1)
        steerSet(180,.1)
    else:
        motorSet(0,.1)
        steerSet(0,.1)
    count += 1
