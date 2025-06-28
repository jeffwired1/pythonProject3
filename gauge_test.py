import tkinter as tk
import math

def draw_needle(canvas, angle_deg, center_x, center_y, length, width=6):
    canvas.delete("needle")

    # Angle in radians
    angle_rad = math.radians(angle_deg)

    # Tip of the needle
    tip_x = center_x + length * math.cos(angle_rad)
    tip_y = center_y - length * math.sin(angle_rad)

    # Perpendicular angle for width
    perp_angle = math.radians(angle_deg + 90)

    # Base width coordinates
    base_left_x = center_x + width * math.cos(perp_angle)
    base_left_y = center_y - width * math.sin(perp_angle)
    base_right_x = center_x - width * math.cos(perp_angle)
    base_right_y = center_y + width * math.sin(perp_angle)

    # Draw the needle as a triangle
    canvas.create_polygon(
        base_left_x, base_left_y,
        base_right_x, base_right_y,
        tip_x, tip_y,
        fill="red", tag="needle"
    )

def update_gauge(value):
    angle = 180 - (value / 100) * 180
    draw_needle(canvas, angle, 150, 150, 100)

def draw_ticks(canvas, center_x, center_y, radius, tick_interval, tick_length, draw_labels=False):
    for value in range(0, 101, tick_interval):
        angle_deg = 180 - (value / 100) * 180
        angle_rad = math.radians(angle_deg)

        x_start = center_x + (radius - tick_length) * math.cos(angle_rad)
        y_start = center_y - (radius - tick_length) * math.sin(angle_rad)
        x_end = center_x + radius * math.cos(angle_rad)
        y_end = center_y - radius * math.sin(angle_rad)
        canvas.create_line(x_start, y_start, x_end, y_end)

        if draw_labels:
            label_radius = radius + 15
            label_x = center_x + label_radius * math.cos(angle_rad)
            label_y = center_y - label_radius * math.sin(angle_rad)
            canvas.create_text(label_x, label_y, text=str(value), font=("Arial", 8), anchor="center")

def loop_update():  # This loop contains the code to run at schedueled intervals
    print("1", end="", flush=True)
    root.after(500, loop_update)  # Schedule next update in 500 ms

root = tk.Tk()
root.title("Gauge with Pointer Needle")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Draw the arc
canvas.create_arc(50, 50, 250, 250, start=0, extent=180, style=tk.ARC)

# Major and minor ticks
draw_ticks(canvas, 150, 150, 100, tick_interval=10, tick_length=10, draw_labels=True)
draw_ticks(canvas, 150, 150, 100, tick_interval=5, tick_length=5, draw_labels=False)

# Draw pointer needle
draw_needle(canvas, 180, 150, 150, 100)

# Slider
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda v: update_gauge(float(v)))
scale.pack()

loop_update()  # Trigger the continuous running code
root.mainloop()
print("")  # Line feed
print("Exit")  # Exit message