"""Question taken from assignment 1"""

"""An Alaskan rescue plane drops a package of emergency rations to a stranded party of
explorers. If the plane is travelling horizontally at 40.0 m/s and is 100 m above the ground, where
does the package strike the ground relative to the point at which it was released? """

import math

# Given data
initial_velocity = 40  # m/s
height = 100  # meters
gravity = 9.81  # m/s^2

# Calculate time of flight
time_of_flight = math.sqrt(2 * height / gravity)

# Calculate horizontal distance
horizontal_distance = initial_velocity * time_of_flight

print("The package strikes the ground at a horizontal distance of", round(horizontal_distance, 2), "meters from the release point.")