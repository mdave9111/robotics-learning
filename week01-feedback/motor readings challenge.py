import numpy as np
import matplotlib.pyplot as plt

# Now, we have a motor spinning smoothly and the motor encoder is returning this stream
# We want to take this stream and analyse it using arrays in numpy

# motor encoder data is assumed as perfect sin: θ(t) = 25 sin(t)

# grab 1000 angle measurements between 0 and 10 seconds
t = np.linspace(0,10,1000) #1000 listed times between 0 and 10s
angles = 25*np.sin(t) # grabbing 1000 25sin(t) measurements at the specified times

print(f"time stream: {t}")
print(f"angles stream: {angles}")

# get the midpoint sample
middle_index = t.size // 2
middle_sample = angles[middle_index]
print(f"Middle Sample: {middle_sample}")

# get the samples from 2s to 5s
mask = (t>=2)&(t<=5)# boolean indexing [False, False, False, True...]
interval_sample = angles[mask] # angles[False, False, False, True, True...]
# really common pattern in robotics and sensor data: one array holds timestamps, another holds measurements, and you use conditions on the timestamp array to filter both.
print(f"Interval Sample: {interval_sample}")

# find all times when the motor angles is greater than 20°
angle_mask = (angles>=20)
time_sample = t[angle_mask]
print(f"Times of angles >= 20°: {time_sample}")
print(f"Number of samples satisfying condition: {time_sample.size}")

exact_mask = (angles==20)
print(f"exact 20°: {t[exact_mask].size}")

# find the first time the sample becomes greater than 20°
new_mask = (angles>=20) # [F,F,T,T,F,....]
loc = np.where(new_mask)[0][0] # from the tuple of arrays: ([2,3,5,6,...]) get the first true
# locations of where angles>=20
print(f"Time of first 20°: {t[loc]}seconds")

# absolute value of motor angle
abs_arr = np.abs(angles)
print(f"Absolute angles: {abs_arr}")

# sample where the motor is furthest from 0°
# numpy has a special method for this:
furthest_index = np.argmax(abs_arr)
furthest_angle = angles[furthest_index]
print(f"Furthest angle from 0°: {furthest_angle}° @ time: {t[furthest_index]}s")

# or you could do a basic for loop
max_val = 0
i = int(0)
for val in abs_arr:
    if abs_arr[i] >= max_val:
        max_val = abs_arr[i]
        max_ind = i
    i += 1

print(f"Max Val = {angles[max_ind]}° @ time: {t[max_ind]}s")

# Create an error signal assuming the desired angle is always 10°
err = 10 - angles
plt.plot(t,err)
plt.xlabel("Time (s)")
plt.ylabel("Error (°)")
plt.title("Error graph")
plt.show()

# use the error signal to calculate the rms error
rms_error = np.sqrt((1/t.size)*np.sum(err**2))
print(f"RMS error: {rms_error}")

# make negative angles become 0 and positive angles remain unchanged

negative_mask = (angles< 0)
new_angles = angles.copy()
new_angles[negative_mask] = 0
print(f"New angles: {new_angles}")














