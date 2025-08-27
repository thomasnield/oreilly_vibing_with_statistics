import numpy as np

dining_tabs = [35, 47, 97, 103, 109, 135,
               172, 194, 205, 225, 2100]

mean = np.mean(dining_tabs)
median = np.median(dining_tabs)

print(f"Mean: {mean:.4f}")     # Mean: 311.0909
print(f"Median: {median:.4f}") # Median:  135.0000
print
