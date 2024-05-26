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
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED
            time.sleep(1)  # Keep the LED on for 1 second
        else:
            GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED
            time.sleep(0.1)  # Poll the motion sensor every 0.1 second

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO pins on exit
