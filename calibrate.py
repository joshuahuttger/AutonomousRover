from pyfirmata import Arduino, util
import time
print 'attaching to adruino device'
board = Arduino('/dev/ttyACM0')


print 'get motor pin(9)'
print 'get steering pin(10)'
motor = board.get_pin('d:9:s')
steering = board.get_pin('d:10:s')



throttleMap = dict()
throttleVals = [80       ,90    ,100]
throttleList = ['REVERSE','STOP','FORWARD','STOP'] 
for i in range(3):
        throttleMap[throttleList[i]] = throttleVals[i]

print 'calibrate ESC'
motor.write(throttleMap['STOP'])
steering.write(throttleMap['STOP'])
time.sleep(10)



for i in range(20):
	i += 1
	throttleString = throttleList[i%4]
	print 'throttle string:',throttleString
	print 'throttle angle :',throttleMap[throttleString]
	motor.write(throttleMap[throttleString])
        steering.write(100) 

	
	board.digital[13].write(i%2)
	time.sleep(2)

	
motor.write(throttleMap['STOP'])
