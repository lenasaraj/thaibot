import RPi.GPIO as GPIO
import time

# Define motor pins

#M2
LEFT_IN1 = 20
LEFT_IN2 = 21
LEFT_PWM = 19

#M3
RIGHT_IN1 = 24
RIGHT_IN2 = 25
RIGHT_PWM = 12

#M1
LEFT_IN3_BACK = 22
LEFT_IN4_BACK = 23
LEFT_PWM2_BACK = 1

#M4
RIGHT_IN3_BACK = 26
RIGHT_IN4_BACK = 27
RIGHT_PWM2_BACK = 13


# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEFT_IN1, GPIO.OUT)
GPIO.setup(LEFT_IN2, GPIO.OUT)
GPIO.setup(LEFT_PWM, GPIO.OUT)

GPIO.setup(RIGHT_IN1, GPIO.OUT)
GPIO.setup(RIGHT_IN2, GPIO.OUT)
GPIO.setup(RIGHT_PWM, GPIO.OUT)

GPIO.setup(LEFT_IN3_BACK, GPIO.OUT)
GPIO.setup(LEFT_IN4_BACK, GPIO.OUT)
GPIO.setup(LEFT_PWM2_BACK, GPIO.OUT)

GPIO.setup(RIGHT_IN3_BACK, GPIO.OUT)
GPIO.setup(RIGHT_IN4_BACK, GPIO.OUT)
GPIO.setup(RIGHT_PWM2_BACK, GPIO.OUT)

# Set initial motor direction and speed
GPIO.output(LEFT_IN1, GPIO.LOW)
GPIO.output(LEFT_IN2, GPIO.LOW)
GPIO.output(RIGHT_IN1, GPIO.LOW)
GPIO.output(RIGHT_IN2, GPIO.LOW)
GPIO.output(LEFT_IN3_BACK, GPIO.LOW)
GPIO.output(LEFT_IN4_BACK, GPIO.LOW)
GPIO.output(RIGHT_IN3_BACK, GPIO.LOW)
GPIO.output(RIGHT_IN4_BACK, GPIO.LOW)
left_pwm = GPIO.PWM(LEFT_PWM, 1000)
right_pwm = GPIO.PWM(RIGHT_PWM, 1000)
left_pwm.start(0)
right_pwm.start(0)

left_pwm2_back = GPIO.PWM(LEFT_PWM, 1000)
right_pwm2_back = GPIO.PWM(RIGHT_PWM, 1000)
left_pw2_back.start(0)
right_pwm2_back.start(0)

# Define motor control functions
def stop_motors():
    left_pwm.ChangeDutyCycle(0)
    right_pwm.ChangeDutyCycle(0)
    left_pwm2_back.ChangeDutyCycle(0)
    right_pwm2_back.ChangeDutyCycle(0)

def forward():
    GPIO.output(LEFT_IN1, GPIO.HIGH)
    GPIO.output(LEFT_IN2, GPIO.LOW)
    GPIO.output(RIGHT_IN1, GPIO.HIGH)
    GPIO.output(RIGHT_IN2, GPIO.LOW)
    GPIO.output(LEFT_IN3_BACK, GPIO.HIGH)
    GPIO.output(LEFT_IN4_BACK, GPIO.LOW)
    GPIO.output(RIGHT_IN3_BACK, GPIO.HIGH)
    GPIO.output(RIGHT_IN4_BACK, GPIO.LOW)

def backward():
    GPIO.output(LEFT_IN1, GPIO.LOW)
    GPIO.output(LEFT_IN2, GPIO.HIGH)
    GPIO.output(RIGHT_IN1, GPIO.LOW)
    GPIO.output(RIGHT_IN2, GPIO.HIGH)
    GPIO.output(LEFT_IN3_BACK, GPIO.LOW)
    GPIO.output(LEFT_IN4_BACK, GPIO.HIGH)
    GPIO.output(RIGHT_IN3_BACK, GPIO.LOW)
    GPIO.output(RIGHT_IN4_BACK, GPIO.HIGH)

def turn_left():
    GPIO.output(LEFT_IN1, GPIO.LOW)
    GPIO.output(LEFT_IN2, GPIO.LOW)
    GPIO.output(RIGHT_IN1, GPIO.HIGH)
    GPIO.output(RIGHT_IN2, GPIO.LOW)
    GPIO.output(LEFT_IN3_BACK, GPIO.LOW)
    GPIO.output(LEFT_IN4_BACK, GPIO.LOW)
    GPIO.output(RIGHT_IN3_BACK, GPIO.HIGH)
    GPIO.output(RIGHT_IN4_BACK, GPIO.LOW)

def turn_right():
    GPIO.output(LEFT_IN1, GPIO.HIGH)
    GPIO.output(LEFT_IN2, GPIO.LOW)
    GPIO.output(RIGHT_IN1, GPIO.LOW)
    GPIO.output(RIGHT_IN2, GPIO.LOW)
    GPIO.output(LEFT_IN3_BACK, GPIO.HIGH)
    GPIO.output(LEFT_IN4_BACK, GPIO.LOW)
    GPIO.output(RIGHT_IN3_BACK, GPIO.LOW)
    GPIO.output(RIGHT_IN4_BACK, GPIO.LOW)

# Listen for keyboard input
while True:
    try:
        c = input()
        if c == 'w':
            forward()
            left_pwm.ChangeDutyCycle(50)
            right_pwm.ChangeDutyCycle(50)
            left_pwm2_back.ChangeDutyCycle(50)
            right_pwm2_back.ChangeDutyCycle(50)
        elif c == 's':
            backward()
            left_pwm.ChangeDutyCycle(50)
            right_pwm.ChangeDutyCycle(50)
            left_pwm2_back.ChangeDutyCycle(50)
            right_pwm2_back.ChangeDutyCycle(50)
        elif c == 'a':
            turn_left()
            left_pwm.ChangeDutyCycle(50)
            right_pwm.ChangeDutyCycle(0)
            left_pwm2_back.ChangeDutyCycle(50)
            right_pwm2_back.ChangeDutyCycle(0)
        elif c == 'd':
            turn_right()
            left_pwm.ChangeDutyCycle(0)
            right_pwm.ChangeDutyCycle(50)
            left_pwm2_back.ChangeDutyCycle(0)
            right_pwm2_back.ChangeDutyCycle(50)
        elif c == 'x':
            stop_motors()
        else:
            print("Invalid input, please enter w, s, a, d or x.")
    except KeyboardInterrupt:
        break

# Clean up GPIO pins and stop PWM
left_pwm.stop()
right_pwm.stop()
GPIO.cleanup()
