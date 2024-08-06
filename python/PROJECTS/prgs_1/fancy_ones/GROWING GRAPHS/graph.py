import random
import matplotlib.pyplot as plt

# Set a seed value for reproducibility
random.seed(0)

# Initialize an empty list to store network speed values
network_speeds = []

# Create a figure and axis for the plot
fig, ax = plt.subplots()
plt.ion()  # Turn on interactive mode for continuous updates

# Set the initial values for x and y
x_values = []
y_values = []

# Plot the initial point
line, = ax.plot(x_values, y_values, 'o-', label='Network Speed')

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('Network Speed (Mbps)')
plt.title('Real-time Network Speed Monitoring')

# Adding a legend
plt.legend()

# Display the plot
plt.show()

# Continuously update the plot with random network speed values
while True:
    # Generate a random network speed value between 1 and 100 (Mbps)
    network_speed = random.randint(1, 700)

    # Append the new network speed value to the list
    network_speeds.append(network_speed)

    # Update x and y values for the plot
    x_values = list(range(len(network_speeds)))
    y_values = network_speeds

    # Update the data on the plot
    line.set_xdata(x_values)
    line.set_ydata(y_values)

    # Adjust the plot limits to accommodate the new data
    ax.relim()
    ax.autoscale_view()

    # Pause to create a real-time effect
    plt.pause(5)  # Adjust the pause duration as needed
