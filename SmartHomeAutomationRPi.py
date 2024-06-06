import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)


motion_sensor_pin = 11
led_pin = 12


GPIO.setup(motion_sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        if GPIO.input(motion_sensor_pin):
            print("Motion detected!")
            GPIO.output(led_pin, GPIO.HIGH)  
            time.sleep(1)
        else:
            GPIO.output(led_pin, GPIO.LOW) 
            time.sleep(0.1) 

except KeyboardInterrupt:
    GPIO.cleanup() 
