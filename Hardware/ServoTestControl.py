### temporary raspberry pi servo motor control test code
###


import RPi.GPIO as GPIO  # for to call GPIO module 
from time import sleep   # for sleep function

GPIO.setmode(GPIO.BCM)   # to set up the rule of GPIO pin's numbers


# to set up the servo motor's GPIO pin number
servo_1 =
servo_2 =
servo_3 =
servo_4 =


# to set up servo motor's pin to output
GPIO.setup(servo_1, GPIO.OUT)
GPIO.setup(servo_2, GPIO.OUT)
GPIO.setup(servo_3, GPIO.OUT)
GPIO.setup(servo_4, GPIO.OUT)


# to set up servo motor pin PWM mode 50Hz
servo_1 = GPIO.PWM(servo_1, 50)
servo_2 = GPIO.PWM(servo_2, 50)
servo_3 = GPIO.PWM(servo_3, 50)
servo_4 = GPIO.PWM(servo_4, 50)


# to set up the initial value of servo motor to 0
servo_1.start(0)
servo_2.start(0)
servo_3.start(0)
servo_4.start(0)


servo_min_duty = 1     # minimum duty rate 1
servo_max_duty = 13    # maximum duty rate 13


# function of which motor move what degree
def set_servo_degree(servo_num, degree):
    # to set up degree minimum 0, maximum 180
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0


    # to calculate angle to duty
    duty = servo_min_duty + (degree * (servo_max_duty - servo_min_duty) / 180.0)

    # to apply calculated duty to motor
    if servo_num == 1:
        servo_1.ChangeDutyCycle(duty)
    elif servo_num == 2:
        servo_2.ChangeDutyCycle(duty)
    elif servo_num == 3:
        servo_3.ChangeDutyCycle(duty)
    elif servo_num == 4:
        servo_4.ChangeDutyCycle(duty)


try:
    while True:
        for ii in range(0, 180, 5):
            set_servo_degree(1, ii)
            set_servo_degree(2, 180-ii)
            set_servo_degree(3, ii)
            set_servo_degree(4, 180-ii)
            sleep(0.1)
        for iin in reversed(range(0, 180, 5)):
            set_servo_degree(1, ii)
            set_servo_degree(2, 180-ii)
            set_servo_degree(3, ii)
            set_servo_degree(4, 180-ii)
            sleep(0.1)

finally:
    GPIO.cleanup()




