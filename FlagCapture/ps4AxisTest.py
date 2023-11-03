import pygame
import time

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Get the number of available joysticks
joystick_count = pygame.joystick.get_count()

# Create a list to store joystick information and axis data
joystick_data = []

while True:
    for event in pygame.event.get():
        # Loop through the available joysticks
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # Get the name of the joystick
            joystick_name = joystick.get_name()

            # Get the number of axes on the joystick
            num_axes = joystick.get_numaxes()

            # Create a row for the horizontal table
            row = []
            
            # Append axis numbers to the row
            # row.extend([f"Axis {axis}" for axis in range(num_axes)])

            # Append axis values to the row
            row.extend([f"{joystick.get_axis(axis):.2f}" for axis in range(num_axes)])
            
            # Append the row to the joystick_data list
            joystick_data.append(row)

        # Find the maximum width of each column for formatting
        column_widths = [max(len(str(row[i])) for row in joystick_data) for i in range(len(joystick_data[0]))]

        # Print the horizontal table with proper formatting
        for row in joystick_data:
            formatted_row = [f"{item: <{column_widths[i]}}" for i, item in enumerate(row)]
            print(" ".join(formatted_row))
        
        # time.sleep(0.3)

# Quit Pygame
pygame.quit()
