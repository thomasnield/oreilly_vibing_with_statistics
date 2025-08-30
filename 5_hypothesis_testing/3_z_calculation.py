from math import sqrt

# Given data
mu = 355.0 # Alleged population mean
n = 40  # Sample size
x_bar = 353  # Sample mean
s = 6 # Sample standard deviation

# Calculate z test value
z_stat = (x_bar - mu) / (s / sqrt(n))

print(f"z-statistic: {z_stat:.2f}")
# z-statistic: -2.11