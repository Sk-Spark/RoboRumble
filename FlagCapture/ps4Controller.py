import pygame

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

# Main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        # print event type & event button        
        print(event)
        # print(event.type, event.button)

        # Quit event
        if event.type == pygame.QUIT:
            running = False

        # Button press event
        elif event.type == pygame.JOYBUTTONDOWN:         
            button = event.button

            # XYAB buttons
            if button == 0:
                print("X button pressed.")
            elif button == 1:
                print("Zero button pressed.")
            elif button == 2:
                print("Square button pressed.")
            elif button == 3:
                print("triangle button pressed.")

            # L1, R1 buttons
            elif button == 9:
                print("L1 button pressed.")
            elif button == 10:
                print("R1 button pressed.")
            
            # D-pad buttons
            elif button == 11:
                print("D-pad up button pressed.")
            elif button == 12:
                print("D-pad down button pressed.")
            elif button == 13:
                print("D-pad left button pressed.")
            elif button == 14:
                print("D-pad right button pressed.")
            # elif button == 12:
            #     print("D-pad up-left button pressed.")
            # elif button == 13:
            #     print("D-pad up-right button pressed.")
            # elif button == 14:
            #     print("D-pad down-left button pressed.")
            # elif button == 15:
            #     print("D-pad down-right button pressed.")

        # Button release event
        elif event.type == pygame.JOYBUTTONUP:
            button = event.button

             # XYAB buttons
            if button == 0:
                print("X button released.")
            elif button == 1:
                print("Zero button released.")
            elif button == 2:
                print("Square button released.")
            elif button == 3:
                print("triangle button released.")

            # L1, R1 buttons
            elif button == 9:
                print("L1 button released.")
            elif button == 10:
                print("R1 button released.")
            
            # D-pad buttons
            elif button == 11:
                print("D-pad up button released.")
            elif button == 12:
                print("D-pad down button released.")
            elif button == 13:
                print("D-pad left button released.")
            elif button == 14:
                print("D-pad right button released.")
            # elif button == 12:
            #     print("D-pad up-left button released.")
            # elif button == 13:
            #     print("D-pad up-right button released.")
            # elif button == 14:
            #     print("D-pad down-left button released.")
            # elif button == 15:
            #     print("D-pad down-right button released.")

        # Joystick axis movement event
        elif event.type == pygame.JOYAXISMOTION:
            axis = event.axis
            value = event.value

            # Left joystick
            if axis == 0:
                print(f"Left joystick X-axis moved to {value}.")
            elif axis == 1:
                print(f"Left joystick Y-axis moved to {value}.")

            # Right joystick
            elif axis == 2:
                print(f"Right joystick X-axis moved to {value}.")
            elif axis == 3:
                print(f"Right joystick Y-axis moved to {value}.")

            # L2 Var button
            elif axis == 4:
                print(f"L2 var button pressed to {value}.")

            # R2 Var button
            elif axis == 5:
                print(f"R2 var button pressed to {value}.")

# Quit pygame
pygame.quit()
quit()
