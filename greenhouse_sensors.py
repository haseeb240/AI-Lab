import numpy as np
np.random.seed(7)
readings = np.random.randint(20, 41, size=(6, 3))

print("Sensor readings:")
print(readings)

sensor_mean = readings.mean(axis=0)
print("Mean per sensor:", sensor_mean)

sensor_std = readings.std(axis=0)
normalized = (readings - sensor_mean) / sensor_std

print("Normalized column means:", normalized.mean(axis=0))
peak_hours = np.argmax(readings, axis=0)
print("Hour of max per sensor:", peak_hours)
new_readings = np.vstack([readings, sensor_mean])

print("New shape:", new_readings.shape)
np.random.seed(7)

readings_again = np.random.randint(20, 41, size=(6, 3))

print("Reproducible:", np.array_equal(readings, readings_again))
print("Overall hottest reading:", readings.max())
