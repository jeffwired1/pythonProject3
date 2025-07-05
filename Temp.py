import tkinter as tk
from math import pi, cos, sin, radians

class Gauge(tk.Canvas):
    def __init__(self, master, size=200, max_value=100, value=70, **kwargs):
        super().__init__(master, width=size, height=size, bg='white', highlightthickness=0, **kwargs)
        self.size = size
        self.center = size // 2
        self.radius = size * 0.4
        self.max_value = max_value
        self.value = value
        self.draw_gauge()

    def draw_gauge(self):
        self.delete("all")
        # Draw background arc
        self.create_arc(self.center - self.radius, self.center - self.radius,
                        self.center + self.radius, self.center + self.radius,
                        start=135, extent=270, style='arc', width=20, outline="#ccc")

        # Draw value arc
        extent = (self.value / self.max_value) * 270
        self.create_arc(self.center - self.radius, self.center - self.radius,
                        self.center + self.radius, self.center + self.radius,
                        start=135, extent=extent, style='arc', width=20, outline="#4CAF50")

        # Draw needle
        angle_deg = 135 + extent
        angle_rad = radians(angle_deg)
        needle_length = self.radius * 0.9
        end_x = self.center + needle_length * cos(angle_rad)
        end_y = self.center - needle_length * sin(angle_rad)
        self.create_line(self.center, self.center, end_x, end_y, width=4, fill="red")

        # Center dot
        self.create_oval(self.center - 6, self.center - 6, self.center + 6, self.center + 6,
                         fill="#4CAF50", outline='')

        # Value label
        self.create_text(self.center, self.center + self.radius / 2, text=f"{self.value:.0f}",
                         font=("Helvetica", 20, "bold"), fill="#333")

# Usage
root = tk.Tk()
root.title("Gauge with Needle")
gauge = Gauge(root, size=300, value=65)
gauge.pack(padx=20, pady=20)
root.mainloop()


