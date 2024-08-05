# python RayleighFading.py

"""
import numpy as np

# Set the scale parameter for the Rayleigh distribution (determines the shape)
scale = 1.0

# Generate a single sample from the Rayleigh distribution
rayleigh_sample = np.random.rayleigh(scale)

# Generate an array of Rayleigh fading samples
num_samples = 1000
rayleigh_fading = np.random.rayleigh(scale, size=num_samples)


import numpy as np

# Set the scale parameter for the Rayleigh distribution (determines the shape)
scale = 1.0

# Generate an array of Rayleigh fading samples
num_samples = 10
rayleigh_fading = np.random.rayleigh(scale, size=num_samples)

# Generate an array of complex fading samples
complex_fading = rayleigh_fading * (np.random.normal(0, 1, size=num_samples) + 1j * np.random.normal(0, 1, size=num_samples))
"""

import numpy as np

# Generate a single Rayleigh fading sample with scale=1.0
rayleigh_sample_1 = np.random.exponential(scale=0.1, size=10)

# Generate a single Rayleigh fading sample with scale=2.0
rayleigh_sample_2 = np.random.exponential(scale=1.0, size=10)

# Generate a single Rayleigh fading sample with scale=2.0
rayleigh_sample_3 = np.random.exponential(scale=2.0, size=10)

print(rayleigh_sample_1)  # Output: Random positive value
print(rayleigh_sample_2)  # Output: Another random positive value, typically larger than rayleigh_sample_1
print(rayleigh_sample_3)  # Output: Another random positive value, typically larger than rayleigh_sample_1

# Generate Rayleigh fading values
rayleigh_fading_values_1 = np.random.rayleigh(scale=0.1, size=10)
rayleigh_fading_values_2 = np.random.rayleigh(scale= 1.0, size=10)
rayleigh_fading_values_3 = np.random.rayleigh(scale= 2.0, size=10)
print(rayleigh_fading_values_1) 
print(rayleigh_fading_values_2) 
print(rayleigh_fading_values_3) 

