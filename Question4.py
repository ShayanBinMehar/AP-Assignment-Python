"""Question taken from assignment 1"""

"""In a relay race, each contestant runs 25 m while carrying an egg balanced on a spoon,
turns around, and comes back to the starting point. Edith runs the first 25 m in 20
seconds. On the return trip she is more confident and takes only 15 seconds. What is
the magnitude of her average velocity for (a) the first 25 m? (the return trip? (c ) What
is her average velocity for the entire round trip? (d) what is her average speed for the
round trip? """

distance = 25  # meters
time1 = 20  # seconds
time2 = 15  # seconds

# Average velocity for the first 25 m
average_velocity1 = distance / time1
print("Average velocity for the first 25 m:", average_velocity1, "m/s")

# Average velocity for the return trip
average_velocity2 = -distance / time2  # Negative sign indicates opposite direction
print("Average velocity for the return trip:", average_velocity2, "m/s")

# Average velocity for the entire round trip (displacement is 0)
average_velocity_total = 0
print("Average velocity for the entire round trip:", average_velocity_total, "m/s")

# Average speed for the round trip
total_distance = distance * 2
total_time = time1 + time2
average_speed = total_distance / total_time
print("Average speed for the round trip:", average_speed, "m/s")