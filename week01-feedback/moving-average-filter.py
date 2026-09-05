import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,10,1000)
angles = 30*np.sin(time)
# let's experiment by injecting noise into the encoder readings
mu = 0
sigma = 0.5
noise = np.random.normal(mu,sigma,size=1000) # this creates positive or negative noise value which we add on
noisy_angles = angles + noise

# now implement the moving average filter to smooth out the noisy signal
window_size = 500 # larger window means larger phase delay, time shift (fourier concept) and attenuation of actual signal (not just noise)
filtered_angles = np.full(noisy_angles.size, np.nan)

# the loop to move the window
for i in range(0,noisy_angles.size):
    if i >= window_size - 1:
        filtered_angles[i] = (1/(window_size))*np.sum(noisy_angles[i-window_size+1:i+1])


plt.plot(time,noisy_angles)
plt.plot(time,filtered_angles)
plt.title("Moving average filtered graph")
plt.xlabel("time (s)")
plt.ylabel("angle (degs)")

plt.show()


