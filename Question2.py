"""Question taken from assignment 1"""

""""An object is launched vertically upward with an initial velocity of 30 m/s. Calculate
the time it takes for the object to reach its maximum height, and then calculate the
total time it spends in the air before hitting the ground. (Assume g = 9.8 m/s²)"""

import numpy as np

# Given data
initial_velocity = 30  # m/s
gravity = 9.8  # m/s^2

# Time to reach maximum height
time_to_max_height = initial_velocity / gravity

# Total time in the air (symmetrical motion)
total_time = 2 * time_to_max_height

# Calculate the values
time_to_max_height = round(time_to_max_height, 2)
total_time = round(total_time, 2)

# Print the results
print("Time to reach maximum height:", time_to_max_height, "seconds")
print("Total time in the air:", total_time, "seconds")