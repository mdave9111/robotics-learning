import numpy as np

# numpy is a powerful tool for linear algebra and numerical computations of matrix multiplications
# we can use it in robotics to perform kinematics calculations and in our example in a motor encoder

# the motor encoder gives a reading of the motor's position in degrees against time.
# we can use numpy to take the data, store in an array, plot it, and perform calculations

motor_encoder_readings = np.array([0, 3, 7, 12, 18, 25, 33, 42, 52, 63])

# 1. find number of readings
print(f"Number of readings: {motor_encoder_readings.size}")

# 2. find largest, smallest, mean angle readings
print(f"Max reading: {motor_encoder_readings.max()}")
print(f"Min reading: {motor_encoder_readings.min()}")
print(f"Mean reading: {motor_encoder_readings.mean()}")

# 3. retrieve the first 5 measurements and multiply every angle by 2

data = motor_encoder_readings[0:5]
print(f"First 5 readings: {data}")

newarr = 2*motor_encoder_readings
print(f"New motor_encoder_readings: {newarr}")