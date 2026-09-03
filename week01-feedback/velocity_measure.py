import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,10,1000)
angles = 30*np.sin(time)
# let's experiment by injecting noise into the encoder readings
mu = 0
sigma = 0.5
noise = np.random.normal(mu,sigma,size=1000) # this creates positive or negative noise value which we add on
noisy_angles = angles + noise

# estimate angular velocity using derivative
angles_delta = np.diff(noisy_angles)
print(f"Angle deltas: {angles_delta}")

time_delta = np.diff(time)

clean_vel = (np.diff(angles))/time_delta
noisy_vel = angles_delta/time_delta

midpoint_time = (time[1:] + time[:-1])/2

# noisy angular velocity graph
plt.plot(midpoint_time,noisy_vel)
plt.xlabel("Time (s)")
plt.ylabel("Angular velocity (°/s)")
plt.title("Velocity graph")

# ideal angular velocity graph
plt.plot(midpoint_time,clean_vel)
plt.xlabel("Time (s)")
plt.ylabel("Angular velocity (°/s)")



plt.show()




