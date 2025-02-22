"""Question taken from assignment 1"""

""" An automobile travels on a straight road for 40 km at 30 km/h. It then continues in the
same direction for another 40 km at 60 km/h. (a) What is the average velocity of the
car during the full 80 km trip? (Assume that it moves in the positive x direction.) (b)
What is the average speed? (c) Graph x versus t and indicate how the average velocity
is found on the graph. """


import matplotlib.pyplot as plt

# Given data
distance1 = 40  # km
speed1 = 30     # km/h
distance2 = 40  # km
speed2 = 60     # km/h

# Calculate time for each segment
time1 = distance1 / speed1
time2 = distance2 / speed2

# Calculate total distance and time
total_distance = distance1 + distance2
total_time = time1 + time2

# Calculate average velocity
average_velocity = total_distance / total_time

# Print the results
print("Average velocity:", average_velocity, "km/h")

# Calculate average speed
average_speed = (distance1 + distance2) / (time1 + time2)
print("Average speed:", average_speed, "km/h")

# Create time intervals for the graph
time_intervals = [0, time1, total_time]

# Calculate distances at each time interval
distances = [0, distance1, total_distance]

# Plot the distance-time graph
plt.plot(time_intervals, distances)
plt.xlabel("Time (hours)")
plt.ylabel("Distance (km)")
plt.title("Distance vs Time")
plt.grid(True)
plt.show()