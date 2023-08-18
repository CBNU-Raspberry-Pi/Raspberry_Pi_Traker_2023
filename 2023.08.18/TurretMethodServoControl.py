## servo motor control code
## using 2 servo motors(turret method)
## algorithm : motors will move until each coordinates become 0


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

servo_x_pin =
servo_y_pin =

# setting motor to output
GPIO.setup(servo_x_pin, GPIO.OUT)
GPIO.setup(servo_y_pin, GPIO.OUT)

# PWM mode, 50Hz (sg90 motor's own value)
servo_x = GPIO.PWM(servo_x_pin, 50)
servo_y = GPIO.PWM(servo_y_pin, 50)

# setting motor's inintial state 0
servo_x.start(0)
servo_y.start(0)

# function of control which motor and move how many degree
def set_servo_degree(servo_num, degree):
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0

    # calculate degree to duty
    duty = servo_min_duty \
    + (degree * (servo_max_duty - servo_min_duty) / 180.0)

    if servo_num == 1:
        servo_x.ChangeDutyCycle(duty)
        # x-direction motor is number 1
    elif servo_num == 2:
        servo_y.ChangeDutyCycle(duty)
        # y-direction motor is number 2


global x_degree, y_degree
x_degree, y_degree = 90, 90

# main servo control function
def servo_control(x_axis, y_axis):
    try:
        global x_degree, y_degree
        
##        set_servo_degree(1, 90)
##        set_servo_degree(2, 90)

        if x_axis > 0:
            x_degree = x_degree + 1
        elif x_axis < 0:
            x_degree = x_degree - 1
        if y_axis > 0:
            y_degree = y_degree + 1
        elif y_axis < 0:
            y_degree = y_degree - 1


        set_servo_degree(1, x_degree)
        set_servo_degree(2, y_degree)


    finally:
        GPIO.cleanup()


        







