import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,10,1000)
angles = 30*np.sin(time)

# estimate angular velocity using derivative
angles_delta = np.diff(angles)
print(f"Angle deltas: {angles_delta}")

time_delta = np.diff(time)

vel = angles_delta/time_delta

midpoint_time = (time[1:] + time[:-1])/2

plt.plot(midpoint_time,vel)
plt.xlabel("Time (s)")
plt.ylabel("Angular velocity (°/s)")
plt.title("Velocity graph")

plt.plot(time,angles)

plt.show()




