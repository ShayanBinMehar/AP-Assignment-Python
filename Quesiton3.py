"""Question taken from assignment 1"""

"""A boy whirls a stone in a horizontal circle of radius 1.5 m and at height 2.0 m above
level ground. The string breaks, and the stone flies off horizontally and strikes the
ground after travelling a horizontal distance of 10 m. What is the magnitude of the
centripetal acceleration of the stone during the circular motion? """

import math

# Given data
radius = 1.5  # meters
height = 2.0  # meters
horizontal_distance = 10  # meters
gravity = 9.81  # m/s^2

# Calculate time of flight
time_of_flight = math.sqrt(2 * height / gravity)

# Calculate horizontal velocity
horizontal_velocity = horizontal_distance / time_of_flight

# Calculate centripetal acceleration
centripetal_acceleration = horizontal_velocity**2 / radius

# Print the result
print("Centripetal acceleration:", round(centripetal_acceleration, 2), "m/s^2")