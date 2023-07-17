class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.last_error = 0
        self.integral_error = 0

    def update(self, current_value, dt):
        error = self.setpoint - current_value
        self.integral_error += error * dt
        derivative_error = (error - self.last_error) / dt
        output = (self.Kp * error) + (self.Ki * self.integral_error) + (self.Kd * derivative_error)
        self.last_error = error
        return output

# Example system: Temperature Control
class TemperatureControlSystem:
    def __init__(self, initial_temperature):
        self.temperature = initial_temperature

    def update(self, heater_output, dt):
        # Simulate system dynamics
        ambient_temperature = 25  # Ambient temperature
        time_constant = 5  # System time constant
        error = ambient_temperature - self.temperature
        self.temperature += (heater_output + error) / time_constant * dt

# Main program
def main():
    # PID controller parameters
    Kp = 44.0
    Ki = 0.0
    Kd = 0.2

    # Setpoint and initial conditions
    setpoint = 50.0
    initial_temperature = 30.0

    # Create PID controller and system objects
    pid_controller = PIDController(Kp, Ki, Kd, setpoint)
    system = TemperatureControlSystem(initial_temperature)

    # Simulation parameters
    dt = 0.1  # Time step
    simulation_time = 10.0  # Total simulation time
    num_steps = int(simulation_time / dt)

    # Run simulation
    for step in range(num_steps):
        # Get current temperature
        current_temperature = system.temperature

        # Update PID controller
        control_signal = pid_controller.update(current_temperature, dt)

        # Apply control signal to the system
        system.update(control_signal, dt)

        # Print current time and temperature
        print(f"Time: {step * dt:.1f}s, Temperature: {system.temperature:.2f}°C")
        print(control_signal)

if __name__ == '__main__':
    main()
