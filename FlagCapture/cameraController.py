import RPi.GPIO as GPIO
import time
from enum import Enum

class XYServo(Enum): # Servo that controlles x, y axies movement of gimbal
    MIN_ANGLE = 0
    MAX_ANGLE = 180

class ZServo(Enum):# Servo that controlles z axis movement of gimbal
    MIN_ANGLE = 0
    MAX_ANGLE = 180

class Servo:
    def __init__(self, pin, angle_range, frequency=50, duty_cycle_range=(2.5, 12.5)):
        self.pin = pin
        self.frequency = frequency
        self.angle_range = angle_range
        self.duty_cycle_range = duty_cycle_range
        # self.servo_state = ServoState.CLOSED
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.pwm.start(0)
        self.set_angle(90)

    # def servo_toggle(self):
    #     if self.servo_state == ServoState.OPEN:
    #         self.set_angle(ServoState.CLOSED.value)
    #         self.servo_state = ServoState.CLOSED
    #     elif self.servo_state == ServoState.CLOSED:
    #         self.set_angle(ServoState.OPEN.value)
    #         self.servo_state = ServoState.OPEN            
        
    def set_angle(self, angle):
        if angle < self.angle_range[0]:
            angle = self.angle_range[0]
        elif angle > self.angle_range[1]:
            angle = self.angle_range[1]
            
        print("Servo angle:", angle)
        duty_cycle = self.map_value(angle, *self.angle_range, *self.duty_cycle_range)
        
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.2)  # Give the servo some time to reach the desired position
        
    def map_value(self, value, in_min, in_max, out_min, out_max):
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()

class Gimbal:
    def __init__(self):
        self.xy_servo = Servo(35,(XYServo.MIN_ANGLE.value, XYServo.MAX_ANGLE.value))
        self.z_servo = Servo(12,(XYServo.MIN_ANGLE.value, XYServo.MAX_ANGLE.value))
    
    def move_xy_servo(self,angle):
        self.xy_servo.set_angle(angle)
        
    def move_z_servo(self,angle):
        self.z_servo.set_angle(angle)
    
    def servo_cleanup(self):
        self.xy_servo.cleanup()
        self.z_servo.cleanup()

# Servo Cariblration Code
if __name__ == "__main__":
    try:
        gimbal = Gimbal()  # Replace 18 with the GPIO pin you're using
        
        while True:
            angle = float(input("Enter xy angle (0 to 180): "))
            gimbal.move_xy_servo(angle)
            angle = float(input("Enter z angle (0 to 180): "))
            gimbal.move_z_servo(angle)
            
    except KeyboardInterrupt:
        gimbal.servo_cleanup()
        print("Servo control interrupted")
