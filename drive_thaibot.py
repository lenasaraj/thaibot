import RPi.GPIO as GPIO
import time

class RobotCar:
    def __init__(self):
        # Motor pin definitions
        self.LEFT_IN1, self.LEFT_IN2, self.LEFT_PWM = 20, 21, 19
        self.RIGHT_IN1, self.RIGHT_IN2, self.RIGHT_PWM = 24, 25, 12
        self.LEFT_IN3_BACK, self.LEFT_IN4_BACK, self.LEFT_PWM2_BACK = 22, 23, 1
        self.RIGHT_IN3_BACK, self.RIGHT_IN4_BACK, self.RIGHT_PWM2_BACK = 26, 27, 13

        self.setup_gpio()
        self.setup_pwm()

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Setting up GPIO pins
        motor_pins = [self.LEFT_IN1, self.LEFT_IN2, self.RIGHT_IN1, self.RIGHT_IN2,
                      self.LEFT_IN3_BACK, self.LEFT_IN4_BACK, self.RIGHT_IN3_BACK, self.RIGHT_IN4_BACK]
        for pin in motor_pins:
            GPIO.setup(pin, GPIO.OUT)

    def setup_pwm(self):
        # Initializing PWM
        self.left_pwm = GPIO.PWM(self.LEFT_PWM, 1000)
        self.right_pwm = GPIO.PWM(self.RIGHT_PWM, 1000)
        self.left_pwm2_back = GPIO.PWM(self.LEFT_PWM2_BACK, 1000)
        self.right_pwm2_back = GPIO.PWM(self.RIGHT_PWM2_BACK, 1000)

        self.left_pwm.start(0)
        self.right_pwm.start(0)
        self.left_pwm2_back.start(0)
        self.right_pwm2_back.start(0)

    def move_motors(self, left_in1, left_in2, right_in1, right_in2, 
                    left_pwm_val, right_pwm_val, 
                    left_in3_back, left_in4_back, right_in3_back, right_in4_back):
        GPIO.output(self.LEFT_IN1, left_in1)
        GPIO.output(self.LEFT_IN2, left_in2)
        GPIO.output(self.RIGHT_IN1, right_in1)
        GPIO.output(self.RIGHT_IN2, right_in2)
        self.left_pwm.ChangeDutyCycle(left_pwm_val)
        self.right_pwm.ChangeDutyCycle(right_pwm_val)
        GPIO.output(self.LEFT_IN3_BACK, left_in3_back)
        GPIO.output(self.LEFT_IN4_BACK, left_in4_back)
        GPIO.output(self.RIGHT_IN3_BACK, right_in3_back)
        GPIO.output(self.RIGHT_IN4_BACK, right_in4_back)

    def forward(self):
        self.move_motors(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, 50, 50, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)

    def backward(self):
        self.move_motors(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, 50, 50, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)

    def turn_left(self):
        self.move_motors(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW, 50, 0, GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW)

    def turn_right(self):
        self.move_motors(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW, 0, 50, GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW)

    def stop(self):
        self.move_motors(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, 0, 0, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)

    def cleanup(self):
        self.left_pwm.stop()
        self.right_pwm.stop()
        self.left_pwm2_back.stop()
        self.right_pwm2_back.stop()
        GPIO.cleanup()

# Create robot car instance
robot_car = RobotCar()

# Listen for keyboard input
try:
    while True:
        c = input("Enter command (w/s/a/d/x): ").strip().lower()
        if c == 'w':
            robot_car.forward()
        elif c == 's':
            robot_car.backward()
        elif c == 'a':
            robot_car.turn_left()
        elif c == 'd':
            robot_car.turn_right()
        elif c == 'x':
            robot_car.stop()
        else:
            print("Invalid input, please enter w, s, a, d, or x.")
except KeyboardInterrupt:
    print("Exiting program...")
finally:
    robot_car.cleanup()
