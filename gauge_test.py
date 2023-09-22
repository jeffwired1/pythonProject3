import tkinter as tk

class Gauge(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.min_value = 0
        self.max_value = 100
        self.value = 0
        self.configure(width=200, height=200)
        self.draw_gauge()

    def set_value(self, value):
        if self.min_value <= value <= self.max_value:
            self.value = value
            self.draw_gauge()

    def draw_gauge(self):
        self.delete("all")
        angle = 240 * (self.value - self.min_value) / (self.max_value - self.min_value)
        start_angle = 30
        end_angle = 270
        self.create_arc(10, 10, 190, 190, start=start_angle, extent=angle, fill="blue")
        self.create_text(100, 100, text=f"{self.value}", font=("Arial", 20))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gauge")

    gauge = Gauge(root)
    gauge.pack()

    def update_gauge():
        print("a")
        gauge.set_value(gauge.value + 10)
        root.after(1000, update_gauge)

    update_gauge()
    print("a")

    root.mainloop()
