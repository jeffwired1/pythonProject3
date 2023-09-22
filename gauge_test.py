import tkinter as tk
import math

class NeedleGauge(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=200, height=200)
        self.angle = 0  # Initial angle for the needle
        self.needle_length = 80
        self.needle_color = "red"
        self.draw_needle()

    def set_angle(self, angle):
        self.angle = angle
        self.draw_needle()

    def draw_needle(self):
        self.delete("needle")
        center_x = self.winfo_reqwidth() / 2
        center_y = self.winfo_reqheight() / 2

        # Calculate the position of the needle
        needle_angle = math.radians(self.angle)
        needle_x = center_x + self.needle_length * math.cos(needle_angle)
        needle_y = center_y + self.needle_length * math.sin(needle_angle)

        # Draw the needle as a line
        self.create_line(center_x, center_y, needle_x, needle_y, fill=self.needle_color, width=3, tags="needle")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Needle Gauge")

    gauge = NeedleGauge(root)
    gauge.pack()

    def update_needle():
        gauge.set_angle(gauge.angle + 1)
        root.after(10, update_needle)

    update_needle()

    root.mainloop()
