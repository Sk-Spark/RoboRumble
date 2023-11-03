import pygame
import json, os
import subprocess
import re
import time

# Define the command to run ds4drv as sudo
command = "sudo ds4drv"

# Start the ds4drv process
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# Regular expression pattern to match the controller connection message
controller_connected_pattern = re.compile(r"Connected to Bluetooth Controller (\S+)")

# Continuously monitor for controller connections
while True:
    # Read the output from the ds4drv process
    line = process.stdout.readline().decode("utf-8").strip()
    if line:
        print(line)

        # Check if the line contains a controller connection message
        match = controller_connected_pattern.search(line)
        if match:
            bluetooth_address = match.group(1)
            print(f"Controller connected: {bluetooth_address}")
            break  # Break the loop when a controller is connected

# You can add additional code here to interact with the connected controller
print("Controller connected")

# Initialize pygame
pygame.init()
pygame.joystick.init()

# Check for connected joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joysticks found.")
    pygame.quit()
    quit()

# Select the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

with open(os.path.join("ps4_keys.json"), 'r+') as file:
    button_keys = json.load(file)

# print(button_keys)

# Main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        # print event type & event button   
        # if (event.type == pygame.JOYAXISMOTION and event.axis == 12)  or event.type != pygame.JOYAXISMOTION :     
            # print(event)
            # print(event.type)

        # print(event.type, event.button)

        # Quit event
        if event.type == pygame.QUIT:
            running = False

        #D-pad controlles
        if event.type == pygame.JOYHATMOTION: #JoyHatMotion : 1538
            value = event.value
            if value == (0, -1):
                print("Down") 
            elif value == (0, 1):
                print("UP") 
            elif value == (1, 0):
                print("Right") 
            elif value == (-1, 0):
                print("Left") 
            elif value == (1, 1):  
                print("Up-Right") 
            elif value == (1, -1):  
                print("Down-Right") 
            elif value == (-1, 1):  
                print("Up-Left") 
            elif value == (-1, -1):  
                print("Down-Left") 
            else:
                print("D-Pad released") 


        # Button press event
        elif event.type == pygame.JOYBUTTONDOWN:         
            button = event.button

            # XYAB buttons
            if button == button_keys['x']:
                print("X button pressed.")
            elif button == button_keys['circle']:
                print("Circle button pressed.")
            elif button == button_keys['square']:
                print("Square button pressed.")
            elif button == button_keys['triangle']:
                print("Triangle button pressed.")
            elif button == button_keys['share']:
                print("Share button pressed.")
            elif button == button_keys['options']:
                print("Options button pressed.")

            # L1, R1 buttons
            elif button == button_keys['L1']:
                print("L1 button pressed.")
            elif button == button_keys['L2_btn']:
                print("L2 button pressed.")
            elif button == button_keys['R1']:
                print("R1 button pressed.")            
            elif button == button_keys['R2_btn']:
                print("R2 button pressed.") 

            # right stick & left stick btn
            elif button == button_keys['left_stick_btn']:
                print("Left stick button pressed.")
            elif button == button_keys['right_stick_btn']:
                print("Left stick button pressed.")

            # touchpad btn 
            elif button == button_keys['touchpad_btn']:
                print("Touchpad btn pressed.")


        # Button release event
        elif event.type == pygame.JOYBUTTONUP:
            button = event.button

            # XYAB buttons
            if button == button_keys['x']:
                print("X button released.")
            elif button == button_keys['circle']:
                print("Circle button released.")
            elif button == button_keys['square']:
                print("Square button released.")
            elif button == button_keys['triangle']:
                print("Triangle button released.")
            elif button == button_keys['share']:
                print("Share button released.")
            elif button == button_keys['options']:
                print("Options button released.")

            # L1, R1 buttons
            elif button == button_keys['L1']:
                print("L1 button released.")
            elif button == button_keys['L2_btn']:
                print("L2 button released.")
            elif button == button_keys['R1']:
                print("R1 button released.")            
            elif button == button_keys['R2_btn']:
                print("R2 button released.") 

            # right stick & left stick btn
            elif button == button_keys['left_stick_btn']:
                print("Left stick button released.")
            elif button == button_keys['right_stick_btn']:
                print("Left stick button released.")
            
            # touchpad btn 
            elif button == button_keys['touchpad_btn']:
                print("Touchpad btn released.")
            

        # Joystick axis movement event
        elif event.type == pygame.JOYAXISMOTION:
            axis = event.axis
            value = event.value

            # Left joystick
            if axis == button_keys['left_stick_x_axis']:
                print(f"Left joystick X-axis moved to {value}.")
            elif axis == button_keys['left_stick_y_axis']:
                print(f"Left joystick Y-axis moved to {value}.")

            # Right joystick
            elif axis == button_keys['right_stick_x_axis']:
                print(f"Right joystick X-axis moved to {value}.")
            elif axis == button_keys['right_stick_y_axis']:
                print(f"Right joystick Y-axis moved to {value}.")

            # L2 Var button
            elif axis == button_keys['L2_axis']:
                print(f"L2 var button pressed to {value}.")

            # R2 Var button
            elif axis == button_keys['R2_axis']:
                print(f"R2 var button pressed to {value}.")

# Quit pygame
pygame.quit()
# To stop ds4drv when you're done, you can use the following:
ds4drv_process.terminate()
quit()

