import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)

motion_sensor_pin = 11
led_pin = 12

GPIO.setup(motion_sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

motion_detected = False

def monitor_motion():
    global motion_detected
    try:
        while True:
            if GPIO.input(motion_sensor_pin):
                print("Motion detected!")
                motion_detected = True
                GPIO.output(led_pin, GPIO.HIGH)
                time.sleep(1)
            else:
                motion_detected = False
                GPIO.output(led_pin, GPIO.LOW)
                time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()

def start_motion_detection():
    threading.Thread(target=monitor_motion, daemon=True).start()

start_motion_detection()
