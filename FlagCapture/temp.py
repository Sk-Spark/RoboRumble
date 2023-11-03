import subprocess
import re

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

# Continue with your code after the controller is connected
print("You can now interact with the connected controller.")

# You can add additional code here to interact with the connected controller
print("Controller connected")