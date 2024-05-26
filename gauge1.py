import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Define gauge parameters
value = 65  # Value to display on the gauge
max_value = 100  # Maximum value of the gauge
units = "%"  # Units for the value label

# Configure gauge dimensions
gauge_radius = 0.4
needle_length = 0.7

# Calculate angles
angle_range = 360
min_angle = 0
max_angle = angle_range - 1
current_angle = min_angle + (value / max_value) * angle_range

# Create figure and axis
fig, ax = plt.subplots()

# Create gauge arc
arc = matplotlib.patches.Arc((0.5, 0.5), gauge_radius, gauge_radius, angle = 0,
                             theta1 = min_angle, theta2 = max_angle,
                             linewidth = 2, color='lightgray')

# Create needle
needle_start_x = 0.5
needle_start_y = 0.5
needle_end_x = 0.5 + needle_length * np.cos(np.radians(current_angle))
needle_end_y = 0.5 + needle_length * np.sin(np.radians(current_angle))

needle = matplotlib.patches.FancyArrowPatch((needle_start_x, needle_start_y),
                                         (needle_end_x, needle_end_y),
                                         mutation_scale=100, color='royalblue')

# Add elements to the axis
ax.add_patch(arc)
ax.add_patch(needle)

# Set labels and limits
ax.set_aspect("equal")
ax.set_xlabel(units)
ax.set_xlim([0.5 - gauge_radius - gauge_radius/5, 0.5 + gauge_radius + gauge_radius/5])
ax.set_ylim([0.5 - gauge_radius - gauge_radius/5, 0.5 + gauge_radius + gauge_radius/5])

# Display the gauge value
ax.text(0.5, 0.85, f"{value:.2f}", ha="center", va="center", fontsize=16)

# Show the gauge
plt.show()
