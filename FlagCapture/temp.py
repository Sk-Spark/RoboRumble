import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin to which the servo is connected
servo_pin = 35

# Set the GPIO pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance with a frequency of 50Hz (typical for servos)
pwm = GPIO.PWM(servo_pin, 50)

# Start the PWM with a duty cycle of 7.5% (for a 90-degree position, adjust as needed)
pwm.start(7.5)

try:
    while True:
        # Get user input for the servo position
        position = float(input("Enter servo position in degrees (0-180): "))

        if 0 <= position <= 180:
            # Map the position to the duty cycle (0-180 degrees to 2.5-12.5%)
            duty_cycle = 2.5 + (position / 180.0 * 10.0)
            pwm.ChangeDutyCycle(duty_cycle)
            print(f"Set servo position to {position} degrees.")
        else:
            print("Invalid input. Please enter a value between 0 and 180 degrees.")

except KeyboardInterrupt:
    # Stop the PWM and cleanup GPIO on Ctrl+C
    pwm.stop()
    GPIO.cleanup()
