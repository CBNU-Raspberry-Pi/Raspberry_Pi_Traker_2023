


import RPi.GPIO as GPIO     # 라즈베리파이 GPIO 관련 모듈을 불러옴
from time import sleep      # time 라이브러리의 sleep함수 사용

GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정

### 이부분은 아두이노 코딩의 setup()에 해당합니다
### 각 방향에 해당하는 서보모터의 GPIO 핀 숫자 기입
servo_up_pin =                      # 서보1 핀은 라즈베리파이 GPIO 번핀으로 
servo_down_pin =                    # 서보2 핀은 라즈베리파이 GPIO 번핀으로 
servo_right_pin =                   # 두 변수에 꽂은 핀 숫자 기입
servo_left_pin =


# 각 서보모터의 핀을 출력으로 설정
GPIO.setup(servo_up_pin, GPIO.OUT)  # 서보1 핀을 출력으로 설정 
GPIO.setup(servo_down_pin, GPIO.OUT)  # 서보2 핀을 출력으로 설정 
GPIO.setup(servo_right_pin, GPIO.OUT)
GPIO.setup(servo_left_pin, GPIO.OUT)


servo_up = GPIO.PWM(servo_up_pin, 50)  # 서보1 핀을 PWM 모드 50Hz로 사용
servo_down = GPIO.PWM(servo_down_pin, 50)  # 서보2 핀을 PWM 모드 50Hz로 사용
servo_right = GPIO.PWM(servo-right_pin, 50)   # 서보모터의 사양을 보고 PWM 모드 헤르츠 맞추기
servo_left = GPIO.PWM(servo_left_pin, 50)  # 서보모터 SG90의 경우 50Hz이므로 50으로 설정


# 각 방향의 서보모터의 초기값을 0으로 설정
servo_up.start(0)  # 서보1의 초기값을 0으로 설정
servo_down.start(0)  # 서보2의 초기값을 0으로 설정
servo_right.start(0)
servo_left.start(0)


servo_min_duty = 1               # 최소 듀티비를 1으로
servo_max_duty = 13              # 최대 듀티비를 13로


def set_servo_degree(servo_num, degree): # 몇번째 서보모터를 몇도만큼 움직일지 결정하는 함수
    # 각도는 최소0, 최대 180으로 설정
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0

    # 각도에 따른 듀티비를 환산
    duty = servo_min_duty+(degree*(servo_max_duty-servo_min_duty)/180.0)

    # 환산된 듀티비를 서보1 혹은 2에 적용
    if servo_num == 1:
        # up servo is no. 1
        servo_up.ChangeDutyCycle(duty)
    elif servo_num == 2:
        # down servo is no. 2
        servo_down.ChangeDutyCycle(duty)
    elif servo_num == 3:
        # right servo is no. 3
        servo_right.ChangeDutyCycle(duty)
    elif servo_num == 4:
        # left servo is no. 4
        servo_left.ChangeDutyCycle(duty)


### 서보모터 제어하는 함수
def servo_control(hmm):
    try:
        # 초기 서보모터의 상태를 90도로 하고 시작
        set_servo_degree(1, 90)      
        set_servo_degree(2, 90)
        set_servo_degree(3, 90)
        set_servo_degree(4, 90)        
        if x == 1:
            set_servo_degree(3, ii)   # ii에 조정한 각도 넣을 것
            set_servo_degree(4, ii)
        elif x == 2:
            set_servo_degree(3, jj)   # jj에 조정한 각도 넣을 것
        elif y == 1:
            set_servo_degree(1, ii)
        elif y == 2:
            set_servo_degree(1, jj)
        elif x == -1:
            set_servo_degree(4, -ii)   
        elif x == -2:
            set_servo_degree(4, -jj)
        elif y == -1:
            set_servo_degree(2, -ii)
        elif y == -2:
            set_servo_degree(2, -jj)
        elif x == 0:
            set_servo_degree(1, 0)
            set_servo_degree(3, 0)
        elif y == 0:
            set_servo_degree(2, 0)
            set_servo_degree(4, 0)

            
    ### 이부분은 반드시 추가해주셔야 합니다.
    finally:                                # try 구문이 종료되면
        GPIO.cleanup()                      # GPIO 핀들을 초기화

        




##### 이부분은 반드시 추가해주셔야 합니다.
##finally:                                # try 구문이 종료되면
##    GPIO.cleanup()                      # GPIO 핀들을 초기화

        
