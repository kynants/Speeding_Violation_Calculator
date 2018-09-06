# Design a program that calculates and displays the number of miles per hour
# over the speed limit that a speeding driver was doing. The program should
# ask for the speed limit and the driver’s speed. Validate the input as
# follows:
#
# - The speed limit should be at least 20, but not greater than 70.
# - The driver’s speed should be at least the value entered for the speed
#   limit (otherwise the driver was not speeding).
#
# Once correct data has been entered, the program should calculate and display
# the number of miles per hour over the speed limit that the driver was doing.

# Prompt User Input for Speed Limit
speed_lim = int(input('What was the speed limit? '))

# Input Speed Limit Validation
while speed_lim < 20 or speed_lim > 70:
    speed_lim = int(input('Error. Speed limit must be between 20-70. Please '
                          'enter the correct speed limit: '))

# Prompt User Input for how fast the driver went
drive_speed = int(input('How fast were you going? '))

# Input Validation for how fast the driver went over the speed limit
while drive_speed <= speed_lim:
    drive_speed = int(input('Error. Driver\'s speed should be at least 1 '
                                'mph over the speed limit. Please enter the '
                                'correct speed you were driving: '))

# Final Output
print('You drove', drive_speed - speed_lim, 'mph over the speed limit.')